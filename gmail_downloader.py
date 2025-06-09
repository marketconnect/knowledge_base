from __future__ import annotations

from typing import List
from pathlib import Path
import base64

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


class GmailAttachmentDownloader:
    """Download all attachments from emails sent by a specific sender."""

    def __init__(self, credentials_path: str, token_path: str, sender: str, download_dir: str = "."):
        self.credentials_path = credentials_path
        self.token_path = token_path
        self.sender = sender
        self.download_dir = Path(download_dir)
        self.download_dir.mkdir(parents=True, exist_ok=True)
        self.service = None

    def _authorize(self) -> None:
        if Path(self.token_path).exists():
            creds = Credentials.from_authorized_user_file(self.token_path, SCOPES)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            with open(self.token_path, "w") as token:
                token.write(creds.to_json())
        self.service = build("gmail", "v1", credentials=creds)

    def fetch_all_attachments(self) -> List[Path]:
        """Fetch attachments from all emails from the configured sender."""
        if not self.service:
            self._authorize()
        attachments: List[Path] = []
        query = f"from:{self.sender}"
        response = self.service.users().messages().list(userId="me", q=query).execute()
        for msg_meta in response.get("messages", []):
            msg = self.service.users().messages().get(userId="me", id=msg_meta["id"]).execute()
            payload = msg.get("payload", {})
            parts = payload.get("parts", [])
            for part in parts:
                if filename := part.get("filename"):
                    att_id = part["body"].get("attachmentId")
                    if att_id:
                        att = self.service.users().messages().attachments().get(userId="me", messageId=msg["id"], id=att_id).execute()
                        data = base64.urlsafe_b64decode(att["data"])
                        file_path = self.download_dir / filename
                        file_path.write_bytes(data)
                        attachments.append(file_path)
        return attachments

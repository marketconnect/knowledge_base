# Knowledge Base

## Telegram Channel Downloader

The project includes `TelegramChannelDownloader` in `telegram_channel.py` for fetching all messages from a Telegram channel.

### Usage

1. Install dependencies:

```bash
pip install -r requirements.txt
```

The dependencies are also listed in `pyproject.toml`.

2. Create a script or use an interactive session:

```python
import asyncio
from telegram_channel import TelegramChannelDownloader

async def main():
    downloader = TelegramChannelDownloader(api_id=123456, api_hash="YOUR_HASH", channel="@yourchannel")
    messages = await downloader.fetch_all_messages()
    for msg in messages:
        print(msg)

asyncio.run(main())
```

Replace `api_id`, `api_hash`, and `channel` with your credentials.

## Gmail Attachment Downloader

`gmail_downloader.py` provides `GmailAttachmentDownloader` for fetching all
attachments from messages sent by a specific Gmail address.

### Basic usage

1. Obtain `credentials.json` from the Google Cloud Console and place it in your
   working directory. The first run will create a token file for reuse.

2. Use the downloader in a script:

```python
from gmail_downloader import GmailAttachmentDownloader

downloader = GmailAttachmentDownloader(
    credentials_path="credentials.json",
    token_path="token.json",
    sender="sender@example.com",
    download_dir="attachments",
)
files = downloader.fetch_all_attachments()
for f in files:
    print("Saved", f)
```

This downloads all attachments from emails sent by `sender@example.com`.

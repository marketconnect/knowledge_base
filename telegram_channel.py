from __future__ import annotations


from typing import List


from telethon import TelegramClient


class TelegramChannelDownloader:
    """Utility for downloading all messages from a Telegram channel."""

    def __init__(self, api_id: int, api_hash: str, channel: str, *, session_name: str = "downloader"):
        self.client = TelegramClient(session_name, api_id, api_hash)
        self.channel = channel

    async def fetch_all_messages(self) -> List[str]:
        """Fetch all messages from the configured channel.

        Returns a list containing the text of each message.
        """
        await self.client.start()
        messages: List[str] = []
        async for message in self.client.iter_messages(self.channel):
            if message.text:
                messages.append(message.text)
        await self.client.disconnect()
        return messages

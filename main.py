"""Entry point for downloading messages from a Telegram channel."""

from __future__ import annotations

import asyncio
import os

from telegram_channel import TelegramChannelDownloader


async def _run_downloader() -> None:
    """Run the TelegramChannelDownloader using environment variables."""
    try:
        api_id = int(os.environ["TELEGRAM_API_ID"])
        api_hash = os.environ["TELEGRAM_API_HASH"]
        channel = os.environ["TELEGRAM_CHANNEL"]
    except KeyError as exc:  # pragma: no cover - simple env parsing
        missing = exc.args[0]
        raise SystemExit(f"Missing required environment variable: {missing}") from exc

    downloader = TelegramChannelDownloader(api_id=api_id, api_hash=api_hash, channel=channel)
    messages = await downloader.fetch_all_messages()
    for message in messages:
        print(message)


def main() -> None:
    """Synchronously run the async downloader."""
    asyncio.run(_run_downloader())


if __name__ == "__main__":
    main()

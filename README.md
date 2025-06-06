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

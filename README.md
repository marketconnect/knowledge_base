# Knowledge Base

## Telegram Channel Downloader

The project includes `TelegramChannelDownloader` in `telegram_channel.py` for fetching all messages from a Telegram channel.

### Usage

1. Install dependencies:

```bash
pip install -r requirements.txt
```

The dependencies are also listed in `pyproject.toml`.


2. Set the following environment variables:

```bash
export TELEGRAM_API_ID=123456
export TELEGRAM_API_HASH="YOUR_HASH"
export TELEGRAM_CHANNEL="@yourchannel"
```

3. Run `python main.py` to print all messages from the channel.

Alternatively, create a script or use an interactive session:

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


Replace the placeholders with your own Telegram credentials.
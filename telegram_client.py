import os
from telethon import TelegramClient
from dotenv import load_dotenv
from storage import add_item

load_dotenv()
api_id = int(os.getenv("TG_API_ID", "0"))
api_hash = os.getenv("TG_API_HASH", "")
channels = os.getenv("TG_CHANNELS", "").split(",")

async def fetch_telegram_posts():
    if not api_id or not api_hash:
        print("⚠️ Telegram API credentials not found in .env")
        return
    async with TelegramClient('session', api_id, api_hash) as client:
        for channel in channels:
            async for msg in client.iter_messages(channel, limit=5):
                if msg and msg.text:
                    url = f"https://t.me/{channel}/{msg.id}"
                    add_item("Telegram", url, msg.text[:200], [])

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from models import NewsItem, create_news_item
from storage import add_item, get_all_items
from telegram_client import fetch_telegram_posts

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/api/feed")
def get_feed():
    return get_all_items()

@app.post("/api/upload")
def manual_upload(
    origin: str = Form(...),
    summary: str = Form(""),
    tags: str = Form("")
):
    tags_list = [t.strip() for t in tags.split(",")] if tags else []
    return add_item(source="Manual", origin=origin, summary=summary, tags=tags_list)

@app.get("/api/telegram/fetch")
async def fetch_telegram():
    await fetch_telegram_posts()
    return {"status": "Fetched latest Telegram posts"}

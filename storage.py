import sqlite3
import json
from models import create_news_item

DB_PATH = "data/feed.sqlite"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS feed (
            id TEXT PRIMARY KEY,
            source TEXT,
            origin TEXT,
            timestamp TEXT,
            summary TEXT,
            tags TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_item(source, origin, summary, tags):
    item = create_news_item(source, origin, summary, tags)
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO feed VALUES (?, ?, ?, ?, ?, ?)", (
        item.id, item.source, item.origin, item.timestamp, item.summary, json.dumps(item.tags)
    ))
    conn.commit()
    conn.close()
    return item

def get_all_items():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.execute("SELECT id, source, origin, timestamp, summary, tags FROM feed ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": rid, "source": src, "origin": ori,
            "timestamp": ts, "summary": summ,
            "tags": json.loads(tags)
        }
        for (rid, src, ori, ts, summ, tags) in rows
    ]

# Initialize DB on import
init_db()

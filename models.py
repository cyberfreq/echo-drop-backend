from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

class NewsItem(BaseModel):
    id: str
    source: str
    origin: str
    timestamp: str
    summary: Optional[str] = ""
    tags: List[str] = []

def create_news_item(source: str, origin: str, summary: str = "", tags: Optional[List[str]] = None):
    return NewsItem(
        id=str(uuid.uuid4()),
        source=source,
        origin=origin,
        timestamp=datetime.utcnow().isoformat() + "Z",
        summary=summary,
        tags=tags or []
    )

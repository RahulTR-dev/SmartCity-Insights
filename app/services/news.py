import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")

async def get_news(city: str) -> str:
    url = f"https://newsapi.org/v2/everything?q={city}&apiKey={API_KEY}"
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        articles = res.json().get("articles", [])
        print(articles)
        return " ".join([article["title"] for article in articles[:3]])

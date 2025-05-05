from fastapi import FastAPI
from app.schemas import CityRequest
from app.services.weather import get_weather
from app.services.news import get_news
from app.services.summary import summarize_text
from app.services.logger import log_data
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(docs_url="/docs")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- your HTML server origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/insights")
async def get_city_insights(data: CityRequest):
    weather = await get_weather(data.city)
    news = await get_news(data.city)
    summary = summarize_text(news)
    log_data(data.city, weather, summary)
    return {
        "city": data.city,
        "news": news,
        "weather": weather,
        "summary": summary
    }

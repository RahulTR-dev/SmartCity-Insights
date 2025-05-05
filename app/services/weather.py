import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

async def get_weather(city: str) -> str:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        
        # Check for request errors
        if res.status_code != 200:
            try:
                error_data = res.json()
                return f"Weather API error: {error_data.get('message', 'Unknown error')}"
            except Exception:
                return "Weather API error: Unable to parse error message"
        
        data = res.json()
        print(data)
        
        try:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            return f"{temp}°C, {description}"
        except KeyError:
            return "Weather data format error: missing 'main' or 'weather' in response"

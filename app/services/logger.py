import polars as pl
from datetime import datetime
import os

LOG_FILE = "insights_log.csv"

def log_data(city: str, weather: str, summary: str):
    new_data = {
        "timestamp": str(datetime.now()),
        "city": city,
        "weather": weather,
        "summary": summary
    }
    df = pl.DataFrame([new_data])
    
    if os.path.exists(LOG_FILE):
        old_df = pl.read_csv(LOG_FILE)
        df = pl.concat([old_df, df])
    
    df.write_csv(LOG_FILE)

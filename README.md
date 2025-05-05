# 🌆 SmartCity-Insights

**SmartCity-Insights** is a full-stack web application that provides users with **real-time weather data** and **summarized local news** for any city.  
It combines a **FastAPI backend** and a modern **React frontend**, powered by external APIs and AI-driven text summarization using **Transformers**.

---

## 📸 Demo Preview

> *(Add a screenshot or deploy link if available)*

---

## 🚀 Features

- 🌦️ Real-time **weather info** using OpenWeatherMap API
- 📰 Live **news headlines** for a given city
- 🧠 AI-generated **summaries** of long news articles using **BART model**
- 🔄 Asynchronous, fast backend powered by **FastAPI + HTTPX**
- ⚛️ Interactive frontend built with **React + Vite**

---

## 🧰 Tech Stack

### 🔙 Backend (Python)
- FastAPI
- HTTPX (async requests)
- OpenWeatherMap API
- News API *(or another news source)*
- Hugging Face Transformers (`facebook/bart-large-cnn`)
- Torch (for model backend)
- Polars (for logging insights)
- Pydantic (for data validation)
- Uvicorn (ASGI server)

### 🔜 Frontend (React + Vite)
- React 18+
- Fetch or Axios for API calls
- Modern layout with responsive components

---

## 🧠 News Summarization with Transformers

We use the `facebook/bart-large-cnn` model from Hugging Face to generate clean summaries from city-specific news content:

```python
  



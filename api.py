# api.py
import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI

from utils import (analyze_sentiment, convert_to_hindi_audio,
                   get_marketscreener_articles, summarize_text)

app = FastAPI()


@app.get("/get_news_summary/")
def get_news_summary(company: str):
    articles_raw = get_marketscreener_articles(company)
    print(f"Found {len(articles_raw)} articles for {company}")
    print(articles_raw)
    articles_data = []

    for article in articles_raw:
        try:
            res = requests.get(article["link"])
            soup = BeautifulSoup(res.text, "html.parser")
            paragraphs = " ".join([p.get_text() for p in soup.find_all("p")])
            if not paragraphs.strip():
                continue
            summary = summarize_text(paragraphs)
            sentiment = analyze_sentiment(summary)
            articles_data.append(
                {
                    "title": article["title"],
                    "summary": summary,
                    "sentiment": sentiment,
                    "url": article["link"],
                }
            )
        except Exception:
            continue

    sentiment_count = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for art in articles_data:
        sentiment_count[art["sentiment"]] += 1

    hindi_summary = (
        f"{company} \u0915\u0940 \u0916\u092c\u0930\u094b\u0902 \u0915\u093e \u0938\u093e\u0930:\n"
        + " \u0964 ".join([f"{a['title']} - {a['sentiment']}" for a in articles_data])
    )

    audio_path = convert_to_hindi_audio(hindi_summary)

    return {
        "company": company,
        "articles": articles_data,
        "comparative_analysis": sentiment_count,
        "audio_path": audio_path,
    }

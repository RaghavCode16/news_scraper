# utils.py
import os
import tempfile

import requests
from bs4 import BeautifulSoup
from gtts import gTTS
from textblob import TextBlob
from transformers import pipeline


# 1. Scrape from Hindustan Times
def get_marketscreener_articles(company, count=10):
    query = company.replace(" ", "+")
    url = f"https://www.marketscreener.com/search/?q={query}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    # Updated selector
    article_links = soup.select("table.table--small a.txt-overflow-2")[:count]

    articles = []
    for item in article_links:
        title = item.get_text(strip=True)
        href = item.get("href")
        if href and not href.startswith("http"):
            href = "https://www.marketscreener.com" + href
        articles.append({"title": title, "link": href})
    return articles


# 2. Summarization pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def summarize_text(text):
    if len(text.split()) < 50:
        return text
    return summarizer(text, max_length=130, min_length=30, do_sample=False)[0][
        "summary_text"
    ]


# 3. Sentiment Analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    return "Neutral"


# 4. Hindi TTS
def convert_to_hindi_audio(text):
    tts = gTTS(text=text, lang="hi")
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(temp_file.name)
    return temp_file.name

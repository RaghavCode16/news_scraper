# 📰 News Summarization & Hindi TTS App 🇮🇳

A simple AI-powered web app that fetches news articles for a given company, summarizes them using a transformer model, performs sentiment analysis, and converts the summary into Hindi audio using Google Text-to-Speech (gTTS).

---

## 🚀 Features

- 🔎 **Scrape Latest News**: Fetch articles from [MarketScreener](https://www.marketscreener.com/) using BeautifulSoup.
- 📝 **Summarize News**: Use HuggingFace `transformers` pipeline with the `distilbart-cnn` model.
- 😊 **Sentiment Analysis**: Analyze summarized text using `TextBlob`.
- 🔊 **Hindi Audio Summary**: Convert final summary into Hindi MP3 using `gTTS`.
- 🧾 **Streamlit UI**: A sleek UI for entering company names and visualizing results.
- ⚡ **FastAPI Backend**: Handles scraping, summarization, sentiment, and TTS.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/news-hindi-tts-app.git
cd news-hindi-tts-app
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Backend (FastAPI)

```bash
uvicorn api:app --reload
```

### 5.Run the Frontend (Streamlit)

```bash
streamlit run app.py
```

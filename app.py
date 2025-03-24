import requests
import streamlit as st

st.title("News Summarization & Hindi TTS App")
company = st.text_input("Enter Company Name", "Tesla")

if st.button("Analyze"):
    with st.spinner("Fetching and analyzing news..."):
        response = requests.get(
            f"http://localhost:8000/get_news_summary/?company={company}"
        )
        data = response.json()

        st.subheader("Comparative Sentiment Report")
        st.json(data["comparative_analysis"])

        st.subheader("Articles")
        for article in data["articles"]:
            st.markdown(f"**{article['title']}**")
            st.write(article["summary"])
            st.write(f"Sentiment: {article['sentiment']}")
            st.markdown(f"[Read more]({article['url']})")

        st.subheader("Hindi Audio Summary")
        st.audio(data["audio_path"])

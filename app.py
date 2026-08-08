import streamlit as st
import pickle
import re
import string


# Load trained model
with open("fake_news_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load TF-IDF vectorizer
with open("tfidf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


def wordopt(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'<.*?>+', '', text)
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub(r'\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text


def predict_news(news):
    news = wordopt(news)

    vectorized_news = vectorizer.transform([news])

    prediction = model.predict(vectorized_news)[0]

    if prediction == 0:
        return "FAKE NEWS"
    else:
        return "REAL NEWS"


st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰"
)

st.title("📰 Fake News Detection System")

st.write("Enter a news article to check whether it is fake or real.")

news = st.text_area(
    "Enter News Article",
    height=250
)

if st.button("Detect News"):

    if news.strip() == "":
        st.warning("Please enter a news article.")

    else:
        result = predict_news(news)

        if result == "FAKE NEWS":
            st.error("❌ Fake News")
        else:
            st.success("✅ Real News")
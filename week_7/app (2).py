
import streamlit as st
import joblib
import re
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download("punkt", quiet=True)
nltk.download("stopwords", quiet=True)
nltk.download("punkt_tab", quiet=True)

# Load trained model and TF-IDF vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Stopwords
stop_words = set(stopwords.words("english"))


# Text preprocessing function
def preprocess_text(text):
    text = text.lower()

    text = re.sub(r'[^a-zA-Z\s]', '', text)

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    return " ".join(tokens)


# -------------------------------
# Streamlit User Interface
# -------------------------------

st.set_page_config(
    page_title="Zynxis Feedback Analyzer",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Zynxis Feedback Sentiment Analyzer")

st.write(
    "Enter student or intern feedback below and the AI model "
    "will predict whether the feedback is positive or negative."
)

st.divider()

feedback = st.text_area(
    "Enter your feedback:",
    placeholder="Example: I really enjoyed the internship and learned many useful skills.",
    height=150
)

if st.button("🔍 Analyze Sentiment"):

    if feedback.strip() == "":
        st.warning("Please enter some feedback first.")

    else:

        # Preprocess input
        cleaned_text = preprocess_text(feedback)

        # Convert text into TF-IDF features
        input_vector = vectorizer.transform([cleaned_text])

        # Make prediction
        prediction = model.predict(input_vector)[0]

        st.subheader("Analysis Result")

        if prediction == "positive":
            st.success("😊 Positive Feedback")

        else:
            st.error("😟 Negative Feedback")

        with st.expander("View Processing Details"):

            st.write("**Original Feedback:**")
            st.write(feedback)

            st.write("**Cleaned Text:**")
            st.write(cleaned_text)

            st.write("**Predicted Sentiment:**")
            st.write(prediction.upper())

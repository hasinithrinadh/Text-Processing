import streamlit as st
from transformers import pipeline

# Page configuration
st.set_page_config(
    page_title="Text Summarization App",
    page_icon="📝"
)

st.title("📝 Text Summarization using AI")
st.write("Paste some text and let the AI summarize it.")

# Load the summarization model
@st.cache_resource
def load_model():
    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6"
    )
    return summarizer

summarizer = load_model()

# User input
text = st.text_area(
    "Enter your text:",
    placeholder="Paste an article or paragraph here...",
    height=200
)

# Summary settings
max_length = st.slider(
    "Maximum summary length",
    min_value=20,
    max_value=200,
    value=80
)

min_length = st.slider(
    "Minimum summary length",
    min_value=10,
    max_value=100,
    value=20
)

# Summarize button
if st.button("Summarize 🚀"):

    if text.strip() == "":
        st.warning("Please enter some text.")

    elif len(text.split()) < 10:
        st.warning("Please enter a longer piece of text (at least ~10 words).")

    else:
        with st.spinner("Summarizing..."):

            result = summarizer(
                text,
                max_length=max_length,
                min_length=min_length,
                do_sample=False
            )

            summary_text = result[0]["summary_text"]

        st.subheader("Summary")
        st.write(summary_text)
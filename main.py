# main.py

import streamlit as st
from rag import process_urls, generate_answer

st.set_page_config(page_title="URL QA App", layout="wide")
st.title("🌐 Website URL processing")

url1 = st.sidebar.text_input("URL-1")
url2 = st.sidebar.text_input("URL-2")
url3 = st.sidebar.text_input("URL-3")

process_url_button = st.sidebar.button("Process URL")
placeholder = st.empty()

# Process URLs
if process_url_button:
    urls = [url for url in (url1, url2, url3) if url.strip()]
    if not urls:
        placeholder.warning("⚠️ You must enter at least one URL.")
    else:
        for status in process_urls(urls):
            placeholder.text(status)
        placeholder.success("✅ URLs processed successfully. You can now enter your query below.")

# Query Input
query = placeholder.text_input("Enter your query")

# Get Answer
if query:
    try:
        answer, sources = generate_answer(query)
        st.header("🧠 Answer")
        st.write(answer)

        if sources:
            st.subheader("🔗 Sources")
            for source in sources.split("\n"):
                if source.strip():
                    st.write(f"- {source.strip()}")
    except RuntimeError as e:
        placeholder.error(str(e))

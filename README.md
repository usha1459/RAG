# 🔍 RAG App – Ask Questions from Web URLs (Groq + LangChain + Streamlit)

This project is a **Retrieval-Augmented Generation (RAG)** application built with **Streamlit** that allows users to input URLs of blog posts or articles, processes their content using LangChain, and answers questions based on the retrieved data using **Groq's blazing-fast LLM APIs** (LLaMA3 or Mixtral).

---

## 🚀 Features

- 📰 Input URLs of articles, blogs, or news
- 📄 Automatically extract and parse content with `UnstructuredURLLoader`
- 🤖 Query any processed content using Groq’s ultra-fast language models
- 💬 Interactive UI built using Streamlit
- 🔁 End-to-end pipeline using LangChain, FAISS, Groq, and vector embeddings

---

## 🧠 Tech Stack

- **Python 3.10+**
- **Streamlit** – for web interface
- **LangChain** – RAG pipeline
- **Groq API** – LLM (LLaMA3/Mixtral)
- **FAISS** – vector search
- **Unstructured** – content parsing
- **dotenv** – environment variables

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```
git clone https://github.com/usha1459/RAG.git
cd RAG
```

2. Install Requirements
```
Copy code
pip install -r requirements.txt
```

3. Add API Keys
Create a .env file in the root folder and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

🧪 Run the App Locally
```
streamlit run main.py
```

☁️ Deploy on Streamlit Cloud
1. Push the repo to GitHub

2. Visit https://streamlit.io/cloud

3. Link your GitHub and select this repo

4. Add GROQ_API_KEY in the app’s Secrets section

5. Click Deploy

👩‍💻 Author
Prathyusha Kopur
📫 kprathyusha799@gmail.com
🌐 GitHub (https://github.com/usha1459) 
LinkedIn (https://www.linkedin.com/in/prathyusha-kopur/)


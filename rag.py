# rag.py

from dotenv import load_dotenv
from pathlib import Path
from uuid import uuid4

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma 
from langchain_groq import ChatGroq
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_community.document_loaders import UnstructuredURLLoader

load_dotenv()

CHUNK_SIZE = 300
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
VECTORSTORE_DIR = Path(__file__).parent / "resources/vectorstore"
COLLECTION_NAME = "ISRO_database"  # ✅ Valid name

llm = None
vector_store = None
vector_initialized = False  # ✅ Flag to check if initialized


# Initialize LLM and vector store
def initialize_components():
    global llm, vector_store
    if llm is None:
        print("[INFO] Initializing LLM...")
        llm = ChatGroq(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            temperature=0.4,
            max_tokens=500
        )
    if vector_store is None:
        print("[INFO] Initializing Vector Store...")
        ef = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={"trust_remote_code": True}
        )
        vector_store = Chroma(
            collection_name=COLLECTION_NAME,
            embedding_function=ef,
            persist_directory=str(VECTORSTORE_DIR)
        )


# Process URL and add content to vector store
def process_urls(urls):
    global vector_initialized
    yield "Initializing Components....."
    initialize_components()

    yield "Resetting vector store....."
    vector_store.reset_collection()

    yield "Loading data...."
    loader = UnstructuredURLLoader(urls=urls)
    data = loader.load()
    print(f"[DEBUG] Loaded {len(data)} documents")

    yield "Splitting text into chunks....."
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=CHUNK_SIZE
    )
    docs = text_splitter.split_documents(data)
    print(f"[DEBUG] Got {len(docs)} chunks")

    yield "Adding Chunks to Vector Database....."
    uuids = [str(uuid4()) for _ in range(len(docs))]
    vector_store.add_documents(docs, ids=uuids)
    print("[DEBUG] Documents added")

    vector_initialized = True
    yield "✅ Vector store ready!"


# Generate answer to user query
def generate_answer(query):
    if not vector_store:
        raise RuntimeError("Vector database is not initialized")
    if not vector_initialized:
        raise RuntimeError("You must process URL first")

    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever()
    )

    result = chain.invoke({"question": query})
    sources = result.get("sources", "")
    return result["answer"], sources

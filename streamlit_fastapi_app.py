# app_combined.py
import threading
import uuid
import requests
import streamlit as st
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4
import uvicorn

# =====================================================
# Import your RAG class
# =====================================================
from app.core.personalized_rag import Personalized_RAG


# =====================================================
# ---------- FASTAPI SECTION ----------
# =====================================================
api = FastAPI(title="Joel's Assistant API", version="1.1")


class QuestionRequest(BaseModel):
    user_id: Optional[str] = None
    question: str


class AskResponse(BaseModel):
    answer: str
    documents: Optional[List[str]] = None


rag = Personalized_RAG(
    file_path="data/user_information/",
    user_id="default_user",
    persist_dir="./chroma_db",
)


@api.get("/")
async def root():
    return {"message": "Welcome to Joel's Personalized RAG API 🚀"}


@api.get("/health")
async def healthcheck():
    try:
        _ = rag.user_id
        return {"status": "ok", "service": "joel-assistant", "version": "1.1"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Healthcheck failed: {e}")


@api.get("/status")
async def status():
    indexed = rag.indexer.is_indexed()
    return {"indexed": indexed, "user_id": rag.user_id}


@api.post("/ask", response_model=AskResponse)
def ask_question(request: QuestionRequest):
    try:
        user_id = request.user_id or str(uuid4())
        rag.user_id = user_id

        if not rag.vectorstore:
            if not rag.indexer.is_indexed():
                raise HTTPException(status_code=400, detail="Index not found. Please run /reindex first.")
            rag.index()

        answer = rag.ask(request.question)
        docs_retrieved = getattr(rag.retriever, "last_retrieved_docs", [])

        return AskResponse(
            answer=answer,
            documents=[doc.page_content for doc in docs_retrieved] if docs_retrieved else [],
        )

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing question: {e}")


@api.post("/reindex")
def reindex_data():
    try:
        rag.index()
        return {"status": "success", "message": "Reindexing completed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during reindexing: {e}")


def run_api():
    """Run FastAPI in background (port 8001)."""
    uvicorn.run(api, host="0.0.0.0", port=8001, log_level="warning")


# =====================================================
# ---------- STREAMLIT SECTION ----------
# =====================================================

# Launch FastAPI in background
threading.Thread(target=run_api, daemon=True).start()

# Page Config
st.set_page_config(page_title="Joel's Assistant", layout="wide")
st.title("Joel's Assistant (Direct Agent + API)")

# Session state initialization
if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())

if "conversation" not in st.session_state:
    st.session_state.conversation = []

API_URL = "http://localhost:8001"

# Function to send a question (via FastAPI endpoint)
def send_question():
    question = st.session_state.question_input.strip()
    if not question:
        return

    try:
        resp = requests.post(
            f"{API_URL}/ask",
            json={"user_id": st.session_state.user_id, "question": question},
            timeout=60,
        )

        if resp.status_code == 200:
            data = resp.json()
            answer = data["answer"]
            docs = data.get("documents", [])
        else:
            answer = f"Error: {resp.status_code} - {resp.text}"
            docs = []

        st.session_state.conversation.append({"role": "user", "content": question})
        st.session_state.conversation.append({"role": "assistant", "content": answer})
        st.session_state.retrieved_docs = docs

    except Exception as e:
        st.session_state.conversation.append(
            {"role": "assistant", "content": f"❌ Request failed: {e}"}
        )

    st.session_state.question_input = ""


# Input
st.text_input("Ask me anything:", key="question_input", on_change=send_question)

# Chat styles
st.markdown("""
<style>
.chat-area {
    background-color: #1E1E1E;
    padding: 15px;
    border-radius: 10px;
    max-height: 400px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
}
.user-msg {
    background-color: #4CAF50;
    color: white;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    text-align: left;
    max-width: 40%;
    font-size: 14px;
    word-wrap: break-word;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    align-self: flex-end;
}
.assistant-msg {
    background-color: #333333;
    color: white;
    padding: 10px;
    border-radius: 10px;
    margin: 5px;
    text-align: left;
    max-width: 50%;
    font-size: 14px;
    word-wrap: break-word;
    overflow-wrap: break-word;
    white-space: pre-wrap;
    align-self: flex-start;
}
</style>
""", unsafe_allow_html=True)

# Display chat
chat_placeholder = st.empty()
with chat_placeholder.container():
    st.markdown('<div class="chat-area" id="chat-area">', unsafe_allow_html=True)
    for msg in st.session_state.conversation:
        if msg["role"] == "user":
            st.markdown(f'<div class="user-msg">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="assistant-msg">{msg["content"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Source documents
with st.expander("Source Documents"):
    for i, doc in enumerate(st.session_state.get("retrieved_docs", []), start=1):
        st.markdown(f"**Doc {i}:** {doc}")

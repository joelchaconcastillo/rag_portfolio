from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from personalized_rag import Personalized_RAG

# ------------------------------
# Initialize FastAPI
# ------------------------------
app = FastAPI(title="Joel's Assistant API", version="1.0")

# ------------------------------
# Request & Response Models
# ------------------------------
class QuestionRequest(BaseModel):
    user_id: str
    question: str

class AskResponse(BaseModel):
    answer: str
    documents: Optional[List[str]] = None

# ------------------------------
# Initialize RAG Backend (once)
# ------------------------------
# You can set file_path and persist_dir as needed
rag = Personalized_RAG(
    file_path="user_information/",
    user_id="default_user",
    persist_dir="./chroma_db"
)

# ------------------------------
# API Routes
# ------------------------------
@app.get("/")
def root():
    return {"message": "Welcome to Joel's Personalized RAG API 🚀"}

@app.post("/ask", response_model=AskResponse)
def ask_question(request: QuestionRequest):
    try:
        # Update user_id dynamically for each request
        rag.user_id = request.user_id

        # Process the question
        answer = rag.ask(request.question)

        # Retrieve the documents used in the retrieval step, if any
        docs_retrieved = getattr(rag.retriever, "last_retrieved_docs", [])

        return AskResponse(
            answer=answer,
            documents=[doc.page_content for doc in docs_retrieved] if docs_retrieved else []
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing question: {e}")

# Optional: Endpoint to reindex data (useful if you update the source files)
@app.post("/reindex")
def reindex_data():
    try:
        docs_splits = rag.indexer.load_and_split()
        rag.vectorstore = rag.indexer.build_vectorstore(docs_splits)
        return {"status": "success", "message": "Reindexing completed."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during reindexing: {e}")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from personalized_rag import Personalized_RAG  # Import your new class

# Initialize FastAPI
app = FastAPI(title="Joel's Assistant API")

class QuestionRequest(BaseModel):
    user_id: str   # Unique identifier for each user
    question: str

# Initialize Personalized_RAG only once
# You can optionally pass a default user_id; individual requests can override
rag = Personalized_RAG(file_path="Joel_info.txt", user_id="default_user")

@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        # Update user_id for this session/query
        rag.user_id = request.user_id

        # Ask the question using Personalized_RAG
        answer = rag.ask(request.question)

        # Retrieve documents (last retrieved docs stored in rag)
        docs_retrieved = getattr(rag.retriever, "last_retrieved_docs", [])

        return {
            "answer": answer,
            "documents": [doc.page_content for doc in docs_retrieved]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

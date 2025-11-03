# 🧠 Joel’s Assistant — Personalized RAG Chatbot

**Joel’s Assistant** is a **Retrieval-Augmented Generation (RAG)** chatbot built with **LangChain**, **FastAPI**, and **Streamlit**.
It’s designed to provide **personalized, professional answers** for recruiters by leveraging both **local knowledge** and **online context** from [Joel’s LinkedIn profile](https://www.linkedin.com/in/joel-chacon-castillo-351bb4194/).

---

## 🚀 Features

* 💬 **Interactive Chat Interface** — Streamlit-based modern UI
* 🧠 **Retrieval-Augmented Generation** — Context-aware answers using embeddings and vector search
* 🔗 **LinkedIn Data Integration** — Uses professional profile as an online data source
* 💾 **Local Knowledge Base** — Reads structured information from `/data/user_information`
* ⚙️ **Multiple Run Modes** — Streamlit, FastAPI (Uvicorn), or command line
* 🎨 **Dark-Mode Chat Design** — Newest messages displayed on top

---

## 🧰 Project Structure

```
rag_portfolio/
├── app/
│   ├── __pycache__/                   # Compiled Python cache
│   ├── config.py                      # Configuration utilities
│   ├── core/                          # Main RAG components
│   │   ├── personalized_rag.py        # Core RAG pipeline
│   │   ├── indexer.py                 # Builds and updates vector database
│   │   └── retriever.py               # Handles document retrieval
│   ├── preprocessing/                 # Preprocessing scripts for data ingestion
│   └── main.py                        # FastAPI backend (Uvicorn entrypoint)
│
├── chroma_db/
│   └── chroma.sqlite3                 # Persistent Chroma vector store
│
├── data/
│   └── user_information/              # Local knowledge base
│
├── frontend/
│   └── streamlit_app.py               # Streamlit frontend (UI version)
│
├── render.yaml                        # Render deployment configuration
├── requirements.txt                   # Project dependencies
├── set_variables.sh                   # Environment variable setup script
├── streamlit_app.py                   # Root Streamlit entry (for local dev)
└── README.md
```

---

## 🧩 Tech Stack

| Component           | Description                                   |
| ------------------- | --------------------------------------------- |
| **Frontend**        | [Streamlit](https://streamlit.io)             |
| **Backend**         | [FastAPI](https://fastapi.tiangolo.com/)      |
| **Core Framework**  | [LangChain](https://www.langchain.com/)       |
| **Vector Database** | [ChromaDB](https://www.trychroma.com)         |
| **Embeddings**      | Gemini, HuggingFace, or OpenAI (configurable) |
| **Deployment**      | Render / Hugging Face Spaces / Local          |

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/joelchaconcastillo/rag_portfolio.git
cd rag_portfolio
```

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

If you’re using external models like **Gemini** or **OpenAI**, create a `.env` file:

```bash
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

You can also export them with:

```bash
source set_variables.sh
```

---

## ▶️ Running the Application

You can run **Joel’s Assistant** in three different modes:

---

### 💻 Option 1: Streamlit (Frontend UI)

This launches the **interactive chat interface**.

**Run from root:**

```bash
streamlit run streamlit_app.py
```

**Or run the version in `/frontend`:**

```bash
streamlit run frontend/streamlit_app.py
```

Then open your browser at:
👉 [http://localhost:8501](http://localhost:8501)

---

### ⚡ Option 2: FastAPI with Uvicorn (Backend API)

If you want to expose an API endpoint for integration (e.g., React, Postman, or external tools):

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Access the FastAPI docs here:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

**Example API call:**

```bash
curl -X POST "http://127.0.0.1:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are Joel’s technical strengths?"}'
```

---

### 🧮 Option 3: Terminal Mode (Direct CLI)

To quickly test the RAG pipeline from the command line:

```bash
python -m app.core.personalized_rag
```

Or, if you have a test script (like `test.py`):

```bash
python test.py
```

**Example prompt:**

```
> What is Joel’s professional background?
Answer: Joel Chacón Castillo is a software engineer specialized in AI, FastAPI, and cloud-based ML deployments...
```

---

## 🧠 How It Works

```
[User Question]
      ↓
 Streamlit / FastAPI
      ↓
Personalized_RAG (LangChain)
      ↓
[Retriever] → [ChromaDB] → [Documents / LinkedIn Data]
      ↓
[LLM Generator]
      ↓
[Final Answer]
```

* The assistant retrieves relevant chunks from your **local data** and **LinkedIn profile**
* Uses **vector embeddings** for semantic search
* Combines retrieved data with an **LLM** to generate a natural, context-rich response

---

## ☁️ Deployment on Render

1. Push the repo to GitHub: [rag_portfolio](https://github.com/joelchaconcastillo/rag_portfolio)
2. Go to [Render.com](https://render.com/)
3. Create a **New Web Service**
4. Connect your GitHub repo
5. Choose the build command and start command:

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
```

6. Deploy 🎉
   Render will automatically wake up your app when it receives traffic.

---

## 🧪 Example Conversation

**User:**

> What projects has Joel recently worked on?

**Assistant:**

> Joel has developed RAG-based assistants integrating LangChain, FastAPI, and Streamlit for intelligent data retrieval and recruiter-focused prototypes.
> His work emphasizes deploying AI solutions with robust cloud integrations and scalable APIs.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 👤 Author

**Joel Chacón Castillo**
💼 [LinkedIn](https://www.linkedin.com/in/joel-chacon-castillo-351bb4194/)
💻 [GitHub Repository](https://github.com/joelchaconcastillo/rag_portfolio)





# Deploy FastAPI on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render.

See https://render.com/docs/deploy-fastapi or follow the steps below:

## Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/joelchaconcastillo/rag_portfolio)

## Thanks

Thanks to [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!

# 🧠 Joel’s Assistant — Personalized RAG Chatbot

**Joel’s Assistant** is a **Retrieval-Augmented Generation (RAG)** chatbot built with **Streamlit**, **FastAPI**, and **LangChain**.
It provides context-aware, professional answers tailored for recruiters, drawing from both local knowledge and online data sources such as [Joel’s LinkedIn profile](https://www.linkedin.com/in/joel-chacon-castillo-351bb4194/).

---

## 🚀 Features

* 💬 **Interactive Chat UI** built with Streamlit
* 🧩 **RAG Pipeline** combining vector retrieval and LLM reasoning
* 🔗 **LinkedIn Data Integration**
* 💾 **Session Memory** with persistent conversation state
* 🎨 **Dark-Themed Chat Bubbles** with newest messages on top
* ⚙️ **Multiple Run Modes:** Streamlit UI, FastAPI (Uvicorn), or terminal

---

## 🧰 Project Structure

```
rag_portfolio/
├── app/
│   ├── core/
│   │   ├── personalized_rag.py       # Main RAG pipeline
│   │   ├── indexer.py                # Builds document embeddings
│   │   └── retriever.py              # Handles retrieval logic
│   ├── main.py                       # FastAPI backend entry point
│   └── ...
├── data/
│   └── user_information/             # Local knowledge base
├── streamlit_app.py                  # Streamlit-based UI
├── requirements.txt
├── config.py
├── README.md
└── ...
```

---

## ⚙️ Installation & Setup

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

### 4️⃣ Set Up Environment Variables

If you’re using external APIs (like Gemini or OpenAI), create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Running the Application

You can run **Joel’s Assistant** in three different modes:

---

### 💻 Option 1: Run with Streamlit (Recommended UI)

This launches the interactive chat interface.

```bash
streamlit run streamlit_app.py
```

Once started, open your browser at:
👉 [http://localhost:8501](http://localhost:8501)

---

### ⚡ Option 2: Run FastAPI Backend with Uvicorn

If you want to expose a backend API (for integration with React or other frontends):

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

You can then access the interactive FastAPI docs at:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Example `curl` test:

```bash
curl -X POST "http://127.0.0.1:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "What are Joel’s technical skills?"}'
```

---

### 🧮 Option 3: Run from Terminal (Direct CLI Mode)

If you prefer to test without a web interface:

```bash
python -m app.core.personalized_rag
```

Or, if you have a test script like `test.py`:

```bash
python test.py
```

You can then enter questions directly in the terminal, e.g.:

```
> What is Joel’s professional background?
Answer: Joel Chacón Castillo is a software engineer specialized in AI, FastAPI, and cloud-based deployment...
```

---

## 🧠 How It Works

1. The assistant loads contextual data from:

   * `data/user_information/`
   * Your [LinkedIn profile](https://www.linkedin.com/in/joel-chacon-castillo-351bb4194/)
2. `Personalized_RAG` generates embeddings, retrieves relevant snippets, and builds a context.
3. A large language model produces a coherent, professional answer.
4. Streamlit or FastAPI displays the conversation dynamically.

---

## 🧩 Tech Stack

| Component      | Description                                  |
| -------------- | -------------------------------------------- |
| **Frontend**   | Streamlit (chat interface)                   |
| **Backend**    | FastAPI + LangChain                          |
| **Vector DB**  | Chroma                                       |
| **Embeddings** | Gemini / HuggingFace / OpenAI (configurable) |
| **Deployment** | Local / Render / Hugging Face Spaces         |

---

## ☁️ Deployment on Render

1. Push your project to GitHub: [rag_portfolio](https://github.com/joelchaconcastillo/rag_portfolio)
2. Go to [Render.com](https://render.com/) → *New Web Service*
3. Connect your GitHub repo
4. In the “Start Command” field, enter:

   ```bash
   streamlit run streamlit_app.py --server.port $PORT --server.address 0.0.0.0
   ```
5. Click **Deploy** 🚀

Render automatically keeps the app alive and restarts on new requests.

---

## 🧪 Example Conversation

**User:**

> What projects has Joel worked on recently?

**Assistant:**

> Joel has built RAG-powered assistants integrating LangChain, FastAPI, and Streamlit.
> His recent work focuses on creating intelligent retrieval systems for recruiters and data-driven applications.

---

## 📄 License

This project is licensed under the **MIT License** — you’re free to use, modify, and share it.

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

import config
from indexer import Indexer
from retriever import Retriever
from llm_agent import LLM_Agent

def main():
    # 1️⃣ Load and index documents
    print("Loading and indexing documents...")
    indexer = Indexer(file_path="test_file.txt")
    doc_splits = indexer.load_and_split()
    vectorstore = indexer.build_vectorstore(doc_splits)

    # 2️⃣ Initialize retriever
    retriever = Retriever(vectorstore)

    # 3️⃣ Initialize LLM agent
    agent = LLM_Agent()

    # 4️⃣ Define a user_id for memory tracking
    user_id = "terminal_user"

    print("Joel's Assistant is ready! Type 'exit' to quit.\n")

    # 5️⃣ Interactive loop
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # Retrieve relevant documents
        docs_retrieved = retriever.retrieve(question)

        # Ask the agent directly
        answer = agent.ask(user_id, question, docs_retrieved)

        print("Assistant:", answer)
        print("-" * 50)

if __name__ == "__main__":
    main()


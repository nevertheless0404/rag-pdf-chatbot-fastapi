from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.llms import Ollama


def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    splitter = CharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30
    )

    texts = splitter.split_documents(docs)

    embeddings = OllamaEmbeddings(model="llama3")

    db = FAISS.from_documents(texts, embeddings)

    return db


def ask_question(db, query):
    docs = db.similarity_search(query, k=1)

    context = docs[0].page_content

    llm = Ollama(model="llama3")

    prompt = f"""
문서 내용:
{context}

질문:
{query}
"""

    answer = llm.invoke(prompt)

    return answer
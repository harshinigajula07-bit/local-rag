from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Load PDF
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(pages)

# Create Vector DB
def create_db(docs):
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    db = Chroma.from_documents(docs, embeddings, persist_directory="vectorstore")
    db.persist()
    return db

# Search relevant text
def search(db, query):
    return db.similarity_search(query, k=3)

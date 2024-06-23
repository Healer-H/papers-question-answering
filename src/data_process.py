from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.vectorstores import FAISS


def extract_document(pdf_file_path):
    loader = PyPDFLoader(pdf_file_path)
    document = loader.load()
    return document


def extract_documents(directory_path):
    loader = DirectoryLoader(
        directory_path, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


def split_text(documents, chunk_size, chunk_overlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

def create_faiss_index(chunks, embedding_model):
    database = FAISS.from_documents(chunks, embedding_model)
    database.save_local("retriever/vector_store/faiss_index")
    return database
    
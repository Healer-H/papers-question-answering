from langchain_huggingface import HuggingFaceEmbeddings
from src.file_loader import (
    extract_documents,
    split_text,
    create_faiss_index
)


def main():
    documents = extract_documents('data/papers')
    chunks = split_text(documents, 512, 32)
    embedding_model = HuggingFaceEmbeddings()
    create_faiss_index(chunks=chunks, embedding_model=embedding_model, save=True)


if __name__ == '__main__':
    main()

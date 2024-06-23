from langchain_huggingface import HuggingFaceEmbeddings
from src.data_process import (
    extract_documents,
    split_text,
    create_faiss_index
)


def main():
    documents = extract_documents('data/papers')
    chunks = split_text(documents, 512, 64)
    embedding_model = HuggingFaceEmbeddings()
    create_faiss_index(chunks, embedding_model)


if __name__ == '__main__':
    main()

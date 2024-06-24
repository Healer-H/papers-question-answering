
from langchain_huggingface import HuggingFaceEmbeddings
from src.retrieval import load_database, create_prompt
from src.base.llm_model import get_llm
from src.prompt import QA_PROMPT_TEMPLATE


def answer_question(query):
    db = load_database("retriever/vector_store/faiss_index", HuggingFaceEmbeddings())
    docs = db.similarity_search(query)
    llm = get_llm(model_name='mixtral-8x7b-32768')
    prompt = create_prompt(QA_PROMPT_TEMPLATE)
    chain = prompt | llm
    return chain.invoke({"question": query, "context": docs}).content
    

if __name__ == "__main__":
    print(answer_question("What is the NLP?"))
    
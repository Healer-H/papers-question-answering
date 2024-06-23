from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from src.base.llm_model import get_llm
from src.prompt import SUMMARIZE_PROMPT_TEMPLATE


def load_database(vector_database_path, embedding_model):
    database = FAISS.load_local(vector_database_path, embedding_model,
                                allow_dangerous_deserialization=True)
    return database

    
def create_prompt(template):
    prompt = ChatPromptTemplate.from_template(template)
    return prompt

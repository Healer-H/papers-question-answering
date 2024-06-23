import streamlit as st
import sys
import os
from src.qa_tool import answer_question

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


st.title('Papers Question-answering')

user_query = st.text_input("Give me a question")

if st.button('Answer'):
    if user_query:
        try:
            answer = answer_question(user_query)
            st.write("Answer:", answer)
        except Exception as e:
            st.write("An error occurred:", e)
    else:
        st.write("Please enter a question.")
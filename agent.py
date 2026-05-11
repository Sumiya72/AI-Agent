from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

def get_llm():
    return ChatGroq(
        groq_api_key=st.secrets["GROQ_API_KEY"],
        model_name="llama3-70b-8192",
        temperature=0.3
    )

def create_agent():
    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant."),
        ("user", "{input}")
    ])

    chain = prompt | llm | StrOutputParser()

    return chain

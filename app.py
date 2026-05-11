import streamlit as st
from agent import create_chain

st.set_page_config(page_title="AI Agent 🤖")

st.title("🤖 LangChain + Groq AI Agent")

chain = create_chain()

user_input = st.text_input("Ask anything:")

if st.button("Send"):
    if user_input:
        result = chain.invoke({"input": user_input})
        st.write("### 🤖 Response:")
        st.write(result)

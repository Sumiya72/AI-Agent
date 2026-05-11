import streamlit as st
from agent import create_agent

st.set_page_config(page_title="AI Agent 🤖")

st.title("🤖 LangChain + Groq AI Agent")

agent = create_agent()

user_input = st.text_input("Ask something:")

if st.button("Send"):
    if user_input:
        response = agent.invoke({"input": user_input})
        st.write("### 🤖 Response:")
        st.write(response)

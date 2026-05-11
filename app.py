import streamlit as st
from agent import create_agent

st.set_page_config(page_title="AI Agent 🤖")
st.title("🤖 LangChain + Groq AI Agent")

if "agent" not in st.session_state:
    st.session_state.agent = create_agent()

user_input = st.text_input("Ask anything:")

if st.button("Send"):
    if user_input:
        result = st.session_state.agent.invoke({"input": user_input})
        st.write("### 🤖 Agent Response:")
        st.write(result["output"])

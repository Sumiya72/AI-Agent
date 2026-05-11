from langchain_groq import ChatGroq
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
import streamlit as st

# =============================
# LLM (Groq Model)
# =============================
def get_llm():
    return ChatGroq(
        groq_api_key=st.secrets["GROQ_API_KEY"],
        model_name="llama3-70b-8192",
        temperature=0.3
    )

# =============================
# Tools
# =============================
def calculator(query: str):
    try:
        return str(eval(query))
    except:
        return "Invalid math expression"

calculator_tool = Tool(
    name="Calculator",
    func=calculator,
    description="Useful for math calculations"
)

def knowledge(query: str):
    data = {
        "langchain": "LangChain is a framework for building LLM apps.",
        "groq": "Groq provides ultra-fast AI inference.",
        "ai agent": "AI Agents can reason, plan and execute tasks."
    }
    for key in data:
        if key in query.lower():
            return data[key]
    return "No info found"

knowledge_tool = Tool(
    name="KnowledgeBase",
    func=knowledge,
    description="Useful for general knowledge"
)

tools = [calculator_tool, knowledge_tool]

# =============================
# Memory
# =============================
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# =============================
# Create Agent
# =============================
def create_agent():
    llm = get_llm()

    prompt = PromptTemplate.from_template("""
You are a smart AI assistant.
You can use tools to answer questions.

{chat_history}
Question: {input}
{agent_scratchpad}
""")

    agent = create_react_agent(llm, tools, prompt)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True
    )

    return agent_executor

from langchain.agents import initialize_agent, AgentType
from llm_model import get_llm
from tools import get_tools
from memory import get_memory

def create_agent():
    llm = get_llm()
    tools = get_tools()
    memory = get_memory()

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        memory=memory,
        verbose=True
    )

    return agent

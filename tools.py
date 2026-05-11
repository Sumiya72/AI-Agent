from langchain.tools import Tool

# Calculator Tool
def calculator_tool(query: str):
    try:
        return str(eval(query))
    except:
        return "Error in calculation"

calculator = Tool(
    name="Calculator",
    func=calculator_tool,
    description="Useful for solving math calculations"
)

# Search Tool
def search_tool(query: str):
    knowledge_base = {
        "langchain": "LangChain is a framework for building LLM apps.",
        "ai agent": "AI Agent can reason and perform tasks.",
        "groq": "Groq provides ultra-fast AI inference."
    }

    for key in knowledge_base:
        if key in query.lower():
            return knowledge_base[key]

    return "No data found"

search = Tool(
    name="Search",
    func=search_tool,
    description="Useful for general knowledge questions"
)

def get_tools():
    return [calculator, search]

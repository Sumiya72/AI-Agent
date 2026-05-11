from agent_setup import create_agent

agent = create_agent()

print("\n🤖 AI Agent Ready! Type 'exit' to stop\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye 👋")
        break

    response = agent.run(user_input)
    print("Agent:", response)

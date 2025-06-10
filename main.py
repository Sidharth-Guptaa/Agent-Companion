from agent.core import create_agent

if __name__ == "__main__":
    agent = create_agent()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = agent.run(user_input)
        print("AI:", response)
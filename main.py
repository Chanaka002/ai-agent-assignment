from agent import Agent


def main():
    print("=== Personal Assistant Agent ===")
    print("Type 'exit' to quit.\n")

    try:
        agent = Agent()
    except Exception as e:
        print(f"Startup error: {e}")
        return

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye.")
            break

        if not user_input:
            print("Assistant: Please enter a message.\n")
            continue

        reply = agent.handle_user_input(user_input)
        print(f"Assistant: {reply}\n")


if __name__ == "__main__":
    main()

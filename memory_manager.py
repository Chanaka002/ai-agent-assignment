class MemoryManager:
    def __init__(self):
        self.history = []

    def add_user_message(self, message):
        self.history.append({"role": "user", "content": message})

    def add_assistant_message(self, message):
        self.history.append({"role": "assistant", "content": message})

    def get_history(self):
        return self.history

    def get_history_as_text(self):
        if not self.history:
            return "No previous conversation."

        lines = []
        for item in self.history:
            lines.append(f"{item['role'].capitalize()}: {item['content']}")
        return "\n".join(lines)

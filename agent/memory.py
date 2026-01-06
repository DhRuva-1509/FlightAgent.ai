class ConversationMemory:
    def __init__(self):
        self.summary = ""

    def update(self, new_summary: str):
        self.summary = new_summary

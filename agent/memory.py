class ConversationMemeory:
    '''
    A class to manage and store conversation history for an agent.
    '''
    def __init__(self):
        self.summary = ""
    
    def update_summary(self, new_summary: str):
        self.summary = new_summary

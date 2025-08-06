import Chat
from datetime import datetime as dt


class ChatCache():
    def __init__(self, storage_time):
        self.storage_time = storage_time*60
        self.current_chats = {}


    def get_chat(self, id):
        if id not in self.current_chats.keys():
            return None
        
        chat = self.current_chats[id]["chat_obj"]
        self.current_chats[id]["last_access"] = dt.now()

        return chat

    def save_chat(self, id, chat):
        if id not in self.current_chats.keys():
            self.current_chats[id] = {
                "chat_obj": chat,
                "last_access": dt.now(),
            }

    def refresh(self):
        now = dt.now()
        ids_to_delete = []
        for id in self.current_chats.keys():
            entry = self.current_chats[id]
            difference = (now - entry["last_access"]).total_seconds 
            if difference > self.storage_time:
                ids_to_delete.append(id)
        
        for id in ids_to_delete:
            del self.current_chats[id]
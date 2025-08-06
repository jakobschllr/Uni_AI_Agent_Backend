import os
from dotenv import load_dotenv
load_dotenv()
import requests
from datetime import datetime as dt


class Chat():
    def __init__(self, id):
        self.id = id

    # load last conversations for context
    def load_chat(self):
        pass

    def generate_answer(self, user_prompt, vector_db_output):
        # load chat context (last messages)

        # create answer


        HF_TOKEN = os.getenv("HF_TOKEN")

        input = f"""
            Du bist ein KI-Assistent der dem Nutzer ausschließlich basierend auf dem aus einer Quelle bereitgestelltem Wissen antwortet.
            Nutzeranfrage: {user_prompt}
            Informationsquelle: {vector_db_output}
            Antworte nur, wenn die Informationen auch in den Quellen enthalten sind.
        """

        API_URL = "https://router.huggingface.co/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {HF_TOKEN}",
        }

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()

        response = query({
            "messages": [
                {
                    "role": "user",
                    "content": input
                }
            ],
            "model": "deepseek-ai/DeepSeek-R1-0528:novita"
        })

        print(response["choices"][0]["message"]["content"].split("\n</think>\n")[1])

        
import random

import dotenv

dotenv.load_dotenv()

from openai import OpenAI
client = OpenAI()

def chat(username, message, history, personality):
  messages = [
      {"role": "system", "content": 
      f"""
      You are a smart AI Assistant with general knowledge.
      Your name: Fred
      Your personality: {personality}

      You are currently chatting with: {username}
      
      Chat History:
      {history}
      """
      },
      {"role": "user", "content": message,
       }
    ]

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
  )

  ai_message = completion.choices[0].message
  history.append(f"User:{message}\nAssistant:{ai_message.content}")
  return ai_message

def start_chat():
    personalities = ["Kind", "Funny", "Sarcastic"]
    personality = random.choice(personalities)
    chatting = True
    history = []
    username = input("What's your name: ")
    while chatting:
        if username:
            message = input(f"{username}: ")
            if message == 'quit' or message == 'end':
                chatting = False
            else:
                response = chat(username, message, history, personality)
                print(f"AI: {response.content}\n")
        else:
            username = input("What's your name: ")

start_chat()
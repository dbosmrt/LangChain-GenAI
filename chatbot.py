from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = []

while True:
    user_input = input("You:")
    chat_history.append(user_input)
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    print("AI:", result.content)

print(chat_history)
#Thats it this is the simple chatbot you can make
# we can add system, human and ai messages here as well
#for more context based chat..


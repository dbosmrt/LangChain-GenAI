from langchain_core.prompts import ChatMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
#chat template
chat_template = ChatMessagePromptTemplate(
    [
        ('system','you are a helpful customer support agent'),
        MessagesPlaceholder(variable_name= 'chat_history'),
        ('human', '{query}')
    ]
)

chat_history = []
with open('chat_history.txt') as f:
    chat_history.extent(f.readlines())


print(chat_history)

#create prompt
chat_template.invoke({'chat_history': chat_history, 'query': HumanMessage(content= "Where is my Refund?")})


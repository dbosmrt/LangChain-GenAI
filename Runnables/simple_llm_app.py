from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# Create a prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

# Create output parser
output_parser = StrOutputParser()

# Chain the components together
chain = prompt | llm | output_parser

# Run the app
if __name__ == "__main__":
    response = chain.invoke({"input": "What is the capital of France?"})
    print(response)
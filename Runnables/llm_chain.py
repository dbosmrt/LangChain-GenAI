from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Load the LLM (GPT-3.5)
llm = OpenAI(model_name = "gpt-3.5-turbo", temperature = 0.6)

prompt = PromptTemplate(
    input_variables=['topic'], #defines what input is needed
    template = 'Suggest a catchy blog title about {topic}.'
)


chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain with a specific topic
topic = input("Enter a topic")
output = chain.run(topic)

print("Generate Blog Title:", output)


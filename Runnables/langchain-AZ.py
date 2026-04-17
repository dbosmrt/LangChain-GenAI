import random 
class FakeLLM:
    def __init__(self):
        print("LLM Created")


    def predict(self, prompt):

        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket leauge',
            'AI stands for Artificial Intelligence'
        ]

        return {'response': random.choice(response_list)}
    

class FakePromptTemplate:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables


    def format(self, input_dict):
        return self.template.format(**input_dict)
    

template = FakePromptTemplate(
    template = 'Write a poem about {topic}',
    input_variables= ['topic']
)

class FakeLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def runt(self, input_dic):
        result = self.llm.predict(final_prompt)
        return result['response']


chain = FakeLLMChain(llm, template)

chain.run({'length': 'short', 'topic': 'India'})


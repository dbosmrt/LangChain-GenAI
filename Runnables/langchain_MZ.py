from abc import ABC, abstractmethod
import random 



class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass



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
    

class RunnableConnector(Runnable):

    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data)
        for runnable in self.runnable_list:
           input_data = runnable.invoke(input_data)


template = FakePromptTemplate(
    template = 'Write a poem about {topic}',
    input_variables= ['topic']
)

chain = RunnableConnector(prompt, llm)



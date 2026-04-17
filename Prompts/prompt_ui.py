from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

st.header("Research Tool")
paper_input = st.selectbox("select research paper name", '------')
style_input = st.selectbox("select expalnation style [],[],[]")
length_input = st.selectbox("select explanation length [],[],[]")

model = []
#template
template = PromptTemplate(
    template = ''''
    Here will be the prompt template
    ''',
    input_variables= ['paper_input', 'style_input', 'length_input']

)

#fill the placeholders
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'lenth_input': length_input
})


if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
    

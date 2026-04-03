

import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


#prompt template

prompt=ChatPromptTemplate.from_message(
    [
        ("system","you are a helpful assistant. please respond to the question asked"),
        ("user","question{question}")
    ]
)


# designing of streamlit framwork

st.title("Langcahin demo with LLAMA2")
input_text=st.text_input("what question you have in your mind")


## calling Ollana llama2 model

llm=Ollama("gemma:2b") # it is a google open source model
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
    

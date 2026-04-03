import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond clearly."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain Demo with Ollama (gemma:2b)")
input_text = st.text_input("Ask your question:")

# LLM (make sure Ollama is running locally)
llm = Ollama(model="gemma:2b")

# Output parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

# Run app
if input_text:
    with st.spinner("Thinking..."):
        try:
            response = chain.invoke({"question": input_text})
            st.success(response)
        except Exception as e:
            st.error(f"Error: {e}")
#streamlit+langchainollama(LLM-gemma2:2b model)
#imporrt required librares

import os
import streamlit as st

#import python built in module 

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#step 1 - create prompt template 
#this define how AI should behave and how it receives user input

prompt = ChatPromptTemplate.from_messages(
    [
        #system message defines AI behavior
        ("system","You are  helpul assitant . Please respond clearly to the Questions asked"),
        #user msg contains placeholder 
        ("user","Question :  {question}")
    ]
)
#step 2 :stream ap UI
#app title
st.title("langchain demo with gemma model(ollama)")

#text input-box for user question
input_txt = st.text_input("What question do you have in your mind")

#step 3 : load ollama model 
LLM = Ollama(model="gemma2:2b") 

#condition - convert output model to string

output_parser = StrOutputParser()


# create langchain pipeline (prompt -->model --> output_parser)
chain = prompt | LLM | output_parser

#step 4 - run the model when user inputs the question 
if input_txt : 
    response = chain.invoke({"question":input_txt})
    st.write(response)




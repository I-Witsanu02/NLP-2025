"""
Original
Anothor: Tim Ruscica techwithtim
Source: https://github.com/techwithtim/LocalAIAgentWithRAG
Modified by: I.Witsanu 
"""
import streamlit as st
from vector import retriever
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# สร้างตัวแปร model
model = OllamaLLM(model="llama3.2")

# สร้าง Prompt Template
template = """
You are an expert in answering questions about restaurant reviews.

Here are some relevant restaurant reviews: {reviews}

User question: {question}

Please provide a helpful answer based on the reviews above.
"""
# สร้างตัวแปร prompt
prompt = ChatPromptTemplate.from_template(template)

# สร้าง Chain 
chain = prompt | model

def call_agent(query):
    """Call the RAG chain with the user query"""

    try:
       reviews = retriever.invoke(query)
       response = chain.invoke({"reviews": reviews, "question": query})
       return response
    
    except Exception as e:
       return f"Error: {str(e)}"
    
st.title("Restaurant Reviews Chatbot")

with st.sidebar:
    st.header("Settings")

if query := st.chat_input("Ask about restaurant reviews"):
    st.chat_message("user").write(query)

    response = call_agent(query)
    st.chat_message("Reviwe").write(response)

    # response = call_agent(query)
    # st.chat_message("Reviwe").write(response)
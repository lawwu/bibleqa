import streamlit as st
from ragatouille import RAGPretrainedModel
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = st.secrets["LANGCHAIN_API_KEY"]
os.environ["LANGCHAIN_PROJECT"] = "bibleqa"

path_to_index = ".ragatouille/colbert/indexes/ESV/"
RAG = RAGPretrainedModel.from_index(path_to_index)

st.header("Bible Q&A")
st.write(
"""
Ask a question about the Bible and get an answer.

This uses ColBERT embeddings to retrieve relevant passages from the Bible (ESV) and then uses OpenAI's `gpt-3.5-turbo-0125` to answer the question.
"""
)

llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
prompt = ChatPromptTemplate.from_template(
"""Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}"""
)

retriever = RAG.as_langchain_retriever(k=10)
document_chain = create_stuff_documents_chain(llm, prompt)
retrieval_chain = create_retrieval_chain(retriever, document_chain)

with st.form(key="query_form"):
    query = st.text_input("Enter a query", "What does the Bible say about money?")
    submit_button = st.form_submit_button(label="Submit")
if submit_button:
    output = retrieval_chain.invoke({"input": query})

    st.header("Answer")
    st.write(output["answer"])

    st.header("Context")
    st.write(output["context"])

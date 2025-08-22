from langchain_openai import  AzureChatOpenAI
import streamlit as st

st.title("Ask Anything")



with st.sidebar:
    st.title("Add Your AZURE OPENAI Credentials First")
    AZURE_ENDPOINT = st.text_input("AZURE_ENDPOINT", type="password")
    AZURE_API_KEY = st.text_input("AZURE_API_KEY", type="password")
    AZURE_DEPLOYMENT_NAME = st.text_input("AZURE_DEPLOYMENT_NAME", type="password")
    AZURE_API_VERSION = st.text_input("AZURE_API_VERSION", type="password")
if not AZURE_ENDPOINT:
    st.info("Enter your AZURE_ENDPOINT to continue")
    st.stop()
elif not AZURE_API_KEY:
    st.info("Enter your AZURE_API_KEY to continue")
    st.stop()
elif not AZURE_DEPLOYMENT_NAME:
    st.info("Enter your AZURE_DEPLOYMENT_NAME to continue")
    st.stop()
elif not AZURE_API_VERSION:
    st.info("Enter your AZURE_API_VERSION to continue")
    st.stop()

llm = AzureChatOpenAI(
        azure_endpoint=AZURE_ENDPOINT,
        api_key=AZURE_API_KEY,
        api_version=AZURE_API_VERSION,  # Use a more stable API version
        azure_deployment=AZURE_DEPLOYMENT_NAME,
        temperature=0.7,
        max_tokens=800,
        streaming=False,  # Disable streaming initially
        timeout=30,
        max_retries=3
)

question = st.text_input("Enter the question:")

if question:
    response = llm.invoke(question)
    st.write(response.content)
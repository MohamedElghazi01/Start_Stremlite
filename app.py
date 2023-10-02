import streamlit as st
from langchain.document_loaders import PyPDFDirectoryLoader
import pypdf
import os

st.title(" Extract text from Pdfs pages")
folder="input_folder"

upload=st.upload_file("put your file here",type=".pdf")

if upload is not none :
  loader = PyPDFDirectoryLoader(folder)
  docs = loader.load()
  for i in range(0,len(docs)):
    st.write(docs[i].page_content)
    print("/n")
    


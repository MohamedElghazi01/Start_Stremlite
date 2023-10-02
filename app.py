import streamlit as st
from langchain.document_loaders import PyPDFDirectoryLoader
import pypdf
import os
import shutil

st.title(" Extract text from Pdfs pages")
folder="folder"
# Create a directory if it doesn't exist
if not os.path.exists(folder):
  os.makedirs(folder)
# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
  # Display the uploaded file name and size
  st.write(f"Uploaded file: {uploaded_file.name} ({round(uploaded_file.size / 1024)} KB)")  
  # Check if the folder is not empty and delete the existing file
  if os.listdir(folder):
    st.warning("Warning: The 'folder' directory is not empty. Deleting the existing file...")
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            st.error(f"Error deleting the existing file: {e}")
    # Save the uploaded PDF file to the 'folder' directory
  with open(os.path.join(folder, uploaded_file.name), "wb") as f:
    f.write(uploaded_file.getbuffer())
    st.success(f"File '{uploaded_file.name}' has been successfully saved to '{output_folder}'") 
    
  loader = PyPDFDirectoryLoader(folder)
  docs = loader.load()
  for i in range(0,len(docs)):
    st.write(docs[i].page_content)
    print("/n")
    if i==4:
      break;













# Display the content of the 'folder' directory
st.subheader("Content of the 'folder' directory")
file_list = os.listdir(output_folder)
if file_list:
    for filename in file_list:
        st.write(filename)
else:
    st.info("The 'folder' directory is empty.")




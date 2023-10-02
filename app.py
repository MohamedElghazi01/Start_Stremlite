import streamlit as st
import os
import shutil

# Define the folder name
output_folder = "folder"

# Create a directory if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Streamlit app title
st.title("PDF Uploader")

# Upload PDF file
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    # Display the uploaded file name and size
    st.write(f"Uploaded file: {uploaded_file.name} ({round(uploaded_file.size / 1024)} KB)")

    # Check if the folder is not empty and delete the existing file
    if os.listdir(output_folder):
        st.warning("Warning: The 'folder' directory is not empty. Deleting the existing file...")
        for filename in os.listdir(output_folder):
            file_path = os.path.join(output_folder, filename)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                st.error(f"Error deleting the existing file: {e}")

    # Save the uploaded PDF file to the 'folder' directory
    with open(os.path.join(output_folder, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.success(f"File '{uploaded_file.name}' has been successfully saved to '{output_folder}'")

# Display the content of the 'folder' directory
st.subheader("Content of the 'folder' directory")
file_list = os.listdir(output_folder)
if file_list:
    for filename in file_list:
        st.write(filename)
else:
    st.info("The 'folder' directory is empty.")


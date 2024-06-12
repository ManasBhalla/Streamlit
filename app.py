# %%writefile app.py

import streamlit as st
import PyPDF2
import os

# Function to extract text from PDF file
def extract_text_from_pdf(pdf_file_path):
    # Open the PDF file
    with open(pdf_file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Extract text from each page
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    return text

# Streamlit app
def app():
    st.title("Vendor Contract - Evidence Lab")

    # Folder location to pick up the PDF file
    folder_path = "sample_data"
    st.title(f"The file location is: ", folder_path)

    # Get the list of PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    if pdf_files:
        # Get the first PDF file in the folder
        pdf_file_path = os.path.join(folder_path, pdf_files[0])

        # Extract text from the PDF file
        text = extract_text_from_pdf(pdf_file_path)

        # Display the extracted text
        st.write(f"Extracted Text from {pdf_files[0]}:")
        st.text(text)
    else:
        st.write("No PDF files found in the folder.")

# Run the Streamlit app
if __name__ == "__main__":
    app()

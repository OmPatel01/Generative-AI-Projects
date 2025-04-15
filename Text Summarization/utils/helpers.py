import PyPDF2
import docx

# Function to read text from various file formats (txt, pdf, docx)
def read_file(uploaded_file):
    file_type = uploaded_file.type

    # For .txt file
    if file_type == "text/plain":
        text = uploaded_file.getvalue().decode("utf-8")
    # For .pdf file
    elif file_type == "application/pdf":
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    # For .docx file
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(uploaded_file)
        text = "\n".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file type")
    
    return text

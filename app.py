import os
import io
import PyPDF2
import openai
import streamlit as st

# Load the OpenAI API key from the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")
if openai_api_key is None:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

openai.api_key = openai_api_key

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
    extracted_text = ""
    for page in pdf_reader.pages:
        extracted_text += page.extract_text() + "\n"
    return extracted_text

def get_openai_response(question, context):
    prompt = f"Answer the question based on the context: {context}\n\nQuestion: {question}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

def main():
    st.set_page_config(page_title="PDF Q&A Chatbot by Shivaji", layout="wide")

    # Custom CSS
    st.markdown("""
    <style>
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        color: #1E90FF;
        margin-bottom: 20px;
    }
    .stTextInput>div>div>input {
        font-size: 16px;
    }
    .stButton>button {
        font-size: 16px;
        font-weight: bold;
    }
    .extracted-text {
        background-color: #E6F3FF;
        border-radius: 10px;
        padding: 20px;
        font-size: 14px;
        border: 1px solid #B8D9F3;
        height: 300px;
        overflow-y: auto;
    }
    .output-text {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        font-size: 16px;
        border: 1px solid #d0d3d9;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">PDF Q&A Chatbot by Shivaji</p>', unsafe_allow_html=True)

    # Sidebar for file upload
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
        if uploaded_file is not None:
            st.success("File uploaded successfully!")

    # Main content
    if uploaded_file is not None:
        with st.spinner("Extracting text from PDF..."):
            extracted_text = extract_text_from_pdf(uploaded_file)

        # Two-column layout
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📄 Extracted Text")
            st.markdown(f'<div class="extracted-text">{extracted_text}</div>', unsafe_allow_html=True)

        with col2:
            st.subheader("❓ Ask a Question")
            question = st.text_input("Enter your question about the PDF:")

            if st.button("🔍 Get Answer", key="get_answer"):
                if question:
                    with st.spinner("Generating answer..."):
                        answer = get_openai_response(question, extracted_text)
                    st.markdown("### 💡 Answer:")
                    st.markdown(f'<div class="output-text">{answer}</div>', unsafe_allow_html=True)
                else:
                    st.warning("Please enter a question.")
    else:
        st.info("👈 Please upload a PDF file to get started.")

if __name__ == "__main__":
    main()
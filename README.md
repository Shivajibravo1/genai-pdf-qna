GenAI PDF QnA Chatbot
This is a Streamlit application that allows users to upload PDF files, convert them into text (including image-based PDFs using OCR), and ask questions about the content using an AI-powered QnA system. The application integrates with OpenAI's API for natural language processing and provides a simple, user-friendly interface for interaction.

Features
Upload PDF files (both text-based and image-based).
Extract text from PDFs using Poppler (for text PDFs) and Tesseract (for OCR).
Ask questions about the PDF content using OpenAI's GPT-based API.
Convert scanned image PDFs to searchable text.
Minimal token usage for API efficiency.


Requirements
Python 3.x
Virtual environment for Python (optional but recommended)
Streamlit
OpenAI API Key
Poppler (for PDF-to-image conversion)
Tesseract (for OCR)


Installation

1. Clone the Repository

git clone https://github.com/your-username/genai-pdf-qna.git
cd genai-pdf-qna

3. Set Up the Virtual Environment (Optional)

# Create a virtual environment
python -m venv env

# Activate the virtual environment

# For Windows:
env\Scripts\activate

# For macOS/Linux:
source env/bin/activate


3. Install Dependencies
pip install -r requirements.txt

5. Install Poppler and Tesseract
Poppler
Download Poppler for Windows
Add the Poppler bin folder to your system's PATH.
Tesseract
Download Tesseract
Add the Tesseract folder to your system's PATH.

7. Set OpenAI API Key
Ensure that your OpenAI API key is stored as an environment variable.

export OPENAI_API_KEY="your_openai_api_key"
Or set it up using the .streamlit/secrets.toml file for deployment on Streamlit Cloud.

Usage:
Run the Streamlit application:
streamlit run app.py
Open the application in your browser at http://localhost:8501.

Upload a PDF file using the interface and ask questions about its content using the QnA box.

Deployment (Optional)
You can deploy this application to Streamlit Cloud by connecting it to your GitHub repository and setting your API keys through Streamlit’s Secrets Management.

Contributing
Feel free to fork this repository and submit pull requests if you'd like to contribute!

License
This project is licensed under the MIT License - see the LICENSE file for details.

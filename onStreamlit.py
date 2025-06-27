import os
import requests
from dotenv import load_dotenv
import pymupdf as fitz
from flask import Flask,request,jsonify
import json
import streamlit as st
import os
import fitz  # PyMuPDF
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("PERPLEXITY_API_KEY")
if not api_key:
    st.error("PERPLEXITY_API_KEY not found in .env file")
    st.stop()

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
url = "https://api.perplexity.ai/chat/completions"

def extract_text_from_pdf(pdf_file):
    try:
        with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text.strip()
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return None

def stream_perplexity_response(pdf_text, question):
    payload = {
        "model": "sonar-pro",
        "messages": [
            {
                "role": "system",
                "content": f"""
                You are a helpful assistant analyzing PDF documents. 
                PDF Content: {pdf_text}... [truncated if long]
                """
            },
            {"role": "user", "content": question}
        ],
        "stream": True  # Enable streaming
    }
    
    try:
        with requests.post(url, headers=headers, json=payload, stream=True) as response:
            response.raise_for_status()
            
            # Stream the response
            full_response = ""
            message_placeholder = st.empty()
            
            for chunk in response.iter_lines():
                if chunk:
                    decoded_chunk = chunk.decode("utf-8")
                    if decoded_chunk.startswith("data:"):
                        try:
                            chunk_json = json.loads(decoded_chunk[5:])
                            if "choices" in chunk_json:
                                delta = chunk_json["choices"][0]["delta"]
                                if "content" in delta:
                                    full_response += delta["content"]
                                    message_placeholder.markdown(full_response + "▌")
                        except json.JSONDecodeError:
                            continue
            
            message_placeholder.markdown(full_response)
            return full_response
            
    except Exception as e:
        st.error(f"API Error: {str(e)}")
        return None

# Streamlit UI
st.title("📄 PDF Q&A with Perplexity AI")
st.write("Upload a PDF and ask questions about its content")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
question = st.text_input("Your question")

if uploaded_file and question:
    if st.button("Ask"):
        with st.spinner("Extracting text from PDF..."):
            pdf_text = extract_text_from_pdf(uploaded_file)
        
        if pdf_text:
            st.success("PDF processed successfully!")
            st.divider()
            
            with st.spinner("Generating answer..."):
                stream_perplexity_response(pdf_text, question)
        else:
            st.error("Failed to extract text from PDF")

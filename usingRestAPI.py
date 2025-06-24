import os
import requests
from dotenv import load_dotenv
import pymupdf as fitz
from flask import Flask,request,jsonify
import json

app = Flask(__name__)

#Env 
load_dotenv()
api_key = os.getenv("PERPLEXITY_API_KEY")
if not api_key:
    raise ValueError("API Key not found in environment variables or .env files")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type":"application/json"
}

url = "https://api.perplexity.ai/chat/completions"

#pdf_url = r"D:\College\SEM 4\AI\DA.pdf"

def extract_text_from_pdf(pdf_file):
    try:
        temp_pdf_path = "temp_uploaded_pdf.pdf"
        pdf_file.save(temp_pdf_path)
        
        #text extraction
        doc = fitz.open(temp_pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        
        #remove temp file
        os.remove(temp_pdf_path)
        
        return text.strip()
    except Exception as e:
        raise Exception(f"Error extracting text from PDF: {str(e)}")

@app.route('/ask',methods=['POST'])

def ask_question():
    try:
        #checking if pdf & question are provided
        if 'pdf' not in request.files or 'question' not in request.form:
            return jsonify({"error":"Both 'pdf' & 'question' are required"}),400
        pdf_file = request.files['pdf']
        question = request.form['question']
        
        if not pdf_file or not question:
            return jsonify({"error": "PDF file or question is empty"}), 400
        
        #extract text
        pdf_text = extract_text_from_pdf(pdf_file)
        if not pdf_text:
            return jsonify({"error":"Failed to extract text from PDF"}),500
        
        payload ={
            "model":"sonar-pro",
            "messages": [
                {"role":"system","content":f"You are a helpful assistant, read the given pdf and answer properly. Don't need to cite any source. Just like a normal conversation, here is the pdf: {pdf_text}"},
                {"role":"user","content":question}
            ]
        }
        #sending req to pplx api
        response = requests.post(url,headers=headers,json=payload)
        response.raise_for_status()
        answer = response.json()
        return jsonify({"answer":answer["choices"][0]["message"]["content"]})
    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON response from API", "status_code": response.status_code, "raw_response": response.text}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    except KeyError:
        return jsonify({"error": "Unexpected response structure from API", "response_content": response.text}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

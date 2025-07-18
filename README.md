# 📄 RAG-based Question Answering with Perplexity

This project allows you to upload a PDF and ask natural language questions about its content using the [Perplexity AI](https://www.perplexity.ai) `sonar-pro` model.

It includes two modes:

- 🖥️ **Streamlit App** – A simple drag-and-drop web interface
- 🌐 **Flask REST API** – A backend service you can integrate with your own frontend

---

## 🚀 Features

- ✅ Upload and extract text from PDF files
- 🤖 Ask questions in plain English
- 🔁 Stream or fetch responses via Perplexity API
- 💡 Uses `sonar-pro` model for intelligent and fast answers
- 📦 Two options: Web App (UI) & REST API (backend)

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web interface
- **Flask** – REST API
- **PyMuPDF (`fitz`)** – PDF parsing
- **requests** – HTTP requests to Perplexity API
- **python-dotenv** – Load API keys securely from `.env`

---

## 📁 Project Structure
```
  pdf-qa-perplexity/
  ├── app.py             # Streamlit App (UI)
  ├── api.py             # Flask API version
  ├── .env               # Contains your Perplexity API key (keep it secret)
  ├── requirements.txt   # Python dependencies
  └── README.md          # Project documentation
```
---



## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/pdf-qa-perplexity.git
cd pdf-qa-perplexity
```

### 2. Create virtual env

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install all packages and dependencies 

```bash
pip install -r requirements.txt
```

### 4. Add api key in the .env folder
  PERPLEXITY_API_KEY=your_perplexity_api_key_here
  
### 5. Run the app

```bash
streamlit run app.py
```

using RestAPI

```bash
python api.py
```

---



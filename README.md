# 📄 PDF Q&A with Perplexity AI

An interactive Streamlit app that lets you upload a PDF, ask questions about its content, and get real-time answers powered by Perplexity AI's `sonar-pro` model.

---

## 🚀 Features

- ✅ Upload and read PDF documents
- 🤖 Ask natural language questions about the PDF content
- 🔄 Stream live answers from Perplexity AI
- 🧠 Uses the `sonar-pro` model via Perplexity API
- 🧾 Simple and elegant Streamlit UI

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **PyMuPDF (`fitz`)**
- **Perplexity AI API**
- **dotenv**

---

### File Structure is as: 
  pdf-qa-perplexity/
  ├── app.py                # Main Streamlit app
  ├── .env                  # Your Perplexity API key
  ├── requirements.txt      # Required Python packages
  └── README.md             # This file

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







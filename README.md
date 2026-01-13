# 📘 Study Management AI Bot

The bot is hosted in render .
The hosted Link: https://study-management-ai-bot-1.onrender.com/

A standalone **AI-powered Study Management Engine** built with **Python** and **Streamlit**.  
The application generates **flashcards, quizzes, summaries**, and **answer evaluations** from study content using a modular, provider-agnostic AI design.

This project focuses **only on the AI intelligence layer** and is independent of any backend framework, database, or authentication system.

---

## 🚀 Features

- 📇 **Flashcard Generation**  
  Automatically generates question–answer pairs from study text.

- 📝 **Quiz Generation**  
  Creates multiple-choice questions with one correct answer.

- ✂️ **Notes Summarization**  
  Produces concise summaries while preserving key concepts.

- ✅ **Answer Evaluation**  
  Evaluates user answers against correct answers with a score and feedback.

- 🔌 **Provider-Agnostic Design**  
  Easily switch AI providers by implementing a new provider class.

---

## 🧠 Architecture Overview

```
Streamlit UI
     │
     ▼
Feature Generators
(Flashcards, Quiz, Summary, Evaluation)
     │
     ▼
BaseProvider (Abstract Class)
     │
     ▼
OpenAIProvider (LLM Implementation)
```

---

## 📁 Project Structure

```
.
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not committed)
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation
```

---

## 📦 1. Clone the Repository

```bash
git clone <your-github-repo-url>
cd <your-repo-folder>
```

---

## 🐍 2. Create & Activate Virtual Environment

### Windows (PowerShell)
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📥 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 4. Environment Variables Setup

Create a `.env` file in the project root.

Example `.env`:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ **Never commit your `.env` file to GitHub**

---

## ▶️ 5. Run the Application

Start the Streamlit app using:

```bash
streamlit run app.py
```

The application will open automatically in your default browser.

---
## 🌐 6. Deploy on Render (Live Hosting)

### Step 1: Push Code to GitHub
Ensure your repository contains:
- `app.py`
- `requirements.txt`

---

### Step 2: Create Render Web Service

1. Go to **https://render.com**
2. Click **New → Web Service**
3. Connect your GitHub repository
4. Configure:

| Setting | Value |
|------|------|
| Environment | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0` |
| Instance Type | Free |

---

### Step 3: Add Environment Variables in Render

```
OPENAI_API_KEY = your_openai_api_key_here
```

---

### Step 4: Deploy 🚀

Render will provide a live URL such as:
```
https://study-management-ai.onrender.com
```

---

## 🧪 Example Outputs

### Flashcards
```json
{
  "flashcards": [
    {
      "question": "What is photosynthesis?",
      "answer": "It is the process by which plants use sunlight to produce food."
    }
  ]
}
```

### Quiz
```json
{
  "quiz": [
    {
      "question": "What do plants need for photosynthesis?",
      "options": ["Water", "Sunlight", "Oxygen", "Nitrogen"],
      "correct_answer": "Sunlight"
    }
  ]
}
```

### Summary
```json
{
  "summary": "Photosynthesis is the process by which plants create food using sunlight."
}
```

---

## 🛡 Hallucination Control Strategy

- Strict JSON output enforcement
- Structured prompts
- Low-temperature generation
- Input-grounded responses
- Graceful error handling for invalid outputs

---


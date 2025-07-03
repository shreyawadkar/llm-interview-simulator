# LLM-Powered Interview Simulator 🎤🤖

This is a GPT-4 powered interview simulator that generates behavioral and technical questions tailored to different roles (e.g., SDE, Data Scientist, PM), and allows users to respond, receive feedback, and download transcripts.

## 🔧 Tech Stack
- Python
- Streamlit
- LangChain
- OpenAI API (GPT-4)
- FAISS (for context memory)
- GitHub CI/CD
- Azure/Streamlit Cloud (for deployment)

## 💡 Features
- Dynamic Q&A generation using prompt engineering
- Role-specific interview categories
- GPT-powered answer evaluation
- PDF/CSV transcript download
- Deployable on cloud for live demo

## 📅 Build Timeline
| Day | Task |
|-----|------|
| Mon | Set up UI + repo |
| Tue | OpenAI API integration |
| Wed | Add FAISS context |
| Thu | Add evaluation logic |
| Fri | Deploy + polish |
## 🤝 Collaborated by Shubham Salunke
# 🤖 LLM Interview Simulator

A web app to simulate behavioral and technical interviews using GPT-4.  
Users can select interview roles, generate role-specific questions, submit answers, and receive AI-powered detailed feedback.

---

## Features

- Choose from Software Engineer, Data Scientist, Product Manager, AI Researcher  
- Get randomized interview questions based on selected role  
- Submit your answer and get a scored evaluation with suggestions  
- Download the full transcript (question, answer, feedback)  
- View your history of generated questions during the session  
- Clean, professional UI built with Streamlit

---

## Demo

Try the live app here:  
[https://llm-interview-simulator-mdsd7zxhay3sxkog4k5aei.streamlit.app/](https://llm-interview-simulator-mdsd7zxhay3sxkog4k5aei.streamlit.app/)

---

## Getting Started

### Prerequisites

- Python 3.8 or higher  
- OpenAI API key from [https://platform.openai.com](https://platform.openai.com)  
- (Optional) Git for cloning the repo

### Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/shreyawadkar/llm-interview-simulator.git
   cd llm-interview-simulator
2. (Recommended) Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
3. Install required packages:
   ```bash
   pip install -r requirements.txt
4. Set up your OpenAI API key securely:
   Create a .streamlit/secrets.toml file (do not commit this file) with the following:
   OPENAI_API_KEY = "your_openai_api_key_here"
   
### Running Locally
   Start the Streamlit app with:
   ```bash
   streamlit run app.py
   Then open http://localhost:8501 in your browser.




Deployment on Azure or other cloud platforms

License
MIT License © 2025 Shreyawadkar

Contact
For feedback or questions, email: your-email@example.com

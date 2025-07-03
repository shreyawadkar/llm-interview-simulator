
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
   \```bash
   git clone https://github.com/shreyawadkar/llm-interview-simulator.git
   cd llm-interview-simulator
2. (Recommended) Create and activate a Python virtual environment:
   \```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
3. Install required packages:
   \```bash
   pip install -r requirements.txt
4. Set up your OpenAI API key securely:
   Create a .streamlit/secrets.toml file (do not commit this file) with the following:
   OPENAI_API_KEY = "your_openai_api_key_here"
   \```
   
### Running Locally
   Start the Streamlit app with:
   ```bash
   streamlit run app.py
   Then open http://localhost:8501 in your browser.
\```

## How It Works

- Select an interview role from the sidebar (Software Engineer, Data Scientist, Product Manager, or AI Researcher).  
- Click **Generate Interview Question** to get a role-specific behavioral or technical question.  
- Type your answer in the **Your Answer** box.  
- Click **Submit Answer** to receive AI-powered detailed feedback including a score, strengths, and areas to improve.  
- Download the full transcript of the interview session including all questions, your answers, and feedback for offline review.  
- Your generated questions history is shown at the bottom to revisit earlier questions in the current session.

---

## Deployment

This app is deployed and hosted on Streamlit Cloud and can also be deployed to Microsoft Azure with proper setup.

### Streamlit Cloud Deployment

- Connect your GitHub repository to Streamlit Cloud.  
- Add your OpenAI API key securely in Streamlit Secrets.  
- Deploy with one click and share your app URL.

### Azure Deployment (Optional)

- Use Azure App Services to host the app for scalability.  
- Configure environment variables for your API keys.  
- Automate deployment with CI/CD pipelines via GitHub Actions.

---










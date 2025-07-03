import streamlit as st
import openai
import os
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Page config
st.set_page_config(
    page_title="🤖 LLM Interview Simulator",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for polished look with clean professional style and no background image
st.markdown(
    """
    <style>
    /* Background gradient for entire app */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* White translucent overlay for entire app area including sidebar and main content */
    .css-18e3th9 {  /* Main content container */
        background-color: rgba(255, 255, 255, 0.97) !important;
        border-radius: 12px;
        padding: 2rem 2rem 3rem 2rem !important;
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    }
    .css-1d391kg {  /* Sidebar container */
        background-color: rgba(255, 255, 255, 0.97) !important;
        border-radius: 12px;
        padding: 1rem 1rem 3rem 1rem !important;
        box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    }

    /* Style question box */
    .question-box {
        background-color: #f7f9fc !important;
        padding: 1.25rem 1.75rem !important;
        border-radius: 10px !important;
        font-size: 1.1rem !important;
        margin-bottom: 1.25rem !important;
        border-left: 6px solid #0a66c2 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }

    /* Style answer box */
    .stTextArea > div {
        background: white !important;
        border-radius: 10px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }

    /* Buttons styling */
    .stButton > button {
        background-color: #0a66c2 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        transition: background-color 0.3s ease !important;
    }

    .stButton > button:hover {
        background-color: #004182 !important;
        color: #fff !important;
    }

    /* Headings */
    .title {
        font-size: 3rem !important;
        font-weight: 700 !important;
        color: #0a66c2 !important;
        margin-bottom: 0 !important;
    }

    .subtitle {
        font-size: 1.2rem !important;
        color: #333 !important;
        margin-top: 0 !important;
        margin-bottom: 1rem !important;
    }

    /* History section */
    .css-1kyxreq {
        background: white !important;
        border-radius: 12px !important;
        padding: 1rem 1.5rem !important;
        box-shadow: 0 4px 18px rgba(0,0,0,0.05);
        margin-top: 2rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and subtitle with styled classes
st.markdown('<h1 class="title">🤖 LLM Interview Simulator</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Simulate behavioral and technical interviews using GPT-4.</p>', unsafe_allow_html=True)

# Role-based questions
role_questions = {
    "Software Engineer": [
        "Tell me about a time you faced a technical challenge and how you resolved it.",
        "Explain a complex system you designed and your approach to scalability.",
        "Describe a situation where you improved the performance of an application."
    ],
    "Data Scientist": [
        "Describe a project where you built a predictive model. What challenges did you face?",
        "How do you handle missing data in a dataset? Give an example.",
        "Explain how you would evaluate the performance of a classification model."
    ],
    "Product Manager": [
        "How do you prioritize features in a product roadmap?",
        "Describe a time you had to handle conflicting stakeholder requirements.",
        "Explain how you measure product success."
    ],
    "AI Researcher": [
        "Describe your experience with developing or fine-tuning large language models.",
        "How do you approach evaluating model bias and fairness?",
        "Explain a novel AI technique you implemented and its impact."
    ],
}

# Role-based feedback styles
feedback_styles = {
    "Software Engineer": "Provide detailed, technical feedback focusing on coding, problem-solving, and system design.",
    "Data Scientist": "Offer analytical feedback emphasizing statistical reasoning, data interpretation, and model evaluation.",
    "Product Manager": "Give business-oriented feedback focusing on communication skills, prioritization, and stakeholder management.",
    "AI Researcher": "Provide research-focused feedback, discussing algorithmic depth, innovation, and ethical considerations."
}

# Initialize prompt history list if missing
if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []

# Sidebar - Role selector & buttons
with st.sidebar:
    st.header("⚙️ Settings")
    selected_role = st.selectbox("Choose interview role:", list(role_questions.keys()))
    generate_btn = st.button("🎯 Generate Interview Question")

if generate_btn:
    question = random.choice(role_questions.get(selected_role, ["Tell me about a time you faced a technical challenge and how you resolved it."]))
    st.session_state.question = f"[{selected_role}] {question}"
    st.session_state.feedback = ""
    st.session_state.user_answer = ""
    st.session_state.prompt_history.append(st.session_state.question)

st.markdown("---")

# Main area layout: question & answer side by side on wide screens
if "question" in st.session_state:
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="question-box">', unsafe_allow_html=True)
        st.markdown(f"### 🎯 Interview Question\n\n{st.session_state.question}")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        user_answer = st.text_area(
            "📝 Your Answer:",
            value=st.session_state.get("user_answer", ""),
            height=180,
            placeholder="Type your answer here...",
            key="answer_input"
        )
        st.session_state.user_answer = user_answer

        submit_btn = st.button("🚀 Submit Answer")

        if submit_btn:
            if not user_answer.strip():
                st.warning("⚠️ Please enter your answer before submitting.")
            else:
                with st.spinner("Evaluating your response..."):
                    style_instruction = feedback_styles.get(selected_role, "Provide clear and constructive feedback.")

                    prompt = f"""
You are a technical recruiter. {style_instruction} Evaluate the following interview response.

Question: {st.session_state.question}
Candidate's Answer: {user_answer}

Give:
1. A score out of 10
2. What was good about the answer
3. What can be improved
4. Suggest a better response if necessary

Format the reply in Markdown with bullet points.
"""
                    try:
                        response = openai.ChatCompletion.create(
                            model="gpt-4",
                            messages=[{"role": "user", "content": prompt}]
                        )
                        st.session_state.feedback = response.choices[0].message.content
                    except Exception as e:
                        st.error("❌ OpenAI API Error:")
                        st.exception(e)

st.markdown("---")

# Feedback & download section
if st.session_state.get("feedback"):
    with st.expander("📝 Interview Feedback (click to expand)"):
        st.markdown(st.session_state.feedback)

    transcript_content = f"""
Interview Question:
{st.session_state.get('question', '')}

Your Answer:
{st.session_state.get('user_answer', '')}

Interview Feedback:
{st.session_state.get('feedback', '')}
"""
    st.download_button(
        label="📥 Download Full Transcript",
        data=transcript_content,
        file_name="interview_full_transcript.txt",
        mime="text/plain",
    )

# Generated questions history
if st.session_state.prompt_history:
    st.markdown("📜 **Generated Questions History:**")
    for idx, q in enumerate(st.session_state.prompt_history, 1):
        st.write(f"{idx}. {q}")

st.markdown("<br>", unsafe_allow_html=True)

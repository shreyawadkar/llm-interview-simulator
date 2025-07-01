import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit UI
st.set_page_config(page_title="LLM Interview Simulator", layout="centered")
st.title("🤖 LLM Interview Simulator")
st.markdown("Simulate behavioral and technical interviews using GPT-4.")

roles = ["Software Engineer", "Data Scientist", "Product Manager", "AI Researcher"]
selected_role = st.selectbox("Choose a role:", roles)

if "question" not in st.session_state:
    st.session_state.question = ""

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# Generate Interview Question
if st.button("Generate Interview Question"):
    st.session_state.question = f"[{selected_role}] Tell me about a time you faced a technical challenge and how you resolved it."
    st.session_state.feedback = ""

# Display Question and Textbox
if st.session_state.question:
    st.success(st.session_state.question)
    user_answer = st.text_area("Your Answer:")

    # Submit Answer
    if st.button("Submit Answer"):
        if user_answer.strip() == "":
            st.warning("Please enter your answer before submitting.")
        else:
            with st.spinner("Evaluating your response..."):
                prompt = f"""
You are a technical recruiter. Evaluate the following interview response.

Question: {st.session_state.question}
Candidate's Answer: {user_answer}

Provide:
1. A score out of 10
2. What was good about the answer
3. What could be improved
4. Suggest a better response if needed

Format the reply in markdown with bullet points.
"""
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.session_state.feedback = response.choices[0].message.content
                except Exception as e:
                    st.error(f"❌ OpenAI Error: {e}")

# Display Feedback
if st.session_state.feedback:
    st.markdown("### 📝 Interview Feedback")
    st.markdown(st.session_state.feedback)

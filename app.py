import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_ke
if not api_key:
    st.error("API key not loaded. Check your .env file!")


# Streamlit App UI
st.set_page_config(page_title="LLM Interview Simulator", layout="centered")
st.title("🤖 LLM Interview Simulator")
st.markdown("Simulate behavioral and technical interviews using GPT-4.")

roles = ["Software Engineer", "Data Scientist", "Product Manager", "AI Researcher"]
selected_role = st.selectbox("Choose a role:", roles)

# Generate question
if st.button("Generate Interview Question"):
    st.session_state.question = f"[{selected_role}] Tell me about a time you faced a technical challenge and how you resolved it."
    st.session_state.feedback = ""

# Show question and answer box
if "question" in st.session_state:
    st.success(st.session_state.question)
    if "user_answer" not in st.session_state:
        st.session_state.user_answer = ""

    st.session_state.user_answer = st.text_area("Your Answer", value=st.session_state.user_answer)

    if st.button("Submit Answer"):
        if not st.session_state.user_answer.strip():
            st.warning("Please enter your answer before submitting.")
        else:
            with st.spinner("Evaluating your response..."):
                prompt = f"""
You are a technical recruiter. Evaluate the following interview response.

Question: {st.session_state.question}
Candidate's Answer: {st.session_state.user_answer}

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
                    st.error(f"OpenAI API Error: {e}")

# Show feedback
if "feedback" in st.session_state and st.session_state.feedback:
    st.markdown("### 📝 Interview Feedback")
    st.markdown(st.session_state.feedback)


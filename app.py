import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
print("🔑 DEBUG - Loaded API Key:", os.getenv("OPENAI_API_KEY"))

api_key = os.getenv("OPENAI_API_KEY")
print("Loaded Key:", api_key)  # ✅ Now api_key is defined before this line
openai.api_key = api_key

# Streamlit UI setup
st.set_page_config(page_title="LLM Interview Simulator", layout="centered")
st.title("🤖 LLM Interview Simulator")
st.markdown("Simulate behavioral and technical interviews using GPT-4.")

# Role selector
roles = ["Software Engineer", "Data Scientist", "Product Manager", "AI Researcher"]
selected_role = st.selectbox("Choose a role:", roles)

# Generate Question Button
if st.button("Generate Interview Question"):
    st.session_state.question = f"[{selected_role}] Tell me about a time you faced a technical challenge and how you resolved it."
    st.session_state.feedback = ""
    st.session_state.user_answer = ""

# If question was generated
if "question" in st.session_state:
    st.success(st.session_state.question)

    # Input answer
    user_answer = st.text_area("Your Answer:", value=st.session_state.get("user_answer", ""))
    st.session_state.user_answer = user_answer

    # Submit button
    if st.button("Submit Answer"):
        if not user_answer.strip():
            st.warning("Please enter your answer before submitting.")
        else:
            with st.spinner("Evaluating your response..."):
                try:
                    prompt = f"""
You are a technical recruiter. Evaluate the following interview response.

Question: {st.session_state.question}
Candidate's Answer: {user_answer}

Give:
1. A score out of 10
2. What was good about the answer
3. What can be improved
4. Suggest a better response if necessary

Format the reply in Markdown with bullet points.
"""
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    st.session_state.feedback = response.choices[0].message.content
                except Exception as e:
                    st.error(f"OpenAI API Error: {e}")

# Display Feedback
if st.session_state.get("feedback"):
    st.markdown("### 📝 Interview Feedback")
    st.markdown(st.session_state.feedback)

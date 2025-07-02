import streamlit as st
import openai
import os
from dotenv import load_dotenv
import random

# Load environment variables
load_dotenv()

# Debug print to verify if key is loaded
api_key = os.getenv("OPENAI_API_KEY")
print("🔑 DEBUG - Loaded API Key:", api_key)

# Set OpenAI API key
openai.api_key = api_key

# Streamlit UI setup
st.set_page_config(page_title="LLM Interview Simulator", layout="centered")
st.title("🤖 LLM Interview Simulator")
st.markdown("Simulate behavioral and technical interviews using GPT-4.")

# Define role-based questions
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

# Define role-based feedback styles
feedback_styles = {
    "Software Engineer": "Provide a detailed, technical feedback focusing on coding, problem-solving, and system design.",
    "Data Scientist": "Offer analytical feedback emphasizing statistical reasoning, data interpretation, and model evaluation.",
    "Product Manager": "Give business-oriented feedback focusing on communication skills, prioritization, and stakeholder management.",
    "AI Researcher": "Provide research-focused feedback, discussing algorithmic depth, innovation, and ethical considerations."
}

# Initialize prompt history list if it doesn't exist
if "prompt_history" not in st.session_state:
    st.session_state.prompt_history = []

# Role selector
roles = list(role_questions.keys())
selected_role = st.selectbox("Choose a role:", roles)

# Generate Interview Question
if st.button("Generate Interview Question"):
    question = random.choice(role_questions.get(selected_role, ["Tell me about a time you faced a technical challenge and how you resolved it."]))
    st.session_state.question = f"[{selected_role}] {question}"
    st.session_state.feedback = ""
    st.session_state.user_answer = ""

    # Log the generated question
    st.session_state.prompt_history.append(st.session_state.question)

# Display Question & Input
if "question" in st.session_state:
    st.success(st.session_state.question)

    user_answer = st.text_area("Your Answer:", value=st.session_state.get("user_answer", ""))
    st.session_state.user_answer = user_answer

    if st.button("Submit Answer"):
        if not user_answer.strip():
            st.warning("Please enter your answer before submitting.")
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

# Display Feedback
if st.session_state.get("feedback"):
    with st.expander("📝 Interview Feedback (click to expand)"):
        st.markdown(st.session_state.feedback)

    # Create transcript content
    transcript_content = f"""
Interview Question:
{st.session_state.get('question', '')}

Your Answer:
{st.session_state.get('user_answer', '')}

Interview Feedback:
{st.session_state.get('feedback', '')}
"""

    # Show download button only after feedback is present
    st.download_button(
        label="📥 Download Full Transcript",
        data=transcript_content,
        file_name="interview_full_transcript.txt",
        mime="text/plain"
    )

# Display Generated Questions History
if st.session_state.prompt_history:
    st.markdown("📜 **Generated Questions History**")
    for idx, q in enumerate(st.session_state.prompt_history, 1):
        st.write(f"{idx}. {q}")

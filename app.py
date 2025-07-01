import streamlit as st

# --- App title and description ---
st.set_page_config(page_title="LLM Interview Simulator", layout="centered")
st.title("🤖 LLM Interview Simulator")
st.markdown("Simulate behavioral and technical interviews using GPT-4.")

# --- Role selection ---
roles = ["Software Engineer", "Data Scientist", "Product Manager", "AI Researcher"]
selected_role = st.selectbox("Choose a role:", roles)

# --- Question display (dummy for now) ---
if st.button("Generate Interview Question"):
    st.success(f"**[{selected_role}]** Tell me about a time you faced a technical challenge and how you resolved it.")
    answer = st.text_area("Your Answer:")
    if st.button("Submit Answer"):
        st.info("✅ GPT evaluation coming soon...")
        if submit and user_answer:
    with st.spinner("Evaluating your response..."):
        evaluation_prompt = f"""
You are a technical recruiter. Evaluate the following interview response.

Question: {question}
Candidate's Answer: {user_answer}

Give:
1. A score out of 10
2. What was good about the answer
3. What can be improved
4. Suggest a better response if necessary

Format your reply in Markdown with bullet points.
"""

        feedback = get_completion(evaluation_prompt)

    st.markdown("### 📝 Interview Feedback")
    st.markdown(feedback)



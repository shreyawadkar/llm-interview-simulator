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


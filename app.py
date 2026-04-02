import streamlit as st
from openai import OpenAI
import os
import streamlit as st
st.write("THIS IS MY FILE") 

# --- OpenRouter Client ---
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #4CAF50; color: white; }
    .stTextInput>div>div>input { border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

# --- MAIN UI ---
st.title("🤖 AI Career Guidance Assistant")
st.write("Enter your details below to get a personalized career roadmap!")

# --- FORM ---
with st.form("user_profile"):
    col1, col2 = st.columns(2)

    with col1:
        education = st.selectbox(
            "Education Level",
            ["High School", "Undergraduate", "Graduate", "Working Professional"]
        )
        interests = st.text_input("Interests (e.g., AI, 3D Design, Gaming)")

    with col2:
        skills = st.text_input("Current Skills (e.g., Python, CSS, Math)")
        goals = st.text_input("Career Goal (e.g., Get a job at TCS, Start a startup)")

    submitted = st.form_submit_button("Generate My Roadmap")

# --- LOGIC ---
if submitted:
    try:
        prompt = f"""
You are an expert Career Guidance Coach.

Student Profile:
- Education: {education}
- Interests: {interests}
- Skills: {skills}
- Goals: {goals}

Provide:
1. Suggested Career Title
2. Why this fits
3. 3-month roadmap (Month 1, 2, 3)
4. Projects to build
5. Salary & job outlook
"""

        with st.spinner("Generating your roadmap..."):
            response = client.chat.completions.create(
                model="meta-llama/llama-3.1-8b-instruct",
                messages=[{"role": "user", "content": prompt}],
            )

        roadmap = response.choices[0].message.content

        st.success("Analysis Complete!")
        st.markdown("---")
        st.markdown(roadmap)

    except Exception as e:
        st.error(f"An error occurred: {e}")

# --- FOOTER ---
st.markdown("---")
st.caption("Built with ❤️ and a bloodfull of hardwork")
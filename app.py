import streamlit as st
from google import genai

st.set_page_config(page_title="Tech.ai App", page_icon="🤖")
st.title("🤖 Tech.ai Assistant")

# Use the environment-free initialization
client = genai.Client()

user_prompt = st.text_input("You:", placeholder="Ask your AI something...")

if user_prompt:
    with st.spinner("Thinking..."):
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=user_prompt,
            )
            st.success("AI Response:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

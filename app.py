import streamlit as st
from openai import OpenAI

# Load API key from Streamlit Secrets
# Make sure you set OPENAI_API_KEY in Streamlit Cloud → Settings → Secrets
client = OpenAI(api_key=st.secrets["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"])

st.set_page_config(page_title="Mood-Based AI Art Generator", page_icon="🎨")

st.title("🎨 Mood-Based AI Art Generator")
st.write("Describe your current mood and watch it turn into AI-generated art.")

# Mood input
mood = st.text_input("How are you feeling today? (Describe in a sentence)")

if st.button("Generate Art 🎨"):
    if not mood.strip():
        st.error("Please describe your mood before generating art.")
    else:
        try:
            # Generate image
            response = client.images.generate(
                model="gpt-image-1",
                prompt=f"An artistic representation of the feeling: {mood}",
                size="1024x1024"
            )

            image_url = response.data[0].url
            st.image(image_url, caption=f"Your mood: {mood}")

        except Exception as e:
            st.error(f"Error: {e}")

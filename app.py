import streamlit as st
from textblob import TextBlob
from openai import OpenAI
import os

# Set your OpenAI API key directly here
openai.api_key = "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"

st.title("🎨 Mood-Based AI Art Generator")
st.markdown("Type how you feel and let AI turn it into art.")

# Get user input
user_input = st.text_input("How are you feeling today?")

# Detect emotion from text
def get_emotion(text):
    blob = TextBlob(text)
    score = blob.sentiment.polarity
    if score > 0.5:
        return "joyful"
    elif score > 0.2:
        return "hopeful"
    elif score < -0.5:
        return "sad"
    elif score < -0.2:
        return "anxious"
    else:
        return "calm"

# Generate image from DALL·E
from openai import OpenAI

client = OpenAI(api_key="your_api_key_here")

def generate_image(emotion):
    prompt = f"Abstract digital painting inspired by {emotion}, expressive texture, emotional color scheme"
    response = client.images.generate(
        model="dall-e-3",   # You can also try "dall-e-2" if needed
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return response.data[0].url

# Main logic
if st.button("Generate Art") and user_input:
    emotion = get_emotion(user_input)
    st.write(f"Detected Emotion: **{emotion}**")
    img_url = generate_image(emotion)
    st.image(img_url, caption=f"Art based on your mood: {emotion}")

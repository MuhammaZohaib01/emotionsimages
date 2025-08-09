import streamlit as st
from textblob import TextBlob
from openai import OpenAI

# Initialize OpenAI client
OPENAI_API_KEY = "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"
st.set_page_config(page_title="Mood-Based AI Art Generator 🎨", layout="centered")
st.title("🎨 Mood-Based AI Art Generator")
st.markdown("Type how you're feeling, and watch your emotion become AI-generated art.")

# Step 1: Detect emotion from text
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

# Step 2: Generate image using DALL·E 3
def generate_image(emotion):
    prompt = f"Abstract digital art representing the emotion {emotion}, colorful emotional textures, modern and expressive style"
    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        return response.data[0].url
    except Exception as e:
        return f"Error: {e}"

# Step 3: UI
user_input = st.text_input("📝 How are you feeling today? (Describe in one sentence)")

if st.button("🎨 Generate Art") and user_input:
    emotion = get_emotion(user_input)
    st.success(f"Detected Emotion: **{emotion}**")
    
    img_url = generate_image(emotion)
    if img_url.startswith("http"):
        st.image(img_url, caption=f"Art based on your emotion: {emotion}", use_column_width=True)
    else:
        st.error(img_url)


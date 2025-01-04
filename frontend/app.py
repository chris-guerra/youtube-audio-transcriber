import streamlit as st
import requests

# Backend URL
BACKEND_URL = "http://backend:8000/download-audio/"

# App Title
st.title("YouTube Audio Downloader 🎵")

# Subtitle
st.markdown("Enter a **YouTube URL** below to download and play audio!")

# Input field for YouTube URL
url = st.text_input("YouTube URL:", placeholder="Paste your YouTube link here...")

# Submit button
if st.button("Download Audio"):
    # Show loading indicator
    with st.spinner("Downloading and processing audio..."):
        try:
            # Send request to backend
            response = requests.post(BACKEND_URL, json={"url": url})

            # Handle response
            if response.status_code == 200:
                data = response.json()

                # Extract details
                audio_url = f"http://localhost:8000{data['audio_url']}"  # Full URL for streaming
                title = data.get("title")

                # Display title
                #st.success(f"**Title:** {title}")

                # Display audio player
                with st.expander(f"🎧 {title}", expanded=True):
                    st.audio(audio_url)  # Use streaming URL for audio playback

            else:
                st.error(f"Failed to download audio: {response.json()['detail']}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
import streamlit as st
import requests

BACKEND_URL = "http://backend:8000/api/metadata/"

st.title("YouTube Metadata Extractor 🎥")

url = st.text_input("Enter YouTube URL:")
language = st.radio("Select Subtitle Language:", ["auto", "en", "es"], horizontal=True)

if st.button("Extract Metadata"):
    with st.spinner("Processing..."):
        try:
            response = requests.post(BACKEND_URL, json={"url": url, "language": language})
            if response.status_code == 200:
                data = response.json()

                st.subheader("Metadata")
                st.write(f"**Title:** {data['metadata']['title']}")
                st.write(f"**Description:** {data['metadata']['description']}")
                st.write(f"**Upload Date:** {data['metadata']['upload_date']}")
                st.write(f"**Tags:** {', '.join(data['metadata']['tags'] or [])}")

                st.subheader("Cleaned Transcription")
                st.text_area("Transcript:", data["transcription"], height=300)

            else:
                st.error(f"Error: {response.json()['detail']}")
        except Exception as e:
            st.error(f"Error: {str(e)}")
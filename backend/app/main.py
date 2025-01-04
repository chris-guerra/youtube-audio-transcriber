from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.youtube_audio_downloader import download_audio

app = FastAPI()

# Input model for YouTube URL
class YouTubeInput(BaseModel):
    url: str


@app.get("/")
def root():
    return {"message": "YouTube Audio Downloader is Running!"}


@app.post("/download-audio/")
def download_audio_endpoint(input: YouTubeInput):
    """
    Endpoint to download audio from YouTube URL.
    """
    try:
        # Call the downloader and get the file path and title
        result = download_audio(input.url)
        return {
            "message": "Download successful!",
            "file_path": result['file_path'],
            "title": result['title']  # Return the video title to frontend
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
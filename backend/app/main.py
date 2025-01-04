from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from services.youtube_audio_downloader import download_audio
import os

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
        # Download audio and get details
        result = download_audio(input.url)
        file_path = result['file_path']
        title = result['title']

        # Return title and API URL to stream audio
        return {
            "message": "Download successful!",
            "audio_url": f"/stream-audio/?file_path={file_path}",  # New endpoint to stream audio
            "title": title
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stream-audio/")
def stream_audio(file_path: str):
    """
    Serve audio file for streaming.
    """
    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise HTTPException(status_code=404, detail="File not found.")

        # Serve file as a response
        return FileResponse(file_path, media_type="audio/wav")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
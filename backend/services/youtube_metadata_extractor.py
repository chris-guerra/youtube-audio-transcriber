import yt_dlp
import os
import tempfile
from typing import Dict


def extract_metadata_and_subtitles(url: str, language: str = "auto") -> Dict:
    """
    Extract metadata and subtitles from a YouTube video in the selected language.
    """
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()

        # yt-dlp options with restricted languages
        ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': [language],  # Supported languages: auto, en, es
            'subtitlesformat': 'vtt',
            'skip_download': True,  # Skip audio download
            'outtmpl': os.path.join(temp_dir, '%(id)s.%(ext)s'),
        }

        # Extract metadata and subtitles
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            # Metadata
            metadata = {
                "title": info.get("title"),
                "description": info.get("description"),
                "upload_date": info.get("upload_date"),
                "duration": info.get("duration"),
                "tags": info.get("tags"),
                "available_languages": list(info.get("subtitles", {}).keys()),  # Available languages
            }

            # Locate subtitles
            video_id = info.get("id")
            subtitle_path = os.path.join(temp_dir, f"{video_id}.{language}.vtt")

            # Read subtitles
            transcription = "No subtitles available."
            if os.path.exists(subtitle_path):
                with open(subtitle_path, "r") as file:
                    transcription = file.read()

            return {
                "metadata": metadata,
                "transcription": transcription,
                "languages": ['auto', 'en', 'es'],  # Limited language options
            }

    except Exception as e:
        raise Exception(f"Failed to process video: {str(e)}")
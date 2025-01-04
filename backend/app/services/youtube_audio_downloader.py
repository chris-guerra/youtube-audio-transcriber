import yt_dlp
import os
import tempfile


def download_audio(url: str) -> dict:
    """
    Downloads audio from a given YouTube URL as a WAV file.
    Stores the file in a temporary directory.
    Returns the file path and the video title.
    """
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        print(f"Temporary directory created at: {temp_dir}")

        # yt-dlp options
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(temp_dir, '%(id)s.%(ext)s'),  # Use video ID for filename
            'quiet': False,
            'ffmpeg_location': '/usr/bin/ffmpeg',  # Explicitly set FFmpeg path
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        }

        # Download audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)  # Extract metadata and download
            print(f"INFO: yt-dlp metadata: {info}")

            # Extract the title and file path
            video_title = info['title']  # Get the YouTube video title
            video_id = info['id']  # Use video ID for filename
            file_path = os.path.join(temp_dir, f"{video_id}.wav")  # Match yt-dlp filename format

            # Debug file path
            print(f"INFO: Expected file path: {file_path}")

            # Ensure the file exists
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Audio file was not found at {file_path}")

            # Return file path and video title
            return {"file_path": file_path, "title": video_title}

    except Exception as e:
        import traceback
        traceback.print_exc()  # Log detailed error
        raise Exception(f"Failed to download audio: {e}")
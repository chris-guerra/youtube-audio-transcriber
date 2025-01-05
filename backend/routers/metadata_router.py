from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.youtube_metadata_extractor import extract_metadata_and_subtitles
from services.llm_processor import LLMProcessor

router = APIRouter()
mistral_processor = LLMProcessor(
    model_path="/models/mistral-7b-instruct-v0.1.Q4_0.gguf", model_type="mistral"
)

class YouTubeRequest(BaseModel):
    url: str
    language: str = "auto"

@router.post("/metadata/")
async def get_metadata_and_transcription(request: YouTubeRequest):
    try:
        data = extract_metadata_and_subtitles(request.url, request.language)
        cleaned_transcription = mistral_processor.clean_transcription(data["transcription"])
        return {
            "metadata": data["metadata"],
            "transcription": cleaned_transcription,
            "languages": data["languages"],
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
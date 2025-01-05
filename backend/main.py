from fastapi import FastAPI
from routers.metadata_router import router

# Initialize the app
app = FastAPI()

# Include the metadata router
app.include_router(router, prefix="/api", tags=["Metadata"])

@app.get("/")
def root():
    return {"message": "YouTube Metadata Extractor API"}
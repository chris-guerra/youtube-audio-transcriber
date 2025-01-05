# **YouTube Metadata Extractor with LLM Processing**  

---

## **Project Overview**  

The **YouTube Metadata Extractor** is a web application that allows users to extract **metadata** (title, description, upload date, duration, and tags) and **transcriptions** from YouTube videos. The transcriptions are cleaned using a **local LLM model** (e.g., **LLaMA 2** or **Mistral**) to remove formatting artifacts and improve readability.  

---

## **Features**  

- **Metadata Extraction**: Fetches video details like title, description, upload date, duration, and tags.  
- **Subtitle Transcription**: Automatically downloads available subtitles or generates auto-captions.  
- **LLM Cleaning**: Uses a local **LLM model** to clean and enhance subtitle readability.  
- **Streamlit Frontend**: User-friendly web interface to process YouTube videos and view results.  
- **Scalable Backend**: Built with **FastAPI** to handle future extensions like summarization and translation.  

---

## **Folder Structure**  

```bash
youtube-metadata-extractor/
├── backend/
│   ├── services/
│   │   ├── youtube_metadata_extractor.py   # Extract metadata & subtitles
│   │   ├── llm_processor.py                # Process transcriptions with LLM
│   ├── routers/
│   │   ├── metadata_router.py              # API route for metadata & transcription
│   ├── main.py                             # FastAPI app with routing
│   ├── Dockerfile                           # Backend Docker configuration
│   ├── requirements.txt                     # Backend dependencies
├── frontend/
│   ├── app.py                              # Streamlit frontend
│   ├── Dockerfile                           # Frontend Docker configuration
│   ├── requirements.txt                     # Frontend dependencies
├── models/                                  # Local LLM models (e.g., LLaMA)
│   ├── llama-2-7b-chat.ggmlv3.q4_0.bin      # LLaMA/Mistral quantized model
├── docker-compose.yml                        # Docker orchestration
├── README.md                                 # Documentation (this file)
```

---

## **Requirements**  
- Python 3.10+
- Docker and Docker Compose
- yt-dlp for downloading metadata and subtitles.
- LangChain and llama-cpp-python for LLM integration.

---

## **Setup Instructions**  

### **Step 1: Clone the Repository**  

```bash
git clone <repository-url>
cd youtube-metadata-extractor
```

---

### **Step 2: Download Model
1.	Download a **quantized model** (optimized for CPU) from HuggingFace:

```bash
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/resolve/main/llama-2-7b-chat.ggmlv3.q4_0.bin
```

```bash
wget https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_0.gguf
```
2. 	Move the model to the models/ directory:
```bash
mv llama-2-7b-chat.ggmlv3.q4_0.bin models/
```
---

### **Step 3: Install Dependencies

**Backend Dependencies:**
```bash
cd backend
pip install -r requirements.txt
```

**Frontend Dependencies:**
```bash
cd ../frontend
pip install -r requirements.txt
```
---

### **Step 4: Run the Application

1.	Build and run the Docker containers:
```bash
docker-compose up --build
```
2.	Access the frontend in your browser:
```bash
http://localhost:8501
```
---

## **Usage**  

1.	Open the web app.
2.	Paste a **YouTube URL** into the input box.
3.	Click **Extract Metadata**.
4.	View the extracted metadata and cleaned transcription in the interface.

---

## **API Documentation**  

The backend provides endpoints for API access:

- **Base URL:**
```
http://localhost:8000
```

- **Metadata Endpoint:**
```
POST /api/metadata/
```

- **Request Body:**
```json
{
  "url": "https://www.youtube.com/watch?v=K-U6eoICrYQ"
}
```

- **Response:**
```json
{
  "metadata": {
    "title": "Sample Title",
    "description": "Sample Description",
    "upload_date": "20240101",
    "duration": 300,
    "tags": ["tag1", "tag2"]
  },
  "transcription": "Cleaned subtitle text here..."
}
```

---

## **Best Practices**  
1. Model Optimization
	•	Use quantized models (e.g., Q4_0) to reduce memory and CPU load.
	•	Test different models like LLaMA, Mistral, or TinyLLaMA based on performance needs.
2. Scalability
	•	Use FastAPI routers to modularize endpoints, making it easy to add features like summarization or translation later.
	•	Implement pagination for larger transcripts.
3. Security
	•	Validate input URLs to avoid unsafe operations.
	•	Add rate limiting to prevent abuse if the API is publicly exposed.
4. Testing
	•	Use pytest or Postman to test API endpoints before deployment.
	•	Monitor logs using Docker logs:
```bash
docker logs backend
```
---

## **Next Steps**  

1.	Add Features:
	•	Summarization of transcription.
	•	Translation of subtitles.
	•	Keyword extraction for content analysis.
2.	Cloud Deployment:
	•	Host the app on AWS EC2, VPS, or Render for remote access.
3.	Optimize LLM Performance:
	•	Test models like Mistral or GPTQ for better efficiency.

---

## **Contributing**  
Contributions are welcome!
1.	Fork the repository.
2.	Create a feature branch:
```bash
git checkout -b feature-name
```
3.	Commit changes:
```bash
git commit -m "Add new feature"
```
4.	Push changes:
```bash
git push origin feature-name
```
5.	Submit a pull request.

---

## **License**  

This project is licensed under the **MIT License**.

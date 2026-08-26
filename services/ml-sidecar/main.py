import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
import uvicorn

# App Initialization
app = FastAPI(
    title="ML Sidecar Service for Matching Service",
    description="Vector embedding generator for topic matching.",
)

# Model Initialization
model_name = os.getenv("MODEL_NAME", "all-MiniLM-L6-v2")
print(f"Loading model: {model_name}")
try:
    model = SentenceTransformer(model_name)
except Exception as e:
    print(f"Error loading model: {e}")
    raise HTTPException(status_code=500, detail="Model loading failed.")
    # Exit with code 1 so Docker / Cloud Run knows the container failed to boot
    sys.exit(1)

class EmbeddingRequest(BaseModel):
    text: str

class EmbeddingResponse(BaseModel):
    embedding: list[float]
    dimension: int

@app.get("/health", status_code=200)
def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "healthy", model: model_name}    

@app.post("/embed", response_model=EmbeddingResponse)
def generate_embedding(request: EmbeddingRequest):
    """
    Generate a vector embedding for the provided text using the specified model.
    """
    try:
        clean_text = request.text.strip()
        if not clean_text:
            raise HTTPException(status_code=400, detail="Text cannot be empty")   
        # Generate 384-dimensional vector embedding
        vector = model.encode(clean_text).tolist()
        return EmbeddingResponse(embedding=vector, dimension=len(vector))
    except Exception as e:
        print(f"Error generating embedding: {e}")
        raise HTTPException(status_code=500, detail="Embedding generation failed.")


# Web Server Execution Block
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000)
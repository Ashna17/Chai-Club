from fastapi import FastAPI

app = FastAPI(title="Chai Club Matching Service")


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}

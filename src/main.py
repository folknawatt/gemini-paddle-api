from fastapi import FastAPI
from routers import gemini_router, ocr_router


app = FastAPI(
    title="Gemini-Paddle-API",
    description="API for Gemini and PaddleOCR services",
    version="0.0.1",
)

app.include_router(gemini_router.router, prefix="/gemini")
app.include_router(ocr_router.router, prefix="/ocr")


@app.get("/", tags=["Root"])
async def read_root():
    return {"Hello": "World"}

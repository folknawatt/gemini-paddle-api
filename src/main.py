from routers import gemini_router, ocr_router
from fastapi import FastAPI


app = FastAPI(
    title="Gemini-Paddle-API",
    description="API for Gemini and PaddleOCR services",
    version="0.0.1",
    # docs_url=None,
    # redoc_url=None,
)

app.include_router(gemini_router.router, prefix="/gemini")
app.include_router(ocr_router.router, prefix="/ocr")


@app.get("/", tags=["Root"])
async def read_root():
    return {"Hello": "World"}

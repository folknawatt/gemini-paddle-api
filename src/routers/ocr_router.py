from fastapi import APIRouter, Request, HTTPException
from functions.ocr_func.paddle_func import paddle_ocr


router = APIRouter(tags=["OCR"])


@router.post("/pddocr")
async def ocr(request: Request):
    try:
        input_data = await request.json()
        if not input_data or "img_path" not in input_data:
            raise HTTPException(status_code=400, detail="Invalid input format")

        img_path = input_data.get("img_path")

        paddle_ocr(img_path)
        return {"answer": "success"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

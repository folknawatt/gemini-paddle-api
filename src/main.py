from gemini_func.gem_func import gen_content
from pddocr_func.paddle_func import paddle_ocr
from fastapi import FastAPI, Request, HTTPException


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/ask")
async def ask(request: Request):
    try:
        input_data = await request.json()
        if not input_data or "question" not in input_data:
            raise HTTPException(status_code=400, detail="Invalid input format")

        question = input_data.get("question", "Who are you")

        response = gen_content(question)
        return {"answer": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ocr")
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

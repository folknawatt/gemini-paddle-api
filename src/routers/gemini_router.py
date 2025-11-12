from fastapi import APIRouter, Request, HTTPException
from functions.gemini_func.gem_func import gen_content


router = APIRouter(tags=["Gemini"])


@router.post("/ask")
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

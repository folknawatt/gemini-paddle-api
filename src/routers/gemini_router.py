from fastapi import APIRouter, Request, HTTPException, Depends, status
from auth import get_api_key_role
from functions.gemini_func.gem_func import gen_content
from pydantic import BaseModel


router = APIRouter(tags=["Gemini"])


class Prompt(BaseModel):
    question: str


@router.post("/ask")
# async def ask(request: Request, role: str = Depends(get_api_key_role)):
async def ask(request: Prompt, role: str = Depends(get_api_key_role)):
    # === นี่คือ Authorization ===
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have admin permissions",
        )
        
    try:
        # input_data = await request.json()
        input_data = request.model_dump()
        if not input_data or "question" not in input_data:
            raise HTTPException(status_code=400, detail="Invalid input format")

        question = input_data.get("question", "Who are you")

        response = gen_content(question)
        return {"answer": response}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

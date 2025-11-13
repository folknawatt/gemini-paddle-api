from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os


load_dotenv()


app = FastAPI()

# Header
API_KEY_NAME = os.getenv("EXAMPLE_API_KEY_NAME")
api_key_header_scheme = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# EXAMPLE KEYS
VALID_API_KEYS = os.getenv("EXAMPLE_VALID_API_KEYS")


async def get_api_key_role(api_key: str = Depends(api_key_header_scheme)):
    # ถ้า Client ไม่ได้ส่ง Key มาเลย
    if api_key is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing API Key"
        )

    # ตรวจสอบว่า Key ถูกต้องหรือไม่ และดึง role
    role = VALID_API_KEYS.get(api_key)

    # ถ้า Key ผิด (ไม่มีใน dict)
    if role is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid API Key"
        )

    # ถ้า Key ถูกต้อง, คืนค่า role
    return role

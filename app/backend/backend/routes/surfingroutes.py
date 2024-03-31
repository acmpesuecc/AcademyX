
from fastapi import APIRouter, HTTPException
from backend.controllers.surfing import top_10_latest

router = APIRouter()

@router.get("/top_10_latest/")
        
        
async def get_latest_courses(db:AsyncSession = Depends(get_async_session)) -> dict[str,str]:
    try:
        return await top_10_latest()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
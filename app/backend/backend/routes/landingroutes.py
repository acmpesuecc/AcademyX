from fastapi import APIRouter, HTTPException
from backend.controllers.landing import get_course_details

router = APIRouter()
@router.get("/course/{course_identifier}", response_model=dict)

async def landing_page(db:AsyncSession = Depends(get_async_session)) -> dict[str,str]:
     try:
        return await get_course_details()
     except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
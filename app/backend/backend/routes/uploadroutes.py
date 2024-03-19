from fastapi import APIRouter,  Depends, HTTPException
from backend.schemas.uploads import (
    CourseUploadRequest,
    ModuleUploadRequest,
    LessonUploadRequest
)
from backend.controllers.uploads import (
    upload_course,
    upload_module,
    upload_lesson
)

from sqlmodel.ext.asyncio.session import AsyncSession
from backend.database.session import get_async_session

router = APIRouter()

@router.post("/upload_course/")
async def handle_upload_course(
    course_data: CourseUploadRequest, 
    session:AsyncSession = Depends(get_async_session)) -> dict[str,str]:
    try:
      await upload_course(
            course_data.username, course_data.title, course_data.description,
            course_data.image_url, course_data.price, session
        )
     
      return {"message": "Course uploaded successfully."}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/upload_module/")
async def handle_upload_module(
    module_data: ModuleUploadRequest, session: AsyncSession = Depends(get_async_session)
) -> dict[str,str] :
    try:
        await upload_module(module_data.course_id, module_data.title, session)
        return {"message": "Module uploaded successfully."}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/upload_lesson/")
async def handle_upload_lesson(
    lesson_data: LessonUploadRequest, session: AsyncSession = Depends(get_async_session)
)-> dict[str,str]:
    try:
        await upload_lesson(
            lesson_data.module_id, lesson_data.title, lesson_data.video_url,
            lesson_data.article_url, lesson_data.video_title, lesson_data.article_title,
            session
        )
        return {"message": "Lesson uploaded successfully."}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
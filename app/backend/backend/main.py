from contextlib import asynccontextmanager
from typing import AsyncGenerator, TypedDict

import uvicorn

from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import close_all_sessions
from sqlmodel.ext.asyncio.session import AsyncSession
#from backend.routes.uploadroutes import router as uploads_router
#from backend.routes.surfingroutes import router as surfing_router  
from core import settings
from database.session import get_async_session,async_session, create_db


class AppState(TypedDict):
    _db: async_sessionmaker[AsyncSession]
    

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[AppState, None]:
    try:
     await create_db()
     
     appstate = AppState(_db=async_session)
     yield appstate
    except Exception:
        print("There is an error!")
    finally:
      close_all_sessions()

app = FastAPI(
    title= settings.app_name, 
    version= settings.version,
    lifespan=lifespan)


app.include_router(uploads_router, prefix="/api/v1", dependencies=[Depends(get_async_session)])
app.include_router(surfing_router, prefix="/api")


@app.get("/")
async def read_root() -> dict[str, str]:
    """
    Hello World
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: str) -> dict[str, str]:
    """
    Get an Item
    """
    return {"item_id": item_id}

@app.get("/course/{course_identifier}", response_model=dict)
async def get_course_details(course_identifier: Union[int, str] = Path(..., description="Course ID or Name")):
    if isinstance(course_identifier, int):
        query = select(Course).where(Course.id == course_identifier)
    else:
        query = select(Course).where(Course.title == course_identifier)


    course = db_session.exec(query).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    modules = db_session.exec(select(Module).where(Module.course_id == course.id)).all()

    course_info = {
        "title": course.title,
        "description": course.description,
        "modules": []
    }
    for module in modules:
        module_info = {
            "title": module.title,
            "estimated_time_minutes": module.estimated_time_minutes,
            "lessons": []
        }
        lessons = db_session.exec(select(Lesson).where(Lesson.module_id == module.id)).all()
        for lesson in lessons:
            lesson_info = {
                "title": lesson.title,
                "estimated_time_minutes": lesson.estimated_time_minutes,
                "articles": [],
                "videos": []
            }
            articles = db_session.exec(select(Article).where(Article.lesson_id == lesson.id)).all()
            for article in articles:
                lesson_info["articles"].append(article.title)
             videos = db_session.exec(select(Video).where(Video.lesson_id == lesson.id)).all()
             for video in videos:
                lesson_info["videos"].append(video.title)

            module_info["lessons"].append(lesson_info)

        course_info["modules"].append(module_info)

    return course_info




if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
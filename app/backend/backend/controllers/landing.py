from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.backend.models.models import Course, User, Review
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
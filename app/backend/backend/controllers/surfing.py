from typing import List, Optional
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.backend.models.models import Course, User, Review 


async def top_10_latest(db: AsyncSession):
    async with db() as session:
        query = select(Course).order_by(Course.updated_at.desc()).limit(10)
        result = await session.execute(query)
        latest_courses = result.scalars().all()

        courses_info = []
        for course in latest_courses:
            teacher = course.teacher

            reviews = course.reviews
            total_ratings = len(reviews)
            average_rating = sum(review.rating for review in reviews) / total_ratings if total_ratings > 0 else 0 #needs to be tested

            course_info = {
                'title': course.title,
                'teacher_username': teacher.username,
                'image_url': course.image_url,
                'average_rating': average_rating,
            }
            courses_info.append(course_info)

    return courses_info

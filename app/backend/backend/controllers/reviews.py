from backend.models.models import (
    User,
    Course,
    Review
)
from backend.database.session import AsyncSession
from sqlmodel import select, update

async def upload_review( user: str, course: str, rating: float, comment: str, session: AsyncSession):
    try:
        user : User = await session.exec(select(User).where(User.username == user))

        if not user:
            raise ValueError("Please create an account before entering a review.")
        
        new_review = Review(
            user=user,
            course=Course,
            comment=comment,
            rating=rating
        )
        session.add(new_review)
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise e

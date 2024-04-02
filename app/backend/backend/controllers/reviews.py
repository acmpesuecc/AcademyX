from backend.models.models import (
    User,
    Course,
    Review
)
from backend.database.session import AsyncSession
from sqlmodel import select, update

async def upload_review( username: str , course: str, rating: float, comment: str, session: AsyncSession):
    try:
        
from backend.models.models import (
User, 
Course,
Module, 
Lesson,
Video,
Article
)
from backend.database.session import AsyncSession
from sqlmodel import select,update

async def upload_course(username: str, title: str, description: str, image_url: str, 
                        price: float, session: AsyncSession):
    try:
        teacher: User = await session.exec(
            select(User).where(User.username == username))
        
        if not teacher:
            raise ValueError(f"User with username {username} not found.")
        
        new_course = Course(
            title=title,
            price=price,
            description=description,
            image_url=image_url,
            estimated_time_hrs= 0,
            teacher = teacher
        )
        session.add(new_course)
        await session.exec(update(User).where(User.id == teacher.id).values(isTeacher=True))
        teacher.courses_uploaded.append(new_course)
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise e
    
async def upload_module(course_id: int, title:str, session: AsyncSession):
    try:
        course: Course = await session.exec(
            select(Course).where(Course.id == course_id)
        )
        if not course:
            raise ValueError("Course does not exist.")
        
        new_module = Module(
            title = title,
            course = course,
            estimated_time_minutes= 0
        )
        session.add(new_module)
        course.modules.append(new_module)
        await session.commit()
    except Exception as e:
        await session.rollback()
        raise e
        
async def upload_lesson(
    module_id: int, title:str, video_url: str, 
    article_url: str, video_title: str,
    article_title: str, session: AsyncSession):
    
    try:
        module: Module = await session.exec(
            select(Module).where(Module.id == module_id)
        )
        if not module:
            raise ValueError("Course does not exist.")
        
        new_video = Video(
            title = video_title,
            url= video_url,
            #length_minutes= Get length from Azure Blob storage
        )
        
        new_article = Article(
            title = article_title,
            url= article_url,
            #length_words= Get length from Azure Blob storage
        )
        #lesson_length = Function to return lesson length 
        # in minutes based on video and article length.
        new_lesson = Lesson(
            title = title,
            module = module,
            article = new_article,
            video = new_video,
            #estimated_time_minutes= lesson_length
        )
        new_video.lesson = new_lesson
        new_article.lesson = new_lesson
        module.lessons.append(new_lesson)
        #module.course.estimated_time_hrs -= module.estimated_time_minutes
        #module.estimated_time_minutes += lesson_length
        #module.course.estimated_time_hrs -= module.estimated_time_minutes
        session.add(new_video)
        session.add(new_article)
        session.add(new_lesson)
        await session.commit()
    except Exception as e:
         await session.rollback()
         raise e
        
        
        
        
        
        
    
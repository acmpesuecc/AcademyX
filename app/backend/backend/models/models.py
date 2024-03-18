
from datetime import datetime
from typing import List, Optional,ForwardRef

from sqlmodel import Field, Relationship, SQLModel


class iDModel(SQLModel):
    id: Optional[int] = Field(primary_key=True,
        default=None,
        index=True,
        nullable=False,
        )
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    
class User(SQLModel, table = True):
    id: Optional[int] = Field(primary_key=True,
        default=None,
        index=True,
        nullable=False,
        )
    profile_image: Optional[str] = Field(default=None)
    username: str = Field(index = True)
    avatar_name: Optional[str] = Field(default = None)
    email: str = Field(index = True)
    """purchased_courses: Optional[List["Course"]] =  Relationship(
        back_populates="subscribers"
        )"""
    joined_at: Optional[datetime] = Field(default_factory=datetime.now)
    last_seen: Optional[datetime] = Field(default_factory=datetime.now)

class Teacher(User, table = True):
    courses: Optional[List["Course"]] = Relationship(back_populates="teacher")

class Course(iDModel, table = True):
    title: str = Field(index=True)
    price: Optional[float] = Field(default=None)
    description: str
    image_url: str
    estimated_time_hrs: Optional[float] = Field(default=None)
    avg_rating: Optional[float] = Field(default=0)
    published: bool = Field(default=False)
    modules: Optional[List["Module"]] = Relationship(back_populates="course")
    """subscribers: Optional[List[User]] = Relationship(
        back_populates="purchased_courses"
        )  """  
    teacher: Optional[Teacher] = Relationship(back_populates="courses")
   

class Module(iDModel, table = True):
    title: str = Field(index=True)
    estimated_time_minutes: Optional[int] = Field(default=None)
    lessons: Optional[List["Lesson"]] = Relationship(back_populates = "module")
    course: Optional[Course] = Relationship(back_populates="modules")

class Lesson(iDModel, table = True):
    title: str = Field(index=True)
    estimated_time_minutes: Optional[int] = Field(default=None)
    video: Optional["Video"] = Relationship(back_populates="lesson")
    article: Optional["Article"] = Relationship(back_populates="lesson")
    module: Optional[Module] = Relationship(back_populates = "lessons")
    
class Video(iDModel, table = True):
    title: str = Field(index=True)
    url: str = Field(index = True)
    lesson: Optional[Lesson] = Relationship(back_populates="video")
    length_minutes: int
    
class Article(iDModel, table = True):
    title: str = Field(index=True)
    url: str = Field(index = True)
    length_words: int 
    lesson: Optional[Lesson] = Relationship(back_populates="article")
    
class Review(iDModel, table = True):
     rating: Optional[float] = Field(default=0)
     comment: Optional[str] = Field(default=None)
     user: Optional[User] = Relationship(back_populates="reviews")
     course: Optional[Course] = Relationship(back_populates="reviews")
     

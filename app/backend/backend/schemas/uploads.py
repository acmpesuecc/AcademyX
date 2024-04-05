from pydantic import BaseModel


class CourseUploadRequest(BaseModel):
    username: str
    title: str
    description: str
    image_url: str
    price: float

class ModuleUploadRequest(BaseModel):
    course_id: int
    title: str

class LessonUploadRequest(BaseModel):
    module_id: int
    title: str
    video_url: str
    article_url: str
    video_title: str
    article_title: str
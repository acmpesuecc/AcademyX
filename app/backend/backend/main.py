from contextlib import asynccontextmanager
from typing import AsyncGenerator, TypedDict

import uvicorn

from fastapi import FastAPI,Depends
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import close_all_sessions
from sqlmodel.ext.asyncio.session import AsyncSession
#from backend.routes.uploadroutes import router as uploads_router
#from backend.routes.surfingroutes import router as surfing_router  
from backend.routes.landingroutes import router as landing_router
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
app.include_router(landing_router,prefix="/api")



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





if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        log_level="debug",
        reload=True,
    )
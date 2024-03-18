from contextlib import asynccontextmanager
from typing import AsyncGenerator, TypedDict

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import close_all_sessions
from sqlmodel.ext.asyncio.session import AsyncSession

from backend import settings
from backend.database.session import async_session, create_db


class AppState(TypedDict):
    _db: async_sessionmaker[AsyncSession]
    

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[AppState, None]:
    try:
     await create_db()
     print("Table created")
     appstate = AppState(_db=async_session)
     yield appstate
     print(appstate)
    except Exception as e:
        print(e)
    finally:
      print(AppState)  
      close_all_sessions()
    

app = FastAPI(title= settings.app_name, version= settings.version,lifespan=lifespan)



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
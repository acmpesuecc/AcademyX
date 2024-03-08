import uvicorn
from fastapi import FastAPI

app = FastAPI()

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
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Union , Dict , Any

app = FastAPI()
class Response(BaseModel):
    data: Union[str, int, float, bool, None, Dict[str, Any], List[Any]]
    success: bool = True
    message: Union[str, None] = None
    
@app.get("/")
async def index() -> Response:
    return Response(message="ai services is online.")
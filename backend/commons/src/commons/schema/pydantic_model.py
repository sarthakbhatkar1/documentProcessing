from pydantic import BaseModel


class ResponseJson(BaseModel):
    code: str = 1
    data: dict = {}
    message: str = 'Failure'

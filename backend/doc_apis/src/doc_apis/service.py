import logging
import uvicorn
from fastapi import FastAPI, APIRouter

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("")
def start():
    print(f'Application starting...')


@app.on_event("/shudown")
def shudown():
    print(f'Application closing...')

# app.include_router()


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, log_level="info")

import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from doc_apis.apis.doc_mgmt_apis import docs
from doc_apis.apis.predict_mgmt_apis import predict


logger = logging.getLogger(__name__)


app = FastAPI(openapi_url="/swagger/openapi.json", docs_url="/swagger", title="Document Processing Application",
              description="", version="0.0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def start():
    print(f'Starting application...')
    try:
        print(f'Application Stated')
    except Exception as e:
        print(f'Exception in startup of application: {e}')


@app.on_event("shutdown")
def shutdown():
    print(f'on application shutdown')
    return 0


app.include_router(docs, prefix="/api/v1/docsProcessing/docs")
app.include_router(predict, prefix="/api/v1/docsProcessing/predict")


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")

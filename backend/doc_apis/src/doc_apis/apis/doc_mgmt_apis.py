from fastapi import APIRouter, UploadFile, File

from doc_apis.services.docs_service import DocumentService
from doc_apis.utils.util import response_json

docs = APIRouter(tags=["Docs Processing APIs"])


@docs.get("")
async def list_of_documents():
    code = 0
    try:
        data = DocumentService().get_all()
        message = f"Successfully retrieved documents."
    except Exception as e:
        raise Exception(f'Exception in get: {e}')
    return await response_json(code=code, data=data, message=message)


@docs.post("")
async def upload_document(document: UploadFile = File(...)):
    code = 0
    try:
        print(f"Filename: {document.filename}")
        data = DocumentService().create(document=document)
        message = f"Successfully uploaded document."
    except Exception as e:
        raise Exception(f'Exception in get: {e}')
    return await response_json(code=code, data={}, message=message)


@docs.get("/{doc_id}")
async def get_document(doc_id: str):
    code = 0
    try:
        print(f"doc_id: {doc_id}")
        data = DocumentService().get(doc_id=doc_id)
        message = f"Successfully retrieved the document with doc_id: {doc_id}."
    except Exception as e:
        raise Exception(f'Exception in get: {e}')
    return await response_json(code=code, data={}, message=message)


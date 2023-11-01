from fastapi import APIRouter

from doc_apis.services.predict_service import PredictService
from doc_apis.utils.util import response_json

predict = APIRouter(tags=["Prediction APIs"])


@predict.get("")
async def list_of_predict_task():
    code = 0
    try:
        data = PredictService().get_all()
        message = "Successfully retrieved prediction tasks."
    except Exception as e:
        raise Exception(f'Exception in get: {e}')
    return await response_json(code=code, data=data, message=message)


@predict.post("/{doc_id}")
async def prediction_process(doc_id: str):
    code = 0
    try:
        print(f"doc_id: {doc_id}")
        data = PredictService().get_all()
        message = "Successfully completed prediction process."
    except Exception as e:
        raise Exception(f'Exception in get: {e}')
    return await response_json(code=code, data=data, message=message)


@predict.get("/{task_id}")
async def prediction_task_result(task_id: str):
    code = 0
    try:
        print(f"task_id: {task_id}")
        data = PredictService().get(task_id=task_id)
        message = "Successfully retrieved prediction results."
    except Exception as e:
        raise Exception(f'Exception in get: {e}')
    return await response_json(code=code, data=data, message=message)

import uuid


async def response_json(code: int, data: dict, message: str) -> object:
    response = {}
    try:
        if code != 0:
            response = {"code": 1, "data": {}, "message": f"{message}"}
        else:
            response = {"code": 0, "data": data, "message": f"{message}"}
    except Exception as e:
        print(f'Exception in response json: {e}')
    return response


def generate_unique_number():
    return str(uuid.uuid4()).lower()

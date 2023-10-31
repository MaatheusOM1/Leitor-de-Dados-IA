from fastapi import FastAPI

model = FastAPI()

@model.get('/model_version')
async def get_info() -> dict:
    model_name = 'YOLO NAS'
    version = '1.0'

    #Informações sobre o modelo
    return {
        'name': model_name,
        'version': version
    }
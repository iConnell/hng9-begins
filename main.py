from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from enum import Enum

class OperationTypeEnum(str, Enum):
    addtition = "addition"
    subtraction = "subtraction"
    multiplication = "multiplication"

class OperationSchema(BaseModel):
    operation_type: OperationTypeEnum
    x: int
    y: int

app = FastAPI()

@app.get("/")
async def home():
    bio = "I am a backend developer, with experience in python web frameworks like django, flask and fastap"
    return { "slackUsername": "iConnell", "backend": True, "age": 22, "bio": bio}

@app.post("/eval")
async def eval(input: OperationSchema):
    result = 0
    if input.operation_type == 'addition':
        result = input.x + input.y
    elif input.operation_type == 'subtraction':
        result = input.x - input.y
    elif input.operation_type == 'multiplication':
        result = input.x * input.y
    else: raise HTTPException(400, "Invalid operation type")

    operation_type = input.operation_type

    return { "slackUsernam": "iConnell", "operation_type" : operation_type, "result": result }

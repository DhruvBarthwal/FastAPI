from fastapi import FastAPI , HTTPException
from pydantic import BaseModel

app = FastAPI(title='Calculator API')

# Request body model
class Numbers(BaseModel):
    a: float
    b: float


@app.get("/")
def home():
    return {"message": "Calculator API is running"}

@app.post("/add")
def add(nums: Numbers):
    return {"result": nums.a + nums.b}

@app.post("/subtract")
def subtract(nums: Numbers):
    return {"result": nums.a - nums.b}

@app.post("/multiply")
def multiply(nums: Numbers):
    return {"result": nums.a * nums.b}

@app.post("/divide")
def divide(nums: Numbers):
    if nums.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero not allowed")
    return {"result": nums.a / nums.b}

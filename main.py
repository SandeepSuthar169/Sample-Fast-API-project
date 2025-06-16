from fastapi import FastAPI, Query, HTTPException
import json

app = FastAPI()

def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)  
        return data

@app.get("/")
def sample():
    return {"message": "hi my name is sandeep"}

@app.get("/hellow")
def hello():
    return {"message": "hello"}

@app.get("/view")
def views():
    data = load_data()
    return data

@app.get("/sort")
def sort_data(
    sort_by: str = Query(..., description='Sort by "density" or "residual_sugar"'),order: str = Query('asc')):
    
    valid_fields = ['density', 'residual_sugar']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field.")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Use 'asc' or 'desc'.")

    data = load_data()

    reverse = True if order == 'desc' else False

    sorted_data = sorted(data, key=lambda x: x.get(sort_by, 0), reverse=reverse)

    return sorted_data

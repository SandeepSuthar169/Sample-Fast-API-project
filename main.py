from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('data.json', 'r') as file:
        data = json.load(file)
        return data

@app.get("/")
def sample():
    return f"hi my name is sandeep "

@app.get("/hellow")
def hello():
    return f"hello"

@app.get("/view")
def views():

    data = load_data()
    return data



@app.get("/sort")
def sort_data(sort_by: str = Query(..., description='sort by the basic of density, residual_sugar'),order: str = Query('asc')):
    valid_file =['density', 'residual_sugar']

    if sort_by not in  valid_file:
        return HTTPException(status_code=400)
    
    if order not in ['asc', 'desc']:
        return HTTPException(status_code=400)
    
    data = load_data()

    sort_data =  True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key=lambda x:x.get('sort_by', 0), reverse=sort_data)

    return sorted_data

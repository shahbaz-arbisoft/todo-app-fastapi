from fastapi import FastAPI

app = FastAPI()


@app.get('/todo/')
async def fetch_all_todos():
    return {'Hello': 'Get'}


@app.post('/todo/')
async def create_todo():
    return {'Hello': 'Post'}


@app.get("/todo/{id}")
async def retrieve_todo(id):
    return {'Hello': 'Get-' + str(id)}


@app.put("/todo/{id}")
async def update_todo(id):
    return {'Hello': 'Put-' + str(id)}


@app.delete("/todo/{id}")
async def delete_todo(id):
    return {'Hello': 'Delete-' + str(id)}

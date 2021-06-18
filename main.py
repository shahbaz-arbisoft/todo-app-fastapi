from fastapi import FastAPI

app = FastAPI()


@app.get('/todo/')
def retrive_all_todo():
    return {'Hello': 'Get'}


@app.post('/todo/')
def create_todo():
    return {'Hello': 'Post'}


@app.put("/todo/{id}")
def update_todo(id):
    return {'Hello': 'Put-' + str(id)}


@app.get("/todo/{id}")
def retrive_todo(id):
    return {'Hello': 'Get-' + str(id)}


@app.delete("/todo/{id}")
def delete_todo(id):
    return {'Hello': 'Delete-' + str(id)}

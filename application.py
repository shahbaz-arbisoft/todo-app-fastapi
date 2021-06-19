from fastapi import FastAPI

from todo.views import router

app = FastAPI()
app.include_router(router)

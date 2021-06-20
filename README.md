# todo-app-fastapi-monogodb
A python based application that use Fast API to perform CRUD functionalities of TODO item. 

## Running Documentation Locally

1. Make sure you have already installed python3.8+
2. Go to the project directory
3. Acticvate virtual environment by running this command `source todovenv/bin/activate`
4. Now install dependencies, for this run this command `pip3.8 install -r requirements.txt`
5. Run the uvicorn server by this command `uvicorn application:app --reload`
6. Go to the browser and hit the URL (http://127.0.0.1:8000/docs)
7. Swagger UI will appear showing all the endpoints

FROM python:3.8

WORKDIR /todo-app

COPY requirements.txt .

RUN pip3.8 install -r requirements.txt

COPY ./ ./

CMD ["python", "application.py" ]
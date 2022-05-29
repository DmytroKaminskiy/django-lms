FROM python:3.10

WORKDIR /project/code

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--port=5000", "--host=0.0.0.0"]

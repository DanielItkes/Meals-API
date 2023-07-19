FROM python:alpine3.17

WORKDIR ./app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "app.py"]

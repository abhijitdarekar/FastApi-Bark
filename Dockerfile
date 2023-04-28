FROM python:3.9

WORKDIR /base
COPY ./app/requirements.txt /base/app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /base/app/requirements.txt

COPY ./app /base/app

CMD ["uvicorn", "app.app:app", "--host=0.0.0.0", "--port=8000"]
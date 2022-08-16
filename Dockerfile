FROM python:3.7

RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt

RUN ls -la

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.10.6

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip3 install poetry==1.4.2 && \
    poetry config virtualenvs.create false && \
    poetry install

#COPY . /app
COPY info_portal /app/info_portal
COPY db.sqlite3 /app
COPY manage.py /app

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

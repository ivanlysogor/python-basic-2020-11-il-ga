FROM python:3.9-buster

WORKDIR /var/app

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY . .

RUN poetry install --no-interaction --no-ansi

EXPOSE 5000

CMD python app.py

# Use 'docker run -d -p 5000:5000 hw45' to run the application

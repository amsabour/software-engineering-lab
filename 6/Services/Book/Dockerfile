FROM python:3.9.4-alpine3.13
WORKDIR /app
RUN pip install Flask Flask-RESTful pyjwt
ENV FLASK_APP=api.py
ENV FLASK_RUN_PORT=5000
EXPOSE 5000
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]
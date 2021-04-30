FROM python:3.9.4-alpine3.13
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
ENV FLASK_RUN_PORT=10000
EXPOSE 10000
CMD ["flask", "run", "--host", "0.0.0.0"]
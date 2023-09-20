FROM python:3.9-slim
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY ./posts_service_app.py /app/app.py
COPY ./init_db.py /app/init_db.py
CMD ["flask", "run", "--host=0.0.0.0"]
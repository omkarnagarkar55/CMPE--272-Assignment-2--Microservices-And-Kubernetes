FROM python:3.9-slim
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
COPY ./static /app/static
COPY ./templates /app/templates
COPY ./frontend_app.py /app/app.py
CMD ["flask", "run", "--host=0.0.0.0"]

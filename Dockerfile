FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=core.server:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=7755

EXPOSE 7755

CMD ["gunicorn", "--config", "gunicorn_config.py", "core.server:app"]

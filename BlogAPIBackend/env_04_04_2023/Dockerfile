FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
ENV FLASK_APP=app.py
COPY . .
EXPOSE 80
CMD ["/bin/bash", "docker-entrypoint.sh"]
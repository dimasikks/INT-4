FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install -r installation.txt

EXPOSE 7777

CMD ["python", "server.py"]
 

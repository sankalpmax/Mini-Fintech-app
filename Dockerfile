FROM python:latest

WORKDIR /myapp

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . /myapp

EXPOSE 5000

CMD ["python", "app.py"]

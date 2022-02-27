FROM python:3-alpine
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
WORKDIR /code
EXPOSE 5000
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD ["python", "simple_api.py"]

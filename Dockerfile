FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

ENTRYPOINT ["python", "HyperPOS/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

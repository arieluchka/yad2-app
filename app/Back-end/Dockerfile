FROM python:3.9

WORKDIR /yad-2/app

COPY ./requirements.txt /yad-2/app

RUN pip install -r ./requirements.txt

COPY . /yad-2/app

CMD ["python", "./main.py"]
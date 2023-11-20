FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update && apt-get install -y ffmpeg

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

CMD ["uvicorn", "run_server:app", "--reload"]

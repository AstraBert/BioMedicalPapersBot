FROM python:3.11.9-slim-bookworm

WORKDIR /app
ADD . /app

RUN apt update && apt install -y gcc g++

RUN python3 -m pip cache purge
RUN python3 -m pip install --no-cache-dir -r requirements.txt 

EXPOSE 7860

ENTRYPOINT [ "python3", "/app/scripts/app.py" ]
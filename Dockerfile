FROM python:3.8 

WORKDIR /mascotas-face-cropper-app

COPY ["./src", "./src"]
COPY ["requirements.txt", "."]
COPY ["app.py", "."]

RUN apt-get update && apt-get install -y build-essential cmake python3-opencv

ENV PYTHONPATH="/mascotas-face-cropper-app:${PYTHONPATH}"
ENV PYTHONUNBUFFERED=1

RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "app.py"]

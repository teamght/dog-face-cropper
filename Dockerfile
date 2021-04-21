FROM python

COPY src /app
COPY requirements.txt /app/requirements.txt
WORKDIR /app

#RUN apt-get update
#RUN apt-get -y install build-essential
#RUN apt-get -y install cmake
#RUN apt-get -y install python3-opencv # RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get update && apt-get install -y build-essential cmake python3-opencv

ENV PYTHONPATH="/app:${PYTHONPATH}"
ENV PYTHONUNBUFFERED=1

RUN pip install -r requirements.txt

CMD ["python", "example_process_file.py"]

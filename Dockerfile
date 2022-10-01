FROM python:3.7
COPY ./requirements.txt /tmp/
RUN pip install -r /tmp/train_requirements.txt
COPY . ./app
WORKDIR /app
ENTRYPOINT python train.py
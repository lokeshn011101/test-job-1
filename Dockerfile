FROM python:3.7
COPY . ./app
WORKDIR /app
RUN python -r ./train_requirements.txt
CMD python train.py
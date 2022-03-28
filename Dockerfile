FROM python:3.9

RUN mkdir -p /usr/src
WORKDIR /usr/src
COPY src/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./
EXPOSE 8000
EXPOSE 8080

CMD python -u main.py

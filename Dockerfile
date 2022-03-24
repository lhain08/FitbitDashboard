FROM python:3.9

COPY src/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
COPY src/ ./
EXPOSE 8000
EXPOSE 8080

CMD python main.py
FROM python:3.11.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /web/cimax/backend/

COPY ./requirements.txt ./

RUN pip install --upgrade pip && pip install -r ./requirements.txt

COPY entrypoint.py /usr/local/bin/entrypoint.py

RUN chmod +x /usr/local/bin/entrypoint.py

COPY . .

EXPOSE 8000

ENTRYPOINT ["python", "/usr/local/bin/entrypoint.py"]
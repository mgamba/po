FROM amancevice/pandas:2.0.0-slim

RUN apt update
RUN apt install sqlite3

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

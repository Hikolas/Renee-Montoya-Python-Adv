FROM python:3.8.12

WORKDIR /application

COPY ./requirements.txt /application/requirements.txt
COPY ./wait-for-it.sh /application/wait-for-it.sh
RUN chmod -R 0777 *
RUN pip install -r requirements.txt

CMD ./wait-for-it.sh db:3306 -- python3 app.py
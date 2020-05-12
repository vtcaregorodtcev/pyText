FROM python:latest

ADD config.py /server/
ADD wsgi.py /server/
ADD application /server/application
ADD requirements.txt /server/

WORKDIR /server/

RUN python -m venv env

ENV PATH=/env/bin/:$PATH
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

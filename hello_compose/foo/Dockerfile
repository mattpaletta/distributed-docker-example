FROM python:3.7
ADD requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
WORKDIR foo
ADD . .
ENTRYPOINT ["python3", "__main__.py"]
FROM python:3.6

RUN mkdir mycode_in_container/

VOLUME mycode_in_container/ 

COPY requirements.txt mycode_in_container/requirements.txt

WORKDIR mycode_in_container

RUN pip3 install -r requirements.txt

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

### docker build -t mypython ./
### docker run -ti --memory=1g -v $PWD:/mycode_in_container -v -p 8000:8000 mypython
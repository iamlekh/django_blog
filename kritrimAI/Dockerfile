FROM python:3.7-buster
RUN mkdir /home/myblog
WORKDIR /home/myblog 
COPY ./ /home/myblog/
RUN pip install -r /home/myblog/requirements.txt
EXPOSE 8000
ENTRYPOINT ["python","manage.py","runserver","0.0.0.0:8000"]

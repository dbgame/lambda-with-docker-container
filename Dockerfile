FROM amazon/aws-lambda-python:3.8

RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

RUN yum install git -y

RUN pip install --upgrade numpy
RUN pip install --upgrade sklearn
RUN pip install --upgrade xgboost

RUN curl -O https://raw.githubusercontent.com/unhochoi/lambda-with-docker-container/main/lambdafunc.py
#RUN git clone https://github.com/unhochoi/lambda-with-docker-container.git

#WORKDIR lambda-with-docker-container/

CMD ["lambdafunc.handler"]

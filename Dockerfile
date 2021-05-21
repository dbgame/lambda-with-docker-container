FROM amazon/aws-lambda-python:3.8

# optional : ensure that pip is up to data
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

# install git 
RUN yum install git -y

# install packages
RUN pip install --upgrade numpy
RUN pip install --upgrade sklearn
RUN pip install --upgrade xgboost

# git clone
RUN git clone https://github.com/unhochoi/lambda-with-docker-container.git

# move lambdafunc.py
RUN cp lambda-with-docker-container/lambdafunc.py /var/task/

CMD ["lambdafunc.handler"]

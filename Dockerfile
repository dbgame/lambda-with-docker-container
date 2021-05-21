FROM amazon/aws-lambda-python:3.8

# optional : ensure that pip is up to data
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

# install git 
RUN yum install git -y

# git clone (lambda_function.py, python model, etc) 
RUN git clone https://github.com/unhochoi/lambda-with-docker-container.git

# move work directory
WORKDIR lambda-with-docker-container/

# install packages
RUN pip install --upgrade numpy
RUN pip install --upgrade sklearn
RUN pip install --upgrade xgboost

# lambda_function.py 의 lambda_handler 함수 호출
CMD ["lambda_function.lambda_handler"]

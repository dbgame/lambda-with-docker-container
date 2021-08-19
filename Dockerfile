FROM amazon/aws-lambda-python:3.8

# optional : ensure that pip is up to data
RUN /var/lang/bin/python3.8 -m pip install --upgrade pip

# install git 
RUN yum install git -y

# git clone
RUN git clone https://github.com/unhochoi/lambda-with-docker-container.git

# install packages
RUN pip install -r lambda-with-docker-container/requirements.txt

# move lambdafunc.py
RUN cp lambda-with-docker-container/lambda_function.py /var/task/

CMD ["lambda_function.handler"]

# lambda-with-docker-container

- API Gateway 로부터 POST 받았을 시, 최적의 SPMM 방법을 추천해주는 Lambda Function 구현 (Container 기반)
  -  Lambda Function 에서 사용하고 싶은 Package 들은 Dockerfile 에 작성한 뒤, Image 로 만들어서 사용해야함
  -  Dockerfile 로부터 생성된 Image 는 ECR 에 업로드
  -  Lambda Function 은, ECR Image 기반 Container 내에서 동작함

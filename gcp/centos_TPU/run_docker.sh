# 부팅 시에 도커 실행 하도록 등록
sudo systemctl enable docker.service
# docker 실행
sudo systemctl start docker.service
# docker 상태 확인
sudo systemctl status docker.service
# 도커 접속하기
sudo docker run -v /data:/data -i -t whtngus3232/bert /bin/bash
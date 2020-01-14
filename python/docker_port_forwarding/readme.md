# Docker Port Forwarding

## ubuntu 기반으로 작성

이미지 생성시 옵션 :  -p "host port":"container port"
```
옵션 설명
-p: 호스트 port와 docker port를 Prot Forwading
-d : 백그라운드에서 계속실행 
ex) docker run -v /data:/data -p 23:22 -it --rm container /bin/bash
``` 

> 도커 접속하여 SSH설치
- apt-get 업데이트 <br>
apt-get update <br>
- ssh 설치 <br>
apt-get install net-tools openssh-server <br>
- ssh 설정 <br>
vi /etc/ssh/sshd_config<br>
PermitRootLogin yes  (루트 계정 접속을 허용)<br>
UsePAM yes    (일반 계정 접속을 허용)<br>
- root 비밀번호 변경<br>
passwd root<br>
변경할 비밀번호 입력<br>
- ssh 서비스시작<br>
service ssh start <br>



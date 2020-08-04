---
layout: post
title: "docker_port_forwarding"
date: 2020-08-05 19:20:23 +0900
category: python
---

# Docker Port Forwarding

## ubuntu 기반으로 작성

#### 언어 설정 
```
export LANGUAGE=ko_KR.UTF-8 
export LANG=ko_KR.UTF-8
locale-gen ko_KR ko_KR.UTF-8
update-locale LANG=ko_KR.UTF-8
dpkg-reconfigure locales
-> 298
```
#### 이미지 생성시 옵션 :  -p "host port":"container port"
```
옵션 설명
-p: 호스트 port와 docker port를 Prot Forwading
-d : 백그라운드에서 계속실행 
ex) docker run -v /data:/data -p 23:22 -it --rm container /bin/bash
``` 

#### 도커 접속하여 SSH설치
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

#### 접속 확인
ssh 접속해서 확인해보기
```
ssh -p "port" "id"@"ip"
ex) ssh -p 23 root@127.0.0.1


최종 실행 예시 
# 적용안되는 경우 이것도 시도 -> -e LC_ALL=ko_KR.UTF-8 
sudo nohup docker run -itd -e LC_ALL=C.UTF-8 -v /data:/data -p 23:22 --rm vnv:v0.4 /bin/bash
sudo docker exec -it "docker_container_id" /bin/bash
service ssh start
```

#### SSH 한글 설정
ssh 새로 접속시 한글이 깨짐 
```
vi /etc/environment
LANG="ko_KR.UTF-8"
LANGUAGE="ko_KR:ko:en_GB:en"

vi /etc/profile 마지막 줄 삽입
LANG="ko_KR.UTF-8"

vi /etc/default/locale 
LANG="ko_KR.UTF-8"
LANGUAGE="ko_KR_UTF-8"
LANG_ALL="ko_KR.UTF-8"

vi ~/.bashrc 마지막 줄 삽입
export  LANG="ko_KR.UTF-8"

설정 후 도커 실행시 -e 옵션 없이 실행
(위의 환경설정 없이 -e 옵션을 주고 실행한 경우 로컬에서만 locale이 적용됨)
```
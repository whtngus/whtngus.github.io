# session 1 환경 구축

ELK 스택(ElasticSearch, Logstash Kibana)으로 데이터 분석

도커 우분투 환경에서 진행

	- ElasticSearch install
1. java Install
sudo add-apt-repository –y ppa:webupd8team/java
sudo apt-get update
sudo apt-get -y install aracle-java8-installer
java –version
* 에러 발생 
<img src="./pic/error1.PNG" width="350px" height="300px"></img> <br>

-> 위가 강의내용이나 되지않아 다른 방식으로 진행
apt-get install openjdk-8-jdk

2. 엘라스틱서치 설치 
* 이번에도 강의와 다른방식으로 설치 진행
https://www.elastic.co/kr/downloads/elasticsearch -> 여기에서 찾아보고 wget으로 다운로드
*강의와 같은 버전을 맞춰서 설치
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.5.1.deb
dpkg -i elasticsearch-5.1.1.deb
# 명령어 없어서 강의와 다른 명령어로 교체
service elasticsearch start


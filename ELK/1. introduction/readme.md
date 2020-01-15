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
*강의와 같은 버전을 맞춰서 설치 (사용 X)
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.5.1.deb
dpkg -i elasticsearch-5.1.1.deb
* 최신 버전 정리를 위해 2020-01-15를 기준으로 최신버전 설치 
https://www.elastic.co/kr/downloads/elasticsearch 에서 검색 최신버전 찾기 <br>
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.5.1-x86_64.rpm
<br>
> rpm으로 받아 det파일로 변환 필요 <br>
```
[rpm 파일 바로 설치하기]
alien -i  elasticsearch-7.5.1-x86_64.rpm
[deb 파일로 변환하여 설치하기]
# sudo alien -c elasticsearch-7.5.1-x86_64.rpm     —->  변환
# sudo dpkg -i elasticsearch-7.5.1-x86_64.rpm     —->  설치
```


##### 명령어 없어서 강의와 다른 명령어로 교체
service elasticsearch start


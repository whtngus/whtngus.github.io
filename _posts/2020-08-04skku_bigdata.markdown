---
layout: post
title: "수업 정리"
date: 2020-08-04 19:20:23 +0900
category: skku_bigdata
---

============= 2 주차 ====================== <br>
### 복습 <br>
빅데이터 (사람에 의해서 생긴 데이터들) -> 나중엔 센서에 의해서도 데이터가 생성됨
3V, 빅데이터 분석 과정 


빅데이터 처리 
1. 결함 허용 시스템 (Fault Tolerance)
2. 저 비용 시스템(Cost Effective System)
 - 수직 확장(Scale Up)
 - 수평 확장(Scale out))
3. 기존 시스템과 연계성


    2주치 시작
책 : Haddop The Definitive Guide 책
23P ~ 

많은데이터 > 좋은 알고리즘  <br>

빅데이터 처리 시스템 원조 : 하둡 (Hadoop) -> 역사 <br>
2003 : 구글 파일 시스템 (GFS) <- HDFS가 이걸보고 만듦  <br>
2004 : 구글 맵리듀스 (MapReduce) <br>
2004 : 아파치 넛지 (Nutch) 프로젝트 <br>
2006 : 야후 하둡 프로젝트 탄생 (더그 커팅) <br>
2008 : 클라우데라(Cloudera) 창립 <br>
2011 : 호튼웍스 (Hotonworks) 창립<br>

- 하둡(Hadoop)
> 대용량의 데이터를 분산 병렬 처리 방식으로 여러 개의 작업 노드에 작업을 분산하여 병렬 수행할 수 있는 프레임워크를 제공
Master - Slave(Woker) 구조로 데이터를 분산 처리 <br>
한대가 장애가 나더라도 작업을 분산처리 하기 때문에 결함 허용 시스템이 적용되어 있음 <br>

하둡1.0 <br>
<img src="./pictures/hadoop1.0.PNG" width="350px" height="300px"></img> <br>
Processing Layer(MapReduce layer)과 Storage Layer(HDFS layer)를 나눠서 처리하도록 설계
mater : jab tracker 와 name node가 main 업무
slave : 데이터 처리하도록

Name node : Name Space를 관리하는 노드 


---

## AWS 사용하기 
<img src="./pictures/aws_student.PNG" width="350px" height="300px"> 학생 계정 AWS</img> <br>
> AWS student 계정으로 계정 생성하면 100$ 무료 사용 가능

# 3주차

## MapReduce
> 대용량을 저장하기 위한 시스템  <br>
> 괜찮은 시간안에 모든 데이터를 보고 분석할 수 있음. <br>
> 실시간 (대화형)분석에는 적합하지 않음 <br>
> 한번 쓰고 여러번 읽어들이는 구조에 특화되어 있음 <br>
> 데이터를 처리하는 프로그래밍 모델
- 데이터 처리 방식 
- word count 같은 집계하는 작업에 강함
<img src="./pictures/MapReduce01.PNG" width="350px" height="300px"></img> <br>
```
- 맵(Map) 단계
    분산된 데이터를 키(key)와 값(value)의 리스트로 만드는 단계
    map()는 데이터를 읽어들여 키 값 쌍으로 출력
- 셔플과 정렬(Shuffle and Sort) 단계
    맵 단계에서 나온 중간 결과를 해당 리듀스 함수에 전달하는 단계
    하둡이 수행 위 작업 후 리듀스로 전달
- 리듀스(Reduce) 단계
    전달받은 리스트에서 원하는 데이터를 찾아서 집계하는 단계
    
    
개발자가 직접 정의
1. 맵(Map) 함수
2. 리듀스(Reduce) 함수
-> 분산처리는 하둡을 통해 자동으로

*위 3단계중 부분적으로 사용도 가능*
```

## hadoop
RDMS아 Hadoop시스템의 경계가 모호함.

Computing 변형 과정
1. Grid Computing
2. Clustering Computing
3. Cloud Computing

- split 단위는 블럭단위
- 기본 블럭사이즈는 128MB
- 작은 여러개의 파일을 읽는경우 오히려 더느릴 수 있음

<br>
Lucene 개발자가 개발을 시작 원래 Apache Nutch에서 시작 
(Web Search를 위해서)

<br>
hadoop : 약어가 아니라 직접 만든것 -> 
 아이가 노란 코끼리인형 이름을 hadoop이라고 불러서 그걸 그대로 적용 <br>

- Nutch 프로젝트 진행시 문제점 -> 웹 페이지를 크롤링하고 유지하는데 너무 많은 비용이 듦 



## 4주차 하둡

```
Yarm 이 데이터를 어떻게 job이 수행될지를 정해줌 

map을 분산하여 나눠준 후 모든 노드가 처리를 다 끝낸 경우 리듀스에게(정렬된 파일을) 전달 

블럭사이즈와 데이터 사이즈가 같으면 가장 최적 


``` 

<img src="./pictures/hadoop01.PNG" width="350px" height="300px"></img> <br>
```
map의 결과는 중복저장을 하지 않기 위해 로컬에 저장하고 
reduce의 결과물은 중요하기 때문에 HDFS replication으로 전달 
b.
node가 죽은경우 다른 node로 이동 
c.
rack이 죽은경우 job을 다른 node로 이동 
```

<img src="./pictures/hadoop02.PNG" width="350px" height="300px"></img> <br>
```
1. 하나의 리듀스가 있는경우 
큰 데이터 하나를 3개로 스플릿 (YARN이 스플릿 및 job할당을 관리)
-> 3개의 map이 생김 
-> 정렬 후 로컬에 데이터 전달 후에 리듀스로 전송
-> 리듀스에서는 받은 데이터를 merge한 후 reduce 함수가 처리를한 결과를 part0로 전달
-> part0의 결과를 HDFS로 file write 
결과물은 중요하기때문에 신뢰성을 가지기 위해서 
```
<img src="./pictures/hadoop03.PNG" width="400px" height="400px"></img> <br>
```
2. 멀티플 리듀스 테스크의 경우 
리듀스의 개수만큼 파티션이 생김 

각각의 맵이 리듀스 개수만큼 나눠서 작업한 후 각각의 리듀스로 전달
yarn -> 각 프로세스로 모든 노드에 저장되있어서 각 싱크가 자동으로 됨 
```
<img src="./pictures/hadoop04.PNG" width="450px" height="400px"></img> <br>
```
3. 리듀스 테스크가 없는경우
HDFS에게 write를 함 (리듀서가 없어서 최종 결과물이기 때문에 )
```
> Combiner Function
```
Map 하고 Reduce task 사이의 데이터 전송을 최소화 할 필요가 있음
(네트워크 속도 업 or Map의 사이즈를 감소)
ex)
- 기존 방식
map1
(1950,	0) (1950,	20) (1950,	10) 
map2
(1950,	25) (1950,	15) 
-> reduce로 전송
(1950,	[0,	20,	10,	25,	15]) -> (output) (1950,	25)

- Combiner Function
각 맵에서 최대값을 구해서 전달 
reduce는 (1950,	[20, 25])를 전달받아 MAX를 구함

* 모든 경우에는 다 적용할 수 없음
ex) 평균을 구하는 경우 적용 불가 
-> 프로그램 구조를 바꾸면 적용은 가능
   ex) 평균시에는 각 맵에서 평균, 개수 를보내면 평균을 구할 수 있음
        (단, 새로운 프로그래밍을 필요로 함)
        
 - Combiner Function 적용 방법
 job.setCombinerClass(MaxTemperatureReducer.class);
 위 라인 한줄만 추가하면 됨 (Combiner Function 사용함을 알리는 역할)
```
> Hadoop Streaming
```
Hadoop Streaming : java, ruby, python을 지원하는 api 
파일 형식의 input, output이 아닌 Standard IO방식 -> command line에서 데이터 입력
```
> HDFS
```
HDFS : The	Hadoop	Distributed Filesystem (하둡 분산파일 시스템)
- 파일의 접근 제어
- 파일의 CRUD
- 파일을 디스크의 어디에 저장할지
- 디렉토리의 구조를 제공하고 관리

파일을 저장해야하는데 DISK의 크기보다 저장해야할 파일의 크기가 큰경우의 문제를 해결하기 위해
개발을 시작  -> 네트워크로 연결된 여러 머신의 스토리지를 관리하는 파일 시스템 

- HDFS 설계원칙
1. Very Large File
2. Write Once, Read Many Times Pattern
3. Fault-Tolerance
-> 당연히 위 설계원칙으로 인하여 약점이 생김
1. Low-latency Data Acess  
빠른 접근이 필요한 경우 
2. Lots of Small Files
작은 파일 사이즈의 파일들이 많은 경우 (작은 => 블록사이즈보다 작은 파일)
3. Multiple Writers, Arbitrary File Modifications
여러개의 파일을 쓰거나 임의의 위치에서 데이터 수정이 어려움 
```
> Block
```
Block : 한번에 읽고 쓸 수 있는 데이터의 최대량
- 기본적으로 128M
HDFS Block을 Chuck라 하고 각 Chuck는 독립적으로 저장함 
```
> Name Node
```
Master node에서 파일시스템의 namespace를 관리함
image와 edit log라는 두 종류의 파일로 로컬 디스크에 영속적으로 저장

block의 위치정보는 시스템이 시작할 때 모든 Data node로부터 받아서 재구성하기 때문에
디스크에 역속적으로 저장하지는 않음 
```
> Data Node
```
Worker node에서 HDFS 클라이언트나 Name node의 요청이 있을 때 block을 저장하고 탐색
Block의 목록을 주기적으로 Name Node에 보고 
```
# 4주차 하둡

> Block 
```
한번에 읽고 쓸 수 있는 데이터의 최대량
HDFS Block의 크기
    ✓기본적으로 128MB
        ▪ Block이 큰 이유는 seek 비용을 최소화히기 위함
    ✓ HDFS Block을 Chuck라 하고 각 Chuck는 독립적으로 저장됨
```
> Name Node
```
Master node에서 파일시스템의 namespace를 관리함

➢ block의 위치정보는 시스템이 시작할 때 모든 Data node로부터 받아서
재구성하기 때문에 디스크에 영속적으로 저장하지는 않음
```
> Data Node
```
➢ Worker node에서 HDFS 클라이언트나 Name node의 요청이 있을 때
block을 저장하고 탐색함
➢ 저장하고 있는 Block의 목록을 주기적으로 Name node에 보고함
```
> HDFS에 디렉토리 생성
```
- Local 파일시스템에서 HDFS로 복사
% hadoop fs -copyFromLocal input/docs/quangle.txt hdfs://ocalhost/usr/tom/quangle.txt
- HDFS에 디렉토리 생성
%hadoop fs -mkdir books
%hadoop fs -ls
```
> HDFS의 Interfaces <br>
<img src="./pictures/interface_01.PNG" width="350px" height="300px"></img> <br>

> ZooKeeper
```
HDFS의 HA를 하기위해 사용 
```

> YARN
```
빅데이터 스케줄링 및 시스템 구성을 도와주는 역할
```





# HADOOP 설치 
### jdk 설치
sudo apt-get update 
sudo apt-get install openjdk-8-jdk
### hadoop 설치
 wget http://apache.mirror.cdnetworks.com/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz
 tar -xzvf hadoop-3.2.1.tar.gz
 sudo mv hadoop-3.2.1 /usr/local/hadoop
### hadoop 환경 설정
```
     vim /etc/environment       (편집)
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/hadoop/bin:/usr/local/hadoop/sbin"
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre/"

     ./bashrc  (가장 하단에 추가)
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
     
```

# Spark 설치
```
wget http://apache.mirror.cdnetworks.com/spark/spark-3.0.0-preview2/spark-3.0.0-preview2-bin-hadoop3.2.tgz
tar -xvzf spark-3.0.0-preview2-bin-hadoop3.2.tgz
cd spark-3.0.0-preview2-bin-hadoop3.2/bin/
    - spark 실행
./spark-shell
```

> PySpark 설치하기

```
    - python3 우선 설치
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ sudo pip3 install --upgrade pip
    - pyspark 설치
$ pip3 install pyspark --user
$ sudo apt-get -y install ipython3 
    - ipython 실행 후 pyspark 실행해 보기
$ ipython3
In [1]: import pyspark
In [2]: pyspark.__version__
Out[2]: '2.4.4'
```





 



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
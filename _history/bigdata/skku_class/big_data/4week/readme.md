
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






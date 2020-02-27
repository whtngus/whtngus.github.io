# 9.고수준언어_HIVE소개

## Hadoop

```
Hadoop
1 -> HDFS -> stoare
2 -> M.R -> compuatation

데이터사이언티스트 들이 java 나 python을 사용하지않고 빅데이터를 처리할 수 있는 방법을 facebook에서 고민해서 나온 랭기지 HIVE

Hadoop은 대용량데이터 처리에 효율적
모든 작업을 자바로 직접 작성하는것은 다소 장황하며 시간이 오래걸림
모두가 자바를 사용하길바라거나 사용할 줄 아는것은 아님

```

> HIVE

<img src="./pic/hive_architecture01.PNG" width="350px" height="300px"></img> <br>

```
Facebook 에서 개발한 언어
(비슷한 언어인 Pig 는 Yahho에서 개발)

"ETL"은 python으로 개발이 됨
    - 특징
Unstructred data를 실체형 데이터 처럼 보이도록 함
이 테이블들에 SQL기반의 쿼리를 직접 사용할 수 있음
해당 쿼리에 대한 지정
    - 장점
대용량데이터를 쉽게 처리하기 위한 방안
SQL-based queries를 제공
사용자가 정의한 확장된 인터페이스 제공
Programmability
    - 단점
데이터를 추가하기가 어려움

```
---
layout: post
title: "book : pyspark 배우기"
date: 2021-04-03 19:20:23 +0900
category: book

---

# PySpark 배우기 책 정리



- 준비 사항

OS : MAC or linux -> Ubuntu 환경에서 공부

java v7 이상

python 3.4 이상



예제코드 URL : https://github.com/drabastomek/learningPySpark



## 1장 스파크

- 아파치 스파크(Apache Spark)

2012년에 초음 배포된 오픈소스 처리 엔진

오픈소스 분산 쿼리 및 처리 엔진

데이터가 메모리에 저장돼 있을 경우 하둡보다 100배, 디스크의 경우 10배 빠르다.

- 스파크 잡과 API

스파크 애플리케이션은 여러 개의 잡을 가질 수 있는 하나의 드라이버 프로세스를 마스터 노드에서 실행한다.

드라이버 프로세스는 실행 프로세스들을 컨트롤한다.

여러 태스크를 포함하고 있는 실행 프로세스들은 여러 개의 우커노드로 태스크를 분산시킨다.

스파크 잡에서의 객체 의존성은 비순환 방향성 그래프(DAG) 형태로 표현할 수 있다.

- RDD(Resilient Distributed Datasets)

이뮤터블(immutable) JVM 객체들의 집합으로 만들어져 있다.

-> python 데이터들이 JVM 객체들에 저장돼 있다.

transformation을 제공한다.

- 카탈리스트 옵티마이저

스파크 SQL의 코어에 카탈리스트 옵티카이저가 있음

함수 프로그래밍 구조에 기반

- 프로젝트 텅스텐

스파크 실행 엔진의 하위 프로젝트에 해당하는 코드네임

스파크 알고리즘을 향상시키는데 목적을 둠

JVM 객체 모델의 메모리를 관리

데이터 구조 디자인

다중 cpu 호출을 줄일 수 있도록 가상 함수 디스패치를 제거

- 텅스텐 페이스 2

> - 목적
>
> > 메모리 관리와 이진 프로세싱 - JVM 객체 모델과 가비지 컬렉션 오버헤드를 제거하기 위한 semantics을 활용
> >
> > 캐시 활용 연산 - 메모리 계층을 활용하는 알고리즘과 데이터 구조
> >
> > 코드 생성 - 최신 컴파일러와 cpu를 활용하는 코드 생성
>
> - 역할
>
> > 가상 함수 디스패치 제거 - 디스패치 많이 발생시 성능에 크게 영향을 주는 다중 cpu 호출을 줄인다.
> >
> > 메모리상 데이터와 cpu 레지스터 - 연산 과정에 있는 데이터를 cpu 레지스터에 저장
> >
> > 루프 언롤링과 SIMD - cpu 최적화

- pyspark 환경설정하기

```
anaconda 가상환경 생성 후 진행
1. python, java 설치 완료된 상태여야 함
java 1.8 설치및 버전 변경
sudo apt-get install openjdk-8-jdk-headless  -> 1.8 버전 설치
update-alternatives --config java -> 환경변수 java 버전 변경
2. pyspark install
pip install pyspark==2.4.7
3. Hodoop 설치하기
http://hadoop.apache.org/releases.html 에서 바이너리파일 다운로드
복사된 tar를 압축을 /usr/local/ 에 풀어준다.
sudo tar -zxvf ./hadoop-* -C /usr/local
버전이 붙어있으면 사용하기 귀찮음으로 mv를 통해 이름을 바꿔줌
sudo mv /usr/local/hadoop-* /usr/local/hadoop
4. spark 설치

5. 환경변수 등록하기
echo "
export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
export PATH=\$PATH:\$JAVA_HOME/bin
export HADOOP_HOME=/usr/local/hadoop
export PATH=\$PATH:\$HADOOP_HOME/bin
export HADOOP_CONF_DIR=\$HADOOP_HOME/etc/hadoop
export YARN_CONF_DIR=\$HADOOP_HOME/etc/hadoop
" >> ~/.bashrc
5. 명령어로 환경변수 등록 여부 확인
/usr/local/hadoop/bin/hadoop
-> JAVA_HOME이 없는경우 등록 필수

- import list
import findspark
from pyspark import SparkContext
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
findspark.init()
sc =SparkContext()
# sc = SparkContext('local')
spark = SparkSession(sc)
```



## 2장 RDD(Resilient Distributed Datasets)

분산된 immutable 자바 객체 컬렉션인 RDD연산을 매우 빠르게 하는 아파치 스파크의 핵심

- dataset

> 데이터셋은 키를 기반으로 Chunk단위로 쪼개져 있고 executor node로 분산돼 있다.
>
> 연산속도를 빠르게 하고 문제로 인해 데이터 손실이 발생했을 경우 대비책을 제공
>
> 데이터 손실에 대한 다른 방어책으로 복제가 아닌 다른 방법을 이용해 데이터를 복구

- RDD 내부 작동 원리

> 병렬로 동작 - 트랜스포메이션은 속도를 비약적으로 향상시키기 위해 실행
>
> 컬렉션에 대해 parallelize 함수를 수행 혹은 특정 위치에 저장된 파일을 읽으면서 사용할 수 있음

- 스키마

> RDD는 schema-less 데이터 구조 - 여러 자료형을 병렬 처리 가능
>
> collect 함수를 수행시 객체 내의 데이터에 접근할 수 있다.

- 전역범위, 지역범위

> - 스파크 두 가지 모드
>
> > 1. 로컬 모드
> >
> > 파이썬을 실행시키는 것과 다르지 않을 수 있다.
> >
> > 2. 클러스터 모드
> >
> > 잡 실행시 그 잡은 드라이버 노드(도는 마스터 노드)에 보내진다.
> >
> > 드라이버 노드는 잡을 위해 DAG를 생성 -> 어떤 실행 노드가 특정 태스크를 실행할지 결정

- 트랜스포메이션

> 데이터셋의 형태를 만드는 작업
>
> - map()
>
> 각 엘리먼트에 적용시 사용
>
> - filter()
>
> 데이터셋으로부터 특정 조건에 맞는 엘리먼트를 선택
>
> - flatMap()
>
> map함수와 비슷하게 동작
>
> 리스트가 아닌 평면화된 결과(flattened result)를 리턴
>
> - distinct()
>
> 특정 칼럼에서 중복된 값을 제거해, 고유한 값을 리스트로 리턴
>
> - sample
>
> 데이터셋으로부터 임의로 추출된 샘플을 리턴
>
> - leftOuterJoin()
>
> 두 개의 RDD를 두 개의 데이터셋에서 찾은 값에 기반해 조인하고, 두 개의 RDD가 매치되는 데이터에 대해 왼쪽 RDD에 오른쪽 RDD가 추가된 결과가 리턴
>
> -> 섞는 과정에서 성능저하가 발생하여 필요한 부분에서만 사요해야 함
>
> intersection 을 통해 교집합을 가질 수 있음
>
> - repartition
>
> 데이터셋을 재 파티션 -> 파티션의 개수가 바뀜 -> 데이터를 섞어 성능을 저하시킬 수 있어 사용시 주의

- 액션

> 데이터셋에서 스케줄된 태스크를 실행
>
> - task 함수
>
> 하나의 파티션에서 가장 위에 있는 n행을 리턴
>
> 큰 데이터셋일수록 중요 (collect는 전체를 리턴해서 느림)
>
> - collect
>
> RDD의 모든 에릴먼트를 드라이버로 리턴
>
> - reduce
>
> 특정 함수를 이용해 RDD의 개수를 줄ㅇ니다.
>
> RDD의 총합을 구하기 위해 이 함수를 사용할 수 있다
>
> - count
>
> RDD의 엘리먼트 개수를 센다.
>
> 전체 데이터셋을 드라이버로 옮기지 않는다.
>
> - saveAsTextFile
>
> RDD를 텍스트 파일로 저장
>
> - foreach
>
> RDD의 각 엘리먼트에 반복적으로 적용되는 함수

## 3장 데이터프레임

데이터프레임은 RDD의 테이블에서 named columns로 구성된 변경 불가능한 분산 데이터 컬렉션이다.

-> 아파치 스파크 1.3 버전에서 도입

- 데이터프레임을 이용한 파이스파크 스피드업

> stringJSONRDD 를 이용해 RDD를 생성하고, 데이터프레임으로 변환
>
> 
>
> - json 명령어 실행
>
> ```
>    - jupyter 에서 spark 쉘 실행하기
> pip install spylon-kernel
> python -m spylon_kernel install
> -> 이후 jupyter 키면 spylon-kernel이 추가된것을 확인할 수 있음
> 책에 있는 sql을 실행시 에러 발생 -> 해결필요 
> ```

## 4장 데이터모델링 준비하기

- 중복, 미관찰 값, 아웃라이어 확인하기

> - 중복값
>
> count와 distinct().count() 를 통해 갯수 비교
>
> ```
> print('Count of rows: {0}'.format(df.count()))
> print('Count of distinct rows: {0}'.format(df.distinct().count()))
> # 값이 다르다면 중복 제거
> df = df.dropDuplicates()
> ```
>
> - 관찰되지 않은 데이터
>
> ```
>    - 미관찰값 체크 예시 코드
> df_miss.rdd.map(
>     lambda row: (row['id'], sum([c == None for c in row]))
> ).collect()
>    - 미관찰값 비율 체크
> df_miss.agg(*[
>     (1 - (fn.count(c) / fn.count('*'))).alias(c + '_missing')
>     for c in df_miss.columns
> ]).show()
> 
> ```
>
> - 아웃라이어
>
> ```
>    - IQR을 이용한 아웃라이어 범위 생성
> cols = ['weight', 'height', 'age']
> bounds = {}
> 
> for col in cols:
>     quantiles = df_outliers.approxQuantile(col, [0.25, 0.75], 0.05)
>     IQR = quantiles[1] - quantiles[0]
>     bounds[col] = [quantiles[0] - 1.5 * IQR, quantiles[1] + 1.5 * IQR]
> 
>    - 아웃라이어 데이터 체크
> df_outliers = df_outliers.join(outliers, on='id')
> df_outliers.filter('weight_o').select('id', 'weight').show()
> df_outliers.filter('age_o').select('id', 'age').show()
> 
> 
> ```

- 데이터 친숙해지기

> - 기술 통계
>
> ```
> import pyspark.sql.types as typ
> 라이브러리 사용 
> ```

- 시각화

```
   - jupyter에서 셋팅
%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('ggplot')

import bokeh.charts as chrt
from bokeh.io import output_notebook

output_notebook()

   - 히스토그램
1. 데이터를 워커 노드에서 집계해 우커 노드가 bin 리스트를 드라이버 노드에게 리턴하고 각 bin의 개수를 드라이버 노드가 세는 방법
2. 데이터를 모두 드라이버 노드에 리턴, 시각화 라이브러리 함수를 이용
3. 데이터를 샘플링해 드라이버에 노드에 리턴, 드라이버는 해당 데이터를 시각화
-> 행의 개수가 많아지면 2번 방법은 사용 힘들어짐 

```

## 5장 MLlib

 MLlib은 현재 스트리밍에 대해 학습 모델링을 지원하는 유일한 라이브러리

- 패키지 개요

> 1. 데이터 전처리
>
> 피처 추출, 변형, 선택, 해싱, nlp
>
> 2. 머신 러닝 알고리즘
>
> 회귀, 분류, 군집화 알고리즘
>
> 3. 유틸리티
>
> 기술 통계, Chi-square 테스트, 선형 대수, 모델 평가





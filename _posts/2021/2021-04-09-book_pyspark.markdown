---
layout: post
title: "book : pyspark 배우기"
date: 2021-04-09 19:20:23 +0900
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

## ML 패키지 

RDD로만 동작하는 스파크의 MLlib 패키지

- 패키지 개요

> - 트랜스포머
>
> 데이터프레임에 새로운 칼럼을 추가하고 데이터를 변형
>
> 트랜스포머의 추상 클래스를 상속할때 각 트랜스포머는 trasnform() 함수를 구현해야 한다.
>
> > - Binarizer
> >
> > 주어진 임계치를 기준으로 연속적인 변수를 이진 변수로 변환
> >
> > - Bucketizer
> >
> > Binarizer와 비슷, 임계치의 리스트를 기반으로 쪼개여 몇 개의 범위로 변환
> >
> > - ChisqSelector
> >
> > 카테고리 변수들 중에서 파라미터로 주어진 numTopFeatures 개의 카테고리 변수들을 선택
> >
> > -> 타깃으 분산을 가장 잘 나타내는 변수들
> >
> > 차이-스케어 테스트를 통해 추출 
> >
> > - ContVectorizer
> >
> > 분리된 텍스트에 유용
> >
> > - DCT
> >
> > 실수로 이뤄진 벡터를 입력, 다른 빈도로 진동하는같은 길이의 벡터를 반환
> >
> > -> 데이터의 기본 빈도를 추출하거나 압축시 사용 
> >
> > - ElmentwiseProduct
> >
> > 벡터와 scalingVec 파라미터를 곱한것을 반환
> >
> > ... 나머지는 정리 생략 

- 에스티메이터

관찰된 데이터들에 대해 예측이나 분류를 수행하는 데 필요한 통계 모델 

추사 에시트메이터 클래스로부터 상속받으려면, 새로운 모델은 데이터프레임에 있는 데이터와 디폴트 또는 사용자가 제공해야 하는 파라미터를 기반으로 모델을 학습하는 fit()함수 구현해야함

> - 분류 모델
>
> LogisticRegression
>
> DecisionTreeClassifier
>
> GBTClassifier (GBT : Gradient Boosted Tree) - 이진, 연속, 카테고리 피처를 지원
>
> RandomForestClassifier
>
> NaiveBayse
>
> MultilayerPreceptronClassifier
>
> OneVsRest
>
> - 회귀 모델
>
> AFTSurvialRegression (AFT : Accelerated Failure Time) - 미개변수 모델
>
> DecisionTreeRegressor
>
> GBTRegressor
>
> GeneralizedLinearRegression
>
> IsotonicRegression
>
> LinearRegression
>
> RandomForestRegerssor
>
> - 군집화 모델
>
> BisectingKMeans
>
> KMeams
>
> GaussianMixture
>
> LDA

- 파이프라인

.. 너무 많고 다 새로워서 정리 힘듦

- 피처 추출

> - NLP
>
> NGram
>
> StopWordsRemover

...

## 7장 그래프프라임

그래프 처리를 지원하기 위해 아파치 스파크 데이터프레임을 사용 

GraphX 라이브러리와 비슷

- 차이점

> 성능 개선과 데이터프레임 API단순화에 영향
>
> python, java, scala api를 지원

-> 따로 설치해야함 

python2버전을 사용하는거 같아서 읽어보기만 하고 pass 



## 8장 텐서프레임

- 텐서프레임

> 아파치 스파크에서 텐서플로우가 배포되고 조금 지난 후인 2016년 처음 소개
>
> 스파크 데이터프레임과 텐서플로우간 다리역할을 수행 
>
> - 최적의 하이퍼파라미터 찾기위한 병렬 수행
>
> - 빠르게 실행하기
>
> ```
> $SPARK_HOME/bin/pyspark --pacakge tjhunter:tensorframes:~버전~
> 
> import tensorframes as tfs
> from pyspark.sql import Row
> ...
> 
> 	- 텐서 그래프 실행
> x = tfs.block(df,"x")  -> 데이터프레임의 칼럼의 타입
> z = tf.add(x,3)
> df2 = tfs.map_blocks(z,df)
>  	- 블록단위 연산자 reduce 연산자
> tfs.print_schema(df) ->데이터 형식 출력
> df2 = tfs.analyze(df)  -> 벡터의 차원을 알아보기 위해
> tfs.print_schema(df2) ->데이터 형식 출력 - 차원 수도 나옴
> 
> tf.readuce_sum : 엘리먼트들의 합을 계산
> tf.reduce_min :  엘리먼트들의 최솟값을 계산
> 
> ```
>



## 9장 블레이즈를 이용한 다언어 지속성

- 블레이즈

대부분의 기술을 추상화해 간단한 형태의 데이터 구조와 API를 제공 

- 블레이즈 설치하기

conda install blaze  # 위 명령어로 가능 

conda install sqlalchemy # postgreSQL 

conda install pymong	#mongoDB 연결 

-> import blaze as bl 로 설치 확인하기 

```
AttributeError: module 'pandas' has no attribute 'tslib'
위 오류 발생 의존성 문제로 확인됨 
 - 해결방법

python 설치위치\\Lib\site-packages\odo\backends\pandas.py 파일 오픈

102 라인에 
@convert.register((pd.Timestamp, pd.Timedelta), (pd.tslib.NaTType, type(None)))
를 아래라인으로 수정 
@convert.register((pd.Timestamp, pd.Timedelta), (type(pd.NaT), type(None)))

-> 변경후 아래 에러 발생
AttributeError: module 'sqlalchemy.engine' has no attribute 'RowProxy'
odo 패키지에 문제가 있는거같음 . #odo 버전을 내리거나 올려도 오류가 바뀌지않음
-> 에러 해결 못함 ㅠ
```

- 다언어 코드 지속성

> bl.data(np.array(~)) # 블레이즈 datashape구조체로 변경
>
> ~.peek()를 통해 구조체 내부 구조를 확인 가능
>
> 



-> 이번장은 설치가 안되서 일단 킵 



## 구조적 스트리밍

- 스파크 스트리밍이란?

스파크 스트리밍의 코어는 확장 가능하고 fault-tolerant를 지원하는 스트리밍 시스템

RDD배치 패러다임 개념을 사용하고 처리속도를 향상시킴

미니배치 or 일정한 간격으로 배치 작동(최소 500ms간격)

스파크 스트리밍은 DStream(Discretized Stream)으로 추상화돼 있음

- 스파크 스트리밍이 필요한 이유

> - 스트리밍 ETL
>
> 데이터가 다운스트림에 들어가기 전에 계속해서 클리닝 또는 집계를 수행 
>
> -> 최종적으로 저장되는 데이터의 양을 줄이기 위해
>
> - 트리거
>
> 이상 행위 등에 대한 실시간 탐지와 다운스트림 액션
>
> - 데이터 enrichment
>
> 풍부한 데이터 분석을 위한 실시간 데이터 조인
>
> - 복잡한 세션과 지속적인 학습
>
> 여러 데이터셋을 합쳐 실시간 데이터들을 지속적으로 분석 모델을 통해 업데이트 

- 스파크 스트리밍 애플리케이션의 데이터 흐름

> 1. 스파크 스트리밍 컨텍스트가 구동될 때, 드라이버가 실행 노드에서(스파크 워커) 작업 수행
> 2. 리시버에 있는 실행 노드는 데이터 스트리밍을 출발지로부터 받아들임 -> 리시버는 스트림을 블록단위로 나눠 블록을 메모리에 저장
> 3. 블록 데이터 유실을 방지하기 위해 다른 실행 노드에 복제
> 4. 블록ID 정보는 드라이버에 있는 블록 관리 마스터로 전달
> 5. 스파크 스트리밍 컨텍스트에서 설정된 모든 배치 데이터에 대해 드라이버는 해당 블록을 처리하기 위해 스파크 태스크를 실행

- 스트리밍 구조

> 스파크 SQL 엔진과 카탈리스트 옵티마이저에서 발생하는 sQL/데이트프레임 쿼리 수행은 아래 3단계를 거침
>
> 1. 논리적플랜과 여러 물리적 플랜을 빌드
> 2. 비용 옵티마이저를 이용해 여러 물리적 플랜 중에서 최적의 물리적 플랜을 찾음
> 3. 최적의 물리적 플랜에 기반해 성능이 좋은 코드를 생성



## 11장 스파크 애플리케이션 패키지화

- spark-submit 명령어

로컬 or 클러스터에서 스파크 잡을 서브미샇는 시작점은 spark-submit 스크립트

잡을 서브밋하는 것뿐만 아니라 상태를 체크하는 부분이나 잡을 종료하는 부분에도 관여 

> - 명령 파라미터
>
> ```
> --master
> 마스터 노드의 URL을 명시하기 위한 파라미터
> 	local : 로컬 컴퓨터를 싱행하기 위해 사용 (default - 하나의 스레드)
> 	spark://host:port : 스파크 standalone 클러스터를 사용할 경우
> 	mesos://host:port : 스파크 클러스터가 Mesos를 이용해 실행될 경우
> 	yarn : workload 균형을 맞추는 경우
> --deploy-mode
> 스파크 드라이버 프로세스를 로컬 컴퓨터에서 실행하거나 클러스터 내부의 다른 워커 머신을 이용해 실행할 경우 사용하는 옵션  -> defulat client
> --name
> 애플리케이션 이름
> --py-files
> 콤마로 분리된 .py .egg .zip파일 리스트
> 파이썬 애플리케이션에 포함될 리스트를 명시
> --files
> 각 실행 노드가 사용할 수 있는 파이을을 전달, 콤마로 분리
> --conf
> 애플리케이션의 설정을 명령행으로부터 동적으로 변경할 수 있는 파라미터
> --properties-file
> 설정 파일
> --driver-memory
> 드라이버에 할당할 메모리 default=1024M
> --executor-memory
> 각 실행 노드에 할당될 메모리 defulat=1G
> --verbose
> 애플리케이션 실행 시 추가적인 디버그 정보 프린트
> --version
> 버전 출력
> --supervise
> 드라이버가 사라지거나 에러발생시 드라이버를 재시작
> --kill
> submission_id에 해당하는 프로레스 종료
> --status
> 애플리케이션의 상태를 요청
> --queue
> 잡을 서브밋할 YARN 큐를 명시하기 위해 
> default : default
> --num-executors
> 잡을 요청할 실행 머신의 개수를 명시하기 위한 옵션
> 동적 할당시, 최소 실행 노드 개수가 적어도 명시된 숫자만큼은 할당
> ```
>
> 


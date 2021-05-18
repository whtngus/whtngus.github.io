---
layout: post
title: "book : Learning Spark"
date: 2021-05-17 19:20:23 +0900
category: book
---

# 책 제목 : Learning Spark

- 정리 
  

코드 관련 정리 x 

pyspark 위주로 내용만 보기

개념이랑 내부 구조 돌아가는걸 익히는걸 목표로! 

코드 url : https://github.com/databricks/learning-spark

# Chapter 1  스파크를 이용한 데이터 분석

- 아파치 스파크란

> 범용적이면서도 빠른 속도로 작업을 수행할 수 있도록 설꼐한 클러스터용 연산 플랫폼
>
> 맵리듀스(MapReduce) 모델을 대화형 명령어 쿼리나 스트리밍처리등이 가능하도록 확장한 것

- 스파크 코어(Spark Core)

> 작업 스케줄링, 메모리 관리, 쟁애 복구, 저장 장치와의 연결등 기본적인 기능 제공
>
> 분산 데이터세트(RDD, Resilient Distributed Dataset)를 정의하는 API의 기반

-  스파크 SQL

> 정형 데이터를 처리하기 위한 스파크 패키지 
>
> SQL, 하이브 테이블, 파케이(Parquet), JSON 등 다양한 데이터 소스를 지원
>
> 아파치 하이브(Hive)의  HQL(하이브 쿼리 언어)를 써서 데이터에 질의를 보낼 수  있다.
>
> 샤크(Chark)라는  SQL-on-Spark 프로젝트가 있는데 이를 스파크 위에서 돌아가도록 하이브를 수정한것

- 스파크 스트리밍 : 실시간데이터 스트림을 처리 간으하게 해 주는 스파크 컴포넌트

- MLib : 머신러닝 기능을 가지고 있는 라이브러리
- 그래프X : 그래프 병렬연산 수행 
- 클러스터 매니저 : YARN, Apach Mesos등 스파크에서 지원하는 가벼운 클러스터 매니저등 동작시킴

# Chapter 2 스파크 맛보기

https://www.apache.org/ 해당 사이트에서 다운로드

### Spark 핵심 개념

스파크 애플리케이션은 클러스터에서 다양한 병렬 연산을 수행하는 드라이버 프로그램으로 구성됨

- 드라이버 프로그램

만든 어플리케이션이 main 함수를 가지고 클러스터의 분산 데이터세트를 정의하고 그 데이터세트에 연산 작업을 수행

드라이버 프로그램들은 연산 클러스터에 대한 연결을 나타내는 SparkContext 객체를 통해 스파크에 접속(보통 sc변수로 선언)

lines.filter(lambda line : "Python" in line) 과 같이 필터로 사용 

- SparkContext 초기화

```
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("~~~")
sc = SparkContext(conf = conf)
```

> - 필수 인자 
>
> 클러스터 URL : local 부분 어떤식으로 클러스터에 접속할지 정보
>
> 애플리케이션 이름 : 클러스터 UI에 저 이름으로 애플리케이션을 구분

SparContext에서 stop() 메소드를 호출하거나 그냥 애플리케이션을 끝냄으로써 종료 가능

# Chapter3 RDD로 프로그래밍하기

RDD(Resilient Distributed Dataset) : 단순하게 분산되어 존재하는 데이터 요소들의 모임

- RDD 기초

> 스파크의 RDD는 분산되어 변경 불가능한 객체 모음
>
> 각 RDD는 클러스터에서 서로 다른 노드들에서 연산 가능하도록 여러 partition으로 나뉨 
>
> RDD는 두 가지 타입의 연산을 지원(transformation 과 action)
>
> - transformation
>
> 존재하는 RDD에서 새로운 RDD를 만들어 냄
>
> ex - filter() transformation ) line.filter(lambda line : "Python" in line)
>
> -  action
>
> RDD를 기초로 결과 값을 계산해 드라이버 프로그램에 되돌려 주거나 외부 스토리지에 저장
>
> ex - first() action ) df.first()

기본적으로 RDD는 필요한 순간에 연산을 하지만 persist()를 사요해서 데이터 결과를 유지할 수 있다.

- RDD 생성하기

외부 데이터세트 로드와 직접 만든 드라이버 프로그램에서 데이터 집합을 병렬화함으로써 RDD 생성 가능

```
- ex
sc.parallelize(["numpy","Tensorflow"])
or
sc.textFile("./path")
```

- RDD의 연산

> - Transformation
>
> 새로운 RDD를 만들어 돌려주는 RDD 연산 방식
>
> 여유로운 수행 방색으로 많은 트랜스포메이션은 한 번에 하나의 요소에서만 작업이 이루어진다.
>
> 모두다가 그런 방식을 따르진 않음
>
> - action
>
> 드라이버에 프로그램에 최종 결과 값을 되돌려 주거나 외부 저장소에 값을 기록
>
> transformation의 계산을 수행하도록 강제함

- 스파크에 함수 전달

> python 에서는 세 가지 방법이 있음
>
> 1. 람다식 (예제는 filter로 계속 사용해서 생략)
>
> 주의점은 함수를 포함한 객체를 직렬화 하는것
>
> 갤체의 필드 참조를 갖고 있는 함수를 전달할 때 스파크는 작업 노드에 전체 객체를 전달하므로 필요로 하는 정보에 비해
>
> 커질 수 있는 문제가 있음 
>
> 2. 함수전달, 지역함수 전달
>
> 3. 최상위 함수 전달
>
> 예시는 다음장에서 설명

- 많이 쓰이는 트랜스포메이션과 액션

> map() 과 filter()를 자주 씀
>
> - map
>
>  rdd에 함수적용 결과를 rdd에 되돌려줌
>
> rdd.map(x=>x+1)
>
> - flatMap
>
> RDD의 각 요소에 함수를 적용하고 반환
>
> 반복자의 내용들로 이루어진 RDD를 되돌려줌 (단어 분해 등)
>
> rdd.flatMap(x=>x.to(3))
>
> - filter() 생략
> - distinct() 생략
> - sample()
>
> 복원추출, 비복원추출 가능
>
> - union(), intersection(), subtract(), cartesian()
>
> 합집합, 교집합, 한 쪽만, 두 RDD의 카테시안곱(모든 경우 수)
>
> - reduce() 액션
>
> 두개의 인자로 데이터를 합쳐 같은 타임 데이터를 하나 반환
>
> rdd.reduce(lambda x, y : x + y)
>
> - fold()
>
> reduce에 전달과 동시에 동일한 형태의 함수를 인자로 받음
>
> 파티션 초기에는 제로 벨류를 인자로 받음
>
> - collect()
>
> RDD의 모든 데이터 요소 리턴
>
> - count()
> - countByBalue()
>
> RDD에 있는 각 값의 개수 리턴
>
> - take(num)
> - top(num)
> - takeOrdered(num)(ordering)
> - takeSample(withReplacement,num,[seed])
> - reduce(func)
> - fold(zero)(func) -> reduce와 동일하나 제로 베류를 넣어준다
> - aggregate(zeroValue) -> reduce와 동일하나 다른타입 반환
> - foreach(func) -> RDD의 각 값에 func을 적용

- 영속화(캐싱)

동일한 RDD를 여러번 수행시킬때, 재연산을 하게 됨

여러번 반복 연산을 피하기 위해 영속화(persist/persistence) 요청을 할 수 있음

persist()



# 4장 키/값 페어로 작업하기

key/value pair는 RDD집합연산에서 쓰이며 ETL(Extract, Transform and Load) 작업에도 데이터를 변환하는 방식으로 쓰임 

- 페어 RDD

> - 페어 RDD 생성
>
> ```
> pairs = datas.map(lambda data: (x.split("\n")[0],x.split("\n")[1:]))
> ```
>
> - 페어 RDD의 트랜스포메이션
>
> ```
> - reduceByKey(func)
> 동일 키에 대한 값을을 합침 
> - groupByKeh()
> 동일 키에 대한 값들을 그룹화
> - combineByKey(createCombiner, mergeValue, mergeCombiners, partitionner)
> 다른 결과 타입을 써서 동일 키의 값들을 합침
> - mapValueS(func)
> 키의 변경 없이 페어 RDD의 각 값에 함수를 적용
> - flatMapValues(func)
> 페어 RDD의 각 값에 대해 반복자를 리턴하는 함수를 적용
> - keys(), values(), sortByKey()
> - 두 페어 RDD 트랜스포메이션
> subtractByKeu, join, rightOuterJoin, leftouterJoin, cogroup
> ```
>
> - 데이터 그룹화
>
> groupByKey()와 reduce(), fold()를 사용시 키별 집합 연산함수를 사용하면 더 효율적이다.
>
> 메모리에 있는 값에 RDD를 합치는 대신 키별로 데이터를 합치고 합친값의 RDD를 받기 때문에 
>
> - 데이터 파티셔닝 - partitionBy()
>
> 네트워크 비용을 줄이기 위해 RDD의 파티셔닝 제어 방법을 사용
>
> 파티셔닝은 조인 같은 키중심의 연산에서 데이터세트가 여러번 재활용될 때만 의미가 있다.

# 5장 데이터 불러오기/저장하기

- 일반적으로 지원하는 파일 포맷

텍스트 파일(구조화 x), json(구조화 일부), CSV, 시퀀스 파일, 프로토콜 버퍼, 오브젝트 파일

> - 텍스트파일
>
> 각 라인이 RDD의 개별 데이터로 들어가게 됨 
>
> sc.textFile("경로")
>
> result.saveAsTextFile(outputFile)
>
> - json
>
> import json
>
> input.map(lambda x: json.loads(x))
>
> (dat.filer(lamda x: x["key"])).map(lambda x: json.dumps(X)).saveAsTextFile(outputFile))
>
> - 그 외에는 그떄그때 검색 ㄱㄱ

- 파일 압축

> 스파크에서 지원하는 압축 옵션들
>
> - gzip
>
> 분할 x, 빠름, 텍스트 우수
>
> - lzo
>
> 분할 o,매우 빠름, 텍스트 보통, 노드에 설치해야 사용 가능
>
> - bzip2
>
> 분할 o, 느림, 텍스트 매우 우수
>
> - zlib
>
> 분할 x, 느림, 텍스트 보통
>
> - Snappy
>
> 분할x, 매우빠름, 텍스트 x, 사용 불가능

# 6장 스파크 프로그래밍

accumulator는 정보들을 누산

broadcast variable는 효과적으로 많은 값들을 분산시켜 줌

- 어큐뮬레이터

> 스파크의 공유 변수인 어큐뮬레이터와 브로드캐스트 변수는 일반적인 통신 타입인 결과의 집합 연산(aggregation)과 broadcast에 대해  map이나 filter 에서 복사볻을 받아 작업하면서 업데이트된 내용이 다시 드라이버 프로그램으로 돌아오지 않는 문제를 해결
>
>  
>
> 가장 흔한 수행방법 중 하나는 작업 수행 중에 발생하는 일에 대한 개수를 디버깅 목적으로 헤아리는 것 
>
> ```
> def test(line):
>    global blankLines # 접근할 전역변수로 지정
>    ~~~
>    
> # 공유변수로 접근
> print(blankLinkes.value)
> ```
>
> pyspark는 여유로운 수행방식을 수행하기땜ㄴ에 saveAsTextFile 수행 후 사용 가능
>
> -  어큐뮬레이터의 동작 방식
>
> > - 드라이버에서 SparkContext.accumulator(initialValue)를 호출하여 초기 값을 가진 어큐뮬레이터를 생성 반환갑슨 org.apache.spark.Accumulator[T] T는 초기값 타입
> > - 스파크 closure의 작업 노드 코드에서 어큐뮬레이터에 += 메소드를 써서 값을 더함
> > - 드라이버 프로그램에서 value 속성을 불러 어큐뮬레이터 값에 접근
>
> 자세한 사용 방식은 그때그때 검색해서
>
> -> pyspark 작동시에 이방을 이용해서 변수 체크및 count 디버깅이 가능하다 에 중점을 두자!
>
> *액션에 사용되어있던 어큐뮬레이션들에 대한 것이며, 각 태스크의 업데이트는 스ㅏ크에 의해 각 어큐뮬레이션에 한 번씩만 반영된다* -> 장애나 방복연산 횟수에 의해 계속 누적될 수 있음

- 브로드캐스트 변수

스파크 연산에 쓸 크고 읽기 적욘인 값을 모든 작업 노드에 효과적으로 전송하는데 쓰임

> 병렬 작업에서 동일 변수를 사용할 수 있으므로 효과적이지 못해 보이지만 스파크는 매 연산마다 그 변수를 보낸다.
>
> 예시코드 생략 (그냥 전체변수로 함수 밖에서 선언 )
>
> - 브로드캐스트 최적화
>
> > 빠르고 작은데이터의 직렬화가 필요
> >
> > spark.serializer 속성을 이용해 다른 직렬화 라이브러리 를 사용 혹은 카이로 등을 사용해야함

파티션별로 작업하기

> mapPartitions(), mapPartitionsWithIndex(), foreachPartiion()

- 수치 RDD 연산들

count, mean,sum, max,min, variance, sampleVariance, stdev, sampleStdev 



# 7장 클러스터에서 운영하기

스파크의 장점은 머신을 추가하고 클러스터 모드에서 돌려 봄으로써 얀산 능력을 더 증대시킬수 있는 장점이다.

- 스파크 실행 구조

> 분산 모드에서 스파크는 하나의 중앙 조정자(coordinator)와 여러 개의 분산 작업 노드로 구성되는 마스터/슬레이브 구조를 사용한다.
>
> 중앙 조정자는 드라이버라고 부른다.
>
> 드라이버는 익스큐터(executor)라고 불리는 다수의 분산 작업자들과 통신하고, 자신만의 자바 프로세스에서 돌아가며 각 익스큐터 또한 독립된 자바 프로세스이다.
>
> 하나의 드라이버와 익스큐터들을 합쳐 스파크 애플리케이션이라고 부른다.
>
> - 드라이버
>
> > main()메소드가 실행되는 프로세스
> >
> > 드라이버는 SparkContext를 생성하고 RDD를 만들고 트랜스포메이션과 액션을 실행하는 사용자 코드를 싱행하는 프로세스
> >
> > 드라이버가 실행될 때 두 가지의 임무를 수행
> >
> > 1. 사용자 프로그램을 태스크로 변환(물리적 하나의 노드에서 실행되는 단위 작업)
> > 2. 익스큐터에서 태스크들의 스케줄링(익스큐터에서 개별 작업을 위한 스케줄을 조정)
>
> - 익스큐터
>
> > 스파크 작업의 개별 테스크를 실행하는 작업 실행 프로세스
> >
> > 두 가지 역할을 함
> >
> > 1. 애플리케이션을 구성하는 작업들을 힝행하여 드라이버에 결과 반환
> > 2. 각 익스큐터 안에 존재하는 블록 매니저 서비스를 통해 캐시하는 RDD를 저장하기 위한 메모리 저장소를 제공
>
> - 클러스터 매니저
>
> > 클러스터 매니저에서 익스큐터와 드라이버 실행
> >
> > 스파크와 붙이거나 뗄 수 있는 컴포넌트(pluggable) -> 얀, 메소스, 내장 매니저 등 다양한 외부 매니저들 가능하도록 함

- 사용자 코드와 의존성 라이브러리 패키징

> 알려지지 않은 라이브러리를 사용한다면 스파크 애플리케이션이 실행 중일 때 그 라이브러리들이 위치해 있도록 해야함
>
> 파이썬은 서드파티 라이브러리를 설치해야함
>
> 1. 라이브러리들을 클러스터 머신들에 직접 설치
> 2. spark-submit의 인자로 00py-files를 써서 개별 라이브러리를 제출 (권한이 없으면 직접 서버에 설치가 편함)

- 의존성 충돌

동일한 라이브러리를 각자 사용하면서 생기는 의존성 충돌(NoSuchMethodError or ClassNotFoundException)

-> 모든 서드파티 같은 버전 사용

-> shading 방법으로 애플리케이션을 패키징

- 스파크 애플리케이션간의 스케줄링

클러스터 매니저가 스파크 애플리케이션들 사이에서 자원을 공유/관리해 주는 기능에 의존하여 스케줄링

스파크 에플리케이션 --익스큐터 서비스요청-> 적당한 개수의 익스큐터 반환

장시간 작동이 필요할 시 Fair Scheduler를 사용하여 우선순위를 조정할 수 있는 큐를 제공

- 애플리케이션 제출

> - 자원 사용량 설정
>
> >  익스큐터들 사이에 자원을 얼마나 할당할지 결정
> >
> > - 익스큐터 메모리
> >
> > 애플리케이션이 각 작업 노드에서 메모리를 얼마나 쓸지 결정
> >
> > - 코어 수의 최대 총합
> >
> > 모든 익스큐터가 사용할 코어 개수의 총합(default 무한대)
>



# 8장 스파크 최적화 및 디버깅

- SparkConf로 스파크 설정

SparkConf 객체는 SparkContext를 만들기 위해필요

```
conf = new SparkConf()
conf.set("spark.app.name", "~~")
...
sc = new SparkContext(conf)
```

- 스파크의 실행 구성

> 스파크를 실행시 명령어들의 결과 RDD인 counts는 각 로그 레벨 메시지의 개수를 갖고 있는다.
>
> 내부적으로 정의된 RDD 객체들의 지향성 비순환 그래프(DAG, Directed Acyclic Graph)를 갖게 되고, 이것이 나중에 액션을 수행할 때 쓰이게 된다.
>
> - RDD 그래프 예시
>
> HadoopRDD -> MappedRDD(sc.textFile(...)) -> MappedRDD(.map(...)) -> FilteredRDD(.filter(..)) -> SuffledRDD(reduceByKey(...))
>
> -  같은 순서의 물리적 실행 RDD 
>
> 단계1
>
> HadoopRDD -> MappedRDD -> MappedRDD -> FiltredRDD
>
> 단계2
>
> -> SuffledRDD

- 병렬화 수준

> RDD의 논리적인 표현은 객체들의 모음
>
> 기본적으로 spark는 병렬화를 자동적으로 수행해 대체로 좋은 성능을 보임 
>
> - 병렬화 수준이 서능에 영향을 미치는 경우
>
> > 1. 병렬화 개수가 너무 적은 경우
> >
> > 스파크 리소스들을 놀리게 되는 경우가 발생
> >
> > 이 경우 더 많은 코어를 더 많은 코어를 쓰도록 병렬화 수준을 올리는 것이 좋음
> >
> > 2. 병렬화가 너무 많은 경우
> >
> > 각 파티션에서의 작은 오버헤드라도 누적되면 성능 문제가 심각해짐
> >
> > 이런 단위는 밀리초 내로 순식간에 끝나는 테스크가 있거나 아무 데이터도 읽거나 쓰지 못하는 태스크가 있는 것을 확인해 파악 가능
>
> - 병렬화 수준 조절
>
> > 1. 데이터 셔플이 필요한 연산 간에 생성되는 RDD를 위한 병렬화 정도를 인자로 전달 
> >
> > 2. RDD를 더 적거나 더 많은 파티션을 갖도록 재배치
> >
> > repartition() 메소드는 RDD를 무작위로 섞어 원하는 개수의 파티션으로 다시 나눠줌 
> >
> > coalesce() 메소드를 통해 파티션의 개수를 줄일 수 있음

- 직렬화 포맷

> 스파크는 기본적으로 자바에서 내장된 직렬화를 이용

- 메모리 관리

각 익스큐터 내부에서 메모리는 다음의 여러 가지 목적으로 사용됨

> - RDD 저장용
>
> persist()나 cache()를 호출할 때 그 파티션들은 메모리 버퍼에 저장된다.
>
> JVM의 힙 메모리 대비 spark.storage.memoryFraction 의 퍼센트로 저장되며 초과시 오래된 파티션들은 메모리에서 제거됨
>
> - 셔플 및 집합 연산 버퍼
>
> 셔플시 셔플 출력 데이터를 저장하는 중간 버퍼를 생성
>
> 이 버퍼는 집합 연산의 중간 결과를 저장하거나 결과 일부분으로 출력될 데이터를 저장하는 용도
>
> spark.shuffle.memoryFraction으로 설정
>
> - 사용자 코드
>
> 사용자 코드는 RDD 저장과 셔플 버퍼 등이 할당된 다음에 JVM 힙에 남아 있는 나머지를 모두 사용

# 9장 스파크 SQL

구조화된 데이터인 스키마(schema)를 가진 모든 데이터를 다룸

- SQL의 세가지 주 기능

> 1. 파이썬, 자바, 슼칼라에서 DataFrame 추상화 클래스를 제공
> 2. 다양한 구조적 포맷의 데이터를 읽고 쓸 수 있음
> 3. 스파크 프로그램 내부에서나 표준 데이터베이스 연결을 제공하는 외부 툴을 사용해 SQL로 데이터 질의 가능

- SQL 라이브러리 링크

> 스파크 SQL은 하둡의 SQL 엔진인 Apache Hive를 포함하거나 포함하지 않고 빌드 가능
>
> HIve는 하이브 테이블(UDF. User Defined Function), SerDes(serialization/deserialization), 하이브 QL(Query Language) 등에 접근할 수 있다.

- SQL 사용 예시

```
# SparkSQL
from pyspark.sql import HiveContext, Row
# 하이브 의존성이 없는경우 
from pyspark.sql import SQLContext, Row
# 컨텍스트 생성
sc = SparkContext(...)
hiveCtx = HiveContet(sc)
# 질의문
hiveCtx.sql("sql query 내용")
```

- 데이터 프레임

> - 기본 데이터 프레임 연산
>
> show() - 내용을 보여줌
>
> select() - 지정 필드나 함수 결과를 보여줌
>
> filter() - 조건에 맞는 레코드만을 가져옴
>
> groupBy() - 칼럼에 따라 그룹화, 이어서 min, max, mean, agg 같은 집합 연산을 필요로함

- 캐싱

각 컬럼의 타입을 알고 있으므로 스파크는 좀 더 효율적으로 데이터를 저장

메모리 효율적인 형태로 캐싱하도록 하기 위해소 hiveCtx.cacheTable("~~") 메소드라는 특수한 메소드를 사용

-> 캐시된 데이터프레임은 다른 RDD처럼 스파크 애플리케이션 UI에 표시된다.

- 사용자 정의 함수

사용자 정의 함수(UDF. User-defined function)은 직접 만든 로직의 함수를 등록하여 SQL 내에서 호출할 수 있게 해준다.

> - 스파크 SQL UDF
>
> 프로그래밍 언어에서 함수만 전달해 쉽게 UDF를 등록할 수 있는 내장 메소드를 지원
>
> python은 람다나 함수를 넘기는 방식을 사용 (java는 적절한 UDF 클래스를 상속해서 사용)
>
> - 하이브 UDF
>
> 기존의 하이브 UDF를 쓸 수 있음
>
> HiveContext를 이용해  hiveContext.sql("~~") 로 사용

- 성능 최적화 옵션

> - spark.sql.codegen - default : false
>
> true이면 스파크 SQl이 쿼리문을 싱ㅎ행할 때마다 자바 바이트코드로 컴파일한다.
>
> 복잡한 쿼리에 대해서는 성능이 향상되지만 수행 시간이 짧으면 오히려 느려질 수 있음
>
> - spark.sql.inMemoryColumnarStroage.compressed - default : true
>
> 메모리에 저장하는 칼럼 지향 저장 포맷을 자동으로 압축
>
> - spark.sql.inMemoryColumnarStorage.batchsize - defulat : 1000
>
> 너무 큰 값은 out of memory 문제를 발생시킬 수 있음
>
> - spark.sql.parquet.compression.codec - default : snappy
>
> 사용할 합축 코덱을 정의 (uncompressed, snappy, gzip, lzo, ... 등)

# 10장 스파크 스트리밍                                                                                                                                                                                

Spark Streaming은 데이터가 도착하자마자 작업할 수 있는 에플리케이션들을 위한 스파크 모듈(ex - 실시간 머신러닝 모듈)

RDD의 개념을 바탕으로 구축된 스파크처럼 스파크 스트리밍은 DStream(discretized stream, 이산 스트림)이라 불리는 추상화 개념을 바탕으로 한다.

주 시작점이 되는 StreamingContext를 생성하는 것 -> 여기에서 SparkContext도 생성

- 아키텍처와 추상 개념

> 스파크 스프리밍은 마이크로 배치(micro-batch) 아키텍처를 사용
>
> -> 작은 배치 단위들 위에서 각 배치 처리의 연속적인 흐름으로 간주
>
>   스파크의각 입력 소스마다 리시버를 실행시킴 
>
> + checkpointg이라는 견고한 파일 시스템에 주기적으로 상태를 저장하는 메커니즘을 가지고있다

- 트랜스포메이션

DSstream의 트랜스포멩션은 무상태(stateless)와 상태 유지(stateful) 로 나뉜다. 

- 핵심소스

DStream을 생서하는 모든 메소드들은 모두 StreamingContext에서 사용할 수 있다.

> - 파일 스트림
>
> 스파크는 모든 하둡 호환 파일 시스탬에서 일기를 지원 
>
> - 아카 액터 스트림
>
> Akka acor를 쓸 수 있게 해주는 actorStrom
>
> 아카 액터를 생성하고 org.apache.spark.streming.recevier.ActorHelper 인터페이스를 구현해야 함 
>
> - 아파치 카프카(Apache Kafka)
>
> 속도와 유연함 때문에 인기 있는 입력 소스
>
> - 아파치 플럼
>
> 두 가지 종류를 가지고 있음 
>
> 푸시 기반 리시버 - 푸시 기반 접근은 빠른 셋업이 가능 그러나 트랜잭션을 쓰지 않는다.
>
> 풀 기반 리시버 - 객체가 주어진 자동 -> 스파크



- 체크포인팅

스파크 스트리밍에서 장애 댕을을 위해 구축할 필요가 있는 핵심 매커니즘

> - 장애 시 재연산 필요한 상황을 제한
> - 드라이버에 대해 자해 대응 기능 제공 

- 성능 고려상황

> - 배치/윈도 크기
>
> - 병렬화 수준
>
> 리시버 개수 늘리기
>
> 받은 데이터를 명시적으로 재파티셔닝(리시버를 더 늘리기 힘들면 재파티셔닝을 통해 받은 데이터를 재배치) 
>
> 집합 연산 시 병렬화 개수 늘리기
>
> - 가비지 컬렉션과 메모리 사용량



마지막 11장 MLlib로 해 보는 머신러닝 은 생략


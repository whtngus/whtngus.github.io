---
layout: post
title: "book : Learning Spark"
date: 2021-05-05 19:20:23 +0900
category: book
---

# 책 제목 : Learning Spark

- 정리 
  

코드 관련 정리 x 

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
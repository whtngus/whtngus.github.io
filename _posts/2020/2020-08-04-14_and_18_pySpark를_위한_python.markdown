---
layout: post
title: "14_and_18_pySpark를_위한_python"
date: 2020-08-04 19:20:23 +0900
category: bigdata_computing
---

# 14. pySpark를 위한 Python

## 챕터 제목은 python 이나 이번 강의는 mysql function 위주로 진행됨

> explode 함수<br>

```
SELECT SPLIT(people,",") FROM example;
people 의 컬럼이 리스트 형태로 나오게 됨 
```

> SENTENCES 함수

```
데이터를 읽어서 문장으로 나눠줌
출력 array 형태 (문장으로 나뉘고 그 다음은 어절단위로 나뉨)
ex)
SELECT SENTENCES(txt) FROM phrases 
```

> NGRAMS 함수 

```
데이터를 n-gram 단위로 분할시켜줌
```

# 15~18.  Python 기초

> python 버전의 spark

```
python 버전의 spark 를 pyspark라고 한다.
python 강의는 알고있는 내용이여서 생략
```




















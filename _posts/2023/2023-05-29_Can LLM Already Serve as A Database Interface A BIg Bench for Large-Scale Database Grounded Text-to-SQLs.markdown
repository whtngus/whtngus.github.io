---
layout: post
title: "Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs"
date: 2023-05-27 00:05:23 +0900
category: paper
---

# Can LLM Already Serve as A Database Interface? A BIg Bench for Large-Scale Database Grounded Text-to-SQLs

2023년 3월 4일 

알리바바

url : https://arxiv.org/pdf/2305.03111v1.pdf

github : https://bird-bench.github.io/

https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/bird



학습 데이터 제공 



# Abstract

Text-to-SQL parsing 테스크는 자연어를 입력으로 받아 구조화된 sql문을 생성하는것 혹은 sql을 실행하는 것을 목표로한다.

최근 Codex and ChatGPT등을 통해 성능향상을 보임

일반적인 벤치마크는 Spider와 WikiSQL 데이터 셋으로 db 스키마에 초점을 맞추고 있음

이를 해결하기 위해 BIRD(a BIg benchmark for laRge-scale Database ) 데이터셋을 제안함 

12,751개의 text - sql 데이터셋의 95개의 데이터베이스, 그리고 37개의 도메인 데이터 (33.4 GB)

-> dirty database contents 에서 sql을 잘생성할 수 있는지 볼 수 있음

ChatGPT의 경우 40%의 정확도를 달성했고 사람의 경우 92.96%로 아직 큰 차이가 있음 

# 1 Introduction

Text-to-SQL parsing은 자연어에서 sql 쿼리로 변환하는 테스크이다.

최근 LLM들이 많이 나오며 성능이 향상됨 

기존에는 해당 테스크를 Spider, WikiSQL 데이터셋으로 평가함 

-> 최근 3년간 연구가 되며 sota모델이 각 53.% 85.3%로 정확도 향상을 보임 

![f_1](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f_1.PNG)

최근 sota 모델들은 현실적인 DB인 노이즈를 많이 가지고 있는 큰 규모의 데이터셋을 해결하지 못하는 문제를 발견

-> 당연하게도 Dataset이 그런식으러 안돼있기 떄문에 

이를 해결하기 위해 데이터셋인 BIRD, a BIg Bench for LaRge-Scale Database Grounded in Text-to-SQL 제안

이 데이터셋은 

학습시 80개의 오픈소스 데이터베이스 , 15개의 추가 RDB를 crowdsourcing 클라우드 소싱을 통해 데이터를 수집함.

이 데이터셋을 통해 테스트해본 결과 Codex는 25.88% 그리고 ChatGPT(3.5)는 28.95% 정확도를 달성함 

# 2 Task Formulation & Annotations

## 2.1 Task Definition.

![f1](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f1.PNG)

Q : Question

Y : Sql query

D = \<C, T\> 데이터 베이스 

C : Column

T : Table 

K  : model’s comprehension (문맥 정보)

θ : parameter

KaggleDBQA, KnowSQL 에서 json, csv 파일 형식으로 제공 (데이터셋)

# 3 Dataset Construction

## 3.1 Database Source

일반적으로 DB를 수집하기는 개인정보 이슈로 매우 어려움 

데이터를 3군대에서 수집함

32%는 Kaggle에서 

48%는 CTU Prague Relational Learning Repository에서 (DB연구를 위해 데이터셋 지원하는곳)

20%는 DuSQL의 open table 에서 



95%의 DB의 학습 평가 테스트 데이터는 69, 11, 15 이렇게 구성됨 

## 3.2 Question Annotation

- Entrance

학사들을 고용해 sql 질문을 만듦 

> 1. ER diagrams and database description
>
> 위 파일을 통해 이해시킴
>
> 2. sample database presentation
>
> 샘플 데이터베이스를 보여줘 이해를 도움 
>
> (10개의 도메인에 대한 sql 질문)
>
> 3. 전문가 사전에 정의된 3가지 룰을  통해 평가
>
> 3명중 2명에게 valid 를 받아야 통과



한 학생이 한 DB에 대해서 8개 이상을 만든 경우에만 사용함 

11명의 학생이 질문셋을 위와같은 규칙으로 생성 

- Database Description File.

![f_2](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f_2.PNG)

DB description은 annotator를 도와주기위한 것

구성

> 1. Full schema name
>
> 이해하기 어려운 DB의 테이블 컬럼 이름을 짧게 요약한 것
>
> 2. Value description
>
> 위의 Figure2에서 처럼 토큰이나 DB의 값이 문자열이 연결되지 않을때 유용함 

- External Knowledge.

전문적인 데이터분석을 위해 4가지 카테코리로 질문을분류

> 1. Numeric Reasoning Knowledge
>
> 수학적인 계산이 필요한 경우 
>
> MINUS, ADDITION, DIVISION, MULTIPLY 등 8가지 수학 계산 
>
> 2. Domain Knowledge
>
> 도메인에 대한 질문인 경우 
>
> 3. Synonym Knowledge
>
> 동의어 단어나 정규식 사용하는 경우 
>
> 4.  Value Illustration
>
> 데이타 값과 타입에 대한 설명을 하는경우 
>
> 예시> "center" can be represented by  "pos = C" in the database professional_basketball

## 3.3 SQL Annotation

- Entrance

SQL 질문의 퀄리티를 높이기 위해 학생들을 팀을 구성함 

각 팀은 질문 생성에 대한 실력을 엄격하게 평가를함 

각 어노테이터는 10개의 질문을 하고 스코어가 10중 9이상인 데이터만을 사용 

- Double-Blind Annotation

Figure 2의 (b)에서 double-blind technique를 사용

두명의 annotator에게 대화를 하지 않고 만든 sql 쿼리(정답)이 같은지 확인함 

- Examination

double-blind 작업 후 전문가가 다시 sql 쿼리를 체크함

-> 이상한 경우 결과를 일부 변경함 

전문가 체크를 통해 약간의 실수도 제거

- Difficulty

난이도를 simple, moderate, challenging 3단계로 같이 레이블링 지정

annotator 1차 체크 -> 전문가 2차 체크 

#  4 Data Statistics

## 4.1~2 Overall Statistics,  Question Statistics

![t_1](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\t_1.PNG)

2개의 큰 타입 Fundamental, Reasoning 타입으로 으로 나누고

각 큰 타입을 4개의 작은 타입으로 나눔

아래 그림 참조

![f_3](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f_3.PNG)

## 4.3 Database Statistics

![f_4](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f_4.PNG)

## 4.4 SQL Statistics

![f_5](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f_5.PNG)s

sql 복잡도 분석 

# 5 Evaluation Metrics.

1. Execution Accuracy (EX)

![f2](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f2.PNG)

![f3](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f3.PNG)

결과가 같아야함

Vn은 정답 SQL을 시행했을때 결과

2. Valid Efficiency Score (VES)

![f4](\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f4.PNG)

R(·)  실행 효율성  - 결과값과 실행 효율이 비슷해야 함  

실행 시간으로 측정 -> 실행시간이 정답값보다 오래 걸릴수록 ves 가 내려감

# 6~7 Experiments, Related Work

ChatGPT 와 T5 모델을 통한 성능비교... 생략











# 참고



- Codex 

오픈ai가 개발한 모델 

자연어 입력을 받아 코드를 생성함 

비주얼 스튜디오 코드와 Neovim등 통합 개발 환경과 깃허브 코파일럿을 지원




























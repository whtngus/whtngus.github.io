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

![f_1](F:\code\whtngus.github.io\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f_1.PNG)

최근 sota 모델들은 현실적인 DB인 노이즈를 많이 가지고 있는 큰 규모의 데이터셋을 해결하지 못하는 문제를 발견

-> 당연하게도 Dataset이 그런식으러 안돼있기 떄문에 

이를 해결하기 위해 데이터셋인 BIRD, a BIg Bench for LaRge-Scale Database Grounded in Text-to-SQL 제안

이 데이터셋은 

학습시 80개의 오픈소스 데이터베이스 , 15개의 추가 RDB를 crowdsourcing 클라우드 소싱을 통해 데이터를 수집함.

이 데이터셋을 통해 테스트해본 결과 Codex는 25.88% 그리고 ChatGPT(3.5)는 28.95% 정확도를 달성함 

# 2 Task Formulation & Annotations

## 2.1 Task Definition.

![f1](F:\code\whtngus.github.io\img\2023\Can LLM Already Serve as A Database Interface A BIg Bench for Large-Scale Database Grounded Text-to-SQLs\f1.PNG)

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









# 참고



- Codex 

오픈ai가 개발한 모델 

자연어 입력을 받아 코드를 생성함 

비주얼 스튜디오 코드와 Neovim등 통합 개발 환경과 깃허브 코파일럿을 지원




























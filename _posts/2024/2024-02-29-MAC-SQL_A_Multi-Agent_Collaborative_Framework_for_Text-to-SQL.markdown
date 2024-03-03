---
43layout: post
title: "MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL"
date: 2024-02-29 02:05:23 +0900
category: paper
---

MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL
2024년 2월 15일 

buaa 대학교, 텐센트



url : https://arxiv.org/pdf/2402.10890v1.pdf

git url : https://github.com/wbbeyourself/mac-sql



# Abstract

최근 LLM 모델 기반의 Text-to-SQL 방법이 좋은 성능을 보이지만 엄청난 연산량을 필요로 하는 문제가 있음

그리고 LLM에 대한 내용은 도외시 하는 경우가 있음 

해당 연구에서는 multi-agent collaborative 프레임워크인 MAC-SQL 모델을 제안함



MAC-SQL은 few-shot chain-of-thought reasoning 방법을 사용함 



GPT-4를 백본으로 둬서 강력한 성능을 보여주지만 해당 연구에서는 SQL-Llama, Code Llama 7B 모델을 이용해서 사용하는 방법도 제안함 -> 7B면 해볼만 할거같은데 

SQL-Llama는 accuracy가 43.94  baseline으로 사용하는 chatgpt-4 가 46.94임 

해당 연구에서는 sota 스코어를 달성했다고 함 

# 1 Introduction

Text-to-SQL은 자연어 질문을 입력 받아 SQL을 자동으로 생성하는것을 목적으로 함 

지난 10년간 3가지 단계를 거쳐 연구됨 ㅠ

1. 입력 텍스트를 임베딩
2. sql decode로 추상 sql 트리 구문 생성 
3. sql 쿼리 생성



최근에는 seq-2-seq 방식을 사용함 -> 최근 LLM을 이용해서 성능이 매우 상승함을 보임 

최근 LLM based 방법론들은 상황에 맞는 프롬프트 전략과 타겟 도메인 데이터를 이용한 fine-tuning 에 집중함 

![f_1](F:\code\whtngus.github.io\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\f_1.png)

Figure 1 은 multi step reasoning 예시 

MAC-SQL는 LLM-based multi-agent collaborative framework에서 Decomposer(generator)를 통해 효과적인 text-to-sql 파싱을 지원함 

2개의 보조 agent인 Selector와 Refiner를 사용함 

selector는 sub database 를 최소화 시키고 refiner는 decomposer에게 피드백을 줌 

추가로 해당 연구에서 7b 모델을 fine tuning 한 SQL-Llama 를 제안 

# 2 Task Formulation and Annotations

![f1](F:\code\whtngus.github.io\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\f1.png)

Q : 입력 질문 

S : 데이터베이스 스키마  {T, C ,R}로 정의됨 

Y : 생성된 sql 쿼리 

K : 추가 정보 (선택)

T: Tables

C: Columns

R : foreign key  관계 정보 

f (· | θ)은 모델의 파라미터 







# 참고 

- BIRD-SQL(A Big Bench for Large-Scale Database Grounded Text-to-SQLs)

BiRD NL-to-SQL 데이터셋은 홍콩 대학교와 알리바바가 제안한 대규모의 크로스 도메인 데이터셋으로, 자연어 질문을 SQL 쿼리로 변환할 수 있는 모델의 개발을 지원하기 위해 설계되었습니다. 이 데이터셋은 12,751개 이상의 고유한 질문-SQL 쌍을 포함하며, 95개의 대형 데이터베이스를 포괄하는데, 이 데이터베이스들의 총 크기는 33.4GB에 달합니다. 블록체인, 하키, 헬스케어, 교육 등 37개 이상의 전문 도메인을 아우르는 것으로, 의미 분석 및 데이터베이스에 대한 자연어 인터페이스 분야의 연구 및 개발을 위한 가장 포괄적인 자원 중 하나입니다.

링크 : https://github.com/eosphoros-ai/Awesome-Text2SQL




















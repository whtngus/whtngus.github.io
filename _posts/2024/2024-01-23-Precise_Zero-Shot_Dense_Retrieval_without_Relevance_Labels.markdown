---
layout: post
title: "Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels"
date: 2024-01-20 02:05:23 +0900
category: paper
---

# Precise Zero-Shot Dense Retrieval without Relevance Labels



22년 10월 20일 게재 

워털루, 카테기 멜런 대학

url : https://arxiv.org/abs/2212.10496



# Abstract

retieval 이 많이 활용되고 잇지만 아직은 zero-shot은 어려움 

논문에서 zero-shot learning과 encoding relevance의 어려움을 인지하고  Hypothetical Document
Embeddings (HyDE). 방식을 제안함 

InstructGPT는 document를 생성하지만 현실적이지 않고 많은 잘못된 내용이 들어있음 



해당 연구에서 적용한 모델이 여러 테스크와 한국어 일본어 스와힐리어(케냐)에서 잘 됨을 보임 


# 1 Introduction

zero shot generalization 과 llm 으로 뻔한 이야기 ...

Hypothetical Document Embeddings (HyDE)를 제안함

 

문서 검색을 위한 테스크를 위해 인코더 방식을 제안함 

![f_1](F:\code\whtngus.github.io\img\2024\Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels\f_1.png)

Step1. query를 입력으로하여 질문 구조를 생성하는 모델을 사용 

"write a document that answers the question" -> 질문에 대답하는 문서를 작성하라고 지시 

=> 이 단계에서는 진짜가 아닌 가짜 데이터를 생성하게 됨 그러나 진짜 문서와 유사한 형식의 문서를 생성할 것이라고 예상 할 수 있음 

Step2. 비지도 학습인 contrastive encoder  모델을 학습함 

해당 벡터로 다시 임베딩을 검색해 -> 가장 가까운 진짜 문서를 반환함 



해당 논문에서 HyDE의 장점은 따로 학습이 필요하지 않는것이 장점이라고 함 

-> 여기에서 문서를 생성하는 모델은 InstructGPT, Contriever을 사용함 



# 2 Related Works

### Dense Retrieval 

Pretrained Transformer Language model이 생기면서 연구되기 시작함 

metric learning의 문제점인 training loss와 negative sampling 그리고 distillation

### Instructions-Following Language Models

LLM이 출현한 이후 instructions - zero-shot generalize 테스크에 대한 관심이 많아짐 

### Zero-Shot Dense Retrieval

설명 생략...

### Generative Retrieval 

설명 생략...



# 3 Methodology

## 3.1 Preliminaries

![f1](F:\code\whtngus.github.io\img\2024\Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels\f1.png)

쿼리와 문서의 유사성을 검색하는 테스크 임

q : query

d : document

enc_q, enc_d : 인코더 함수  여기에서 d는 dimension

L : query set의 수 Q_1 ,.... Q_l 

r_ij :  벡터로 판단한 관계성 순서 



## 3.2 HyDE

HyDE 방식은 3.1에서 전술한 방식의 문제점을 우회함(임베딩 공간에서만 데이터를 찾는것)

 ![f2](F:\code\whtngus.github.io\img\2024\Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels\f2.png)

![f3](F:\code\whtngus.github.io\img\2024\Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels\f3.png)

2번 수식은 그냥 constrastive encoder 함수를 표현  

3번 수식은 2번 수식의 encoder함수를 통해 나온 벡터를 표현함 

![f4](F:\code\whtngus.github.io\img\2024\Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels\f4.png)

INST는 instruction 텍스트  -> 생성모델로 가짜 답변을 생성하기 위해 미리 정해둔 instruction과 같이 넣어 답변을 반환함 

g를 통해서 가상 답변을 생성함 

![f5.](F:\code\whtngus.github.io\img\2024\Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels\f5..png)

g로 생성된 가짜 문서를 다시 벡터화함 

![f6](F:\code\whtngus.github.io\img\2024\Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels\f6.png)

쿼리가 모호하지 않은 경우의 단순 기대값을 정의함 

![f8](F:\code\whtngus.github.io\img\2024\Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels\f8.png)

그 이후 문서를 검색함 



# 4 Experiments

### Datasets

TREC DL19, DL20, BEIR 데이터셋을 사용하고 논문에서 계속 강조하는 MS-MARCO를 베이스로 사용

-> 여러가지 데이터셋을 사용하는 이유는 한국어, 일본어, 벵골어 3개국어를 테스트하기 위함 

![a1](F:\code\whtngus.github.io\img\2024\Precise_Zero-Shot_Dense_Retrieval_without_Relevance_Labels\a1.png)

Instruction 구조는 위와 같이 사용함 

### 

성능 결과는 ... 생략 



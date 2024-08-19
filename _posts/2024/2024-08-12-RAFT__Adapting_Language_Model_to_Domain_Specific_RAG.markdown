---
layout: post
title: "RAFT: Adapting Language Model to Domain Specific RAG"
date: 2024-08-19 02:05:23 +0900
category: paper
---

# RAFT: Adapting Language Model to Domain Specific RAG

2024년 1월 5일 

UC Berkeley

url :  https://arxiv.org/pdf/2403.10131

code :  https://github.com/ShishirPatil/gorilla

# Abstract

거대한 텍스트 데이터에서 LLM을 학습하는건 표준 트렌드로 자리잡고 있음

기반의 사전학습된 LLM들은 최근 트렌드로 자리잡고있음

여러 다운스트림 테스크에서 잘 작동하며 RAG-based-prompting과finetuning을 포함함 

그러나 정보를 통합하는 최고의 방법은여전히 미해결 과제임



해당 논문에서는 오픈 데이터에 대해 잘 답변하기 위해 Retrieval Augmented Fine Tuning (RAFT)를 제안함 

post-training 방으로 PubMed, HotpotQA, and Gorilla datasets기반으로 테스트시 좋은 성능을 보였다고 함

# 1 Introduction

엄청난 데이터양을 기반으로 학습된 LLM은 성능히 높은 성능을 보여주고 있음 

그러나 많은 LLM 들이 특정 도메인에대한 성능을 올리기 위해 사용되고 있음

-> 일반적인 지식 추론이 덜 중요해지며 주어진 문서를 기반으로 정확도를 올리는을 목표로 함 



아래와 같은질문으로 논문을 시작함

```
How do we adapt pre-trained LLMs for Retrieval Augmented Generation (RAG) in specialized domains?
```



LLM을 특정 도메인에 적용시킥 위해서 2가지 후보를 고려함

1. in-context learning through Retrieval-Augmented Generation (RAG)
2. supervised fine-tuning

즉 RAG와 LLM 둘 다 잘 하겠다는걸로 보면 될듯



하지만 1번의 RAG based in-context learning methods의 경우 고정된 도메인에 의해 학습 기회를 활용하지 못함

RAG 없이 LLM만 fine-tuning 하는 방법은 테스트시 RAG를 활용하지 못하거나, 검색 과정(RAG)의 불완전성을 고려하지 못함 



open book 시험을 예시로 들면

Existing in-context retrieval methods은 open-book 시험을 공부하지 않고 보는 방법이고

finetuning based approaches 방법은 공부를 하는 대신 rag가아니라 바로생각해서 시험을 보는 방법

이렇게 한가지만 사용하는 경우 open-book 시험에 맞는 셋팅을 하지 못하게됨 



해당 연구에서는 IFT(instruction FT) 와 RAG를 둘 다 고려하는 RAFT를 제안함



RAFT는 문서로부터 질문된 q를 통해서 답변 a*을 생성함

Q : 질문들

D : 문서 들

A* : 생성된 답변 (COT를 포함한 답변)

그리고 답변은 어떤 문서를 참조했는지를  D_k를 보여줌 



# 2 LLMs for Open-Book Exam

![f_1](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\f_1.PNG)

테스크의 이해를 돕기 위해 비유를 했다고함 

#### Closed-Book Exam

closed book exam은 LLMs이 문서 정보에 접근하지 않고 질문에 답변하는것

LLM 은 pre-training 혹은 sft 시에 학습한 지식으로만 답해야함 

#### Open Book Exam

LLM이 외부 정보(웹사이트, 책 등)에 접근할 수 있음 

일반적으로 문서를 검색해 와서 user의 프롬프트에 추가하는 방식을 사용함 

-> 도메인 정보를 LLM이 취득함

이때, 성능은 일반적으로 학습된 LLM의 성능이 검색기의 품질과 검색 정보에서 LLM이 얼마나 정확하게 정보를 식별할 수 있는지에 의존한다고 함 



 이러한 설정에서 일반 목적으로 훈련된 LLM의 성능이 검색기의 품질과 검색기가 가장 관련성 높은 정보를 얼마나 정확하게 식별할 수 있는지에 크게 의존한다고 주장

#### Domain-Specific Open-Book Exam

논문에서 보고자 하는 테스크는 더 좁지만 인기있는 도메인 에대한 오픈북 시험임 -> 도메인 특화 오픈북 시험

그리고 특정 도메인에 대해서 LLM을 먼저 테스트함 (기업 문서, 코드 등)

# 3 RAFT



#### Supervised Finetuning

Q : 질문들

D : 문서 들

A* : 생성된 답변 (COT를 포함한 답변)

SFT는 각 Q D A 가 한쌍이 돼서 상요할 수 있게 구성해서 학습

LLM이 사전학습 or SFT된 지식을 바탕으로 질문에 답변을 함 

이렇게 훈련된 모델에도 테스트시에 RAG를 사용할 수 있음 

![ff1](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\ff1.PNG)

##### RAFT

![f_2](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\f_2.PNG)

Retrieval Augmented Fine-Tuning (RAFT) 방법 

데이터를 우선 각각의 Q, D_k 그리고 COT 스타일의 답변 A* 셋을 준비함 

이떄 A*는 하나의 문서 D에서 생성된 답변

이때 문서를 2개의 타입으로 구분함 

1. ‘golden’ documents (D∗) : 질문에 답변하기 위해 잘 추출된 문서
2. ‘distractor’ documents (Di) : 정답과 관련이 없는 문서



P : 정답 문서의 비율을 유지함  -> (1 − P) 는 정답 문서가 없음(위의 그림2의 우측) 

![ff2](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\ff2.PNG)

아래는 프롬프트 템플릿

![f_3](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\f_3.PNG)

위 시나리오는 질문에 대해서 top-k 문서를 RAG가 검색해온 후 LLM에서 답변하는 케이스 



 Chain-of-Thought로 추론시 품질을향상시키고 응답에 대한 설명을 할 수 있음

 Gorilla APIBench dataset을 통해 실험함

 원분 문서를 사용할 경우  특수 토큰 "##begin_quote##"과 "##end_quote##"를 사용해서 어떻게 답변을 했는지 자세하게 보여줌 

#  4 Evaluation

다양한 베이스라인을 설정 

그리고 해당 논문은 LLaMA-2 를 베이스로한 RAFT-7B model을 제안

#### Datasets

Wikipedia, Coding/API documents 그리고 의료도메인 QA 도메인을 포함하고 있는 데이터들을 통해 평가를 진행함



 PubMed QA : 의료전문의 QA데이터셋



- Baselines

> - LlaMA2-7B-chat with  0-shot prompting
>
> intruction 질문을 주고 평가를 함 (질문 관련 문서 정보는 주지 않음)
>
> - LlaMA2-7B-chat mode wiht RAG
> - Domain-Specific Finetuning with 0-shot prompting (DSF):
>
> 일반적인 sft 방법으로 학습하고 관련 문서정보는 주지 않음 
>
> - Domain-Specific Finetuning with RAG (DSF + RAG)
>
> 모델 학습과 RAG 둘 다 사용

## 4.1 Results

![t_1](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\t_1.PNG)

위에서 명시된 4개의 모델을 여러 데이터셋으로 비교해봄 

RAFT 방식이 gpt3.5보다 높은 성능을 보임을 알 수 있음 

해당 모델과 DSF + RAG를 비교할때 큰 개선이 관찰되지 않았다고 함 



PubMed QA는 Yes/No 로 답하는 질문

HotPot : 11만 3천 개의 위키피디아 기반 질문-답변 쌍으로 구성된 새로운 데이터 세트



## 4.2 Effect of CoT

![t_2](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\t_2.PNG)

CoT를사용하고 안하고의 성능 차이를 비교함 

대체로 CoT를 사용한경우 성능이 많이 높음 

-> CoT 예시는 Figure 3 

## 4.3 Qualitative Analysis

![f_4](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\f_4.PNG)

figure 4에서 시나리오작가를 묻는 질문에 dsf는 잘못된 답을 하게됨 

RAFT는 CoT 기반으로 답변을 하기 때문에 더 정확한 답변을 할 수 있음

##  4.4 Should we train the LLM always with the golden context for RAG?

![f_5](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\f_5.PNG)

RAG가 정답을 가지고 있을 가능성P 를 얼마나 잡아야 될까라는 질문을 하게 됨

만약 RAG가 항상 정답을 가지고 온다면 100을 기준으로함 

위의 그림 5에서 P%가 100인경우 오히려 중간보다 성능이 낮음을 확인할 수 있음 

rag 로 5개의 문서를 가져오고 그중 하나만 정답인 케이스로 봄 

# 5 RAFT Generalizes to Top-K RAG

![f_6](F:\code\whtngus.github.io\img\2024\RAFT__Adapting_Language_Model_to_Domain_Specific_RAG\f_6.PNG)

rag 를 top k를 몇으로 설정해야 llm이 답을 잘할 수 있을까?

figure를 기반으로상관없는 문서를 가져오는 케이스를 4~6이 적정해 보이는데 각각 문서가 크다면 top 6까지 못가고 메모리가 접근 가능한 수준까지만 해야될듯..

학습 시 top 1~3개 여부는 두 데이터셋 다 결과가 달라서 정하기 어려우나 중간지점인 top3가 맞아보임

#### Generalization to a variable number of test-time documents

오답 문서를 같이 학습한 경우 rag 에대해 학습을 더 잘함을 봉미 



# 6 Related Works

#### Retrieval-Augmented Language Models

Retrieval-Augmented Language Models (RALMs)은 외부 데이터에 대한 LLM의 성능을 향상시킴 



#### Memorization

large neural language models이 정말 텍스트를 이해했는지 혹은 그냥 보이는 패턴을 기억해두고 답변하는지에 대한 질문

메모리에 기억해두는 방식을 극복하기 위해 많은 연구가 진행되고 있음 

#### Finetuning for RAG

최근 몇몇 논문에서 RAG 테스크를 위해 LLM을 학습하는 방법이 제안되고 있음 

# 7 Conclusion

RAFT의 학습 전략은 특정 도메인에 대한 qa성능을 높이기 위해 제안됨 (open-book setting)

chain-of-thought와 RAG가 답변과 상관없는 문서를 가져오는 경우를 전부 대비해두고 여러 데이터셋을 통한 테스트를 통해 이를 증명함 












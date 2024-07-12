---
layout: post
title: "ChatQA: Surpassing GPT-4 on Conversational QA and RAG"
date: 2024-07-10 02:05:23 +0900
category: paper
---

# ChatQA: Surpassing GPT-4 on Conversational QA and RAG



NVIDIA

2024년 5월 22일

url : https://arxiv.org/abs/2401.10225

https://chatqa-project.github.io/



# Abstract

GPT-4 보다 뛰어난 ChatQA 를 제안함 



생성 성능을 높이기 위해  two-stage instruction tuning 방법을 제안함 

-> 이방법을 통해 RAG 성능을 상당히 높힐 수 있다고 함 



1. QA 대화를 위한 dense retriever optimized 방법

기존 sota 방식인( query rewriting models)에 비해 비용감소도 가능하다고함 

CHATRAG BENCH 데이터셋 을통해 10가지 데이터셋으로 RAG를 종합적으로 평가함

- table-related QA
- 산술 계산
- 대답할 수 없는 질문들이 포함된 시나리오

등이 있음



해당 모델은 Llama2를 베이스로 함 ChatQA-1.0-70B (score: 54.14),



GPT-4-0613 (score: 53.90) and GPT-4-Turbo2024-04-09 (score: 54.03) 두 모델보다 높은 성능을 달성



# 1 Introduction

ChatGPT는  QA와 RAG의 패러다임을 바꾸고 이끌었다. 

1) 유저와 QA를 하면서 상호작용 할 수 있으며 대화가 가능해 후속질문이 가능
2) 개방형 도메인과 긴 문서 설정 모두 RAG를 통해 통합할 수 있으며 LLM의 컨텍스트 길이보다 더 큰 범위의 문맥을 사용 가능 

3) generalist models 로  도메인에 맞는 fine-tuning 없이도 사용 가능한 모델 



본 연구에서는 학슴 모델 데이터 기술등을 공개한다고함 

연구의 컨트리뷰션

1. a two-stage instruction tuning method을 제안함 

그리고 dataset을 디자인하고 QA와 RAG 테스크에서 높은 성능을 달성함 

2. 사람이 테깅한 싱글턴과 멀티턴 QA retriever 데이터에서 sota를 달성 

비교모델 GPT-3.5-Turbo  

맞춤형 합성을 통해 합성 데이터 생성등 방법을 강조함

3. CHATRAG BENCH 10개의 대화 QA데이터셋 구축 

그중 5개는  긴 문서 3개는 수치형 데이터 문서와 수학 계산문서로 다양한 데이터셋을 포함

4. 대답할수 없는 시나리오에 대한 연구를 함 

이때 LLM은 "대답할 수 없음"을 반환할 수 있어야함 

# 2 Related Work

## 2.1 Conversational QA and RAG

대화식 QA는 다음 질문들을 해결하며 유저의 경험을 향사시킴 

모델은 사용자의 명확한 질문이 있다면 할루시네이션도 감소할 수 있음 

-> 이점을 착안하여 QA모델들은 default format을 만들어서 사용함

 최근 LLM-based방법론들은 도메인최적화를 위해 fine-tuned 방법을 선호하고있음 



이를 평가하기 위한 많은 데이터셋이 최근에 많이 소개되고 있음 (많아서 생략...)



## 2.2  Retrieval for Multi-Turn QA

open-domain QA에서 RAG는 매우 중요한 역할을 함 (LLM 의 긴 문맥처리를 해결하기 위해서)

RAG에서 질문에 따른 top k개의 관련있는 청그를 가져옴 

만약 RAG에서 가져온 정보가 불충분한 정보라면 장황환 답변이 나오게 됨 

#### Conversational Query Rewriting

지금까지 대부분의 해결책은 Query rewriting 방법임 

RAG의 경우 이전 질문 문맥에 상관없이 지금 질문에 의해서만 문서를 가져와서 이를 해결하기 위한 방법론들이 잇음 

#### Fine-tuning Retriever for multi-turn QA

이전 연구에서 fine-tuning 학습은 in-domain의 single-turn 질문에 대해서 학습함 

이전 문맥과 현재 질문을 같이 검색할 수 있는 방법이 필요하며 이를 해결하귀 위해 해당 논문에서는 zero-shot 평가 방법을 도입 

-> single-turn query 와 잘 구축된 multi-turn dataset을학습했다고함 

## 2.3 Instruction Tuning

instruction tuning의 목표는 자연어의 지침을 따를 수 있는 기능을 갖추기 위함 

high-quality instruction tuning datasets이 필요함 FLAN, Self-Instruct, unnatural Instructions, Dolly, OpenAssistant 등이 있음 



그리고 여기에서 답변할 수 없는경우 cannot answer라는 답변을 할 수 있어야함

-> 이 대답은 할루시네이션을 막기 위한 필수적인 작업 이라고함 

# 3 ChatQA

![f_1](\img\2024\ChatQA__Surpassing_GPT-4_on_Conversational_QA_and_RAG\f_1.PNG)

a two-stage instruction tuning method를 제안함 

위의 그림 1과 같음 (그림 1만 본경우 매우 일반적인 LLM 학습방법으로 보임)

- stage-1

SFT를 통해 f instruction-following and dialog datasets을 학습

stage-1으로도 충분히 좋은 성능을 보인다고함 

그러나 RAG-based QA를 하는경우 한계점이 있음 이를해결하기 위해 2차 학습을 진행

- subsequent stage

context-enhanced instruction tuning 방법이라고 부르며 

문맥을 이해하고, RAG 기반의 생상을 강화하기 위한 후속 학습방법을 소개함

## 3.1 Stage-1: Supervised Fine-tuning

크고 종합합적인 SFT 데이터셋을 구성함 

12만 8천개의 높은 품질의 학습용 데이터를 만들었다고함 

데이터셋 구성

1) Soda

소셜 다이얼로그 데이터셋

2. ELI5

long-form QA 에 매우 정교한 답변을 포함함

3. FLAN과 chain-of-thought dataset

4. LLM 합성 instruction turning datasets

Self-Instruct와 Unnatural Instruction을 포함함

5. crowd-sourced conversational dataset

두명의 사람이 만든 대화 데이터셋 (OpenAssistant , Dolly)

처음에 “System” 로 시작하여 답변 가이드를 제공하는 프롬프트를 생성함 

그리고 “User”와 "Assistant"을 이용해 데이터셋을 생성함 



## 3.2 Stage-2: Context-Enhanced Instruction Tuning

주어진 문맥에서 Model QA의 대화 능력을 향상시키기 위해  두 번째 학습을 함 

문맥을 통합하는 QA 데이터셋을 결합하여 학습을 함 

해당 대이터는 single-turn QA와 대화 QA 데이터셋이 결합되어 있음 

### 3.2.1 Human Annotated Data

사람이 직접 라벨링한 7천개의 대화 HumanAnnotatedConvQA데이터와가 있음

이를 구축하기 위해 인터넷에서 7천개의 다양한토픽에 대한 문서를 수집하여 질문과 agent를 사용한 답변을 활용하여 생성함 

 이때 문서에서 멀티턴을 사용해서 질문을 함 

평균적으로 하나의 문서에서 5 번의 질문을 함 

 ```
 질문 방식
 User behavior
 1) 문서를 기반으로 질문
 2) agent가 더 명확한 질문을 뭉러보는경우 다시 대답 
 Agent behavior
 1) 문서를 기반으로 질문에대한 답변을함
 2) 유저의 질문이 명확하지 않은경우, 광범위한경우, 너무 일반적인경우 다시 질문을 함 
 ```

할루시네이션을 줄이기 위해 알수없는 답변 케이스를  같이 추가함

이때의 답변은 “Sorry. I cannot find the answer based on the context”

1,500개의 알수없는는 답변 케이스를 생성 

### 3.2.2 Synthetic Data Generation

HumanAnnotatedConvQA를 평가하기 위해 GPT-3.5-Turbo를 사용함



gpt-3.5의 instruction은 3가지를 포함함

1. system role 로 답변에 대한 가이드를 제공 
2. 필요한 데이터 유형을 나타내는 예시 대화 QA
3. 모델이 내용을 기반으로 대화영 QA를 생성하도록 지시하는 문서



에이전트의 답변과 '높은 중복'을 보이는 청크가 제거되고, 나머지 청크들이 에이전트의 답변과 '낮은 중복'을 보일 때만, 그것을 유효한 무응답 샘플로 간주하여 처리함(이때 4-gram recall score을 기반으로함)

0.5이상 겹치면 high overlaps  0.1 이하로 겹치면 low overlaps

### 3.2.3 Training Blends

수치형데이터 문서와 수학계서문서를  처리해 QA성능을 햐상시키기 위해 TAT-QA dataset을 추가함

(수치 수학문서 같이 들어있음) -> QA성능을 강화홤 



여러 데이터셋을 혼합해서 사용한걸로 보임

1) A conversational QA dataset: HumanAnnotatedConvQA or SyntheticConvQA
2) single-turn QA datasets: DROP (Dua et al., 2019), NarrativeQA (Kocisk ˇ y et al. ` , 2018), Quoref (Dasigi et al., 2019), ROPES (Lin et al., 2019), SQuAD1.1 (Rajpurkar et al., 2016), SQuAD2.0 (Rajpurkar et al., 2018), NewsQA (Trischler et al., 2017), TATQA (Zhu et al., 2021)
3) 1 stage에서 사용한 SFT 데이터셋

# 4 Retrieval for Multi-Turn QA

![f_2](\img\2024\ChatQA__Surpassing_GPT-4_on_Conversational_QA_and_RAG\f_2.PNG)

대화형 QA 테스크에서 문서가 너무 길어져서 LLM에 직접 넣을수 없게 되면서 retriever 이 필수적이게 됨 

retriever encodes 는 dialogue 히소트리와  새로운 질문을 concat함 



대안 방법으로 conversation input과 contetns 들을 이용해 history를 다시작성해서 사용 할 수 있음

-> 그럼 다시 작성한 쿼리를 기반으로 single-turn 쿼리 형식으로 사용가능함 

그러나 재 작성을 위해 엄청난 비용이소모됨

## 4.1 Fine-tuning Retriever for Multi-turn QA

높은 퀄리티의 fine-tuning 데이터셋을 만들기 위해서 HumanAnnotatedConvQA와 SyntheticConvQA 데이터의 컨텍스트 쌍을 만듦

 

HumanAnnotatedConvQA는 대화 쿼리와 컨텍스트 쌍의 주석을 직접 가져와서 사용 

 SyntheticConvQA는 각 문서에서 대화 QA 데이터셋에서 각각의 청크로 커팅함 그리고 4-gram recall로 스코어링해서 유저의 답변과 비교함 그 후 스코어가 높으면 gold chunk로 지정함 



## 4.2 Conversational Query Rewriting



GPT-3.5-Turbo를 이용해 rewiter로 사용함

재작성시 퀄리티를 향상시키기 위해 예시데이터를 추가함 

Fine-tuning Retriever for multi-turn QA



### 4.3 Comparisons

![t_1](\img\2024\ChatQA__Surpassing_GPT-4_on_Conversational_QA_and_RAG\t_1.PNG)

zero-shot으로 5개의 데이터에 대해서 질문 재작성 방법과 fine-funing 을 비교함 

```
- 5개 데이터셋 설명(chatgpt로 번역)
Doc2Dial (D2D) (Feng et al., 2020)은 DMV, SSA, VA, 그리고 학생 지원의 네 가지 도메인을 다루는 문서 기반 대화형 QA 데이터셋입니다. 각 샘플은 사용자가 문서에 대한 질문을 제기하고, 에이전트가 그 질문에 응답하는 대화로 구성됩니다. 문서의 평균 길이는 약 101,000 단어입니다.

QuAC (Choi et al., 2018)는 위키백과 문서를 기반으로 합니다. 원래 문서는 짧지만, 각 대화가 여러 위키백과 URL에 연결되어 있어 이 링크들에서 텍스트를 추출하여 문서 크기를 평균 약 15,000 단어로 늘립니다. 또한 주어진 문맥 내에서 답변을 찾을 수 없는 경우도 포함됩니다.

QReCC (Anantha et al., 2021)는 여러 소스를 아우르는 오픈 도메인 대화형 QA 데이터셋입니다. QuAC와 유사하게, 각 대화에는 해당 URL이 있습니다. 이 URL에서 텍스트를 추출하여 문서를 구성합니다. 최종적으로 문서의 평균 크기는 약 5,000 단어이며, 최대 문서 크기는 20,000 단어입니다.

TopiOCQA (TCQA) (Adlakha et al., 2022)는 전체 위키백과를 기반으로 합니다. 주제 전환을 포함하며 에이전트가 사용자 질문에 대한 답변을 찾기 위해 전체 위키백과를 검색해야 합니다.

INSCIT (Wu et al., 2023) 또한 전체 위키백과를 기반으로 합니다. 사용자 질문이 불충분하게 명시된 경우에 대한 연구를 다룹니다.
```

# 5 Experimental Setup

## 5.1 Baselines

아래부터 생략.









# 참고

1. Self-Instruct

![self-instruction](\img\2024\ChatQA__Surpassing_GPT-4_on_Conversational_QA_and_RAG\self-instruction.PNG)

`self-insturct`는 언어모델을 사용해 insturction 데이터를 생성하는 방법

ex) `Alpaca`는 `self-instruct`의 방법을 사용하지만, 간략화된 `self-instruct` 방식을 사용

->인간이 작성한 175개의 시드 데이터로 시작해  `text-davinci-003`에 예시데이터로 넣어서 데이터를 500달러 미만으로 5만 2천개의 데이터를 생성해서 사용해 데이터셋을 만들고 LLaMA모델을 파인튜닝함

https://blog.harampark.com/blog/llm-alpaca/




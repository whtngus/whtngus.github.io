---
layout: post
title: "RQ-RAG: LEARNING TO REFINE QUERIES FOR RETRIEVAL AUGMENTED GENERATION"
date: 2024-08-12 02:05:23 +0900
category: paper
---

# RQ-RAG: LEARNING TO REFINE QUERIES FOR RETRIEVAL AUGMENTED GENERATION

url : https://arxiv.org/pdf/2404.00610v1

code : https://github.com/chanchimin/RQ-RAG

홍콩 대학교



# ABSTRACT

LLM은 놀라운 성능을 보여주고 있지만 할루시네이션과 부정확한 답변을하기 쉬움 

LLM의 한계는 거대한 사전학습 데이터에 의존하기때문에 보지않은 데이터에 취약함

이를 해결하기 위해 RAG로 외부에서 관련있는 데이터를결합하여 LLM의 맥락 내 학습 능력과 함께 비모수적(non-parametric) 지식을 활용

그러나 RAG는 주로 초기 입력에 주목을 하여 생성을 하기 때문에  애매모호한 미묘한 뉘앙스와 복잡한 질문에 답하기 힘듦

이를 해결하기 위해 Refine Query for Retrieval Augmented Generation (RQ-RAG)를 제안함 

# 1 Introduction

최근 LLM들은 초기 학습시 상당한 학습 데이터를 학습하고 fine-tuning을 통해 다양한 컨셉에 대한 이해와 다운스트림 테스크에대해서 상당히 좋은 성능을 보여주고 있음 

그러나 지식은 계쏙 업데이트되어 새로운 정보에 대해서는 계속해서 업데이트해야함 

 최신 정보에 접근할 수 없기 때문에, LLM은 환각(hallucinations)을 생성하기 쉽고, 정확하고 시의적절한 응답을 제공하는데 어려움을 겪을 수 있음

![f_1](\img\2024\RQ-RAG__LEARNING_TO_REFINE_QUERIES_FOR_RETRIEVAL_AUGMENTED_GENERATION\f_1.PNG)

LLM은 빠르게 발전하고 있지만 아직 아래와 같은 문제가 있음

1. 정보를 맥락화하기위해 RAG를 무차별적으로 쓰는것은 역효과를 낳을 수 있음 (그림1 왼쪽)

RAG가 관려없는 결과를 가져온 경우 LLM은 더 안좋은 출력을 하게 됨 

인사와 같은 질문에 llm은 바로 반응할 수 있지만 문맥을 추가하며 퀄리티가 내려갈 수 있음

2. 복잡한 질문의 경우 원래의 질문만으로 검색하면 적절한 정보를 찾는 데 실패하는 경우가 종종 발생함(그림일 우측)

이때는 LLM이 답변가능한 질문의 하위그릅으로 질문을 나눈 다음 

하위 구성요소와 관련된 정보를 검색하는것이 더 중요함 

그 후 하위질문에 대한 응답을 결함하여 포괄적인 답변을 구성

3. 답변이 여러개인 애매모호한 질문의 경우 (그림1을 아래)

이때는 기존 질문으로만 검색하는것은충분하지 않음 

이경우 LLM이 이를 분류하여 질문을 명확히하여 사용자의 의도를 파악해야함



해당 논문에서는 7B Llama2 모델을 기반으로 실험함 

해당 논문은 Self-RAG, SAIL에서 영감을 얻었다고 함 (데이터 증강과 모델이 노이즈를 필터링하는 방법)

또한 ChatGPT를 이용하여 다양한 시나리오(다시작성, 분해, 명확성)을 구별함 



논문의 컨트리뷰션

-  7B Llama2 모델을 학습해 sota달성 singe hop QAtask  과 3개의 턴의 질문 테스크
- 사용자의 질문을 검색하기 위해 효율적으로 다시 생성함 
- 이전 방법과 비교하여 다양한 데이터 소스에 대한 탄력성뿐만 아니라 상당히 높은 상한을 통해 잠재력을 보여줌



# 2 RQ-RAG: Learning to Refine Query for Retrieval Augmented Generation

데이터 구조, 학습, 샘플링을 제안함

## 2.1 Dataset Construction

사용자의질문을 다시 작성하는것을 학습하기 위해 추론 시간에 프로세스를 반영하는 훈련 데이터를 수집해야함

검색을 위해 정제된 질의를 생성학고 응답을 작성하는것을 포함함

Xorigin, Yorigin : 스페셜토큰이 포함되지 않은 오리지널 데이터의 입력 출력 쌍 

스페셜 토큰은 SPECIAL_type  으로 질문을 재작성하기 위해 사용

![f1](\img\2024\RQ-RAG__LEARNING_TO_REFINE_QUERIES_FOR_RETRIEVAL_AUGMENTED_GENERATION\f1.PNG)

Qi, type : 재작성된 토큰이며 type은 개선된 행동(재작성, 분할, 애매모호함) i는 interation

k : top k 개의 문서를 검색

Dik : 문서 k에 대한 이터레이션 스텝 

y_new : 는 마지막 이터레이션 응답 

![f_5](\img\2024\RQ-RAG__LEARNING_TO_REFINE_QUERIES_FOR_RETRIEVAL_AUGMENTED_GENERATION\f_5.PNG)

figure 1의 시나리오를 포함하며 멀티턴 대화도 포함함 (queries requiring decomposition, and queries needing disambiguation)

figure5와 같은 데이터 구주로  되어있으며, 데이터 셋 별 테스크는 아래와 같음

single-hop QA : Arc-Easy/Arc-Challenge, OpenbookQA

multi-hop QA : HotpotQA, Musique

ambiguous tasks : ASQA

instruction following tasks : LIMA, WizardLM, Open-Orca, OpenAssistant, GPT4-Alpaca



전부다 합쳐서 42,810개의 인스턴스가 존재하며 증강에 의해 생성된 데이터는 150~2000토큰 사이라고함 

원본 데이터셋은 200토큰 이하라고함 

![f_2](\img\2024\RQ-RAG__LEARNING_TO_REFINE_QUERIES_FOR_RETRIEVAL_AUGMENTED_GENERATION\f_2.PNG)

Figure 2는 자동으로 태깅하기위한 흐름도

1. 테스크를 3가지 카테고리로 분류함

2. 각각의 데이터 타입에 대해서 ChatGPT를 사용해 미리정의된 템플릿으로 질문을 다시 생성함 

   정제된 커리를 이용하여 외부에서 데이터를 검색함 이때 DuckDuckGo 검색기를 토앻 검색했다고함 

   즉, 검색 알고리즘은 뭔지모르는 블랙박스

3. 마지막으로 재정의된 질문과 검색된 문서를 기반으로 chatgpt로 최종 응답을 생성 

   이렇게 하니 40k개 정도의 응답을 수집했다고함  

## 2.2 Generator Training

LLM을auto-regressive 방식으로 학습함 

![f2](\img\2024\RQ-RAG__LEARNING_TO_REFINE_QUERIES_FOR_RETRIEVAL_AUGMENTED_GENERATION\f2.PNG)

likelihood 로스 함수 

di는 문서

i는 각 스텝 

## 2.3 Sampling Strategies

 inference-time strategy 전략을 소개함 

![f_7](\img\2024\RQ-RAG__LEARNING_TO_REFINE_QUERIES_FOR_RETRIEVAL_AUGMENTED_GENERATION\f_7.PNG)

각각의 스텝에서 사용자의 질문에서 모델은 재작성, 질문 분해, 애매한 지룸ㄴ중 하나를 선택하여 최적화 답변을 생성함



질문을 트리방식을 통해 3가지 다른 decoding 전략을 수행함 

다른 질문은 서로 다른 답변이 나오게 됨 



재정의하는 방법을 3가지 방법을 통해 사용

pM : M 파라미터를가진 언어 모델 

R_1~ R_n : x y에 대해한 트랜잭션

x : 입력 프롬프트

y : 중간스텝 Z1~ Zn을 concat

y_final : 최종 답변

#### PPL Based Selection

전체 생성된 출력에서 가장 낮은 perplexity(당황)을 가진 경로 R_final을 선택함

![ff1](\img\2024\RQ-RAG__LEARNING_TO_REFINE_QUERIES_FOR_RETRIEVAL_AUGMENTED_GENERATION\ff1.PNG)

L은 모델 output의 token 길이

#### Confidence Based Selection

R_final 에서 최종답변 Y_finnal을 생성하기 위해 높은 confidence 를 선택함

![ff2](\img\2024\RQ-RAG__LEARNING_TO_REFINE_QUERIES_FOR_RETRIEVAL_AUGMENTED_GENERATION\ff2.PNG)

l은 답변의 시작 위치  t는 (최종 답변 y_final의 시작위치 부터 시작)

생선된 출력을 평가하는게 아니라 최종 답변의 신뢰도를평가함 

#### Ensemble Based Selection

마지막 결론들을 결합해 가장 높은 스코어의 답변을 추출함 

![ff3](\img\2024\RQ-RAG__LEARNING_TO_REFINE_QUERIES_FOR_RETRIEVAL_AUGMENTED_GENERATION\ff3.PNG)

#### Upper Bound

upper bound시스템을정의함

하나의 경로가올바른 답변으로 이어진다면 이를 정답으로 간주

# 3 Experiments

## 3.1 Evaluation Tasks



결과 생략.,.





# 참고

- DuckDuckGo

사용자의 개인정보를 수집하지 않는 검색엔진






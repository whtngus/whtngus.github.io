---
layout: post
title: "NV-Retriever: Improving text embedding models with effective hard-negative mining"
date: 2024-12-26 02:05:23 +0900
category: paper
---

# NV-Retriever: Improving text embedding models with effective hard-negative mining

2024년 7월 22일 

NVIDIA

# Abstract

Text embedding 모델은 semantic search와 RAG기반의 QA system에서 인기를 끌고있음 

해당 모델은 transformer를 베이스로 contrastive learning으로 학습된 모델을 사용함 

많은 논문에서는 새로운 임베딩 모델을 소개하거나 학습 방법을 소개하지만, 하나의 키인 negative 셈플링에 대한 논문은 거의 없음 

해당 논문에서는 이를 해결하기 위해  positive-aware mining 방법을 제안함 

-> 명칭은 NV-Retriever-v1 모델



# 1 Introduction

LLM에서 QA를 하기 위해 RAG는 필수적임 작업이 됨

사용자의 질문은 정답 쿼리와 비교하기 위해 MIPS를 사용

임베딩 모델을 학습할때 negative 셈플링은 고정적으로 고름 

 teacher retrieval model 을 선택한 후에 질문에 따른 관련 있는 문서들을 negatie 셈플로 선택함

-> positive 보단 관련 없지만 관련있는 문서를 선택

이렇게하면 난이도가 올라가고 구별하기 어려워짐 



논문의 컨트리뷰션

- Positive-aware hard-negative mining methods.

 family of hard-negative mining 방법을 제안함 

positive와 관련 있는 스코어의 negative 를 고르고 잘못된 네거티브 를 제거할 수 있는 방법을 제안함 

- Hard-negative mining ablation study

hardnegative mining 에 대한 스터디 

- Release of the an open state-of-the-art text retrieval model: NV-Retriever-v1

sota인 NV-Retriever-v1모델을 제안 

# 2 Background

## 2.1 Text embedding models

생략

## 2.2 Hard-negative mining for fine-tuning embedding models

DPR은 hard negatvies 방법으로 BM25 검색기를 사욯암

ANCE 방법은 학습 중 ANN 방법으로 비동기적으로 네거티브 셈플을 업데이트함 

생략



# 3 Investigation on hard-negative mining for fine-tuning text embedding models

아래와 같은 3가지 Research Question을 기반으로 연구함 

- RQ1: g hard-negatives의 모델들이 얼마나 다운스트림 테스크의 정확도에 영향을 주는지
- RQ2 : hard-negative 방법들을 앙상블 할 수 있는지
- RQ3 : finetunig한 경우 hard-negative mining의 정확도가 얼마나 달라지는지 



## 3.1 Hard-negative mining methods

가장 기본적인 Hard-negative mining 방법은 top-k 의 질문과 유사한 후보를 추출하여 사용하는것 으로 "Naive Top-K."이라고 명칭함 

-> 단점으로는 negotiave로 들어왔지만 사실 positie인데 태깅되지 않은 데이터가 들어올 수 있음 

이걸 필터링 하기 위해 두가지 방법이 제안됨

- Top-K shfited by N :  유사도 가 높은 top n개를 제외하고 추출
- Top-k with absolute threshold(TopK-Abs) : 관련도 score가 특정 값 이상인 대상을 제외하고 추출



TopK-Abs 방식들은 오직  질문에만 신경쓰며 긍정 문장의 관계성은 신경쓰지 않음 

그래서 positive-aware hard-negative mining 방식을 만들어서 제안함

![f_1](F:\code\whtngus.github.io\img\2024\NV_Retriever__Improving_text_embedding_models_with_effective_hard_negative_mining\f_1.PNG)

- Top-k with margin to positive threshold (TopK-MarginPos) : positive score에서 마이너스 하여 특정값 이하 추출 


- Top-k with percentage to positive threshold (TopKPercPos) : posirie score 에서 특정 펏네트 이하 추출



위와같이 top k 기를 기준으로 접근하는게 일반적인 방식 이지만 관련문서의 다양성을 위한 접근이 필요함 

- Sampled Top-k  : 가장 관련있는  top k중  혹은 30~100범위에서 n개를 선택 
- Top-1+sampled top-k : 가장 관련성 높은 문서하나와 Sample top-k 방식으로 n-1개 선택

## 3.2 Selected embedding models

여러 임베딩 모델들을 선택해서 비교함 

다양한 모델 사이즈와 아키텍처를 기준으로 설정 

- e5-large-unsupervised (334M params) : CL 방식으로 비지도학습 로 학습함
- e5-large-v2 (334M params) : 지도학습 방식으로 학습 
- e5-mistral-7b-instruct (7.1B params) : sLLM 수준, decoder-only mistral 모델이고 CL 방식으로 finetuning됨 
- NV-Embed-v1 (7.8B params) : bi-directional와 latent attention을 추가함 

## 3.3 Training and evaluation

### 3.3.1 Training. 

실험을 위해 e5-large-unsupervied 에 4가지 hard-negative 기법을 선택하요 비교 함

287k개의 Natural Questions, Stack Exchange, SQUAD 데이터셋을 섞어서 학습 데이터를 만듬 

### 3.3.2 Evaluation

MTEB Retrieval / BEIR benchmark (15 datasets) 을 사용 하기엔 많은 시간과 컴퓨팅 자원이 필요함 

그래서 3개의 BEIR의  QuestionAnswering datasets을 선택함 

-> NQ, HotpotQA and FiQA-2018

NDCG@10으로 평가함 

## 3.4 Ablation Study Results

### 3.4.1 RQ1.

다른 임베딩 모델을 비교 평가함 

RQ1: g hard-negatives의 모델들이 얼마나 다운스트림 테스크의 정확도에 영향을 주는지

![t_1](F:\code\whtngus.github.io\img\2024\NV_Retriever__Improving_text_embedding_models_with_effective_hard_negative_mining\t_1.PNG)

BM25알고리즘으로 추출 한 랜덤 네거티브 셈플리을 한 경우 랜덤보다 낮은 점수를 보임 

임베딩 모델을 사용하여 학습 셋의 각 질문에 대한 4개의 하느 네거티브를 추출함

그리고 역시 그중 모델이 가장큰 7B 의 성능이 가장 높음 

####  3.4.2 RQ2.

- RQ2 : hard-negative 방법들을 앙상블 할 수 있는지

다른 임베딩 모델을 앙상블하여 hard-negatives를 할 수 있는지를 연구함 

top-4 hardnegatives를 사용함  (jaccard similarity lower than 30%).



2가지 방식을 비교 실험함 

E5와 Mistral based embedding 모델인 e5-large-v2, snowflake-arctic-embed-l, NV-Embed-v1, and e5-mistral-7b-instruct 모델

- cross-sample ensembling : teacher model의 셈플링을 모두 획득 
- Intra-sample ensembling: 각 teacher model의 top-1 을 취함

   -> 이경우 top-1이 겹치면 어떻게 되는거지?

![t_2](F:\code\whtngus.github.io\img\2024\NV_Retriever__Improving_text_embedding_models_with_effective_hard_negative_mining\t_2.PNG)

cross-sample ensembling의 경우 성능이 좋아지지 않음 

Intra-sample ensembling의 경우 중복을 제거한경우 성능이 좋아졌으나 개인적 판단으로는 이정도 수치는 랜덤성이라고 봐도 좋을듯 

#### 3.4.3 RQ3

- RQ3 : finetunig한 경우 hard-negative mining의 정확도가 얼마나 달라지는지 

e5-mistral-7b-instruct을 teachur 모델로 사용해서 e5-large-unsupervised를 학습함 

TopK-Abs, TopK-MarginPos and TopK-PercPos 3가지를 비교

![t_3](F:\code\whtngus.github.io\img\2024\NV_Retriever__Improving_text_embedding_models_with_effective_hard_negative_mining\t_3.PNG)

각각 파라미터 최적인 값을 보여줌 

-> 참고는 할 수 있으나 데이터마다 다를테니 그대로 사용은 불가능해보임

top n 도 10~100까지 실험했지만 10이 가장 높은걸로 봐선 그냥 유사문서일 수록 좋은것으로 보임 

![t_4](F:\code\whtngus.github.io\img\2024\NV_Retriever__Improving_text_embedding_models_with_effective_hard_negative_mining\t_4.PNG)

 Mistral-7B-v0.1 b을 베이스모델로 한 경우

최고 스코어가 다른 sllm모델과 비슷하여 유사한 형상을 보임

그리고 top-10보다는 top-1 engative가 성능이 조금 높았다고함 -> 즉 그냥 top n처리없이 그냥하는게 더 좋은듯 

# 4 NV-Retriever-v1

## 4.2 Train sets and instruction prefixes

MTEB은 retrieval, reranking, classification, clustring 등 여러가지 테스크를 포함하고 있음 

NV-Retriever-v1를 학습하기 위해 일부 데이터를 사용함 

E5-Mistral-7B 임베딩 모델을 사용하고 잠재적인 false negative 샘플을 피하기 위해 TopK-PercPos를 사용함 (95%) -> 선택한 이유는 Table3 ,4의 결과



그리고 템플릿은 원본 템플릿인

```
"Instruct: {task_definition} \n Query: {query}"
```

대신 

```
e "{task_definition}: {query}"
```

를 사용함 

## 4.3 Training

two stage 학습 구조를 사용함 

첫 번째 스테이지는 in-batchnegatives 방식의 hard-negative를 사용하여  retrieval 지도학습 

두 번째 스테이지는 retrieval task와 다른 테스크(classification, regression) 데이터 셋을 섞어서 사용 

## 4.4 NV-Retriever-v1 Results

![t_5](F:\code\whtngus.github.io\img\2024\NV_Retriever__Improving_text_embedding_models_with_effective_hard_negative_mining\t_5.PNG)

 different negative mining 방식과 비교 했을때 NV-Retriever-v1이 가장 높은 점수를 달성함 

# 5 Conclusion

positive-aware hardnegative mining methods 에 대해 실험하고 포괄적인 hard-negative 방식에 대한 실험 결과를 제공함 

이를 통해 최적 방식인 NV-Retriever-v1를 제안









# 참고

1.  Maximum Inner Product Search (MIPS)

답 후보의 갯수를 n개라고 하면, O(n) complexity의 exact search를 베이스로, 그보다 개선된 sub-linear-time approximate search 방법

-참고 : https://medium.com/platfarm/mips-c1db30a3e73e

2. hard negative mining

negative sample이 너무 많은 경우 클래스 불균형을 겪음 . 이걸 방지하고자 하는 방법

모델이 오답을 낸, 예측을 잘못한 어려운 셈플을 추출하는 방법 

3. Jaccard Coefficient

J(A,B) = |A 교집합 B| / |A 합집합 B|

4. MTEB(Massive Text Embedding Benchmark)

다양한 임베딩 작업에서 텍스트 임베딩 모델의 성능을 측정하기 위한 대규모 벤치마크 

129 데이터셋, 13 언어, 14667 스코어, 126모델로 구성
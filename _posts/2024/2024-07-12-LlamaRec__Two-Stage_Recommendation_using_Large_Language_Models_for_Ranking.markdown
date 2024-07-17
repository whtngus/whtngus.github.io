---
layout: post
title: "LlamaRec: Two-Stage Recommendation using Large Language Models for Ranking"
date: 2024-07-17 02:05:23 +0900
category: paper
---

# LlamaRec: Two-Stage Recommendation using Large Language Models for Ranking

2023년 10월 25일 

nvidia 

LlamaRec: Two-Stage Recommendation using Large Language Models for Ranking

url : https://arxiv.org/abs/2311.02089



# ABSTRACT

textual feature로 LLM을 이용하여 추천을 하는 방식이 향상되고있음



LLM을 이용하여 generation할때는 실시간으로 사용하기에는 속도가 느림 

이를 해결하기 위해 tow-stage framework를 제안함 

large language models for ranking-based recommendation (LlamaRec)

-> 트랜잭션을 이용한 작은 스케일의 시퀀스기반의 추천을 한다고함 

  즉, long text 생성을 하지 않음 



다음 아이템의 제목을 생성하는것 보다 verbalizer-based approach가 더 좋다고함 



# 1 INTRODUCTION

Llama 2 모델이 좋다고 설명... 베이스 모델을 Llama 2로 함 



그럼에도 기존 연구들은 LLM을 추천시스템에 적용시키는데만 목적이있고 효율성은 점점 버려지고 있음 

현실적으로 LLM을 이용해서 긴 텍스트를 생성하는 실시간 배치는 불가능하다고함 

이를 해결하기 위해 LLM위에 분류 및 회귀 레이어를 씌워서 토큰생성을 방지해야 한다고함 



sota 방식인 ID-based item retrieval 방식을 이용함

-> 이 방식을 사용하면 사용자의 history 길이에 상관없이 사용 가능하다고함



최적화 시키기 위해 verbalizer 방식의 ranking을 사용

1. 우회적인 자귀회기생성을 이용해 inference 시간을 최적화 시킴
2.  한번의 포워드로 모든 후보자들에 스코어를 생성함 그리고 디코딩에서 메모리를 많이 사용하는 방식을 제거(빔서치 같은 거) 



컨트리뷰션

1) LLM 기반의 two-stage 전략인 LlamaRec 프레임워크 제안
2)  verbalizer renking방식을 사용하여 LLM 기반의 ID-based 시퀀스 추천시스템을 제안함 
3) 여러 데이터셋으로 벤치마크 결과를 제공 및 높은 스코어를 보임

# 2 RELATED WORK 

## 2.1 Large Language Models

생략

## 2.2 LLM-based Recommendation LLMs are applied as recommender systems to und

text features 이용한 추천시스템은 좋은 성능을 보이고 있음 

그리고 학습을 하지 않는 tuning-free 방식들이 많이 제안됨 

다음 아이템을 생성하여 예측하는 방식으로 보임 

ex) Chat-REC는 ChatGPT를 사용해 사용자의 선호도를 파악하고 대화형으로 설명가능한 추천 기능을 개선ex2) TallRec는 아이템 추천을 위한 instruction-tuning을 함

 

그러나 대부분 LLM 기반 추천시스템은 autoregressive 생성방식의 예측방식을 사용 

-> 이때 시간이 오래 걸림



# 3 METHODOLOGY 

## 3.1 Setup



![f1](F:\code\whtngus.github.io\img\2024\LlamaRec__Two-Stage_Recommendation_using_Large_Language_Models_for_Ranking\f1.PNG)

X : 사용자 상호작용 히스토리 x 데이터셋

I : Item Space

𝒇retriever : retriever 모델

𝒇ranker (𝒇 = 𝒇ranker ◦ 𝒇retriever) : LLM 기반 랭킹 모델 



negative log likelihood loss  L 사용

## 3.2 The Proposed LlamaRec

![f_1](F:\code\whtngus.github.io\img\2024\LlamaRec__Two-Stage_Recommendation_using_Large_Language_Models_for_Ranking\f_1.PNG)

large scale의 경우 아이템 히스토리 |I|가 100만건에 달함 

 이를 효율적으로 retriver 하고 llm에 실어서 해결할 수 있는 방법을 제안 

### 3.2.1 Retrieval.

𝒇retriever 모델로 linear recurrence-based LRURec을 선택

LRURec은 작은 스케일의 추천시스템으로 linear recurrent units임 

-> item embedding과 예측된 feature item top 20개의 score를 내적함 

그 이후 ranking stage 스텝으로 이동

### 3.2.2 LLM Ranker.

 𝒇ranker 모델로는 Llama 2 7B를 사용함 

![prompt](F:\code\whtngus.github.io\img\2024\LlamaRec__Two-Stage_Recommendation_using_Large_Language_Models_for_Ranking\prompt.PNG)

위와 같은프롬프트 템플릿을 사용 

LLM을 이용하여 추천 아이템은 예측할 수 있으나 추천한 아이템에 대한 스코어는 확인할 수 없는 문제가 있음 

이를 위해 모델 예측 순서대로 출력을 하게되면 긴 리스트를 출력하기 위해 계산 연산량을 많이 필요로 하게됨 

![f_2](F:\code\whtngus.github.io\img\2024\LlamaRec__Two-Stage_Recommendation_using_Large_Language_Models_for_Ranking\f_2.PNG)

이러한 문제를 해결하기 위해 위의그림 2와 같은 방법을 사용함 

next token의 logits 값을 이용해서 뽑음



-> introduction 에서 하나의토큰만 만든다는게 이 방식으로 보임 

# 4 EXPERIMENTS

### 4.0.1 Datasets.

![t_2](F:\code\whtngus.github.io\img\2024\LlamaRec__Two-Stage_Recommendation_using_Large_Language_Models_for_Ranking\t_2.PNG)

평가 데이터셋 

- ML-100k

영화 추천 데이터 100k개의 사용자 item 상호작용 데이터

- Beauty

아마존 웹사이트의 제품 리뷰 데이터셋 

- Games

아마존의 vidieo 게임 데이터셋 

리뷰와 랭킹등을 포함함 - 5 interactions (i.e., 5-core). I

### 4.0.2 Baseline Methods.

baseline 모델로 

RNN 기반 sota 모델과 Transformer 기반의 모델과 비교 

- NARM : RNN 기반의 sota 모델
- SASRec :  unidirectional attention 방식을 사용 
- BERT4Rec : maksed 방식으로 맞추는 방식
- LRURec : linear recurrence를 통해 효과적으로 예측을함  (retriver 모델로 LlamaRec 사용)

### 4.0.3 Evaluation

![t_1](F:\code\whtngus.github.io\img\2024\LlamaRec__Two-Stage_Recommendation_using_Large_Language_Models_for_Ranking\t_1.PNG)

M : MRR@K

N : NDCG@K

R : Recall@K

![f_3](F:\code\whtngus.github.io\img\2024\LlamaRec__Two-Stage_Recommendation_using_Large_Language_Models_for_Ranking\f_3.PNG)

위는 verbalizer을 사용했기 때문에 title 길이에 상관없이 연산량이 같음을 나타냄

그냥 LLM사용시에는 당연히 느려지고.. 

















# 참고

- verbalizer

구조화된 데이터를 자연어 텍스트로 변환하는 역할

변형 예시

```
chatgpt 시킴
Verbalizer는 주로 다음과 같은 방식으로 작동합니다:

 - 범주형 레이블 변환: 머신 러닝 모델의 출력이 범주형 데이터일 경우, 이를 자연어 텍스트로 변환합니다. 예를 들어, 감정 분석 모델의 출력이 "긍정적", "부정적", "중립적"일 때, 이러한 레이블을 실제 텍스트 설명으로 변환합니다.

예: "긍정적" -> "이 문장은 긍정적인 감정을 나타냅니다."

 - 숫자 점수 변환: 예측 결과가 숫자 점수인 경우, 이를 설명하는 텍스트로 변환합니다.

예: "80%" -> "이 모델의 정확도는 80%입니다."

 - 텍스트 생성: 사용자의 질의에 따라 모델이 생성한 결과를 자연어로 표현합니다. 이는 주로 챗봇이나 대화형 AI에서 사용됩니다.

예: 사용자가 "오늘 날씨 어때?"라고 물었을 때, "오늘 서울의 날씨는 맑고 기온은 25도입니다."와 같은 답변을 생성합니다.
```

- Mean reciprocal rank (MRR) 

```
MRR은 질의(Q)에 대해 가장 적절한 아이템의 역순위 평균
제안된 리스트에서 적절한 아이템이 나타난 위치의 숫자로 나눈 것
```

https://bigdatamaster.tistory.com/178

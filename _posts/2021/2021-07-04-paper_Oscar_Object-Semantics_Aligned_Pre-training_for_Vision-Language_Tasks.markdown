---
layout: post
title: "paper : Oscar: Object-Semantics Aligned Pre-training for Vision-Language Tasks"
date: 2021-09-20 19:20:23 +0900
category: paper
---
# Oscar: Object-Semantics Aligned Pre-training for Vision-Language Tasks

# 논문 정보 

학회 : 	ECCV 2020

논문 URL : https://arxiv.org/abs/2004.06165

코드 URL : https://github.com/microsoft/Oscar

소속 : Microsoft Corporation

# Abstract

영상과 텍스트 쌍의 cross-modal representation 학습은 최근에 많은 연구가 되고 있다.

기존 방법은 사전 교육할 모델에 대한 입력으로 단순히 이미지 영역 특징과 텍스트 특징을 연결해서 학습 

해당 논문에서는 훨씬 더 쉽게 사용하기 위해 새로운 학습 방법인 Oscar를 제시

영상에서 650만개의 텍스트 이미지 쌍으로 구성된 공개 말뭉치에 Oscar 모델을  Pre-training 하고 downstream task를 fine-tuning을 통해 사용 

# 1. Introduction

![fig_1](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\fig_1.PNG)

cross modal representations 학습을 위해서 이미지 캡션과 같은 다양한 V(Vision) + L(Language) 에 대한 연구는 필수 작업이다.

VLP(Vision Language Pretraining) 의 최근 연구로는 대규모 이미지-텍스트 쌍에서 일반적인 표현을 효과적으로 학습한다.

이러한 VLP모델은 transformer를 기반으로 학습  -> 이러한 모델을 Pretraining 하기 위해 기존 방법은 단순히 입력으로 인지 영역 특징과 텍스트 영역 특징을 연결하고 의미 정렬을 학습하는 방식이다.

-> 오버셈플링과, 도메인에 한정적인 학습 방식이됨 



해당 연구에서는 영상에서 검출된 객체 태그를 기준점으로 도입하여 영상과 텍스트의 의미정렬 학습을 용이하게 함으로써 교차모형 표현 학습을 크게 개선할 수 있음을 보여준다.



오스카 모델은 650만 쌍으로 구성된 대규모 V+L 데이터셋에 대해 사전 교육을 함

7가지 V+L task 에서 sota를 찍음 

이미지-텍스트 정렬을 학습하기 보다는 이미지 영역의 기능 표현을 향상시키기 위해 V+L 작업에서 객체 또는 이미지 태그를 사용함

논문의 컨트리뷰션

1.  V+L 이해 및 생성 작업을 위한 일반적인 이미지 텍스트 표현을 학습하기 위한 강력한 VLP 방법인 Oscar를 소개합니다. 
2. 여러 V+L 벤치마크에서 기존 접근 방식보다 훨씬 우수한 새로운 SoTA를 달성하는 오스카 모델을 개발했습니다. 
3. 객체 태그를 교차모형 표현 학습 및 다운스트림 과제의 기준점으로 활용하는 효과성에 대한 통찰력을 제공하기 위해 광범위한 실험과 분석을 제시합니다.

# 2. Background

![fig_2](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\fig_2.PNG)

위 그림과 같이 많은 V+L 연구에서 영상-텍스트 쌍으로 구성된 데이터를 사용해 Transformer 기반의 모델을 학습한다. -> VLP의 품질은 입력 데이터의 품질에 의존한다

I - Image

w - taxt sequence

N - Data Size

 D = {(Ii , wi)}

기존 VLP 방법은 이미지의 v={v1, ... , vk} 쌍으로 구성된 텍스트 단어 임베딩 w = {w1, ··, wT} 를 사용 

-> 기존 VLP 방법은 다음과 같은 문제정이 있음

1. 모호성

시각적 영역 기능은 주로 Faster R-CNN Object detection을 통해 셈플링을 하는데, Object detection된 객체가 많아 영역간의 중복이 발생한다 .

예는 위 사진의 dog와 couch의 영역이 많이 겹치는것을 보면 알 수 있음 

2. 학습 

 VLP는 영상의 영역 또는 개체와 텍스트의 단어나 구 사이에 라벨이 명시적으로 지정된 정렬이 없기 때문에 자연스럽게 약하게 감독되는 학습 문제

그림 2(a)와 같이 개와 소파 같은 눈에 띄는 물체가 영상과 쌍으로 구성된 텍스트에서 모두 나타나며, 그림 2(b)와 같이 영상 영역과 텍스트 단위 간의 의미 정렬을 학습하기 위한 기준점으로 사용할 수 있다.



# 3. Oscar Pre-training

![fig_3](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\fig_3.PNG)

인간은 많은 경로를 통해 세상을 인지한다. 개별 채널이 불완전하거나 소음이 발생하더라도, 여러 채널 간에 공유되는 경향이 있기 때문에 중요한 요소는 여전히 지각할 수 있다

이러한 점을 바탕으로 오스카는 이미지-텍스트 쌍 및 새로운 Pre-training 표현방식을 제시한다

### Input

각 입력 이미지-텍스트 쌍을 워드-태그-이미지 삼중(w, q, v)으로 나타낸다  (기존 연구에서는 W,V 쌍을 사용 )

w : 텍스트의 워드 임베딩 시퀀스

q : 이미지에서 감지된 개체 태그의 워드 임베딩 시퀀스

v : 이미지의 영역 벡터 세트

오스카는 이미지와 텍스트 정렬을 쉽게 배울 수 있도록 q를 핵심 포인트로 소개

 텍스트로 된 q와 w 사이의 정렬은 오스카의 VLP에 대한 초기화로 사용되는 사전 훈련된 BERT 모델을 사용하여 비교적 쉽게 식별할 수 있으므로, 객체 태그가 감지되는 영상 영역은 의미론적으로 관련된 단어로 쿼리할 때 다른 영역보다 주의 가중치가 높을 수 있다.

 언어 공간에 나타난 독특한 개체에서 개와 소파 같은 시야 공간에 모호하게 표현될 수 있는 영상 개체를 접지시키는 학습으로도 해석할 수 있다.

### Pre-Training Objective

![formular_1](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\formular_1.PNG)

 x : 텍스트와 이미지 사이의 표현을 구분하는 modality view

,x 0은 입력이 표현되는 두 개의 서로 다른 의미 공간을 구분하는 공간

개별 토큰 시퀀스를 h, [w, q]로 정의하고 사전 교육을 위해 MTL(Masked Token Loss)을 적용

-> BERT 처럼 15%확률로 각 입력 토큰을 무작위 마스킹하고 이를 예측

![formular_2](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\formular_2.PNG)

negative log-likelihood 를 통해 마스크된 토큰을 학습 

![formular_4](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\formular_4.PNG)



q를 데이터 세트 D에서 무작위로 샘플링된 다른 태그 시퀀스로 50% 확률로 대체하여 일련의 "오염된" 영상 표현을 샘플링

-> BERT를 그대로 따라 사용 

![formular_3](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\formular_3.PNG)



두 로스를 합한게 최종 로스 



BERT 처럼 학습하니 좋은 학습 성능을 만들었다 함 



### Pre-training Corpus

COCO [21], 개념 캡션(CC) [31], SBU 캡션 [26], 깜박임 30k [44], GQA [13] 등을 포함한 기존 V+L 데이터 세트를 기반으로 사전 교육 말뭉치를 구축했다. 총, 고유한 영상 세트는 410만 개이며 말뭉치는 650만 개의 텍스트 태그 영상 세 개로 구성됩니다. 자세한 내용은 부록에 있습니다.

### Implementation Details 

We pre-train two model variants, denoted as OscarB and OscarL, initialized with parameters θBERT of BERT base (H = 768) and large (H = 1024), respectively, where H is the hidden size. To ensure that the image region features have the same input embedding size as BERT, we transform the position-sensitive region features using a linear projection via matrix W. The trainable parameters are θ = {θBERT,W}. The AdamW Optimizer is used. OscarB is trained for at least 1.0M steps, with learning rate 5e −5 and batch size 768. OscarL is trained for at least 900k steps, with learning rate 1e −5 and batch size 512. The sequence length of discrete tokens h and region features v are 35 and 50, respectively.



# 4. Adapting to V + L Tasks

5개의 V+L 이해 작업과 2개의 생성 작업을 포함하여 7개의 다운스트림 V+L 작업에 맞게 조정

### Image-Text Retrieval

검색된 대상으로 사용되는 촬영장비에 따라 영상 검색과 텍스트 검색의 두 가지 하위 작업 - 이항 분류 문제

정렬된 이미지-텍스트 쌍이 지정된 경우 다른 이미지 또는 캡션을 임의로 선택하여 정렬되지 않은 쌍을 형성

 [CLS]의 최종 표현은 주어진 쌍이 정렬되었는지 여부를 예측하기 위한 분류기의 입력으로 사용

### Image Captioning

델이 이미지 내용에 대한 자연스러운 언어 설명을 생성

 문장 생성을 가능하게 하기 위해 Seq2seq 목표를 사용하여 오스카를 미세 조정

### Novel Object Captioning (NoCaps) 

이미지 캡션 작업을 확장하고 개방형 이미지 데이터 세트의 이미지를 포함한 벤치마크를 제공하여 교육 말뭉치에서 볼 수 없는 새로운 개체를 설명하는 모델의 능력을 테스트

### VQA

미지를 기반으로 자연어 질문에 답해야 한다.

이미지와 질문이 주어진 경우, 과제는 객관식 목록에서 정답을 선택하는 것

데이터 세트는 교육(83,000개의 이미지 및 444,000개의 문제), 검증(41,000개의 이미지 및 214,000개의 문제), 테스트(81,000개의 이미지 및 448,000개의 문제) 세트로 분할

### GQA

VQA와 비슷 질문에 대답할 수 있는 모델의 추론 능력을 테스트

모델은 각 질문에 대해 1,852개의 후보 답변 공유 집합에서 답변을 선택

### Natural Language Visual Reasoning for Real (NLVR2)

 이미지 쌍에 대한  자연어 문장이 참인지 확인하는 것



# 5. Experimental Results & Analysis

![table_1](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\table_1.PNG)

![table_3](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\table_3.PNG)

![table_2](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\table_2.PNG)

![fig_4](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\fig_4.PNG)





## 기타 공부 

### 1. scst(Self-Critical Sequence Training)

https://openaccess.thecvf.com/content_cvpr_2017/papers/Rennie_Self-Critical_Sequence_Training_CVPR_2017_paper.pdf



샘플링된 캡션과 추론 알고리즘으로 생성된 캡션 의 사이의 CIDEr-D 스코어의 오차를 리워드로 주 어 강화 학습하여 모델을 최적화한다.



![formular_5](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\formular_5.PNG)

테스트에 사용한 추론 알고리즘에 따라 현재 모델에서 얻은 보상으로 알고리즘을 기본화하는것.

t 시간 단계에서 softmax activation 샘플의 w의 보상에 대한 계산

![formular_6](\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\formular_6.PNG)



r(w^) : 테스트 시간에 사용된 추론 알고리즘에 따라 현재 모델에 의해 얻어진 보상



### 2. CBS(Constrained beam search)

단순히 beam search를 포함한 구조?

 
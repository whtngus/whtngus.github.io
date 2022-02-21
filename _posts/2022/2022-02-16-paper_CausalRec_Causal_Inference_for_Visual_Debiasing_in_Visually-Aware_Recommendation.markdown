---
layout: post
title: "paper : CausalRec: Causal Inference for Visual Debiasing in Visually-Aware Recommendation"
date: 2022-02-17 00:20:23 +0900
category: paper
---

# CausalRec: Causal Inference for Visual Debiasing in Visually-Aware Recommendation

url : https://arxiv.org/pdf/2107.02390.pdf

code :  https://github.com/PreferredAI/cornac/tree/master/cornac/models/causalrec		

https://github.com/PreferredAI/cornac/blob/master/examples/causalrec_clothing.py

[21: Proceedings of the 29th ACM International Conference on Multimedia](https://dl.acm.org/doi/proceedings/10.1145/3474085)



# ABSTRACT

E-commerce 플랫폼은 user-item 상호 작용 뿐만 아니라 시각적인 정보를 함께 활용해 고객의 선호도를 예측하고자 한다.

일반적인 추천 시스템은 시각정인 정보까지는 반영하지 않는다 

-> 하지만 그 외의 특징 브랜드, 가격 등의 정보는 활욯하지 못하는 문제 발생 

추가로 기존의 visually-aware 모델은 시각적 특징을 다른 기능과 유사하게 별도의 collaborative 와 비슷하게 접근해 잠재적인 편향을 식별하지 못한다

해당 연구에서는 이러한 점을 기준으로 새로운 제안을 하려는 것으로 보임 

시각적 정보의 지지적 중요성을 효과적으로 유지하고 시각적 편향을 제거하기 위해 CausalRec으로 표시되는 저하된 시각적 인식 추천 시스템을 제안

# 1 INTRODUCTION

![f_1](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f_1.PNG)

E-commerce 플랫폼의 visually-aware은 과거 user-item 상호작용 외에도 사용자 선호도를 예측할 대 시각정 정보또한 고려함

기존 추천시스템에 비해 쇼핑 의류와 같은 많은 도메인에서 성능을 향상시킴

시각적 특징이 다른 특징(예: 브랜드, 재료, 가격)과 함께 일반적으로 사용되지만 collaborative에서 널리 사용되는 모델링은 편향된 학습 쳬계를 수행하고 있음.

위의 Figure 1 에서 흰 셔츠를 볼때 사용자가 특정 재료를 찾는다고 하면 다른 입력 특징들과 상호작용 들은 영향이 없어진다. 그리고 이러한 모든 클릭들이 기록된다. 이를 visual bias(시각적 편향화) 라고 한다.

 기존의 시각 인식 추천 시스템은 주로 편파 절차 없이 시각적으로 편향된 기록에 대해 훈련



위에서 말한 편향들은 , position bias, selection bias and popularity 등 다양한 편향이 존재해 이에대한 몇가지 접근 방법이 연구됬다.

그러나 기존 연구의 접근 방식은 외부편향 보다는 항목 자체에서 발생하는 시각적 편향을 제거하기 위해 거의 적용할 수 없음. (이미지 기반에서 적용하기 힘들다는 의미)

vision-language 테스크들이 존재  ->  일반적으로 이러한 방법에서 인과 그래프는 작업에 대한 서로 다른 구성 요소 간의 인과 효과를 나타내도록 구성

(인과 효과 - 특정 구성 요소가 다른 구성 요소에 미치는 영향을 정량화)

시각적 편향을 제거하기 위해 User ID, Item ID, 시각적인 특징, user-item 선호도 등을 식별하고, 다른 특징의 영향을 받지 않고 순순한 시각적 선호도를 나타냄

실제 쇼핑 시나리오에서 사용자의 시각적 통지는 사용자가 아이템을 한눈에 고려할 수 있는 다른 정보(재료, 브랜드 등)가 부족할 때 user-item 상호작용으로 강하게 이뤄질 수 있다 -> 나도 쇼핑할때 그런것 같다 .

편견 없는 예측을 추구하기 위해 개입과 반사실적 추론을 활용 주요 아이디어는 

-> 사용자가 동일한 시각적 특징을 가진 다른 항목을 보았다면 이 사용자는 여전히 이러한 항목과 상호 작용합니까?



기존의 시각 인식 권장 방법의 시각적 편향을 분석하기 위해 인과 그래프를 개발

-> e Total Indirect Effect (TIE)

지원적 시각적 정보를 유지하고 시각적 편차를 수행하기 위해 인과적 추론 기반 새로운 추천 모델을 제한

-> CausalRec

# 2 PRELIMINARIES

아래 수식부터 

랜덤 변수에는 대문자를 사용하고 랜덤 변수 관측에는 소문자를 사용

이제부터 수식이 많이나온다 집중!

- 다시보기 !

## 2.1 Causal Graph A causal graph is a directed

![f_2](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f_2.PNG)

- G = (V, E)

> V : 그래프에서 node,  랜덤 변수 집합
>
> E : 위의 변수들 간의 특성 및 결과 관계 (edges)를 나타냄
>
> Figure2의 그림 참조
>
> 그림의 A,B,C 가 random variables와 각 관계를 볼 수 있음
>
> A -> B   A->C  B->C 를 향함 즉, A->C and A->B->C
>
> 간단한 그래플 a->c 로 변환

## 2.2 Intervention

- 𝑃 (𝐶 | 𝑑𝑜 (𝐴)) =  SIGMA 𝑏 𝑃 (𝐶 | 𝐴, 𝑏)𝑃 (𝑏)

> 𝑃 (𝐶 | 𝐴) = SIGMA 𝑏 𝑃 (𝐶 | 𝐴, 𝑏)𝑃 (𝑏 | 𝐴),
>
> 위 식을 전개하면 n 𝑃 (𝐵 = 𝑏) = 𝑃 (𝑏)를 얻을 수 있고 위의식으로 치환 가능

## 2.3 Counterfactual Notations

![f1](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f1.PNG)

> - 수식 (1) -  Total Effect
>
> a 가 c에 미치는 영향을 figure 2의 (a)와 (b)를 이용해  표시
>
> Figure(a) 는 a에 의해 영향을 받은 C 이고  (b)는 a를 관측(무시했을경우)했을경우의 값이다.
>
> 즉, (a) - (b)로 a가 영향을 주는 정도
>
> - 수식 (2) - Natural Diredt Effect
>
> Figure(d) - (b)   - (b)의 경우 b가 a에 영향을 받아 c에 영향을 줌으로 
>
> A가 직접적으로 C에 영향을 준 내용만을 수식으로 표시 
>
> - 수식(3) - total indirect effect 
>
> 수식 1은 A의 영향 수식2는 직접적인 영향임으로 
>
> 간접적인 영향은 수식(1) - 수식(2)  이다.

# 3 VISUAL BIAS IN VISUALLY-AWARE RECOMMENDATION

##  3.1 Notation and Task Definition

변수 셋팅 

u : user ID

i : item ID

Yu : User Vector

Yi : Item Vector

Vi : 고 차원의 이미지 아이템 벡터

I : node

V : visual feature item

U : User feature

M : 사용자와 항목의 실제 선호도

Y : 시각적 특징에 대한 사용자의 시각적 선호도

## 3.2 Non-visual Example: Matrix Factorization

Matrix Factorization (MF)가 sota 인 경우가 많다 𝑃 (𝑌 | 𝐼,𝑈 )

![f4](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f4.PNG)

알파 - 오프셋 텀

Bu Bi - user item의 bias

𝜸𝑢  𝜸i - e latent embedding factors

offset과 bias는 평균으로 계산 

![f_3](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f_3.PNG)

Figure3의 (a)가 MF 

## 3.3 Visual Bayesian Personalized Ranking

![f5](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f5.PNG)

Visual Bayesian Personalized Ranking (VBPR) 을 baseline으로 함 -  𝑃 (𝑌 | 𝐼,𝑉 ,𝑈 )

E - transform matrix

Phi - backbone network(Resnet and VGG)

Vi  𝜽u - visual feature representation

𝜽 𝑇 𝑢 (𝑬𝜙 (𝑽𝑖))  : visual feature 임베딩함 representation vector 

## 3.4 DeepStyle and Adversarial Multimedia Recommendation

DeepStyle과 Adversarial Multimedia Recommendation(AMR)은 성능을 개선하기 위해 그래프를 공유하는 VBPR의 후속 방법

![f6](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f6.PNG)

ci : 이미지에서 사용되는 카테고리 정보

r 𝜸 : 유저 아이템 벡터 

![f7](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f7.PNG)

위 식의 중앙의 delta는 adversary 학습 방식으로 훈련된 적대자 -> 시각적 특징에 노이즈를 추가함



## 3.5 Deep Visual Bayesian Personalized Ranking

Deep Visual Bayesian Personalized Ranking (DVBPR) 도 VBPR을 베이스로 함 

![f8](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f8.PNG)

Figure 3 (d)

위 수식에 따르면 시각적 특징이 item feature를 대표한다고 볼 수 있음 



# 4 VISUAL DEBIASING

```
- 다음과 같은 질문을 base 아이디어로 제안 
question: If a user had seen other items with the same visual feature,
would this user still interact with these item
-> 그럼 Figure 3 의 (d)는 고려대상에서 제외?
```

## 4.1 Counterfactual Inference in Visually-Aware Recommendation

시각저거 인식은 시각적 특징을 포함한 항목의 특징에 대한 실제 선호도를 기반으로 사용자와 항목의 일치를 예측하는것이 중요 

상호 작용의 원일을 추가로 분석하기 위해 시각적 특징을 가진 사용자 i와 item을 기반으로 해야함

![f9](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f9.PNG)

![f10](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f10.PNG)

시각적 편향을 제거하기 위해 상호 작용에 대한 시각적 특성의 직접적인 영향을 제거 

-> 같은 사진의 다른 아이템을 본경우 유저는 여전이 아이템에 관계성을 가질것인지에 대한 의문에 대한 해결책

### 4.1.1 Intervention

![f12](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f12.PNG)

직접적인 영향만을 가져오기 위해 전체 영향(u, v)에서  vision의 직접적인 영향을 제거 

### 4.1.2 Counterfactual Inference

![f13](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f13.PNG)

2 의 식과 같이 전체 영향도에서 직접적 영향도를 제거 

![f15](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f15.PNG)

![f14](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f14.PNG)

실제 TIE를 예측하는것을 목표로 함



## 4.2 CausalRec Model

![f_4](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f_4.PNG)

### 4.2.1 Base Model.

![f16](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f16.PNG)

VBPR, DeepStyle and AMR 모델

F : represents 함수  M과 visual 특징인 N을 포함 

![f17](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f17.PNG)

M과 N은 위의 수식과 같이 계산됨 

M - User - Item Representation vector 의 곱 

N -   세타는 Yu와 같음  시각적 특징의 임베딩과 user 특징의 곱 

### 4.2.2 CausalRec Model

![f19](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f19.PNG)

시각의 간접적인 영향도를 포함한 base model  - Figure 4 (a) 참조

◦ : Hadamard product

sigma : sigmoid

F : 단순 scalar 곱 

multi-task learning framework 를 사용 

![f23](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f23.PNG)

위 수식은 multi-task learning의 object function

- l rec 는 BPR  loss 

![f24](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f24.PNG)

Y hat :  상호작용 예측

O : 학습 데이터 셋 

i : positive user item

j : negative user item    

theta  : training parameters

lambda : L2 정규화 가중치

### 4.2.3 CausalRec Inference. 

Figure 4 의 (b) 참조 

CausalRec 모델 예측시 다음과 같은 방식 사용 

![f25](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f25.PNG)

![f26](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f26.PNG)

전체의 영향과 직접적인 영향 

![f27](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f27.PNG)

inference 대상인 TIE  - 간접적인 영향을 예측

![f28](\img\2022\CausalRec_Causal_Inference_for_Visual_Debiasing_in_Visually-Aware_Recommendation\f28.PNG)

시각적 편향을 일정량 유지하기 위해  lambda2를 이용해 시각적 편향을 제거 

# 5 EXPERIMENTS







# 참고

- Hadamard product

아다마르 곱

같은 크기의 두 행렬의 각 성분을 곱하는 연산 

기호는 ◦ 을 사용 


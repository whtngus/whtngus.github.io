---
layout: post
title: "paper : Enhancing VAEs for Collaborative Filtering: Flexible Priors & Gating Mechanisms"
date: 2022-04-04 00:01:01 +0900
category: paper
---

# Enhancing VAEs for Collaborative Filtering: Flexible Priors & Gating Mechanisms

 Information Retrieval (cs.IR); Machine Learning 

ACM Conference on Recommender Systems 2019

서울대 

https://arxiv.org/abs/1911.00936

# ABSTRACT

협업 필터링을 위한 뉴럴 모델이 주목받기 시작함 

variational autoencoder를 사용해 생성모델을 생성하는데 기초를 두고있는 경우도 있다.

지금까지의 CF용 가변 variational autoencoders 에는 문제가 될 수 있는 특성이 있다.

1. VAE가 유저 정보를 담기 위해 아직 너무 단순한 형식임
2. 각 네트워크에 대해 딥러닝을 통한 표현학습을 하기가 힘들어짐 

해당 논문에서 동 필터링에 유연한 우선 순위를 적용하여 (오리지널 VAE에서) 단순한 우선 순위가 full_model 사용자 기본 설정에 너무 제한적일 수 있음을 보여 주는 첫 번째 사례

 CF에서 flexible_priors의 효과를 조사하기 위해 원래 이미지 생성용으로 제안된 VampPrior를 사용하여 실험

Gating_mechanism과 조합된 VampPriors가 Variational_을 포함한 SOTA 결과를 능가



MovieLens 와 Netfilx 데이터셋을 사용

# 1 INTRODUCTION

최근 웹 기반의 다양한 개인화 추천시스템을 사용하고 있음 . + 대용량의 데이터

딥러닝을 이용한 다양한 연구가 활성화됨 

해당 연구에서는 유저 임베딩을 통한 latent vector 생성에 초점을 맞춘다.

 구매 history를 이용해 사용자 latent vector를 재구성해 수행할 수 있음.

vanilla autoencoders, denoising autoencoders,  Variational Autoencoders (VAEs)  의 모델을CF 추천시스템에 주용 사용함

-> 나중에 찾아보기 

최근에는 Variational Autoencoders 를 이용한 collaborative filltering이 sota를 찍음 

-> 그러나 더 연구된 내용은 없고 고품질의 user latent vector가 필요함 

해당 논문에서는 잠재적인 문제가있는 VAE시스템을 해결하고 좋은 latent벡터를 생성하는것을 목표로함

본 연구에서 제시하는 두가지 연구 동기

1. VAE에서 사용되는 분포는 CF에서 제한적일 수 있어 보다 풍부한 잠재 변수를 만드는데 방해가 될 수 있음
2. 사용자 항목 간의 상호작용 이력을 통해 학습하는 것은 고유한 특성이 있으며, 보다 효과적인 아키텍처를 통해 deep_latent 표현을 학습할 수 있음 (딥러닝 모델에 GLU를 사용)

VampPrior 과 Recurrent 모델을 같이 병목시켜 성능을 향상시키고자 함 

MovieLens-2000M과 Netflix 데이터셋에서 NDCG and recall의 sota 스코어를 찍음 

논문의 컨트리뷰션

1. VAE CF 모델의 문제를 처음으로 제안
2. autoencoder cf 와 glu 를 사용해 sota 스코어 찍음

# 2 RELATED WORK

생략

# 3. PRELIMINARIES

 협업 필터링에서 권장 성능을 더욱 향상시키기 위해 적절한 아이디어를 통합하는 CF용 VAE 프레임워크

## 3.1 Problem Formulation

상호작용 이력을 기반으로 사용자 기본 설정을 모델링

u ∈ {1, … ,N} : Users

i ∈ {1, … , M} : Items

 𝐗 = {𝒙1, … , 𝒙𝑁}  : 사용 히스토리

## 3.2 VAE for Collaborative Filtering

연구의 기본 모델 Multi-VAE 

 모든 사용자 a에 대해 표준 정규 사전 분포에서 잠재 변수 D를 생성 (D - standard normal prior distribution)

잠재 표현은 다항 분포를 가정하여 각 항목을 소비했는지 여부를 나타내는 기록을 이용

x^u : consumption history - > back of word 형식으로 소비여부를 임베딩함 

 ![f1](E:\code\whtngus.github.io\img\2022\Enhancing_VAEs_for_Collaborative_Filtering__Flexible_Priors_and_Gating_Mechanisms\f1.PNG)

 P(𝑿) = ∫ 𝑝(𝑿|𝒛)𝑝(𝒛) 𝑑𝒛 .

𝑓𝜃 (∙) : non-linear mapping

그러나 다루기 어려움 

![f2](E:\code\whtngus.github.io\img\2022\Enhancing_VAEs_for_Collaborative_Filtering__Flexible_Priors_and_Gating_Mechanisms\f2.PNG)

- Evidence Lower Bound (ELBO) 식 

𝑝𝜃 (𝒙|𝒛) : generative model - decoder

𝜃 : neural network parameter

𝑝𝜆 (𝒛) : 사전 분포의 잠재변수

𝑝(𝒛|𝒙) : 모델의 예측 

𝑞𝜙(𝒛|𝒙)  :  recognition model (e𝛽 ∈ [0,1] ncoder) 위의 p(z|x) 에서 사용됨

𝛽 ∈ [0,1] :  scale the KL term similar to 𝛽-VAE - Multi-VAE for CF

# 4 ENHANCING VAES FOR CF

VAE의 이전 분포를 분석하여 정규_표준 가우스의 이전 분포가 모델링 성능을 제한할 수 있음

## 4.1 Flexible Priors for Modeling User Preference

 ELBO 목표를 추가로 분석하여 다음과 같이 다시 작성

![f3](E:\code\whtngus.github.io\img\2022\Enhancing_VAEs_for_Collaborative_Filtering__Flexible_Priors_and_Gating_Mechanisms\f3.PNG)

![f3_2](E:\code\whtngus.github.io\img\2022\Enhancing_VAEs_for_Collaborative_Filtering__Flexible_Priors_and_Gating_Mechanisms\f3_2.PNG)

negative reconstruction error를 사용 - cross-entropy   𝑞(𝒛) =_1_𝑁_∑ 𝑞𝜙(𝒛|𝒙𝑢)_𝑁_𝑢=1

VAE는 미리 선택된 표준 가우스 분포를 따름

표준 가우스 분포의_단순한 유니모달 특성으로 인해 의도하지 않은 강력한 정규화 효과를 가져옴

#### VampPrior((variational mixture of posteriors prior)

4.1의 수식을 다시보면 

𝑝𝜆(𝒛) :  prior  cross-entropy 로 볼수 있다.

라그랑주 함수를 풀어서 ELBO를 최대화하는 최적의 전제를 찾는다면, 그것은 단순히 주어진 𝑝𝜆_∗_(𝒛) =_1_𝑁_∑ 𝑞𝜙(𝒛|𝒙𝑢)_𝑁_𝑢=1 를 풀면 된다

VampPrior는 K개의 학습 가능한 의사 입력에 맞춰진 변형 포스터의 혼합 분포를 사용하기 전에 최적의 근사치

![f4](E:\code\whtngus.github.io\img\2022\Enhancing_VAEs_for_Collaborative_Filtering__Flexible_Priors_and_Gating_Mechanisms\f4.PNG)

위 수식에서 K는 M차원의 의사 입력수 

의사 입력 : 역전파를 통해 학습되며 , 하이퍼 파라미터로 생각할 수 있음

### Hierarchical Stochastic Units

![f5](E:\code\whtngus.github.io\img\2022\Enhancing_VAEs_for_Collaborative_Filtering__Flexible_Priors_and_Gating_Mechanisms\f5.PNG)

VampPriors의 원래 작업에서처럼 훨씬 더 풍부한 잠재 표현을 배우기 위해 계층적 확률 단위를 채택

협업 필터링을 위해 계층적 VAE는 사용된적이 없다.

확률적 잠재 변수 z1 z2 의  계층 구조로 변경됨, 

![f6](E:\code\whtngus.github.io\img\2022\Enhancing_VAEs_for_Collaborative_Filtering__Flexible_Priors_and_Gating_Mechanisms\f6.PNG)

𝑝(𝒛2 ) = 1 𝐾 ∑ 𝑞𝜙(𝒛2|𝒖𝑘)  는 뉴럴 네트워크의 조건부 분포에 최적화함

## 4.2 Gating Mechanism

r collaborative filtering에서 인코더를 사용한 이전의 연구에서는 비교적 얕은 네트워크를 사용

-> 내가 적용하려는 추천시스템도 차원수가 커서 얇은 네트워크를 적용해야 할 것 같다.

모델에서는 숨겨진 레이어가 없는 인코더 네트워크를 사용 -> 즉 1차만 사용

Multi-VAE  인코더에서는 1개의 숨겨진 레이어가 사용되며 레이어를 추가해도 퍼포먼스가 향상되지 않음

위에서 향상되지 않은 이유를 2가지로 유추

1) 희박한 소비 이력
2) 인코더와 디코더로 인해 비교적 쉽게 심화된 자동 인코더 구조

#### Gated Linear Units

네트워크 구조가 깊어질 수록 비재귀 신경망은 하위 계층에서 상위 계층으로 정보를 제대로 전달하지 못하는 문제도 발생

더 깊은 네트워크에서 정보 전파를 돕기 위해 제안된 게이트 CNN 논문에서 제안된 비재귀 게이트 메커니즘을 실험

![f7](E:\code\whtngus.github.io\img\2022\Enhancing_VAEs_for_Collaborative_Filtering__Flexible_Priors_and_Gating_Mechanisms\f7.PNG)

⊗ : element-wise product

X : input 

W, V, b, c : 학습 파라미터 

시그마 : 시그모이드

네트워크의 모델링 용량을 증가시켜 더 높은 수준의 상호작용을 가능하게 하는 것으로도 해석

# 5 EXPERIMENTS






























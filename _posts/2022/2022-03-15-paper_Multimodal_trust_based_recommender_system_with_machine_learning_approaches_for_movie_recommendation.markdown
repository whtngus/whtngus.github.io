---
layout: post
title: "paper : Multimodal trust based recommender system with machine learning approaches for movie recommendation"
date: 2022-03-16 00:20:01 +0900
category: paper
---

# Multimodal trust based recommender system with machine learning approaches for movie recommendation

짧은 요약 

https://drsachinandan.com/publication/2021/3.MultimodalTrustBasedRecommende_sasmita.pdf

2020 11월 3일

코드 없음 ㅠ

# Abstract

Recommender system (RS)은 최소한의 결정 시간으로 영화를 볼 수 있는 가장 효율적이고 유용하며 널리 퍼져 있는 애플리케이션 중 하나

대부분 추천시스템 연구는 콜드 스타트 문제, 데이터 희소성, 악의적인 공격을 다루지 못함 (메크로 등 )

사용자 유사성과 가중 신뢰 전파를 결합한 신뢰 매트릭스 측정을 제안

콜드 유저가 아닌 사용자는 신뢰 필터로 여러 모델을 통과했고 콜드 유저는 추천 선호도에 따라 최적의 점수를 생성

사용자에게 적합한 영화를 추천하기 위해 역전파(BPNN) 모델, SVD(Single Value Decomposition) 모델, DNN(Deep Neural Network Model), DNN with Trust 등 4가지 추천 모델을 비교

# 1. Introduction

하이브리드 추천 시스템은 하나 이상의 RS 접근 방식을 취함으로써 형성

가장 널리사용 되는 추천시스템은 협업 추천시스템 

추천시스템은 콜드 스타트(신규 사용자뿐만 아니라 추천 목록이 없는 신규 사용자), 데이터 희소성(사용자 항목 매트릭스에는 등급 수가 적음), 악의적인 공격(사용자의 비율이 다른 사용자에 의해 복사됨) 및 그레이 쉬프 문제(사용자의 취향은)와 같은 다른 문제로 어려움이 있음.



 협업(CF) 권장의 제한과 문제 때문에 유사성 기반 사용자 대신 사용자 간의 신뢰와 유사성이 더 나은 권장 사항에 고려

- 사용자 들의 관계

> -  Implicit trusts
>
> 사용자 간의 신뢰를 지정하며 데이터 세트에서 사용 가능한 정보를 기반으로 계산
>
> - Explicit trust s
>
> 사용자가 제공한 사용자의 신뢰를 지정
>
> 데이터 희소성 또는 정보 가용성이 없기 때문에 명시적 신뢰를 얻기가 어렵다. 
>
> 
>
> 즉, 암묵적 신뢰를 계산하는데 사용되는 다양한 측정 지표들이 있고 주로 사용됨

# 2. Related work

추천시스템에서 collaborative filter(CF) 방법론은 더 각광받오고 있음 

이는 전통적인 추천시스템 방법과 사용자 간의 신뢰를 기반으로 하는 Trust-worthy recommendation 이다.

## 2.1 Traditional collaborative filtering based ecommender systems

CF 알고리즘은 두가지 메모리기반 알고리즘이 있다.

Memory based algorithme - 사용자 프로필 DB를 기반으로 함 

-> 아마존도 CF 추천시스템을 쓴다고함.

그러나 CF 추천시스템은 사용자에게 예상치못한 정보를 제공함 -> cold start의 데이터 희소성과,  Gray sheep problem

Gupta와 Hagpal은 사용자의 취향이 다른 사용자와 일치하지 않을때 CF를 비활성화 해 gray sheep 문제를 해결하고자 했다

## 2.2 Trust-worthy recommender systems

전통적인 CF에서 신뢰는 사용자에 대한 친구와 동료 선택의 합???

신뢰를 평가하는것은 이러한 문제점을 극복하기 위함(악의적 혹은 비악의적인 데이터)

Tidal Trust 알고리즘을 사용하여 영화 추천에 대한 신뢰 값을 평가 ->  가장 가까운 신뢰 경로를 통해 대상 사용자가 만든 모든 사용자의 점수를 구함

k-nearest recommenders를 통해서 CF의 단점을 제거하는 방법도 제안됨

CF에서 발생한 문제점을 유지하면서 사용자 간의 신뢰와 유사성을 모두 고려했습니다.

# 3 Proposed model of recommendation

![f_1](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f_1.PNG)

제안 모델은 영화에서 신뢰할 수 있는 user 가치와 머신러닝을 이용한 접근 방법

CF은 유저와 아이템의 유사성을 처리한다. -> 사용자와 아이템관의 관계를 지속적으로 찾아 추천을 함

두가지 잘알려진 CF기반 접근방법

> 1. memory-based approach
>
> user/item의 유사도를 계산하기위해 메모리 기반의 접근
>
> 데이터 희소성과, 확장성을 해결해야함
>
> 2. moelbased approach
>
> 머신러징 알고리즘을 통해 rating을 함
>
> -> 유저기반의 아이템을 추천하기위한 알고리즘들이 주로 개발됨

- Matrix Factorization 

특징을 임베딩하기 위해 사용되는 가장 자주사용되는 모델 

머신러닝 기법으로는 SVD, Auto encoder모델등이 사용됨

## 3.1 Matrix factorization

![f_2](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f_2.PNG)

Matrix factorization 은 두 종류의 다른 엔티티를 곱할 때 잠재 특징을 생성하는 방법

-> 아이템과 유저 사이의 관계를 확인함 

95%의 희박한 행력은 계산량이 많아지고 정확도를 낮게 만든다 

유저 등급 메트릭스를 두 특징으로 나누고(사용자, 아이템)  비슷한 메트릭스를 출력한다.(Fig 2)

Matrix factorization은 구현하기 쉽고 잠재적으로 해석이 가능하며 시간도 적게 소모된다.

but, 복잡한 관계를 파악하지는 못한다.

## 3.2 Singular value decomposition (SVD)

![f1](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f1.PNG)

SVD는 실수 행렬 또논 복소 행렬의 인수분해.

U : m*x matrix

V : n*x matrix

X : x*x diagonal matrix with non-negative 

SVD는 유저에 대해 아이템 등급을 예측하는 방법을 제안한다. 레이팅이 높을경우 해당 아이템을 추천하는 방식

새로 계산된 사용자 항목 등급 매트릭스에서 대상 사용자의 사용자 특징 벡터에 대한 user-item 등급을 생성하고 높은 예측 등급 항목을 선택한다.

SVD는 효율적이고 큰 metrics에서 잘 작동하지만 강한 non-linear 데이터의 경우 svd는 잘 작동하지 않는다.

또한 단일 수학 공식으로 바꿀 수 있는 파라미터가 특징 수 뿐이여서 정확도를 향상시킬 수 없음

 ## 3.3 Backpropagation neural network (BPNN)

![f_3](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f_3.PNG)

User Feature 임베딩은 입력 레이어와  hidden layer 

Fig 3의 모델은 user와 item의 특징 벡터가 latent 벡터를 만들어 냄 

- user 임베딩 size :  nUsers x nFeatures
- item 임베딩 size :  nItems x nFeatures

user i - User Feature embedding

item i - Item Feature embedding

위 네트워크는 SGD를 통해 학습 됨

user-item dot-prodoct

## 3.4 Deep neural network (DNN)

![f_4](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f_4.PNG)

DNN은 End-to-End로 넷트워크를 훈련 

데이터의 복잡성과 대량의 훈련 샘플은 상당한 성능 향상

embedding layer는 사용자 항목 피쳐 매트릭스를 입력으로 받음

정확도는 MSE를 통해 측정

## 3.5 Trust based filter

CF에서 소비자 정보를 검색하고 생산자가 정보를 제공

trust :  특정 시간에 전문지식과 성과를 바탕으로 고객의 진실을 받아들일 준비가 되어 있는 것으로 평가 -> ?? 이해안됨 

trust system : 인터페이스 제공자

Local trust(사용자 개인화) 와 Global trust(범용적인)는 다르다고 함 

peer dependency가 없는경우 Global trust의 단일점수로 계산

i : 품목

c : 소비자

i 와 c에 대한 예측 등급은 소비자와의 유사성에 따른 개인화 추천기반으로 평가 가능하다.

![f2](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f2.PNG)

위 식은 Resnick’s  standard prediction rating

c(i) - 품목 i에 대해 예측되는 등급

p(i) - 제공자에 따른 품목 i 등급

c와 p의 유사성은 Pearson 상관 계수에 의해 측정함

용자에 대한 파트너의 등급 예측에 대한 기여도는 Resnick이 제공한 파트너 간의 유사성 수준에 따라 달라집니다. 

유사성이 높으면 시스템이 등급 예측에 더 많이 기여

![f3](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f3.PNG)

![f4](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f4.PNG)

correct 는 p와 i의 차이가 특정 엡실론 이하인 값 

RecSet은  생산잔에 대한 전체 권장값 

-> 즉, 전체정답 분에 p와c가 유사한값



신뢰할 수 있는 기반 권장 사항은 필터가 예측 프로세스에 참여할 신뢰할 수 있는 프로파일을 결정하는 것

![f5](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f5.PNG)

 Resnick’s formula [4] (위위의 식)에서는 신뢰값이 임계치를 넘어간 값들도 고려를 함 

추천 시스템에서 사용자 간의 유사성 측정과 예측 등급 및 실제 등급의 변동으로부터 생산자에 대한 신뢰치를 무효화할 수 있다. -> 콜드 유저를 테스트 함으로 써 

다른 유저와 대상 유저 사이의 신뢰는, Donovan의 신뢰 공식을 사용해 계산

 계산 중인 모든 참조 모델의 성능 및 권장 사항에 대해 생성된 신뢰 가치와의 결합. 콜드 유저의 경우, Optimal Score Generator 는, 등급이 매겨진 무비에 근거해 스코어를 생성해, 내림차순으로 정렬

![f6](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f6.PNG)

사용자 선호도와 함께 최적의 고차 점수를 얻으면 정확한 동영상을 추천

# 4 Result and discussion

## 4.1 SVD model

사용자 610명,  아이템 9724개, 100,837개의 레이팅, All the non zero value

- 결과는 봐도 해석이 안돼서 figure 생략

## 4.2 BPNN model

![f_6](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f_6.PNG)

Fig6은 epoch 별 MSE loss 그래프 위 그램에서 파악 되듯이 오버피팅이 예상됨

## 4.3 Deep neural network model

![f_7](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f_7.PNG)

![f_8](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f_8.PNG)

대상 사용자를 기준으로 K-가장 가까운 이웃이 가장 유사한 k명의 사용자를 찾아내고 최고 등급의 영화를 추천 대상으로 사용

피처 맵에 표시될 수 있다

Fig 7 에서 딥러닝은 잘 학습되는걸로 보임 

## 4.4 Trust computation

![f_10](\img\2022\Multimodal_trust_based_recommender_system_with_machine_learning_approaches_for_movie_recommendation\f_10.PNG)

생산자-소비자 신뢰 매트릭스는 소비자 등급 매트릭스와 사용자 기능 매트릭스에서 도노반의 신뢰 방법을 사용하여 계산

SVD 및 DNN 모델에 대해 MSE(평균 제곱 오차) 값이 각각 감소하고 있는 것으로 확인

DNN에 신뢰가 통합되면 MSE 값이 개선(위의 그림 10)



# 5 Conclusion and future work

추천시스템 모델은 기계 학습 기술을 사용하여 개발된 다음 신뢰 기반 필터링을 사용하여 더 정확하게 권장하고 있다. 정확도는 BPNN(41%), SVD(69%) 및 DNN(78%)으로 측정

역전파와 DNN 모델의 손실 값을 비교했고 신뢰도를 가진 DNN의 유효성 검사 손실(83%)이 더 나은 결과

콜드 유저는 항상 CF의 잠재적인 문제였기 때문에 최적 점수의 높은 값이 더 좋다.

 CF, 콘텐츠 기반 및 인구 통계 기반 필터링에 다양한 생물학적 영감을 받은 최적화 기술을 구현할 수 있으며 향후 더 나은 권장 사항을 위해 성능을 비교할 수 있다.

 

# 참고 지식

- Gray sheep problem

검색봇 등 추천에 방해되는 인자




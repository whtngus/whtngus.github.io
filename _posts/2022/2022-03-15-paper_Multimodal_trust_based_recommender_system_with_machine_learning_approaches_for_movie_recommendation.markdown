---
layout: post
title: "paper : Multimodal trust based recommender system with machine learning approaches for movie recommendation"
date: 2022-03-15 00:20:23 +0900
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

. CF에서 발생한 문제점을 유지하면서 사용자 간의 신뢰와 유사성을 모두 고려했습니다.





# 5 Conclusion and future work

추천시스템 모델은 기계 학습 기술을 사용하여 개발된 다음 신뢰 기반 필터링을 사용하여 더 정확하게 권장하고 있다. 정확도는 BPNN(41%), SVD(69%) 및 DNN(78%)으로 측정

역전파와 DNN 모델의 손실 값을 비교했고 신뢰도를 가진 DNN의 유효성 검사 손실(83%)이 더 나은 결과

콜드 유저는 항상 CF의 잠재적인 문제였기 때문에 최적 점수의 높은 값이 더 좋다.

 CF, 콘텐츠 기반 및 인구 통계 기반 필터링에 다양한 생물학적 영감을 받은 최적화 기술을 구현할 수 있으며 향후 더 나은 권장 사항을 위해 성능을 비교할 수 있다.

 

# 참고 지식

- Gray sheep problem

검색봇 등 추천에 방해되는 인자






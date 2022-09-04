---
layout: post
title: "paper : DDTCDR: Deep Dual Transfer Cross Domain Recommendation"
date: 2022-08-31 01:01:01 +0900
category: paper
---


# DDTCDR: Deep Dual Transfer Cross Domain Recommendation



2019년 10월 11일 

New York University

WSDM

url : [https://arxiv.org/pdf/1910.05189.pdf](https://arxiv.org/pdf/1910.05189.pdf)

# ABSTRACT

두 개의 관련 도메인 간에 반복적으로 정보를 전송하는 이중 학습 메커니즘을 기반으로 한 교차 도메인 권장 사항에 대한 새로운 접근 방식을 제안

서로 다른 잠재 공간에 걸친 사용자 간의 관계를 유지하면서 여러 도메인에 대한 사용자 선호도를 추출하기 위해 새로운 잠재 직교 매핑을 개발

영화, 책, 음악 항목의 세 가지 영역을 포함하는 대규모 데이터 세트에서 제안된 방법을 테스트

# 1. INTRODUCTION

추천 시스템은 CF(Collaborative filtering), MF(matrix factorization) 방법들을 통해 사용자가 만족할만한 제품을 발견하는데 도움을 주는 시스템 

그러나 기존 추천 시스템은 과거 트랜잭션의 일부만 액세스 가능하기 때문에 cold start 과 data sparsity problems에 어려움을 겪고 있다.

→ 이를 해결하기 위해 cross domain recommendation 이 제안됨 

![f1](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f1.png)

예를 들어, 사용자가 특정 영화를 본다면, 우리는 그 사용자에게 영화의 원작 소설을 추천

또한 사용자가 책을 읽는 성향을 보고 비슷한 성향의 영화를 추천 해 줄 수 있음

→ 다른 도메인 간의 좋은 영향을 주는 학습 루프 생성 

- 기존의 문제점
- 1.  이전의 이중 전송 모델은 사용자 및 항목 간의 잠재적이고 복잡한 관계를 고려하지 않고 명시적인 정보에만 초점을 맞춘다.
    2.  추천시스템에서 user item 항목을 다 사용하지 않음 

이를 해결하기 위해 Latent embedding 방식을 통한 연구가 진행되고 있으며, 사용자와 item의 feature또한 효율적으로 사용할 수 있음. 

→ 즉 Latent embedding을 어떻게 설계할지가 매우 중요한 포인트

해당 논문의 가정 사항

두 명의 사용자가 특정 도메인에서 유사한 선호도를 가지고 있다면, 다른 도메인에서도 그들의 선호도가 비슷해야 한다고 가정

→ 음….

또한 이중 추천 모델을 반복적으로 업데이트함으로써 두 도메인에 걸쳐 추천 성능을 동시에 향상시키고 모든 기준 모델을 능가한다는 것을 실험적으로 입증

논문의 이점 및 컨트리뷰션

- latent representation을 이용한 정보 전송을 통해 최적의 user, item의 정보를 전송
- dual transfer learning mechanism을 통해 두 도메인에서 동시에 성능을 향상시키는 양방향 전송 방법 제안
- 사용자 선호도의 유사성을 보존하고 역매핑 함수를 효율적으로 계산할 수 있는 두 도메인에 걸쳐 잠재된 직교 매핑 함수를 학습
- sota
- 모델의 단순화된 사례에 대한 수렴 조건을 이론적으로 입증 + 실험 입증
- 다른 도메인에도 쉽게 확장할 수 있음을 증명

# 2. RELATED WORK

제안된 모델은 

cross domain recommendation 과 deep learning based 두 가지 

## 2.1 Cross Domain and Transfer Learning-based
Recommendations

cross domain recommendation은 데이터 희소성 문제를 해결할 수 있는 강력한 방법

일반적으로 CMF, CDCF, CDF, 등을 사용

→ 서로 다른 패턴 사용자가 특정 도메인의 항목과 상호 작용하는 방식을 특징짓고 보조 도메인의 상호 작용 정보를 허용하여 대상 도메인의 권장 사항을 알린다고 가정

위처럼 이전의 방식은 두 도메인의 권장 성능을 동시에 향상 시킬 수 없음. 

## 2.2 Dual Transfer Learning

Transfer learning은 서로 다른 리소스에서 얻은 데이터가 다르게 분포되는 상황을 다룸

→ 공유하는 지식이 있다고 정의하고 latent feautre 공간을 공유해 학습하는 방식

이 당시에는 주로 NLP에서 사용되며 cross domain recommendation에서는 사용하기가 어렵다 

( 소스 도메인과 대상 도메인의 사용자 선호도 사이의 대칭적 상관 관계에 있기 때문에)

## 2.3 Deep Learning-based Recommendations

최근 딥러닝을 사용한 추천시스템이 많이 연구 중이며 auto encoder를 사용한 사용자와 아이템 간의 관계를 추출하는 연구가 진행중이다. 그러나 두가지 도메인을 동시에 사용하기 위한 접근은 하지 않고있다.

# 3. METHOD

![f2](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f2.png)

위 그림은 해당 연구에서 제안한 DDTCDR 모델 

1. autoencoder 기법을 이용해 feature embeddings을 진행 
2. embeddinge된 feature들을 latent orthogonal mapping을 진행
3. 도메인 내 및 도메인 간 사용자 기본 설정을 계산하고 권장 사항을 제공

이렇게 보면 이해가 안가니.. 순서도를 같이 보자![f4](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f4.png)

![f3](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f3.png)





## 3.1 Feature Embeddings

각 입력 데이터는 연속적인 입력을 받음 

![f5](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f5.png)

user feature를 잘 표현하기 위해 vae를 하는것을 보임 

인코더와 디코더를 통과 후 다시 원본 feautre를 잘 복원 했는지  확인

## 3.2 Latent Orthogonal Mapping

사용자의 선호를 소스에서 타겟 도메인으로 전송하기 위한 방법을 소개 

기본적인 가정은 두 사용자가 소스 도메인에서 유사한 선호도를 가지고 있다면 대상 도메인에서도 유사한 선호도를 가져야 한다. 

1. 직교 변환은 벡터의 내적을 보존하기 때문에 서로 다른 잠재 공간에서 사용자 임베딩 간의 유사성을 보존
2. Y = X^T (XY) 이 직교매핑 행력에서 유지되기 때문에 역 매핑 행렬이 X^T로 도출됨 

이 방식을 사용하면 모델의 복잡성을 줄일 수 있다고 함. 

- 사용자 선호도의 유사성을 보전하고 역매핑 함수를 효율적으로 계산
- ​

## 3.3 Deep Dual Transfer Learning

![f6](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f6.png)

두 도메인 간의 상호 작용을 통해 같이 학습하기 위한 추천 모델 수식 

첫번째 항은 도메인 내 사용자 선호도 두번 째 항은 서로 다른 도메인의 이질성을 포착하고 교차 도메인의 선호도를 측정 

여기에서 α = 0이 되는 경우 두 도메인 간의 사용자가 전혀 겁치지 않는다는 것을 의미 ( 실험적으로 0 ~ 0.2 의 값이 적당하다고 함  즉, 거의 겹치지 않는다고 해석)

## 3.4 Convergence Analysis

introduction 에서 말했던 전이 학습 메커니즘 사용시 인수 분해의 수렴 정리를 제시 

두 도메인 A와 B에 대한 등급 매트릭스를 각각 VA, VB로 표시

![f7](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f7.png)

reconstruction loss로 두 도메인의 추천 결과를 평가 

뜬금없이 나타난 H변수는 뭐지?

### 3.5 Extension to Multiple Domains

델이 두 도메인 간의 교차 도메인 권장 사항에도 작동할 뿐만 아니라 여러 도메인 간의 권장 사항으로도 쉽게 확장할 수 있음을 보임 

![f8](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f8.png)

Xjk : represents the latent orthogonal transfer matrix

다른 모든 도메인을 대상 도메인의 orthogonal 한 공간안에 매핑시겠다는 걸로 보임 

# 4. EXPERIMENT

![f9](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f9.png)

위 테이블은 논문에서 접근하는 3가지 도메인 설명 

## 4.1. Dataset

0과 1 사이의 등급 척도를 정규화

## 4.3. Baseline Models

RMSE, MAE, Preision, recall 을 기반으로 성능을 평가 

- CCFNet

교차 도메인 콘텐츠 강화 협업 필터링 신경망(CCCFNet)은 인수 분해를 활용하여 통합 다중 뷰 신경망과 함께 CF 및 콘텐츠 기반 필터링을 결합

- CDFM

교차 도메인 인수 분해 기계(CDFM)는 도메인 정보를 이 패턴에 통합하는 FM의 확장을 제안

- CoNet

CoNet(Collaborative Cross Networks)은 기본 네트워크 간 연결을 통한 도메인 간 지식 전송을 가능하게함

- NCF

신경 협업 필터링(NCF)은 협업 필터링 방법을 사용하여 사용자와 항목의 잠재적 기능을 모델링하는 신경망 아키텍처

# 5. RESULTS

![f10](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f10.png)

(a) 명시적 기능 대신 잠재 상호 작용에 대한 정보를 소스 도메인에서 대상 도메인으로 전송하고, 

(b) 이중 전송 학습 메커니즘을 활용하여 두 도메인에 대한 성능 측정을 동시에 개선하는 양방향 교육을 가능하게 한다는 점을 포함하여 몇 가지 이점을 제공한다.분석적으로

(c) 잠재 직교 지도 사용자 선호도를 학습하여 적절한 전송 학습을 가능하게 하고 (ii) 역 매핑 함수를 효율적으로 계산

# 참고

## 1. Orthogonal Mapping

- Orthogonal Matrix

Orthogonal Matrix는 정방행렬로 이것의 열과 행들은 Orthogonal (직교) 단위 벡터가 된다. 즉, Orthonormal Vector가 되는 것이다. 이것은 아래와 같은 관계를 가지면 된다.

즉, Q의 역행렬이 Q의 전치행렬이 되는 것 

![f11](\img\2022\DDTCDR__Deep_Dual_Transfer_Cross_Domain_Recommendation\f11.png)

1. 두 행렬이 직교 하게 매핑 한다면 벡터의 내적을 보존하기 때문에 임베딩간의 유사성을 보존 
2. 내적을 보존 ** → 즉 어떤 직교행렬 Q*x. Q*y 를 해도 내적이 유지된다

# 참조

1. cross domain recommendation 그림

논문 - ****Cross domain recommendation based on multi-type media fusion****

[https://www.semanticscholar.org/paper/Cross-domain-recommendation-based-on-multi-type-Tan-Bu/417db271a2e52cdd39c26975922c7a268b1a1ea9](https://www.semanticscholar.org/paper/Cross-domain-recommendation-based-on-multi-type-Tan-Bu/417db271a2e52cdd39c26975922c7a268b1a1ea9)

1. 직교행렬

[https://normal-engineer.tistory.com/92](https://normal-engineer.tistory.com/92)


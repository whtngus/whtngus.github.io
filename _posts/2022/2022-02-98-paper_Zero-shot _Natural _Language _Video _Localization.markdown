---
layout: post
title: "paper : Zero-shot Natural Language Video Localization"
date: 2022-02-07 16:20:23 +0900
category: paper
---

# Zero-shot Natural Language Video Localization



# Abstract 

비디오를 이해해 장면을 자연으로 바꾸기 위해 많은 영상과 데이터들이 필요하다.

제로샷 방식으로 자연어 비디오 지역화 모델을 교육하는 첫 번째 시도

감독되지 않은 이미지 캡션 설정에서 영감을 받아, 모델을 교육하기 위해 랜덤 텍스트 말뭉치, 레이블이 없는 비디오 컬렉션 및 기성품 객체 감지기가 필요

비지도 학습인 NLVL(natural language video localization) 모델을 제안 

 Charades-STA 및 ActivityNet-Captions에 대한 보다 강력한 감독을 사용하는 여러 가지 방법과 여러 기본 접근법을 능가



# 1. Introduction

natural language video localization (NLVL)은 최근 비디오의 순간 장면에서 자연어와 함께 이해하는것이다.

최근 몇년간 많은 성능적 성장을 했고 데이터 셋 또한 많이 생성됬다 

![f_1](E:\code\whtngus.github.io\img\2022\Zero-shot_Natural_Language_Video_Localization\f_1.PNG)

위 Figure 1은 데이터셋에 대한 예시이다 

영상의 각 장면에 대한 데이터에 대한 설명 이다.

그러나 위와 같이 각 영상의 장면 쌍으로 구성된 데이터를 얻는 것은 힘들고 비용이 많이 든다.

NLVL은 이를 해결하기 위해 주어진 문장의 시간적 정렬 없이 순간을 localize 하는것을 목표로 한다.

위 그림의 b에서 처럼 질의 문장의 시작과 긑을 비디오로 지정하는 방법이 있으나 자연어 질의에 주석을 다는것은 여전히 비용이 많이 든다.

영상에서 장면과 연결되지 않은 데이터에 객체 디텍션과 텍스트를 통해 지식을 추출하고 (c)

-> (c) 방법과 (b)방법을 통해 (d) 방법을 제안한다.



NLVL 모델은 비디오및 문장에서 후보 시간 영역에 대한 학습을 한다.

위 방법의 장점은 학습하기 위한 생성된 문장과 위치를 제공한다. 또한,  태깅 비용을 감소시킨다.

-> 손쉽게 지도학습과 같이 학습할 수 있다??? 

NLVL은 두 가지를 학습한다

1) 쿼리할 수 있는 의미 있는 시간 영역을 찾는 것
2) 발견된 시간 영역에 대한 해당 쿼리 문장을 얻는 두 가지 과제

가능한 시간 영역을 찾기 위해 시각적 정보를 클러스터링할 것을 제안

프레임에 보이는 명사를 찾고 언어 말뭉치의 명사-동사를 예측

명사와 동사의 집합을 유사질의라고 정의(off-the-shelf object detector)

시간적 영역 제안과 의사 쿼리 생성을 가진 NLVL 모델을 유사 감독 비디오 로컬라이제이션 또는 PSVL이라 부른다.

### 컨트리뷰션

- zero-shot NLVL task
- pseudo supervising framework PSVL
- NLVL 모델을 제안
- 베이스라인 모델은 제로샷 기준



# 2. Related Work

## Natural language video localization.

 NLVL 연구는 요리 사건만 연구하는 등 상대적으로 제한된 환경을 연구

최근에는 Charades-STA, ActivityNetCaptions -> (** 논문 찾아보기) 연구에서 딥러닝 기법이 사용되며 진보되고 있다.

NLVL에 대한 라벨링은 비용이 많이 들기 때문에 일부 문헌은 시간적 사건 주석을 완화하기 위해 NLVL-(WS-NLVL)의 세미 감독된 설정을 다룬다.

 ## Action recognition without annotation.

라벨링 없이 시간에 대한 행동을 분류하기 위한 제로샷 연구가 기존에도 존재하며,

객체 - 행동 공동 패턴을 이용해 학습도 함. -> 유사 쿼리 생성과 유사성을 공유

그러나 위 연구들은 대상 데이터 세트에 대해 주석을 달아야 하고, 행동 범주를 미리 정의해야 하며, 지상 진실 사건 영역에 따라 비디오를 이미 잘라내야 한다고 가정 -> 많은 라벨링 시간이 필요

또한 행동 인식 모델은 쉽게 큰데이터를 학습할 수 있는것 처럼 보이지만 개인정보의 잠재적인 문제가 있으며 약한 라벨학습 가정으로한다.(라벨링 된 데이터가 있어야 함)

숨로? 가 비디오 수집만을 사용하여 조치를 국소화하기 위한 비지도 행동 발견 과제를 제안

행동 클래스가 미리 정의되어 있다고 가정하고 조치를 언어 쿼리와 관련시키는 것을 고려

## Grounded language generation. 

레이블이 없는 데이터에서 자연어 문장을 생성하는 것은 쿼리 제너레이션이랑 유사하다.

지도학습 없는 기계번역 모델을 다른 연구들 또한 있다.

객체 감지기와 독립적인 이미지 및 문장 세트를 사용하여 이미지 캡션을 훈련

 제로샷 NLVL은 기성 객체 감지기와 독립적인 비디오 및 문장 세트를 사용

# 3. Approach

![f_2](E:\code\whtngus.github.io\img\2022\Zero-shot_Natural_Language_Video_Localization\f_2.PNG)



지도 학습에는 두 가지 양식에 대한 쌍으로 구성된 학습이 필요하지만,  논문에서는 두 가지 양식에 대한 쌍의 데이터를 제공하지 않는다.

대신 텍스트 말뭉치와, 비디오 컬렉션 및 객체탐지 를 이용해 유사 감독학습을 통해 문제를 해결하고자 한다.

-> 이 프레임 워크를 PSVL(Pseudo-supervised Video Localization) 이라고하고 위 그림2와 같다.

- 프레임워크 구성

> 1. 시간적 사건 제안
> 2. 응답을 생성
> 3. NLVL model 사용
>
> (위 figure 2 그림의 좌측 순서 설명)



 









# 참고지식

-












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












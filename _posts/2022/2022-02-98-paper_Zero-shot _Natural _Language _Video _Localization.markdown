---
layout: post
title: "paper : Zero-shot Natural Language Video Localization"
date: 2022-02-16 00:20:23 +0900
category: paper
---

# Zero-shot Natural Language Video Localization

url : https://arxiv.org/pdf/2110.00428.pdf

code : https://github.com/gistvision/PSVL

ICCV 2021







# Abstract 

비디오를 이해해 장면을 자연으로 바꾸기 위해 많은 영상과 데이터들이 필요하다.

제로샷 방식으로 자연어 비디오 지역화 모델을 교육하는 첫 번째 시도

감독되지 않은 이미지 캡션 설정에서 영감을 받아, 모델을 교육하기 위해 랜덤 텍스트 말뭉치, 레이블이 없는 비디오 컬렉션 및 기성품 객체 감지기가 필요

비지도 학습인 NLVL(natural language video localization) 모델을 제안 

 Charades-STA 및 ActivityNet-Captions에 대한 보다 강력한 감독을 사용하는 여러 가지 방법과 여러 기본 접근법을 능가



# 1. Introduction

natural language video localization (NLVL)은 최근 비디오의 순간 장면에서 자연어와 함께 이해하는것이다.

최근 몇년간 많은 성능적 성장을 했고 데이터 셋 또한 많이 생성됬다 

![f_1](\img\2022\Zero-shot_Natural_Language_Video_Localization\f_1.PNG)

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

![f_2](\img\2022\Zero-shot_Natural_Language_Video_Localization\f_2.PNG)



지도 학습에는 두 가지 양식에 대한 쌍으로 구성된 학습이 필요하지만,  논문에서는 두 가지 양식에 대한 쌍의 데이터를 제공하지 않는다.

대신 텍스트 말뭉치와, 비디오 컬렉션 및 객체탐지 를 이용해 유사 감독학습을 통해 문제를 해결하고자 한다.

-> 이 프레임 워크를 PSVL(Pseudo-supervised Video Localization) 이라고하고 위 그림2와 같다.

- 프레임워크 구성

> 1. 시간적 사건 제안
> 2. 응답을 생성
> 3. NLVL model 사용
>
> (위 figure 2 그림의 좌측 순서 설명)

## 3.1. Temporal Event Proposal

![f_3](\img\2022\Zero-shot_Natural_Language_Video_Localization\f_3.PNG)

첫 단계로, 비디오에서 시간적 영역의 사건을 발견 

-> 의미 있는 시간적 세그먼트의 개념을 어떻게 정의하냐가 핵심 

논문에서는 시간적 영역에서 의미있는 이벤트를 선택할 수 있다고 가정하고 비디오의 프레임별 CNN 특징이 사건 경계에서 갑자기 변화한다는 가설을 새움 

 위 그림 3의 a에서 글로벌 컨텍스트를 통합하기 위해 유사한 전역 정보를 열 벡터를 사용을 통해 인코딩 할것을 제안 (k-means를 사용해 상황벽 특징을 클러스터링해 특징을 발견)

복합 이벤트를 생성하기 위해 연속 이벤트의 모든 조합을 채운 다음 균등 분포를 따라 몇 개 샘플을 추출 

## 3.2. Pseudo-Query Generation

![t_1](\img\2022\Zero-shot_Natural_Language_Video_Localization\t_1.PNG)

시간적 영역 - temporal regions (TEP)

3.1 과정을 통해 발견된 TEP에 해당하는 자연어를 생성

위에서의 가정은

1) 쿼리는 시간 영역에 시각적으로 기초해야 하며

2. 쿼리는 의미적으로 자연스러워야 한다.

이 방식을 사용하려면 지도학습이 필요한데 지도학습을 사용하지 않는다고 했으니 위 방식은 사용 불가능

### Simplified sentence.

데이터를 사용하지 않는 대신 semi supervised learning을 위해 아래와 같은 학습법을 제안

객체 감지를 통해 기초 명사를 사용하고, 언어 말뭉치에서 예측되는 동사를 추출 (코퍼스 문장에서 해당 단어와 자주 쓰이는 동사를 추출하는것으로 보임)

이 렇게 학습한 결과를 위의 Table 1을 통해서 보여줌 

원본(자연적) 질의 문장과 해당 간결 문장으로 훈련된 모델의 성능 -> 생각보다 성능이 비슷한게 놀랍다 

생성된 문장들을 봐야 할것 같다.

### Nouns

이미지에서 객체탐지를 이용한 태그에서 이미지캡셔닝을 하는 모델에서 아이디어를 얻음.

연구에서는 상용 객체 탐지 모델을 이용해 프레임에서 명사를 추출

(여기에서 사용된 모델은 해당 영상을 학습한 모델이 아님  - 비지도 학습 컨셉을 확실히 잘 지키는 걸로 보인다.)

-> 결국은 그래서 객체탐지 모델의 정확도가 비교적 높지 않다.

이러한 안좋은 명사가 추출되는걸 막기 위해 스코어가 높은 상위 N개를 추출해서 사용 

### Verbs

동사를 예측하기 위해 pre-trained된 행위 인식 모델을 사용, 그러나 비디오의 다양한 이벤트를 다루기에는 아직 부족함.

zero-shot 의 대안으로  모델에서 결국 이미지에서 추출된 명사에 의존할 것으로 볼 수 있다

ex) 공 야구배트 사람 의 객체가 추출된 경우 히팅 달리기 등의 동사를 예상할 수 있다.

위의 가정에 기초해서, 명사-동사 공존 패턴을 학습 후 문맥 객체에서 가능한 동사를 추론

-> 당연히 실제 상황과는 부정확 할 수 있음!

![f_4](\img\2022\Zero-shot_Natural_Language_Video_Localization\f_4.PNG)

이런 동사-명사 패턴을 추론하기 위해 RoBERTa 모델을 베이스로 문맥 목적 명사에서 동사만을 추론하는 모델을 학습한다 이를 Verbert라고 한다. 

VerbBERT 모델은 동사를 예측하는 모델! (예시는 위의 Figure 4)

## 3.3. A simple NLVL Model

![f_5](\img\2022\Zero-shot_Natural_Language_Video_Localization\f_5.PNG)

지도학습을 통해 NLVL 모델을 사용할 수 있지만, 덜 구조화된 문장(생성 문장)을 사용하기 때문에 적합한 NLVL 모델을 추가로 제안 

그림5 처럼 문장 구조를 덜 학습하고 단어 프레임을 더 집중하는 교차 모달 신경망을 제안 

모델 구성

1. 비디오 및 단순화된 문장 입력 데이터를 전역적으로 인코딩하기 위한 상황별 특징 인코딩
2.  multi-modal cross attention network
3. 입력 단순 문장에 해당하는 시간적 사건 영역을 회귀시키기 위한 시간적 회귀

위에서 multi-modal cross attention network는 비디오와 언어 사이의 다중 모드 정보(Words-aware Video Attention, WVA)와 비디오 인식 쿼리 임베딩(Video-aware Words Attention, VWA)을 융합한 쿼리 유도 동적 필터를 사용하고 멀티 모드 크로스 모드를 사용

모든 정보를 융합하기 위한 고정 메커니즘(다중 모드 교차 주의 또는 MCA). 그런 다음 비로컬 블록(NL-블록)[51]을 적용하여 교차 주의 모듈에서 얻은 전역 상황별 정보를 인코딩한다. 전역 컨텍스트 특징이 서로 인코딩된 후, 우리는 시간 주의 메커니즘에 의해 대상 시간 세그먼트를 살펴본다. 마지막으로, 우리는 다층 퍼셉트론을 통해 시간 경계 영역을 예측한다.

### Objective function

![f1](\img\2022\Zero-shot_Natural_Language_Video_Localization\f1.PNG)

두가지 로스로 구성됨

1. 시간 경계 회귀 손실 - reg
2. 시간 attention 손실 - guide

λ 는 균형 파라미터 

### Inference

학습시에 단순화된 문장을 이용해 학습하기 때문에 예측 시에도 질의어를 단순화된 문장으로 변환해야 함 

이때 형태소 태깅을 사용해서 단순화 

-> 문장 생성 이부분이 수정사항이 보임 

# 4. Experiments

### Datasets and setups.

 NLVL 작업에 Charades-STA 및 ActivityNetCaptions 의 두 데이터 세트를 사용

객체 검출기로 사용되는 Visual Genome 데이터 세트와 licker 설명 말뭉치의 1,600개 객체 범주로 훈련된 사전 훈련된 고속 R-CNN제공

### Evaluation metrics.

 (R@tIoU). 를 사용 (we use threshold values of {0.3, 0.5, 0.7}

### Implementation details

 I3D 및 C3D 모델을 각각 사용하여 각 프레임에 대한 시삭적 특징을 추출

비디오 기능을 고정 길이로 만들기 위해 비디오에서 128개의 기능을 균일하게 샘플링

두 데이터 세트에 대한 k-벡터 클러스터링 알고리즘에 k = 5를 사용

### Baselines.

제로샷 NLVL을 다루는 첫 번째 작업이기 때문에

1. 무작위 영역 예측
2. 무작위 이벤트 제안(Rand. Q+TEP)
3. 무작위 시간 영역에 대한 유사 쿼리(PQ+Rnd)로 훈련된 모델과 같은 PSVL의 절제 방법을 포함한 다양한 기준선을 고려
4. TEP(PQ)에서 '근거 명사'(랜덤 동사)를 사용한 의사 질의만 가능합니다.N+TEP
5. TEP(PQ)에서 '추천 동사'(랜덤 명사)를 사용한 유사 질의만 가능합니다.V+TEP). 우리는 동일한 NLVL 모델을 사용

## 4.1. Quantitative Analysis

![t_2](\img\2022\Zero-shot_Natural_Language_Video_Localization\t_2.PNG)

위의 표 2와같이 간단히 결과 간단히 요약

- 이벤트 제안 모듈을 TEP(Temporary Event Proposal)로 대체하고 랜덤 쿼리를 제공하면 랜덤에 비해 NLVL 작업 성능이 약간 향상

-> 좋은 의사 쿼리가 없으면 NLVL 성능이 저하될 수 있음을 의미

- PQ에 의한 설명은 모델이 몇 가지 교차 모달 표현을 학습할 수 있음을 의미한다. PQ를 비교할 때.N+TEP 및 PQ.V+TEP, 우리는 동사가 NLVL 성능에 대한 명사보다 더 중요한 역할을 한다는 것을 관찰한다. 우리는 이것이 동사가 시간 영역을 설명할 때 문맥 객체 간의 관계를 포함하기 때문

### 4.1.1 Temporal Event Proposal

#### Event proposal methods

![t_3](\img\2022\Zero-shot_Natural_Language_Video_Localization\t_3.PNG)

위으 table 3에서 4개의 베이스 라인 모델과 비교 

#### 4.1.2 Pseudo Query

##### Effectiveness of VerbBERT.

동사 예측 변수인 VerbERT를 RoBERTa를 이용해 만듦

table 4에서 성능을 비교 해 볼 수 있음 (당연히 동사만을 이용해 학습했으니 좋아지는건 확실)

명사의 품질에 따라 얼마나 성능이 안좋아지는지를 확인하기 위해 테스트를 함 

중복이 감소하면(36.54% → 27.48% → 17.97% → 9.64% → 1.15%) NLVL 'R@0.5' 성능도 감소합니다(31.88 → 31.09 → 28.25 → 25.94 → 23.82).

#### 4.1.3 NLVL Model

![f_6](\img\2022\Zero-shot_Natural_Language_Video_Localization\f_6.PNG)

![f_7](\img\2022\Zero-shot_Natural_Language_Video_Localization\f_7.PNG)

![t_5](\img\2022\Zero-shot_Natural_Language_Video_Localization\t_5.PNG)

Table 5 에서  WVA, VWA 및 MCA를 단순 완전 연결 레이어로 대체하여 세 개의 모델을 비교

 WVA의 결과는 Attention 모듈이 주어진 시간 영역에 대해 실제로 의미 있는 단어에 주의를 기울임으로써 의사 쿼리의 노이즈를 추가로 필터링한다는 것을 의미

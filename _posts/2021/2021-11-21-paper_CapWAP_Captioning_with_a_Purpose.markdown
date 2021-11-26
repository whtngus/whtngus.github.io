---
layout: post
title: "paper : CapWAP: Captioning with a Purpose"
date: 2021-11-25 19:20:23 +0900
category: paper
---



#  CapWAP: Captioning with a Purpose

학회 - EMNLP 2020

소속 - csail.mit.edu

게재 - 9 Nov 2020

url - https://arxiv.org/pdf/2011.04264.pdf



# Abstract

기존 이미지 캡션 작업은 일반적인 참조 캡션을 사용해 이미지에 대한 텍스트 정보를 제공한다.

즉 이미지의 다른 시각적 관점에만 집중하게 된다 (어떤의미진지는 뒤에서 이어서 설명)

-> 의도된 인구의 정보 요구에 맞게 조정될 수 있는 시스템을 개발하는 것

이를 해결하기 위해 CAPWAP(Caption with a Purpose)를 제안



 질문 답변 모델이 샘플링된 사용자 질문에 대한 정답을 제공할 수 있는 출력을 보상함으로써 강화 학습을 사용하여 의도된 정보 요구에 맞게 직접 최적화할 수 있음을 보여준다.



# 1. Introduction

![f_1](\img\2021\CapWAP_Captioning_with_a_Purpose\f_1.PNG)



일반 이미지 캡션의 경우 명확하지 않고 VQA는 질문에 대한 정보만을 제공함.

해당 논문에서는 

 (1) 일반 주석이 사용자의 정보 요구를 대표하지 않을 수 있고, 

(2) 사용자 질문이 정보 요구를 명확히 표현하는 더 자연스러운 방법이며, 

(3) 그러한 질문에 대한 정확한 답을 제공하기 위해 캡션을 최적화하면 훈련이 정보 요구에 집중할 수 있다고 주장

![t_1](\img\2021\CapWAP_Captioning_with_a_Purpose\t_1.PNG)

1. 서로 다른 대상 사용자층이 표현하는 특정 정보 요구를 충족하기 위해 이미지 캡션을 생성하는 새로운 작업(CAPWAP)을 정의한다. 
2. 우리는 우리의 정보 중심 모델이 최첨단 기존 일반 캡션 시스템의 캡션보다 이 작업에 대해 훨씬 더 높은 품질의 캡션을 생성할 수 있음을 보여준다. 
3. 우리는 이 새로운 패러다임 하에서 강화 학습의 성능을 크게 향상시키는 새로운 합성 사전 훈련 루틴을 제안한다.

# 2. Related Work

사용자의 질문에 의해 표현된 정보 요구에 의존하여 보다 경험적인 접근법을 취한다.

빈번한 문구를 삭제하는 등 체계적인 사용적합성 문제로 어려움을 겪고 있다고 관찰했다

정보 품질을 평가하기 위해 QA를 사용하는 아이디어는 텍스트 요약을 위한 최근 연구에서 제안되었다

# 3. Problem Formulation

![f_2](\img\2021\CapWAP_Captioning_with_a_Purpose\f_2.PNG)

- Task Setting

x : 임력 이미지

y : 캡션 

D : 샘플링된 질문-응답 쌍 (q-a)

- Information Need

QA 데이터가 아래와 같은 프로세스에 의해 도출된다고 가정

> 1. 이미지 x는 분포 p(x)에서 도출
> 2. D에서 사용자에게 중요한 것으로 인식되는 x의 정보 세부 사항을 대상으로 하는 (q,a)은 분포 p(q, a|x) 에서 도출됨
>
> (q,a) 쌍에 대한 한계 분포가 일반적인 사용자의 시각적 관심을 나타낸 것 

- Question Anticipation

완벽한 정답셋이 있다고 가정하지 않음

캡션 y는 잠재 변수이고 G(y|x)는 우리가 배워야 할 확률적 생성기라고 가정(완벽한 정답이 없기 때문에)

표본 y ~ G(y|x)는 무작위로 샘플링된 새로운 질문-응답에 대해 상황별로 제공해야 함 

논문에서는 y를 q에 대한 컨텍스트로 사용할 때 사전 훈련된 QA모델 M(q, y)의 정확도를 사용해 추정한다.

CAPWAP는 아래 기대치를 최대화 해야한다

![f1](\img\2021\CapWAP_Captioning_with_a_Purpose\f1.PNG)

θ  : 파라미터 

R(y, q, a) : 리워드 

M(q, y) : output을 비교하기 위해 사용

- CapWAP vs. Other Tasks

표 1은 표준(일반) 캡션 및 시각적 질문 답변의 설정과 비교

VQA와 CAPWAP 모델은 QA 데이터로 교육 및 평가되지만, CAPWAP는 생성 전에 질문을 제공하지 않는다. (즉 질문 없이 이미지의 포인트인 답변을 캡션 하는것)

VQA 모델은 단일 답변을 출력하는 반면, CAPWAP 모델은 예상 컨텍스트를 출력 -> 모든 답변을 출력하기 위해 

# 4. An Approach to CAPWAP

훈련 중에 질문-답변 쌍에만 접근할 수 있고 추론 중에는 접근할 수 없다는 것을 고려할 때, 우리는 이 과제에 대한 모델을 어떻게 배울 수 있는가?

-> 이를 해경하기위해 강화학습을 사용

델이 생성된 각 캡션 y와 교육 QA 쌍(q, a)에 대해 보상 r(예: r = R(y, q, a)을 받는 강화 학습(RL) 프레임워크에 자연스럽게 부합

그러나 이러한 정책을 최적화하는 것은 모델이 처음에는 드문 사건인 정답(또는 부분적으로 정답)에 대해서만 보상을 받기 때문에 기술적인 문제를 제기



해당 논문에서는 아래와 같은 방법을 따름

1. 지도학습을 이용해  Gθ(y|x)를 학습해 파라미터를 생성 ( x^, y^) ~ D
2. Fine-tune G(y|x) QA data , (x, q, a) ∼ Dtarget.

D(generic)은 의도된 캡션 목적인 Dtarget에 대해 도메인 밖에 있는 것으로 가정

다양한 사용자 생성 질문과 정보 요구에 관심이 있기 때문에 일반적인 캡션 데이터는 종종 최종 목표와 크게 다를 수 있다. 



### 4.1 Model Architecture

이미지 캡션 시스템에서 공통되는 시퀀스 투 시퀀스 프레임워크를 따라 고속 R-CNN 및 트랜스포머 기반 인코더-디코더로 구성된 기본 캡션 모델을 간략하게 설명 (sota 모델 사용)

이미지 x가 주어지면, 우리는 먼저 사전 훈련된 고속 R-CNN 모델(Anderson 등, 2018)에서 계산된 탐지된 객체 경계 상자 임베딩 시퀀스로 나타낸다 -> 그다음 Transformer 기반 모델을 사용해  캡션 워드피스 y = (y1, . . . , yn)를 생성

### 4.2 Policy Training

QA 데이터를 사용하여 캡션 모델을 교육하기 위한 RL 프레임워크를 설명

Gθ(y|x)  MLE을 사용해 최적화

![f2](D:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\f2.PNG)

- QA Model

SQuAD 2.0에 쓰인 BERTLARGE모델을 이용해 모델 M을 구축 

-> no answer 대답도 하기 위해서

- QA Reward

![f3](D:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\f3.PNG)

QA의 보상정책으로 기울기 LQA를 계산하기 위해 REPORINCE(Williams, 1992년)를 사용

 b를 R(y,, q, a)로 받아들인다. 

### 4.3 Synthetic Policy Pre-Training

![f_3](D:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\f_3.PNG)



생성된 캡션은 일반적으로 많은 질문에 올바르게 답변하지 않아 보상 신호가 거의 없다. (거의 틀려 리워드가 없다는 듯)

, 정책 G((y|x)가 잘 초기화되지 않은 경우 보상은 희박하다.  -> 초기값에 영향을 크게받는 불안정함을 보임 

그 대안으로 안내된 정책 검색의 한 형태로 높은 보상으로 캡션 Dsynthetic의 합성 데이터 세트를 생성하는 방법을 도출한다(Levine and Koltun, 2013). 

런 다음 전체 방법은 세 가지 데이터 세트에 대해 훈련하는 세 단계로 구성된다. Dgeneric → Dsynthetic → Dtarget.



 QA 모델이 긍정적인 보상을 얻으려면 답은 캡션의 한 구간이어야 한다. 

- QA Conditional Model

![f4](D:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\f4.PNG)

답변 범위를 지원하는 캡션을 생성할 때 QA 쌍을 명시적으로 조절

y는 M(y, q) = a를 만족

어렵따..

- Synthetic Data Generation

고정 가중치와 함께 전송하여 대상 QA 데이터 세트의 참(x, q, a, null) 예를 사용하여 역 엔지니어링된 캡션 y를 생성

beam search를 사용하고 점수가 높은 캡션쌍으로 구성된 데이터 세트 Dsynthetic을 만듦

# 5. Experimental Setup

- Evaluation

1차 평가는 이미지에 대한 질문과 답변의 데이터 세트를 가정

- Automatic Evaluation

생성된 캡션을 "맥락"으로 하여 주어진 QA 쌍에 적용되는 SQuAD 2.0.3에 추출 질문 답변 모델(M)을 활용

겹치는 단어를 기준으로 F1을 보고 측정

- Human Evaluation

평가자에게 질문-응답 쌍과 관련하여 캡션이 다른 캡션보다 덜, 같은, 더많은 정보를 판단하도록 함 

유창성(캡션이 문법적이고 일관성이 있는지 여부), 충실성(캡션이 이미지에 있는 내용에 대해 잘못된 주장을 하는지 여부)

### 5.1 Datasets

질문가능 비가능 과 알파벳 아닌 질문을 평가

사용 데이터셋

- COCO
- CapVQA
- CapGQA
- CapVisual7W
- CapVizWiz

### 5.2 Generic Captioning Models

CiDer손실과 다른 캡션생성 손실을 최적화 함 

# 6. Results

![t_2](D:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\t_2.PNG)

CAPWAP에 대한 접근 방식과 QA를 사용하여 프로세스를 추진하는 데 따른 광범위한 가정, 장점 및 제한과 관련된 몇 가지 주요 연구 질문을 다룸

- Evaluation of Generic Captions

이 논문은 일반적인 참조 캡션에 대한 교육이 다양한 사용자별 정보 요구를 제대로 반영하지 못할 수 있다는 도입 주장을 경험적으로 검증하는 것으로 시작

표 2는 예측 캡션이 다른 분포에 대한 QA를 얼마나 잘 지원하는지 평가할 때 기준 일반 캡션 시스템의 결과를 제시

OCO 벤치마크에서 측정한 강력한 방법이지만, 놀랍지 않게도 다양한 시각적 질문에 답하는 데 필요한 모든 정보를 캡처하지 못한다. CapVizWiz의 성능은 매우 저조합니다. 시각 장애가 있는 사용자는 COCO에서 나타내는 것과 현저하게 다른 정보를 요구합니다. 이 저조한 성능의 원인은 현재 최신 모델의 단순한 한계를 넘어선다. 대상 자체가 불충분하다. 예를 들어 COCO와 이미지가 겹쳐서 인간 캡션을 직접 사용할 수 있는 CapVQA에서는 이러한 "골드" 참조의 평균 성능이 약간 더 우수할 뿐

- Adaptation to Information Need

데이터 세트에 의해 규정된 특정 정보 요구에 맞게 캡션을 조정할 때 제안된 접근 방식의 효과를 테스트

표 2의 결과는 네 가지 데이터 세트 모두에서 QA 주도 모델(RL 및 RL + SYN)이 크게 개선되어 평균 8.0 절대 F1의 이득을 달성했음을 보여준다. 특히, 우리는 CapVQA의 평균 인간 캡션보다 7.5 EM, CapVizWiz의 최상의 일반 모델에 비해 16.5 EM 향상된다. 표 4는 적응 프로세스가 실제로 각 QA 데이터 세트에 맞춰져 있음을 보여준다. (프록시 모델 M 사용) 자동 QA 기반 메트릭의 개선은 인간의 판단으로도 해석된다. 표 3은 제안된 모델과 MLE 기준선에 대한 HU-man A/B 테스트 결과를 보여준다. MLE에 비해, 우리는 우리의 방법이 모든 데이터 세트에 걸쳐 보이지 않는 QA 쌍과 관련하여 훨씬 더 많은 정보를 제공한다는 것을 발견했다. 예상대로, 가장 큰 개선 사항은 일반 COCO 콘텐츠(예: CapVizWiz)에서 크게 벗어난 데이터셋이다.

![t_3](D:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\t_3.PNG)

- Importance of Synthetic Pre-training

QA 기반 보상의 부족은 텍스트 유창성을 명시적으로 시행하지 않거나 관련이 없거나 사실이 아닌 콘텐츠가 생산될 때 시스템에 불이익을 주지 않는다

참조 캡션을 사용할 수 있으면 유창한 언어 모델을 쉽게 배울 수있다고 주장함 

표 5는 Dgeneric과 고려된 각 Dtarget 사이의 격차를 해소하기 위해 보조 QA 조건부 모델 F,(y|x, q, a)(§4.3)의 합성 유도 은 표본을 통합하면 QA 보상만으로 교육에서 발생하는 유창성과 섬망 문제를 크게 줄일 수 있음을 보여준다. 그러나 표 6은 참조 훈련 MLE 기준선에 비해 우리 모델이 여전히 이러한 2차 지표에 어려움을 겪고 있음을 보여준다. 이는 텍스트 생성을 위한 거의 모든 비교 가능한 RL 기반 방법(예: Guo 등, 2018; Paulus 등, 2018 등)과 공유되는 과제이다. 보완적 유창성 보상을 통합하는 것(예: 사전 훈련된 언어 모델 복잡성을 통해)은 향후 작업을 위한 귀중한 방향이다.

![t_4](D:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\t_4.PNG)

- Qualitative Discussion

CapVizWiz 질문은 긴 형식일 수 있으며 SQuAD와 상당히 다를 수 있으며, 사전 훈련에 F)를 사용하는 역엔지니어링이 더 노이즈적이다(표 5의 +SYN 성능에서 입증됨). 다른 데이터 세트의 인위적인 설정은 이상적이지 않지만, 그 다양성은 우리의 접근 방식의 유연성을 입증하는 역할을 한다.

- Ablation Studies

표 7과 8은 RL 및 RL + SYN 모델에서 다양한 설계 선택의 영향을 보여준다. 표 6에서 설명되고 설명된 것처럼 CAPWAP 시스템의 중요한 과제는 유창성을 유지하면서 정보 요구를 학습하는 것이다. 표 7은 합성 사전 훈련이 어떻게 모델을 정규화하여 인간 수준의 생산 패턴에 더 가깝게 유지하는지 보여준다. 마찬가지로, 표 8은 QA 모델을 사용하여 (단순 키워드 검색이 아닌) 보상을 제공하는 방법을 보여줍니다.

- Future Work

CAPWAP 패러다임은 효과적인 시스템을 학습하기 위한 새로운 과제를 도입하는데, 그 중 일부는 우리의 접근 방식이 해결되고 다른 것들은 여전히 열려 있다(예: 유창성과 신뢰도 유지). 일부는 대규모 다중 모델 모델(Li 등, 2019; Tan and Bansal, 2019)로 다룰 수 있지만, 실제 사용자가 관심을 갖는 정보의 다양성을 완전히 커버할 수 있을지는 여전히 불확실하다(예: OCR)

# 7. Conclusion

사용자가 제공한 질문-응답 쌍을 시각적 정보 요구를 학습하기 위한 감독 소스로 사용하는 CAPWAP 작업을 정의하고 연구했다. 우리의 결과는 대상 청중의 일반적인 QA 쌍에 대한 답변을 논리적으로 지원하는 능력에 의해 캡션 콘텐츠를 측정하는 것이 (1) 실현 가능할 뿐만 아니라 (2) 정보 요구를 파악하는 데 좋은 대용치라는 것을 나타낸다. 우리는 이 작업이 이미지 캡션 분야가 특정 사용자 커뮤니티의 정보 요구를 예측하고 제공하는 방법을 배우도록 동기를 부여하기를 바란다.

![a_1](D:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\a_1.PNG)
























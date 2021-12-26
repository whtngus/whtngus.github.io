---
layout: post
title: "paper : Robustness Evaluation of Transformer-based Form Field Extractors via Form Attacks"
date: 2021-12-26 16:20:23 +0900
category: paper
---

# Robustness Evaluation of Transformer-based Form Field Extractors via Form Attacks

Subjects:	Computer Vision and Pattern Recognition (cs.CV); Artificial Intelligence (cs.AI)

소속 : Salesforce Research, Palo Alto, USA -> 캘리포니아 팰로앨토의 연구소

url : https://arxiv.org/abs/2110.04413

# Abstract

OCR 위치/순서 재배열, 양식 배경 조작 및 양식 필드 값 확대를 포함하여 OCR 수준과 양식 수준 모두의 양식 공격에 대한 최첨단 필드 추출기의 취약성을 평가하기 위해 14개의 새로운 형태 변환을 소개

송장 및 영수증을 사용하여 건전성 평가를 수행하고 종합적인 연구 분석을 수행

현장 추출기의 설계와 데이터 수집 프로세스를 개선하기 위한 권장 사항을 제시

# 1. Introduction

![f_1](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\f_1.PNG)

형태 이해를 바탕으로 자동으로 현장 값을 추출하는 방식을 개발하는 것이 인적 노동을 줄여 업무 효율을 높이는 데 매우 중요

첫째, 대부분의 방법은 내부 데이터 세트를 사용하여 평가

-> 일반적으로 매우 제한된 편차를 가지며 데이터 수집 프로세스의 제약으로 인해 특정 데이터 분포에 편향되는 경우가 많다.

실제 양식은 대개 고객의 개인 정보를 담고 있어 공개적으로 접근할 수 없기 때문에 매우 어렵다. 

형태 변환을 사용하여 모델을 공격함으로써 양식 필드 추출기의 견고성을 평가하는 새로운 프레임워크를 제안한다. 

14가지 형태 변환이 제안

제안된 프레임워크를 사용하여 일반적으로 사용되는 두 가지 양식 유형, 즉 송장과 영수증에 대한 견고성 분석을 수행한다.

# Related Work

- Information extraction from forms

Reisswig(2019) 양식의 각 페이지를 2차원 그리드로 인코딩하고 완전한 컨볼루션 네트워크를 사용하여 그것에서 헤더와 라인 항목을 추출

DocStruct(Wang 등, 2020)는 텍스트 조각의 그래프와 같은 계층 구조로 인코딩하여 문서 구조 추론을 수행

작업에 대한 뛰어난 예측 능력을 고려할 때 트랜스포머 기반 필드 추출 방법을 평가하는 데 중점을 둔다.

- Robustness evaluation

모델의 건전성 평가는 상당한 관심을 받았다.

Erudite(Wu 등, 2019)는 NLP 모델의 정보 오류 분석을 위해 모델 및 작업 불가지론 원칙을 도입

Ma (2019)는 모델 견고성을 개선하기 위한 간단한 텍스트 증가를 포함하는 NLPAug를 제안

시각적 모델의 건전성을 연구하는 최근 방법도 있다(Santurkar 등, 2020; Salman 등, 2020; Taori 등, 2020).

# 3 Preliminary: Transformer-based Form Field Extractor

표준 필드 추출 시스템에서 OCR 엔진은 단어 집합 {w1, w2, ..., wN }과(와) 해당 경계 상자 위치 {b1, b2, ..., bN }을(를) 추출하는 데 사용

N은 총 단어 수

텍스트 토큰 간의 상호 작용을 모델링하고 유용한 토큰 표현을 생성하기 위해 트랜스포머 기반 기능 백본을 사용

의미론과 레이아웃은 필드 값 추론을 위해 필수적이기 때문에, 우리는 레이아웃을 사용

백본으로 LM(Xu 등, 2020). 또한 부록에서 텍스트를 입력으로만 받아들이는 BERT(Devlin 등, 2019)와 RoBERTa(Liu 등, 2019)의 두 가지 트랜스포머를 사용

(FC) 레이어는 필드 공간에 토큰 피쳐를 투영하고 si = F C(Fi)를 생성하는 데 사용됩니다.

si ≤ R1×(M+1)는 예측 필드 점수를 나타내고 M은 양의 필드 총 수를 나타냄

si와 필드 라벨 사이의 교차 엔트로피 손실이 모델 최적화를 위해 사용
 
(1) 우리는 Δf d = argmax c (c)에 의한 각 단어에 대한 예측 필드 레이블을 찾는다

c는 기본적으로 필드 (2)에 해당하며, 각 필드의 예측 점수가 모든 단어 중에서 가장 높고 임계값보다 큰 경우에만 단어를 값으로 유지

- Evaluation Metric

F1 점수 평균은 모델을 평가하는 데 사용

# 4. Robustness Evaluation via Form Attacks

![f_2](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\f_2.PNG)

그림2는 OCR 추출 후에 수행되며, 변환된 데이터는 트랜스포머 기반 필드 추출기에 입력

분석은 원래 세트와 변환된 세트 간의 성능 비교를 통해 수행
 
##  4.1 OCR Location and Order Rearrangement

OCR 위치와 텍스트 순서 배열을 약간 변경하여 원본 데이터를 의미 있는 변형으로 변환

변환은 OCR 엔진의 품질과 같은 다양한 이유로 인해 필드 추출기에 입력하기 전에 다른 OCR 결과를 얻을 수 있는 시나리오를 시뮬레이션

- Center Shift and Box Stretch

두 가지 단어 수준 위치 변환을 제안

중심 이동에서는 상자 크기를 유지하고 상자의 중심을 랜덤하게 이동

- Margin Padding

여백 패딩을 사용하여 양식의 모든 단어의 위치를 조작
 
여백 길이가 페이지 크기의 1~rmp 사이에서 생성된 임의의 숫자인 양식의 왼쪽, 오른쪽, 위쪽 및 아래쪽 측면에 흰 여백을 채운다.

- Global Shuffle

글로벌 셔플을 사용하여 트랜스포머에 입력하기 전에 단어 순서를 섞는다.

- Neighbor Shuffle and Non-neighbor Shuffle.

직관적으로 값의 로컬 이웃은 예측에 더 많은 기여를 한다.
 
Non-livenor Shuffle  - wi라는 단어는 값의 인접 영역과 bi 사이의 IoU가 0.5보다 크면 값의 인접 영역으로 정의

## 4.2 Form Background Manipulation

- BG Drop

배경(BG) 삭제는 OCR 탐지에 의해 일부 단어가 완전히 누락되는 시나리오를 모방

배경 단어를 해당 상자와 함께 pbgd 확률로 제거

- Neighbor BG Drop

BG Drop과 같음 모든 background words를 제거 

- Key Drop

키는 폼에 있는 필드의 구체적인 텍스트 표현

키는 값이 키 근처에 위치하는 경우가 많기 때문에 값 지역화에 매우 중요한 기능

OCR 탐지에 의해 실수로 키가 누락된 경우 모델 성능 변화를 확인하기 위해 키 드롭을 제안

- BG Typo

단어 수준의 문자열 오타를 시뮬레이션
 
각 배경 단어를 ptypo 확률로 선택

선택한 각 단어에 대해 임의 문자 또는 특정 문자를 스왑, 삭제, 추가 및 교체하는 오류 유형 중 하나를 적용

- BG Synonyms

유사한 의미론은 다른 동의어를 사용하여 표현될 수 있다

BG 동의어는 각 배경 단어를 pbg의 확률로 동의어로 임의로 대체

- BG Adversarial

일부 양식에는 필드 값과 동일한 데이터 유형에 하나의 단어만 포함됩니다. 

BG Adversarial은 산만함을 추가하여 난이도를 높이기 위해 사용

pbga 확률로 배경 단어를 선택하고 대체를 위해 대립 단어를 사용

각 교체에 대해 데이터 유형을 임의로 선택한 다음 해당 데이터 유형의 랜덤 값을 생성

날짜, 숫자 및 돈의 세 가지 데이터 유형에 초점

숫자의 경우, 먼저 무작위로 길이를 생성한 다음 그에 따라 길이의 임의 수를 생성합니다.
 
## 4.3 Form Field-Value Augmentations

- Value Text Augment

필드 값은 데이터 수집 프로세스의 한계로 인해 편향될 수 있습니다

값 텍스트 데이터 유형을 기준으로 필드 값을 확대할 때 변환 대상을 확대
 
각 필드 값에 대해 BG Adversarial에서와 동일한 값 생성 절차에 따라 동일한 데이터 유형의 대체물을 임의로 생성

- Value Location Augment

직관적으로 키-값 쌍을 문서 어디에 두더라도 키가 제대로 표현되기만 하면 필드-값을 유추할 수 있어야 한다.

레이아웃 다양성을 높이기 위해 Value Location Augment를 도입

양식 형식을 최대한 유지하기 위해 배경을 그대로 유지하고 양식에서 키 값 쌍의 위치를 섞습니다.

# 5. Experiments

![f_3](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\f_3.PNG)
![f_4](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\f_4.PNG)
![f_5](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\f_5.PNG)
![t_1](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\t_1.PNG)
![t_2](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\t_2.PNG)
![t_3](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\t_3.PNG)
![t_4](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\t_4.PNG)
![t_5](\img\2021\Robustness_Evaluation_of_Transformer-based_Form_Field_Extractors_via_Form_Attacks\t_5.PNG)




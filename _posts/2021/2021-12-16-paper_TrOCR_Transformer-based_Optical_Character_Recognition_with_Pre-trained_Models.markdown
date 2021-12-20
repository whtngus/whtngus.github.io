---
layout: post
title: "paper :TrOCR: Transformer-based Optical Character Recognition with Pre-trained Models"
date: 2021-12-21 19:20:23 +0900
category: paper
---


# Transformer-based Optical Character Recognition with Pre-trained Models

url : https://arxiv.org/pdf/2109.10282.pdf

code : https://aka.ms/TrOCR

2021년 9월 25일 

Microsoft

Computation and Language (cs.CL); Computer Vision and Pattern Recognition (cs.CV)

# Abstract

텍스트 인식은 문서 디지털화를 위한 오랜 연구

CNN과 문자 수준 텍스트 생성을 위한 RNN을 기반으로 구축된다

일반적으로 후 처리 단계로서 전체적인 정확도를 향상시키기 위해 다른 언어 모델이 필요

-> 글짜 위치 detectioon 모델 -> 글자 인식모델로 일반적으로 두 가지 모델 사용 

사전 훈련된 이미지 트랜스포머 및 텍스트 트랜스포머 모델을 통해 TroCR을 통한 종단 간 텍스트 인식 접근법을 제안

-> 즉 하나의 모델로 둘다 처리하겠다는 의미 

TrOCR 모델은 간단하지만 효과적이며 대규모 합성 데이터로 사전 교육하고 사람이 레이블링한 데이터 세트로 미세 조정할 수 있다.

-> 영어 데이터에서는 fine-tuning 가능하다는 듯 

document 형식과 손필기에서 sota 달성 

# 1. Introduction


![f_1](\img\2021\Transformer-based_Optical_Character_Recognition_with_Pre-trained_Models\f_1.PNG)

OCR은 입력된 텍스트, 손으로 쓴 텍스트, 인쇄된 텍스트의 이미지를 스캔 문서, 문서 사진, 장면 사진 또는 이미지에 겹쳐진 자막 텍스트에서 기계로 변환하는 것을 말한다. 

OCR 시스템은 텍스트 감지 모듈과 텍스트 인식 모듈의 두 가지 주요 모듈을 포함
 
현재의 사전 훈련된 CV 및 NLP 모델에서는 여전히 개선할 여지가 많다. 

1. 네트워크의 파라미터는 대용량의 데이터(전부 검증되지 않음)로 학습된 값으로 잘 학습된건지 확인이 불가능 

2. 기존 텍스트 인식 모델과 달리 TrOCR은 CNN을 백본으로 사용하지 않는 단순하지만 효과적인 모델이다 

-> 기존 트랜스포머 베이스 모델들은 백본을 사용 

위의 사진과 같이 입력 텍스트 이미지의 크기를 먼저 384 × 384로 조정한 다음 이미지 트랜스포머의 입력으로 사용되는 16 × 16 패치의 시퀀스로 분할 하는 방식을 사용

# 2. TrOCR

## 2.1 Model Architecture

TrOCR은 시각적 특징을 추출하기 위한 이미지 트랜스포머와 언어 모델링을 위한 텍스트 트랜스포머를 포함하여 트랜스포머 아키텍처와 함께 구축

TrOCR에서 바닐라 트랜스포머 인코더-디코더 구조를 채택

인코더는 이미지 패치의 표현을 얻도록 설계되었으며 디코더는 인코더 출력과 이전 세대에 주의를 기울이면서 워드피스 시퀀스를 생성

### 2.1.1 Encoder

인코더는 입력 이미지 ximg < 3×H0×W0 를 수신하고 고정 크기(H, W)로 크기를 조정


입력 토큰 시퀀스가 아니면 원시 이미지를 처리할 수 없으므로, 인코더는 입력 이미지를 고정 크기 (P, P)의 N = HW/P2 4제곱 패치 배치로 분해
 
크기 조정된 이미지의 너비 W와 높이 H는 패치 크기 P로 분할됩니다. 는 벡터로 평탄화되고 패치 임베딩인 D차원 벡터에 선형 투영되며 D는 트랜스포머의 모든 층에 걸쳐 숨겨진 크기

![f1](\img\2021\Transformer-based_Optical_Character_Recognition_with_Pre-trained_Models\f1.PNG)

그냥 흔한 트랜스포머 모델

softmax 함수의 극히 작은 기울기를 피하기 위해 Δ 1 dk의 스케일링 계수를 적용

여기서 dk는 쿼리와 키의 치수


![f2](\img\2021\Transformer-based_Optical_Character_Recognition_with_Pre-trained_Models\f2.PNG)

CNN 유사 네트워크에서 추출한 기능과 달리 Transformer 모델은 이미지별 유도 편향이 없으며 이미지를 일련의 패치로 처리하여 모델이 전체 이미지 또는 독립 패치에 다른 주의를 기울일 수 있다.

### 2.1.2 Decoder

TrOCR에 오리지널 트랜스포머 디코더를 사용

표준 트랜스포머 디코더는 또한 동일한 레이어의 스택을 가지고 있는데, 이는 디코더가 다중 헤드 자기 주의와 피드포워드 네트워크 사이에 인코더-디코더 주의(encoder-decoder attention)를 삽입하여 인코더의 출력에 다른 주의를 분산시킨다는 점을 제외하면 인코더 내의 레이어와 유사한 구조를 가지고 있다

디코더의 출력이 디코더의 입력으로부터 한 위치 오른쪽으로 이동한다는 사실에 기초하여, 주의 마스킹은 i보다 작은 위치의 입력인 알려진 출력에만 주의를 기울일 수 있음을 보장해야 한다.


![f3](\img\2021\Transformer-based_Optical_Character_Recognition_with_Pre-trained_Models\f3.PNG)

어휘에 대한 확률은 소프트맥스 함수에 의해 계산되고 최종 출력을 얻기 위해 빔  서리츨 사용

## 2.2  Model Initialization

인코더와 디코더 모두 대규모 라벨링 및 라벨링되지 않은 데이터 세트에서 사전 훈련된 공개 모델에 의해 초기화된다.

### 2.2.1 Encoder Initialization

DeiT(Touvron 등, 2021a) 및 BEiT(Bao 등, 2021a) 모델은 TrOCR 모델에서 인코더 초기화에 사용

### 2.2.2  Decoder Initialization

Roberta 모델을 사용하여 디코더를 초기화

RoBERTa 모델을 디코더에 로드할 때 구조가 정확히 일치하지 않습니다. 예를 들어, RoBERTa 모델에는 인코더-디코더 주의 계층이 없다. 

이를 해결하기 위해 RoBERTa 모델로 디코더를 초기화하고 없는 레이어는 무작위로 초기화한다.

## 2.3 Task Pipeline

텍스트 인식 작업의 파이프라인은 텍스트 라인 이미지를 통해 모델이 시각적 특징을 추출하고 이전에 생성된 이미지와 컨텍스트에 의존하여 워드피스 토큰을 예측한다는 것을 설명

그라운드 참 토큰의 순서는 일반적으로 문장의 끝을 나타내는 "EOS" 토큰 뒤에 온다. 

훈련하는 동안, 우리는 시퀀스를 한 위치 뒤로 회전시키고 "EOS" 토큰을 처음으로 이동시킨다. 

회전된 지상 진리 시퀀스는 디코더로 공급되며, 그 출력은 교차 엔트로피 손실과 함께 원래의 지상 진리 시퀀스에 의해 감독된다. 

추론하자면, 디코더는 출력을 반복적으로 예측하기 위해 "[EOS]" 토큰에서 시작하며, 계속해서 새로 생성된 출력을 다음 입력으로 받아들인다.

## 2.4 Pre-training

첫 번째 단계에서는 해당 텍스트 내용과 함께 수억 개의 인쇄된 텍스트 라인 이미지로 구성된 대규모 데이터 세트를 합성하고 이에 대한 TrOCR 모델을 사전 교육

두 번째 단계에서는 각각 약 수백만 개의 텍스트 라인 이미지를 포함하는 인쇄 및 수기 다운스트림 작업에 해당하는 두 개의 비교적 작은 데이터 세트를 구축

그 후, 인쇄된 데이터와 첫 번째 단계 모델에 의해 초기화되는 두 번째 단계의 필기 데이터에 대해 두 개의 개별 모델을 사전 교육

## 2.5 Fine-tuning

TrOCR 모델은 인쇄 및 필기 텍스트 인식 작업에서 미세 조정된다.

TrOCR 모델의 출력은 BPE를 기반으로 함

##  Data Augmentation

이 작업에서는 총 7가지 종류의 이미지 변환(원본 입력 이미지 보관 포함)이 수행

각 샘플에 대해 동일한 가능성을 가진 이미지 변환을 임의로 결정합니다. 임의 회전(-10도), 가우스 흐림, 이미지 확장, 이미지 침식, 다운스케일링, 밑줄 치기 또는 원본 유지로 입력 이미지를 증가

# 3. Experiments

## 3.1 Data

### 3.1.1 Pre-training Dataset

대규모 고품질 데이터 세트를 구축하기 위해 인터넷에서 공개적으로 사용할 수 있는 PDF 파일에서 200만 개의 문서 페이지를 샘플로 추출

PDF 파일이 디지털로 만들어지기 때문에 PDF 파일을 페이지 이미지로 변환하여 텍스트라인과 자른 이미지를 추출하면 예쁘게 인쇄된 텍스트라인 이미지를 얻을 수 있습니다

총 6억 8400만 개의 텍스트 라인이 1단계 사전 교육 데이터 세트에 포함되어 있다.


![t_1](\img\2021\Transformer-based_Optical_Character_Recognition_with_Pre-trained_Models\t_1.PNG)

두 번째 단계에서는 5,427개의 손으로 쓴 글꼴1을 사용하여 오픈 소스 텍스트 인식 데이터 생성기인 TRDG2에 의해 손으로 쓴 텍스트 라인 이미지를 합성

생성에 사용되는 텍스트는 위키피디아의 임의의 페이지에서 가져온 것

이터 세트는 17개로 구성된다.IIIT-HWS 데이터 세트를 포함한 9M 텍스트 라인(Krishnan 및 Jawahar, 2016). 또한 실제 세계에서 약 53,000개의 영수증 이미지를 수집하고 상업용 OCR 엔진으로 그 위에 있는 텍스트를 인식합니다. 

OCR 엔진은 2차원 좌표와 방향과 같은 입력 이미지의 추가 정보로 텍스트를 반환합니다. 

우리는 방향을 세로로 수정하고, 전체 영수증 이미지에서 텍스트 라인을 자르고, 수평이 아닌 경우 텍스트 라인 이미지를 회전시키고, 잘라낸다. 

또한 두 개의 영수증 글꼴과 내장된 인쇄 글꼴로 1M 인쇄 텍스트 라인 이미지를 합성하기 위해 TRDG를 사용한다. 

2단계 사전 훈련을 위한 인쇄된 데이터 세트는 3.3M 텍스트 줄로 구성된다.

### 3.1.2 SROIE Task 2

SROIE(스캔 영수증 OCR 및 정보 추출) 데이터 세트(작업 2)는 영수증 이미지의 텍스트 인식에 초점을 맞춘다.

SROIE의 열차와 테스트 세트에는 626개의 영수증 이미지와 361개의 영수증 이미지가 있습니다.

텍스트 감지가 포함되지 않기 때문에 평가를 위해 텍스트 라인의 자른 이미지를 사용

텍스트 라인의 자른 이미지는 접지 진실 경계 상자에 따라 전체 영수증 이미지를 자름하여 얻습니다.

-> 디텍션이 없네?

### 3.1.3 IAM Handwriting Database

IAM 필기 데이터베이스는 필기 텍스트 인식에 가장 많이 사용되는 데이터 집합인 필기 영어 텍스트로 구성

Aachen의 데이터 세트 분할을 사용

열차 세트의 747 양식 6,161 라인, 유효성 검사 세트의 115 양식에서 966 라인, 테스트 세트의 336 양식에서 2915 라인.

## 3.2 Settings

생략

## 3.3 Evaluation Metrics

![t_2](\img\2021\Transformer-based_Optical_Character_Recognition_with_Pre-trained_Models\t_2.PNG)


![f4](\img\2021\Transformer-based_Optical_Character_Recognition_with_Pre-trained_Models\f4.PNG)

IAM 데이터 세트는 대소문자를 구분하는 문자 오류율(CER)로 평가된다. 

CER은 문자의 삽입 수(i), 대체 수(s), 삭제 수(d), 일명 레벤슈테인 거리를 나타내며, 참조 텍스트의 문자 수(n)로 정규화된다.


## 3.4 Results 

![t_3](\img\2021\Transformer-based_Optical_Character_Recognition_with_Pre-trained_Models\t_3.PNG)

# 4 Related Work

생략

-  Scene Text Recognition

- Handwritten

#  5. Conclusion and Future Work

엔드 투 엔드 트랜스포머 기반 OCR 모델인 TrOCR을 제시한다.

TrOCR을 클라우드/에지 계산을 지원하기 위해 아키텍처 및 모델 크기 측면에서 플러그 앤 플레이에 대해 다양한 시각적 및 텍스트 사전 훈련된 모델이 허용되는 연구 프레임워크로 취급한다. 

또한 텍스트 인식 정확도를 더욱 향상시키기 위해 사전 훈련된 인코더 및 디코더와 잘 작동할 수 있는 보다 효율적인 데이터 동기화 및 증강 전략을 조사할 것이다. 

우리는 또한 다국어 텍스트 인식 문제를 해결하기 위해 TrOCR을 확장하는 데 관심이 있다.
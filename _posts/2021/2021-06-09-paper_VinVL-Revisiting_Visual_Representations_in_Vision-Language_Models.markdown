---
layout: post
title: "paper : VinVL: Revisiting Visual Representations in Vision-Language Models"
date: 2021-06-24 19:20:23 +0900
category: paper
---

# 논문 정보 

논문 명 : VinVL: Revisiting Visual Representations in Vision-Language Models

2021년 3월 11일 CVPR 2021 게재

기관 - Microsoft

url : https://arxiv.org/abs/2101.00529

git url : https://github.com/pzzhang/VinVL



# Abstract

VL(Vison Language) 의 시각적 표현을 개선하기 위한 연구 

d bottom-up and top-down model과 비교할 때 더 좋은 성능을 나타냄 

시각적 특징을 중요하게 살리는 모델을 재시 

7가지 밴치마크에서 sota 달성 

# 1. Introduction

VLP(Vison Language pre-training)은 광범위한 VL에 효과적임을 많은 논문에서 입증했다.

VLP는 일반적으로 두 가지 스텝으로 구성됨

1. object detection 모델은 이미지를 인코딩하기 위해 사전 훈련

-> object detection 데이터셋이 많기 때문 -> nlp영역처럼 semi supervised는 방법이 없을까?

2. 멀티모달모델을 통해 시각적 특징을 텍스트와 혼합

 ![OB_score](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\OB_score.PNG)

기존 모델들은 두 가지 스텝이서 자연어와 vision을 융합하는 모델에 초점을 두고 있지만 해당 논문에서는 object detection 모델에서 시각적인 표현을 개선하는데 초점을 둠

기존 모델들은 객체 중심 표현을 블랙박스로 사용했으나 이부분이 중요함 ResNext-152 C4 의 모델을 사용 (위 표 참조)

여러가지 OB(Object Detection) 데이터를 사용 1848개의 객체 카테고리오 524개의 속성 범주 카테로가 있다. 885만 개의 텍스트-이미지 쌍으로 구성된 공개 데이터 세트에서 트랜스포머 기반 모델을 통해 Pre-training을 함 

# Improving Vision (V) in Vision Language (VL)

VL 모델은 두 가지로 구성됨 -> image understanding Vision module, 멀티모달인 VL

![formula_1](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\formula_1.PNG)

> 위 식에서 Img와 w는 입력 vision 과 언어 이다.
>
> vision의 출력은 q와 v.q로 구성됨 
>
> q는 OB 개체의 위치, v는 이미지 representaion vector 
>
> VQA 에서 w는 query이고 y는 예측해야 하는 대답 셋
>
> 이미지 검색에서는 w는 문장, y는 예측 대답셋 
>
> imagae caption 에서는 w는 제공되지 않으며 y는 생성할 캡션!

### 2.1  Object Detection Pre-training

OD(Object Detction) 모델을 개선하기 위해 4개의 공통 객체 디텍션 데이터 세트를 활요함.



4개의 공개 데이터 세트로 구성된 대규모 말뭉치에 OD 모델을 pre-training을 진행

Visual Genome의 추가 속성을 사용해 객체와 속성을 모두 감지 

- DATA

![table_2](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\table_2.PNG)

위 표는 COCO, OI(Open Image V5), Objects365V1, VS(Visual Genome)을 포함한 Pre-training에 사용된 4가지 데이터셋을 정리한 내용

각각 데이터 셋은 불안정한 경우를 보임 -> VG는 데이터 누락등의 문제가 있음 

이러한 문제를 해결하기 위해 다음과 같은 방법을 사용함

> 1.  각 클래스의 시각적 개념을 강화하기 위해 class-aware sampling을 통해 OpenImages and Objects365 데이터셋을 최소 2---개의 인스턴스를 가져오고 각 2.2M 0.8의 이미지를 생성
> 2. 각 데이터셋의 불균형을 해결하기 ㅜ이해 각 데이터셋의 조합을 적절히 섞음
> 3. vocab를 전체 데이터셋에 대해서 생성?
> 4. 30개의 인스턴스를 포함하는 모든 VG클래스를 유지  => 총 1848개의 클래스를 포함 



- Model Architecture (FPN vs C4).

결론 C4 Architecutre가 더 좋음 

이유

> - C4 모델의 모든 레이어가 ImageNet 데이터 세트를 사용함
>
> FPN 모델의  MLP 헤드는 그렇지 않음
>
> VG 데이터세트로 충분한 시각적 데이터를 학습하기엔 양이 적기 때문에 
>
> - 서로 다른 네으워크 아키텍처 때문
>
> C4의 Convolutional head는  FPN의 MLP 헤드보다 시각적인 정보를 인코딩하는 방법이 더 뛰어남

- Model Pre-Traning

첫 convolution layer와 residual network와 batch-norm레이어를 freeze 시키고  데이터 아규먼테이션을 진행함  총 1.8M iterations을 학습 (16 batch)

 -> 오래 걸릴듯 ;;

### 2.2  Injecting attribute information into the model

Pre-training된 OD모델에 VG의 524class를 fine-tuning을 통해 학습시킴 

-> 이 fine-tuning방법에 포커스를 함 

### 2.3 Efficient region feature extractor for VL tasks

시각정보를 더 풍부하게 구성된 학습 개체를 이용해서 NMS(Non-maximal suppression)을 수행

Titan-X GPU를 통해서 학습 -> 부럽다 

요약

> 1. pre-training된 OD 모델 가져옴 
>
> vision presentations(q,v) 다운 스트림을 함
>
> 데이터는 VL tasks
>
> q는 object 이름 . v는 위치
>
> 각 영역에대한 특징 정보는  (vˆ, z),로 표기
>
> v^ 는 P-dimentional representation  이고 z는 R-dimentional position encoding 이다.



#  3. OSCAR+ Pre-training

이미지 텍스트 정렬을 위한 OSCAR모델로 사전 교육을 시킴

### 3.1 Pre-training corpus

![table_3](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\table_3.PNG)

세 가지 유형의 기존 VL 데이터 세트를 기반으로 사전 교육 코퍼스를 구축

데이터셋에 대한 내용읜 위Table3 에서 확인 가능 

VL 테스크에서 : q는 image tag (COCO, Conceptual Cations. CC, SBU captions, flicker 30k)

qA 테스크에서 : w는 visual QA datasets의 question q는 대답 (GQA, VQA and VG-QAs)

machine-generated 6 captions as w and human-annotated tags as q

### 3.2 Pre-training Objectives

![formula_2](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\formula_2.PNG)

L(MTL) 는 Masked Token Loss  (입력 텍스트에서 w,q)

L(CL3)는  novel 3-way Contrastive Loss3 <- 논문에서 제공

![formula_3](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\formula_3.PNG)

loss 계산을 위해서 위와 같은 데이터셋을 입력으로 함 (테스크에 따라 좌우가 다름)

![formula_4](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\formula_4.PNG)

 (w, q, v; c) ∈ D는 50%의 데이터, w와 qsms 25%는 의 오류 데이터를 포함

### 3.3 Pre-trained models

BERT 모델을 사용 

# 4. Adapting to VL tasks

5개의 VL task와 2개의 genration task 에서 sota를 찍음 

- VQA & GQA

이 두 가지 연구는 VL 모델을 평가하기 위해 사용되는 task

이미지를 이해하고 자연어 질문에 대답할 수 있는 능력을 가지고 있어야함 

VQA v2.0 데이터 세트 및 GQA 데이터 세트에 대할 실험을 수행 VLP 모델을 이용해 응답을 예측할 때 Softmax레이어를 가진 작업별 선형 분류기에 OSCAR+ 를 사용

- Image Captioning & NoCaps

모델이 [STOP] 토큰을 출력하거나 생성된 문장이 사전 정의된 최대 길이를 초과하면 생성 프로세스가 종료

COCO 데이터셋을 사용 

IVO 성능을 크게 개선(VinVL+VIVO로 줄였습니다)

- Image(-to-Text) Retrieval & Text(-to-Image) Retrieval

문장 사이의 유사성 점수를 계산하기 위한 모델이 필요

-> cross-modal VL representation 

일치된 이미지-텍스트 쌍이 주어지면, 우리는 무작위로 다른 이미지 또는 다른 문장을 선택하여 일치하지 않는 쌍을 형성  

-> 쌍이 일치할 가능성알 나타내는 점수로 loss 결정

- NLVR2

미세 조정을 위해 먼저 주어진 텍스트 설명과 이미지 중 하나를 포함하는 두 개의 입력 시퀀스를 구성한 다음, 오스카+의 두 개의 [CLS] 출력이 연결되어 예측을 위해 이진 분류기에 입력을 형성합니다. (번역기)

# 5. Experiments & Analysis

![ㄴ](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\table_4.PNG)

![image-20210620200451761](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\table_5.png)



# 참고 지식

- Visual Genome

데이터셋 종류의 일종 

https://visualgenome.org/

지식 베이스의 OD 데이터셋

![visual_genome](\img\2021\VinVL_Revisiting_Visual_Representations_in_Vision-Lanaguage_models\visual_genome.PNG)

- NMS(non-maximum-suppression)

연산량을 줄이고, mAP도 올리는 효과를 가짐 

디텍션 에지를 찾기 위해 현재 픽세을 기준으로 주변 픽셀과 비교했을 때 최대값인 경우 그대로 두고 아닐 경우 제거하는 방식
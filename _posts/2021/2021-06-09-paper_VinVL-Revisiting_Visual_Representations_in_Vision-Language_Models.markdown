---
layout: post
title: "paper : VinVL: Revisiting Visual Representations in Vision-Language Models"
date: 2021-06-15 19:20:23 +0900
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


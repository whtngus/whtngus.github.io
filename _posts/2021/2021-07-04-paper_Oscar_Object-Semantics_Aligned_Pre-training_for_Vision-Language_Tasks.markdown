---
layout: post
title: "paper : Predicting Camera Viewpoint Improves Cross-dataset Generalization for 3D Human Pose Estimation"
date: 2021-07-03 19:20:23 +0900
category: paper
---

# 논문 정보 

학회 : 	ECCV 2020
논문 URL : https://arxiv.org/abs/2004.06165
코드 URL : https://github.com/microsoft/Oscar
소속 : Microsoft Corporation

# Abstract

영상과 텍스트 쌍의 cross-modal representation 학습은 최근에 많은 연구가 되고 있다.



기존 방법은 사전 교육할 모델에 대한 입력으로 단순히 이미지 영역 특징과 텍스트 특징을 연결해서 학습 

해당 논문에서는 훨씬 더 쉽게 사용하기 위해 새로운 학습 방법인 Oscar를 제시

영상에서 650만개의 텍스트 이미지 쌍으로 구성된 공개 말뭉치에 Oscar 모델을  Pre-training 하고 downstream task를 fine-tuning을 통해 사용 



# 1. Introduction

![fig_1](E:\code\whtngus.github.io\img\2021\Oscar_Object-Semantics_Aligned_Pre-training_for_Vision-Language_Tasks\fig_1.PNG)

cross modal representations 학습을 위해서 이미지 캡션과 같은 다양한 V(Vision) + L(Language) 에 대한 연구는 필수 작업이다.

VLP(Vision Language Pretraining) 의 최근 연구로는 대규모 이미지-텍스트 쌍에서 일반적인 표현을 효과적으로 학습한다.

이러한 VLP모델은 transformer를 기반으로 학습  -> 이러한 모델을 Pretraining 하기 위해 기존 방법은 단순히 입력으로 임지ㅣ영역 특징과 텍스트 영역 특징을 연결하고 의미 정렬을 학습하는 방식이ㅏㄷ.

-> 오버셈플링과, 도메인에 한정적인 학습 방식이됨 



해당 연구에서는 영상에서 검출된 객체 태그를 기준점으로 도입하여 영상과 텍스트의 의미정렬 학습을 용이하게 함으로써 교차모형 표현 학습을 크게 개선할 수 있음을 보여준다.



오스카 모델은 650만 쌍으로 구성된 대규모 V+L 데이터셋에 대해 사전 교육을 함

7가지 V+L task 에서 sota를 찍음 

이미지-텍스트 정렬을 학습하기 보다는 이미지 영역의 기능 표현을 향상시키기 위해 V+L 작업에서 객체 또는 이미지 태그를 사용함

논문의 컨트리뷰션

1.  V+L 이해 및 생성 작업을 위한 일반적인 이미지 텍스트 표현을 학습하기 위한 강력한 VLP 방법인 Oscar를 소개합니다. 
2. 여러 V+L 벤치마크에서 기존 접근 방식보다 훨씬 우수한 새로운 SoTA를 달성하는 오스카 모델을 개발했습니다. 
3. 객체 태그를 교차모형 표현 학습 및 다운스트림 과제의 기준점으로 활용하는 효과성에 대한 통찰력을 제공하기 위해 광범위한 실험과 분석을 제시합니다.

# 2. Background


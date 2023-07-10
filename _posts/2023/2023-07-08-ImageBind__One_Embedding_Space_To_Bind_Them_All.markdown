---
layout: post
title: "ImageBind: One Embedding Space To Bind Them All"
date: 2023-07-09 02:05:23 +0900
category: datascience
---

# ImageBind: One Embedding Space To Bind Them All

2023년 3월 9일

facebook research

cvpr 2023 CVPR 2023 (Highlighted Paper). 

paper : https://arxiv.org/abs/2305.05665

https://imagebind.metademolab.com/

code : https://github.com/OpenGVLab/LLaMA-Adapter/tree/main/imagebind_LLM/ImageBind



# Abstract

6개의 다른 데이터를 임베딩해서 조인한 IMAGEBIND모델을 제안

 images, text, audio, depth(거리값 센서), thermal(온도센서 데이터), IMU( Inertial Measurement Unit) data

VLM과 zero shot learning, 수학, cross-modal detection, 그리고 생성 테스크를 지원 



#  1. Introduction

![f_1](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\f_1.PNG)

최근 이미지와 텍스트, 임지와 오디오 등 2개의 멀티모달 모델을을 기반으로 few shot 방법들이 많이 제안되고 있음

그러나 제약사항이 많음 - 학습한 도메인에만 바로 적용 가능 (이미지 텍스트 임베딩의 경우 바로 오디오에 쓸수 없음)

IMAGEBIND에서 제공하는 방법은 데이터가 6가지 모두 동시에 있을 필요가 없다고 함 

IMAGEBIND는 웹 스케일을 (image, text) (video, audio), (image, depth) 데이터를 이용 



기존 llama adapter와 같이 CLIP를 베이스로 사용(대용량 Text, Image학습 모델) 그리고 4가치 추가 도메인을 학습하기 위한 방법을 제안 

#  2. Related Work

#### Language Image Pre-training

#### Multi-Modal Learning

다양한 도메인을 동일한 embedding space에 매칭시키는 테스크

생략 ..

# 3. Method

![f_2](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\f_2.PNG)

6가지 도메인을 한 공간에매칭시키는 것을 목표로함

## 3.1. Preliminaries

#### Aligning specific pairs of modalities.

Contrastive learning을 이용해 각 도메인간 벡터 생성 (2개의 쌍식 활용)

그러나 2개의 쌍의 데이터씩 이용함으로

text image 로 학습된 경우 audio는 바로 활용하지 못함

#### Zero-shot image classification using text prompts

zero-shot classifiation 방법론이 인기를 끔 (image, text) 주로 image caption 테스크

IMAGEBIND운 zero shot 방법론을 이용해 text 와 image 페어가 아닌경우에도 분류할 수 있도록 함 

## 3.2. Binding modalities with images

IMAGEBIND 동메인간 Pair 정보 사용  (I,M)

I : image representation

M : another modality representation

이미지와 다른 도메인을 각각 다른 모델을 통해 임베딩함

-> qi = f(Ii) and ki = g(Mi)

- InfoNCE 

> ![f1](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\f1.PNG)
>
> 그 후 InfoNCE 로스함수 사용 
>
>  τ는 소프트맥스의 smoothness 변수
>
> j는 i와 관계까 없는 데이터
>
> 즉, 같은 데이터가 유사한 벡터에 위치하게하는 메트릭 러닝인듯
>
>  LI,M + LM,I.

#### Emergent alignment of unseen pairs of modalities

위처럼 되면 (M1, M2) (M2, M3) 이렇게 페어로 학습 되는것이 아닌 

(I,M1), (I,M2) ... 이런식으로 각 도메인 데이터가 이미지와 학습됨 

## 3.3. Implementation Details

바닐라 모델을 만들어 비교함

#### Encoding modalities

Transformer architecture를 사용 

이미지, 비디오(2초간 2 frame)는 Vision Transformer (ViT)  - patch size of 16 and stride 10

오디오는 2초간 16kHz, spectrograms 128 mel-spectrogram bins 로 임베딩

등등 .. 나머지 생략

#  4. Experiments






















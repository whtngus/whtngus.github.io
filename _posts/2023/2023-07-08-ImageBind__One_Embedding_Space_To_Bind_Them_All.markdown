---
layout: post
title: "ImageBind: One Embedding Space To Bind Them All"
date: 2023-07-13 02:05:23 +0900
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

#### Naturally paired modalities and datasets

![t_1](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\t_1.PNG)

멀티모달 데이터셋 - image/video, text, audio, depth, thermal images, IMU

Audioset dataset  - video, audio

SUN RGB-D dataset - image, depth

LLVIP dataset - image, thermal

Ego4D dataset - video, IMU

위의 테이블 1 참조

#### Large scale image-text pairs.

 large-scale web data를 사용해 pretrian 함 

ViT-H 630M params vision 모델과  OpenCLIP 302M params의 text 인코딩 코델

#### Encoders for each modality.

오디오는 mel-spectrograms으로 변환해 인코딩함

thermal 는 depth 1개의 채널 이미지로 ViT-B와 ViT-S 인코더로 학습

#### Emergent zero-shot vs. zero-shot. 

CLIP와 AudioCLIP의 경우 image,text 그리고 audio, text 멀티모달 zero-shot 분류를 보여줌



IMAGEBIND도 text prompt를 통해 zero-shot learing이 가능함 

직접적인 zero shot learning이 아니기 때문에 emergent zero-shot classification 라고 몇명함

 -> 그냥 prompt learning 아닌가?

#### Evaluation on downstream tasks.

IMAGEBIND 검증을 위해 많은 down stream tasks를 실험함

(Table 1 참조)

## 4.1. Emergent zero-shot classification

![t_2](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\t_2.PNG)

prompt templates을 통해 emgergent zero-shot 분류문제를 테스트함

text prompt 가 필요한경우  prompt를 사용했으나 image base인 depth, termal 등을 사용한경우 vision model인 CLIP를 바로 사용

위 그림에서 우측을 보면 visual이 아닌 경우에도 잘 됨을 보임 

## 4.2. Comparison to prior work

이전 다른 모델들과 비교

#### Zero-shot text to audio retrieval and classification.

![t_3](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\t_3.PNG)

이전 모델들은 지도학습을 통해 멀티모달을 학습함

예시로 AudioCLIP는 audio와 text페어가 있는 AVFIC 데이터셋을 통해 학습 

-> 비교대상 모델은 지도학습으로 불리한 조건이라는걸 말하고 싶은걸로 보임

table 3 에서 스코어를 비교함 

#### Text to audio and video retrieval.

![t_4](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\t_4.PNG)

MSR-VTT 1k-A 벤치마크를 수행



여기에서는 zero shot lerning의 경우 상대적으로 성능이 매우 내려감 -> 역시 지도학습과 차이가 많이 남

#### 4.3. Few-shot classification

![f_3](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\f_3.PNG)



n shot learning 분류 스코어 비교 (audio classification)

오디오와 depth encoder를 사용 

AudioMAE는 Audioset 데이터셋을 통해 self superpised 하고  audio 분류를 fine-tuning 시킴

## 4.4. Analysis and Applications

#### Multimodal embedding space arithmetic

![f_4](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\f_4.PNG)

IMAGEBIND 모델의 인코딩 결과가 다른 도메인에 사용 가능한지 검증함 

위의 Figure 4에서 그 결과를 보여줌 

이미지 + 음성을 임베딩한 벡터를 더해 새로운 이미지를 생성 해본 결과

#### Upgrading text-based detectors to audio-based.

![f_5](F:\code\whtngus.github.io\img\2023\ImageBind__One_Embedding_Space_To_Bind_Them_All\f_5.PNG)



학습하지 않고 text와 audio 임베딩을 이용해 audio prompt로 이미지에서 detection 테스크를 수행

####  Upgrading text-based diffusion models to audio-based.

DALLE-2 pretrain model을 사용 (diffusion model)

맨위의 Figure 1 참고

다른 타입의 데이터를 받아 오디오를 통해 difuusion을  수행




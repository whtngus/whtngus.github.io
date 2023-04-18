---
layout: post
title: "an image is worth 16x16 words transformers for image recognition at scale"
date: 2023-04-21 00:05:23 +0900
category: paper
---

# an image is worth 16x16 words transformers for image recognition at scale



2020년 10월 22일 최초 게재

google에서 게재



url : https://arxiv.org/abs/2010.11929

code : https://github.com/google-research/vision_transformer



# ABSTRACT

Transformer 는 nlp에서 거의 필수로 사용됨 

그러나 computer vision에서는 아직 제한적이고 CNN과 함께 사용됨 -> 지금은 당연하게 transformer가 쓰지이지만 2020년도 논문이라 이렇게 언급한듯



기존 vision 은 cnn에 많이 의존하기 때문에 해당 논문에서는 cnn 없이 transformer만으로 vision을 접근하는 방법을 제안(ImageNet, CIFAR-100, VTAB 데이터 셋으로 벤치마크)

Vision Transformer (ViT) 는 기존 CNN 베이스의 sota모델들을 많이 향상시킴 

 

# 1. INTRODUCTION

Transformer는 nlp테스크에서 많이 사용되고 있음 

-> 엄청난 학습 데이터와 모델 크기를 사용



# 2. RELATED WORK

pixcel 단위 attention을 많이 사용하지만 pixcel크기의 제곱에 해당하는 메모리 사용이 필요하기 때문에 현실적으로 이미지를 담기에는 부족함 

... 생략

# 3. METHOD

![f_1](\img\2023\an_image_is_worth_16x16_words_transformers_for_image_recognition_at_scale\f_1.PNG)

제안하는 모델은 기본적인 Transformer와 상당히 유사함 

 ## 3.1 VISION TRANSFORMER(ViT)

![fm_1](\img\2023\an_image_is_worth_16x16_words_transformers_for_image_recognition_at_scale\fm_1.PNG)

Figure1은 기본적인 1D 임베딩의 그림인데 사진은 2D 여서 이를 해결할 방법이 필요 

채널까지 하면 3D인 (H\*W\*C)이미지를 P^2*C로 flatterned 시킴

 P는 resolution된 N=HW/(P^2) 수가 발생

D : transformer latent 벡터 사이즈 - 수식 1

'[class]' 토큰 초롬 첫 임베딩 벡터를 output으로 사용 - 수식4

position 임베딩을 2D로 넣어준다고 1D랑 특별해 다른점을 발견하지 못했다고 함 

-> 이미지의 임베딩이 고정이기 때문에 1D로 포지션 임베딩을 넣어도 알아서 잘 이해하는걸로 보임

- Inductive bias

2차원의 구조(이미지)는 매우크고 sparse하기 때문에 image patch를 이용함 

- Hybrid Architecture

이미지 patche 대신에 CNN의 1*1 feature map 사용

-> CNN과 transformer의 혼합  (최근에 자주 쓰이는방식인듯)

### 3.2 FINE-TUNING AND HIGHER RESOLUTION

일반적으로 큰 데이터로 pre-training 작은 데이터로 fine-tuning을 진행하는데 

pre-training시에 head와 zero-initialized(D*K)를 제거함 

K는 다운스트림 classes 

이미지 해상도와 상관 없이 같은 사이즈의 patch를 사용 

# 4 EXPERIMENTS

Resnet과 같이 임베딩한 모델을 포함해 평가를 진행함 

## 4.1 SETUP

- DataSets

ILSVRC-2012 ImageNet dataset : 1K개의 클래스와 1.3M개의 이미지 

 ImageNet-21k : 21K 클래스, 14M개의 이미지

JFT : 18K 클래스와 303M개의 고해상도 이미지

벤치마크 데이터셋의 경우 

ReaL labels, CIFAR-10/100, Oxford-IIIT Pets, Oxford Flowers-102, 19-task VTAB(분류),  VTAB

데이터셋 사용



- Model Variants

![t_1](\img\2023\an_image_is_worth_16x16_words_transformers_for_image_recognition_at_scale\t_1.PNG)

Table1과 같이 BERT를 따라감

ex) Large의 경우 16*16 input patch 

ResNet모델의 Batch Normalization 레이어 위치를 이동하고, standardized convolution 사용 

- Training & Fine-tuning

4096 배치 사이즈 .. -> 집에서 돌리긴 힘들듯

그외 생략

## 4.2 COMPARISON TO STATE OF THE ART

![t_2](\img\2023\an_image_is_worth_16x16_words_transformers_for_image_recognition_at_scale\t_2.PNG)

학습시 TPUv3 사용 <- 구글에서 한참 TPU를 밀고 있을때

Figure2는 VTAB task를 그룹으로 나눈것 

BiT, VIVI, S4L은 기존 sota모델

## 4.3 PRE-TRAINING DATA REQUIREMENTS

![f_3](\img\2023\an_image_is_worth_16x16_words_transformers_for_image_recognition_at_scale\f_3.PNG)

그림 3 :  데이터셋 별 비교 

그림 4 : pre training 데이터 셋 별 Image Net 스코어 비교 

아래는 JFT-300M 데이터셋을 통해 학습한 모델로 비교 (Hybrid가 대체로 연산량 대비 정확도가 좋은걸로 보임)

## 4.5 INSPECTING VISION TRANSFORMER

![f_6](\img\2023\an_image_is_worth_16x16_words_transformers_for_image_recognition_at_scale\f_6.PNG)

우측 아래는 어텐션이 잘 안된거같은데 ? ,,

![f_7](\img\2023\an_image_is_worth_16x16_words_transformers_for_image_recognition_at_scale\f_7.PNG)

왼쪽은 임베딩 필터를 보여주는데 다양한 패턴에 대해 필터링을 하는것으로 보임 (특정 패턴이 안보임)

중앙은 embedding 시각화

우측은 attetion



























# 참고 

- de-facto

 사실상(事實上)의 의미로 쓰이는 표현으로, 법적으로 공인된 사항이 아니더라도 실제 존재하는 사례를 가리키는 말
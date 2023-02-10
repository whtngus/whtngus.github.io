---
layout: post
title: "Zero-Shot Text-to-Image Generation
date: 2023-02-10 01:20:23 +0900
category: datascience
---

# Zero-Shot Text-to-Image Generation

DALL-E

2021년 2월 24일 최초 arxiv

OpenAI 에서 연구됨

- paper  url

[Zero-Shot Text-to-Image Generation](https://arxiv.org/abs/2102.12092)

- 사용 사이트

[openai.com/blog/dall-e](http://openai.com/blog/dall-e)

- github

<https://github.com/openai/dall-e>

- 관련 대표 기사

<https://www.aitimes.com/news/articleView.html?idxno=146393>

![f1](D:\src\whtngus.github.io\img\2023\Zero-Shot_Text-to-Image_Generation\f1.jpg)

![f1](D:\src\whtngus.github.io\img\2023\Zero-Shot_Text-to-Image_Generation\f2.jpg)

# Abstract

Text-to-image 생성은 이미지와 텍스트 쌍의 고정된 학습 데이터를 이용해 학습하는 방식을 사용하고 이를 추론하기 위해 복잡한 구조의 auxiliary losses 등의 방식을 사용함

또한 정보량은 국한된 데이터셋에 있어 정보량이 부족 함

해당 연구에서는 AUTOREGRESSIVELY MODEL과 충분한 데이터량으로 학습할 수 있는 모델을 제안

그리고 zero-shot fashion으로 평가를 진행

# 1. Introduction

최근 machine learning을 이융한 text to image 방법론들이 연구되고 있다.

DRAW :2015년 이미지 생성 모델

goodfellow : 2014년 visualization GAN 모델

2016년 생성 뿐만아니라 zero-shot learning을 통한 인식도 되는 모델

multi-scale generation : 성능이 향상된 생성모델 2017년

2016~2021년 단지 text만으로 이미지를 생성할 수 있는 연구 수행

또한 대규모 학습 데이터를 제공하는 MS-COCO 데이터셋과 pretrained 트랜스포머 모델등 다양한 연구가 진행됨

- 관련 데이터셋

MS-COCO : 이미지당 5개의 캡션으로 구성된 대규모 데이터셋

CUB : 북미 새 200종에 대한 11,788개의 이미지당 5개의 캡션으로 설명을 추가

해당 연구에서는 MS-COCO데이터셋을 zero-shot 을 통해 label없이 정확도를 비교하여 보여줌 또한 image-to-image 도 같이 보여줌

# 2. Method

연구의 목표는 transformer를 이용해 text에서 이미지를 생성할 수 있도록 하는것

그러나 pixcel 단위로 바로 이미지를 생성하려고 하면 지나치게 많은 메모리가 필요하다.

→ 이미지 해상도가 좋아질수록 더 많은 메모리가 필요

이러한 방법들을 해결하기 위해 연구에서는 2개의 stage로 학습을 진행

1. Stage 1

> ![img](file:///D:/src/whtngus.github.io/img/2023/Zero-Shot_Text-to-Image_Generation/f3.jpg?lastModify=1676010143)
>
> 분리된 오토인코더인 dVAD(discrete variational autoencoder)를 학습한다.
>
> 이는 위에서 말한 pixcel 단위로 이미지를 생성시 지나치게 많은 메모리가 사용되는걸 방지하기 위한 압축을 위해서 사용
>
> → 256 * 256 RGB 이미지를 32*32 이미지 토큰으로 변경  이렇게 되면 8192의 정보만 예측하면 됨   -  8192 = 32*32*8 (rgb 2^3) → 8이 rgb값이 맞는지 확인하기
>
> 이렇게 압축된 저 용량의 데이터를 사용 (위의 그림1 - 위쪽이 원본 아래쪽이 dVAD를 통해 축소된 이미지

- Stage 2

256 BPE-encoding된 텍스트 토큰과 32*32=1024개의 이미지토큰을 conctenate  그리고 이 두 관계를 joint distribution 방식을 통해 학습 진행
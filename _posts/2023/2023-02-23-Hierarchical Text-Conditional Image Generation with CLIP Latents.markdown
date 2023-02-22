---
layout: post
title: "Hierarchical Text-Conditional Image Generation with CLIP Latents"
date: 2023-02-23 01:20:23 +0900
category: datascience
---

# Hierarchical Text-Conditional Image Generation with CLIP Latents

dall-e 2

open AI

2022년 4월 13일

paper url : https://arxiv.org/pdf/2204.06125v1.pdf

code url : https://github.com/lucidrains/DALLE2-pytorch

# Abstract

dall-e에서 사용한 CLIP의 contrastive 모델은 representation을 robust하게 보여주는걸 증명함

-> 이미지 생성 

더 이미지를 잘 생성하기 위해 이번에도 2 stage 의 model 방법을 사용 

- step 1

텍스트를 입력받아 CLIP를 이용해 image embedding 

- step 2

embedding된 이미지를 이용해 decoder 모델에서 이미지 생성



위의 방식을 통해 완벽하고 다양한이미지를 생성한다고 함

# 1 Introduction

![f1](F:\code\whtngus.github.io\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\f1.PNG)

CLIP embedding에는 여러가지 장점이 있음

> CLIP로 이미지의 분포를 정확하게 이동시켜줌
>
> 분포를 바르게 만들어줘서 zero-shot learning을 가능하게 해줌 

또한 image 뿐만 아니라 이를 연속적으로 만들어 video도 generation tasks도 수행

연구에서 두 가지 테스크를 동시에 진행

1. text-conditional image generation

CLIP를 통한 encoder

decoder에서 image generation

2. 이미지 변환

이미지 임베딩 공간을 이용한 임베딩 공간을 이용해 이미지 변환 

+ 임베딩 공간을 이용해 CLIP에서 이미지의 어떤 특징을 인식하거나 무시하는지 관찰할 수 있음

















# 참고 지식

1. CLIP(Learning Transferable Visual Models From Natural Language Supervision)

>  OpenAI - 2021년 1월(OpenAI Blog)
>
> 
>
> 이미지와 텍스트를 같은 공간으로 매핑하여 representation learning을 수행하는 모델 
>
> - 이미지에서의 임베딩 단점 
>
> 이미지 분야에서는 CNN 기반 모델이 강한 면모를 보이기는 하지만, zero-shot learning에서는 매우 낮은 정확도를 보임
>
>  weak supervised learning 방식으로도 어느 정도 성과를 보였으나, 저자들은 이 방식은 zero-shot 학습 능력을 제한한다고 주장
>
> - WIT(WebImage Text)라는 세로운 데이터셋을 만듦
>
> 기존 MS-COCO, Visual Genome은 품질이 좋지만 데이터가 별로 없고 YFCC100M는 데이터가 많지만 품질이 안좋기 때문 
>
> 인터넷에서 수집한 4억 개의 image, text 쌍으로 구성된 데이터
>
> - 학습 방법
>
> negative와 positive를 나눠서 이미지에 대해서 같은 image caption 쌍과 다른 image caption쌍을 만든다.
>
> N개의 image,text 쌍이 있으면 총 데이터는 N(N-1)개 생성됨 
>
> ![clip](F:\code\whtngus.github.io\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\clip.PNG)
>
> - ResNet은 ResNet-50, ResNet-101, ResNet-50의 4배, 16배, 64배에 해당하는 EfficientNet-style 모델 3개(RN50x4, RN50x16, RN50x64)를 추가로 더 학습시켰다.
> - ViT는 ViT-B/32, ViT-B/16, ViT-L/14를 사용하였다.
> - 전부 32 epoch만큼 학습시켰다.
>
> ![clip2](F:\code\whtngus.github.io\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\clip2.PNG)















# 참고

- clip

https://greeksharifa.github.io/computer%20vision/2021/12/19/CLIP/


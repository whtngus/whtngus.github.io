---
layout: post
title: "Hierarchical Text-Conditional Image Generation with CLIP Latents"
date: 2023-02-23 00:05:23 +0900
category: datascience
---

# Hierarchical Text-Conditional Image Generation with CLIP Latents

dall-e 2

open AI

2022년 4월 13일

paper url : https://arxiv.org/pdf/2204.06125v1.pdf

code url : https://github.com/lucidrains/DALLE2-pytorch

tutorial code ? : https://github.com/jina-ai/dalle-flow

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

![f1](\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\f1.PNG)

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




# 2. Method

(x,y) : x는 image y는 캡션 

zi, zt : CLIP에 의해 임베딩된 latent vector

- generation 하기 위해 두가지 구성요소가 사용됨

> 1. p(zi | y)
>
> 캡션 y의 조건에 따른 이미지 임베딩 zi 을 계산
>
> 2. decoder p(x | zi, y)
>
> CLIP에 의해 임배딩된 이미지와 캡션 y로 이미지 x를 계산 (선택적으로 zi 대신 xi 도 가능  -> inference 시 사용하는걸로 보임)

![formula1](D:\src\whtngus.github.io\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\formula1.PNG)

CLIP를 이용해 임베딩 된 zi와 캡션 y를 통해 이미지 x를 생성

## 2.1 Decoder

CLIP은 diffusion 모델을 통해 이미지 + GLIDE text encoder를 통해 임베딩 함

![figure15](D:\src\whtngus.github.io\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\figure15.PNG)

![figure16](D:\src\whtngus.github.io\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\figure16.PNG)

GLIDE는 CLIP가 잘못하는 영역의 자연어 임베딩을 잘 학습할 수 있을거라고 생각했지만 위 figure 16 처럼 잘 되지는 않음 



CLIP 임베딩 중 10%를 0으로, 50%로 text caption을 랜덤하게 드랍시킴

dall-e 에서는 64\*64를 256\*256 으로 resolution 하나만 시켰는데 dall-e2 에서는 1024*1024 도 resolution 시킴 + 학습하는 동안에는 noise를 약하게 줌 


















# 참고 지식

1. CLIP(Learning Transferable Visual Models From Natural Language Supervision)

>  OpenAI - 2021년 1월(OpenAI Blog)
>
>  
>
>  이미지와 텍스트를 같은 공간으로 매핑하여 representation learning을 수행하는 모델 
>
>  - 이미지에서의 임베딩 단점 
>
>  이미지 분야에서는 CNN 기반 모델이 강한 면모를 보이기는 하지만, zero-shot learning에서는 매우 낮은 정확도를 보임
>
>  weak supervised learning 방식으로도 어느 정도 성과를 보였으나, 저자들은 이 방식은 zero-shot 학습 능력을 제한한다고 주장
>
>  - WIT(WebImage Text)라는 세로운 데이터셋을 만듦
>
>  기존 MS-COCO, Visual Genome은 품질이 좋지만 데이터가 별로 없고 YFCC100M는 데이터가 많지만 품질이 안좋기 때문 
>
>  인터넷에서 수집한 4억 개의 image, text 쌍으로 구성된 데이터
>
>  - 학습 방법
>
>  negative와 positive를 나눠서 이미지에 대해서 같은 image caption 쌍과 다른 image caption쌍을 만든다.
>
>  N개의 image,text 쌍이 있으면 총 데이터는 N(N-1)개 생성됨 
>
>  ![clip](F:\code\whtngus.github.io\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\clip.PNG)
>
>  - ResNet은 ResNet-50, ResNet-101, ResNet-50의 4배, 16배, 64배에 해당하는 EfficientNet-style 모델 3개(RN50x4, RN50x16, RN50x64)를 추가로 더 학습시켰다.
>  - ViT는 ViT-B/32, ViT-B/16, ViT-L/14를 사용하였다.
>  - 전부 32 epoch만큼 학습시켰다.
>
>  ![clip2](F:\code\whtngus.github.io\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\clip2.PNG)

2. Diffusion model

Diffusion model은 데이터를 만들어내는 deep generative model 중 하나로, data로부터 noise를 조금씩 더해가면서 data를 완전한 noise로 만드는 forward process(diffusion process)와 이와 반대로 noise로부터 조금씩 복원해가면서 data를 만들어내는 reverse process를 활용

![diffusion_model](D:\src\whtngus.github.io\img\2023\Hierarchical_Text-Conditional_Image_Generation_with_CLIP_Latents\diffusion_model.PNG)

1. 오른쪽에서 왼쪽으로 noise를 점점 더해가는 forward process q를 진행
2. forward process를 반대로 추정하는 reverse process p를 학습
3. noise(xt)로부터 data(x0)를 복원하는 과정을 학ㄱ습 

위의 방법을 통해 random noise롤부터 원하는 image, text, graph등을 generate할 수 있는 모델을 만듦 

-> 이를 이용해 실제 data 분포인 p(x0)를 찾아내는것을 목표로 함 













# 참고

- clip

https://greeksharifa.github.io/computer%20vision/2021/12/19/CLIP/

- diffusion model

https://process-mining.tistory.com/182
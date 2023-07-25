---
layout: post
title: "Generative Pretraining in Multimodality"
date: 2023-07-27 02:05:23 +0900
category: datascience
---

# Generative Pretraining in Multimodality

2023년 7월 11일

대학생 

url : https://arxiv.org/abs/2307.05222

code : https://github.com/baaivision/Emu

# Abstract

멀티모달, 싱글모달 을 지원하고 동시에 학습할 수 있는 Emu모델을 제안 

1. 사진, 텍스트를 임베딩해 다음 토큰(생성인듯) 을 분류및 리그레션을 수행
2. g image captioning, visual question answering, video question answering
   and text-to-image generation 테스크를 수행





# 1 Introduction

LLM 모델은 대용량 텍스트 데이터에서 다음단어를 예측하는 방식으로 자연어를 이해하고 빠른 속도로 좋은 성능을 달성하여 현실 세계에서 많이 응용되고 있음

Flamingo 모델은 좋은 성능과 멀티모달 기반의 zero-shot learning 까지 가능

연구에서 제시하는 Emu은 large multimodal model 로 영상과 이미지 그리고 텍스트데이터를 학습함

textboook 과 웹페이지에서 멀티모달 학습을 함

![f_1](F:\code\whtngus.github.io\img\2023\Generative_Pretraining_in_Multimodality\f_1.PNG)

텍스트 영상 이미지 등 온라인상의 대용량의 데이터가 제공되고 있음

-> https://commoncrawl.org/ 여기를 이용해서 크롤링을 했다고 함(디지털 지식을 자유롭게 학습, 이용, 협업할 수 있는 개방형 플랫폼)

여러가지 데이터와 모델을 비교 했으며 EVA-CLIP모델의 visual prepresentation을 사용하기로 함 (이미지를 바로 받지 않음)

Emu는 기존의 LMMs 모델 학습 방식과 다르게 다음 토큰을 예측 시 다음 토큰만을 로스함수에 넣는게 아니라 모든 텍스트, 연속적인 image embedding을 모두 활용해 crossentropy classification loss 함수로 계산

이미지 임베딩에 ℓ2 regression loss 추가로 적용함

 text, images, video 멀티모달 프롬프트를 지원하고 동시에 여러 데이터도 지원 

-> Figure 1의 예시 확인

그래고 zero-shot, few-shot 방법을 이용해 image caption, visual QA, video question answering, test-to-image generation 테스크를 실험

# 2 Emu: Predict the Next in Multimodality

## 2.1 Architecture

![f_2](F:\code\whtngus.github.io\img\2023\Generative_Pretraining_in_Multimodality\f_2.PNG)

이미지는 EVA-CLIP를 통해 임베딩 하고 다양한 멀티모달 입력을 받고 출력을 함 

Visual Encoder, Causal Transformer, Multimodal Modeling 그리고 Visual Decoder 4개의 파트로 구성됨

시작과 끝 그리고 이미지를 구분하는 특수토큰을 추가함 <s> </s> 와 [IMG], [\IMG]

-> 토큰수 제한이 많아야할탠데 .. 모델사이즈가 어떻게 될지..

#### Causal Image-text Transformer

일반적인 생각과 다르게 2D인 이미지 처리시 이미지를 그대로 raster로 넣으면 성능이 잘 나오지 않음 

이미지를 텍스트와 다르게 seq 시그널 없이 넣으면 좋은 성능을 보임 

이미지를 임베딩 하기 위해 Causal Transformer모델을 사용해 1D Z space에 매핑해 입력함 

-> 결국 이미지는 EVA-CLIP 임베딩을 했다는 이야기

![f1](F:\code\whtngus.github.io\img\2023\Generative_Pretraining_in_Multimodality\f1.PNG)

>  z : 임데딩된 벡터
>
> g() : EVA-CLIP 임베딩 모델
>
> i : 이미지
>
> e : 랜덤 초기화 벡터 (같은값이 안나오도록 하는 장치)

#### Visual Decoder

visual embeding 모델 Decoder에서 latent diffusion model을 사용 

Emu에서 N개의 embedding을 받아 이미지 decoding을 함 (linear projections of the cross-attention modules)

## 2.2 Training Objective













# 참고 지식

- raster

필셀로 구성된 이미지

- Q-Former

BLIP-2 논문에서 제안한 transformer 구조로 frezoen된 image encoder에서 정보를 뽑아 멀티모달에 사용될 수 있도록 하는 image encoder

-  diffusion model

generative 모델 중 하나로 data에서 noise를 조금씩 더해 data를 완전한 noise로 만드는 과정을 반대로 학습해 조금씩 복원해 가면서 data를 만들게 하는 모델 


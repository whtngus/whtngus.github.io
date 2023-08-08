---
layout: post
title: "Generative Pretraining in Multimodality"
date: 2023-08-07 02:05:23 +0900
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

![f_1](\img\2023\Generative_Pretraining_in_Multimodality\f_1.PNG)

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

![f_2](\img\2023\Generative_Pretraining_in_Multimodality\f_2.PNG)

이미지는 EVA-CLIP를 통해 임베딩 하고 다양한 멀티모달 입력을 받고 출력을 함 

Visual Encoder, Causal Transformer, Multimodal Modeling 그리고 Visual Decoder 4개의 파트로 구성됨

시작과 끝 그리고 이미지를 구분하는 특수토큰을 추가함 <s> </s> 와 [IMG], [\IMG]

-> 토큰수 제한이 많아야할탠데 .. 모델사이즈가 어떻게 될지..

#### Causal Image-text Transformer

일반적인 생각과 다르게 2D인 이미지 처리시 이미지를 그대로 raster로 넣으면 성능이 잘 나오지 않음 

이미지를 텍스트와 다르게 seq 시그널 없이 넣으면 좋은 성능을 보임 

이미지를 임베딩 하기 위해 Causal Transformer모델을 사용해 1D Z space에 매핑해 입력함 

-> 결국 이미지는 EVA-CLIP 임베딩을 했다는 이야기

![f1](\img\2023\Generative_Pretraining_in_Multimodality\f1.PNG)

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



![f2](\img\2023\Generative_Pretraining_in_Multimodality\f2.PNG)

레이블링 되지 않은 web-scale 데이터 D의 멀티모달데이터 x = (x1, .... xn)

여기에서 각 x는 vision - langauge 페어 

2D 입력인 image 혹은 video의 경우 Casual Transformer를 통해 인코딩을해 1D embedding 후 삽입

p(x) 의 데이터를 유사하게 만드는 p(u)를 만드는걸 목적으로 함 



loss 함수는 text token 의 cross-entropy 사용  + l2 regression loss

## 2.3 Generalist Interface

위의 Figure 1의 예시처럼 2개의 이미지를 입력시에도 구분자 특수 토큰을 넣고 입력하면 됨 



사용 시 이미지 output을 원한다면 [IMG] 특수 토큰으로 끝내면 됨 

# 3 Emu Training

image - text pair : LAION-2B,  LAION-COCO 데이터셋

image text interleaved : MMC4   데이터셋

video-text pairs : WebVid-10M 데이터셋 

interleaved video-text data : YT-Storyboard-1B

을 사용해 학습함 

## 3.1 Data

#### Image-text Pairs.

LAION-2B, LAION-COCO 데이터셋을 사전학습 시 사용 

LAION-2B 데이터셋은 이미지와 웹사이트의 노이즈를 포함한 텍스트셋

LAION-COCO 는 600M 텍스트셋 이미지 캡션 데이터

#### Video-text Pairs

WebVid-10M 짧은 비디오에서 텍스트 대본을 수집한 데이터셋 (여러나라 데이터가 있음)

#### Interleaved Image and Text.

Multimodal-C4 (MMC4) 데이터셋은 텍스트만 있는 C4 데이터셋에서 확장한 데이터셋

75M의 image-text-interleave 문서가 있음 

->400M 이미지와 38B 텍스트 토큰 

#### Interleaved Video and Text.

![f_3](\img\2023\Generative_Pretraining_in_Multimodality\f_3.PNG)

YT-Storyboard-1B 데이터셋 사용 

Youtube에서 수집한 18M의 비디오 자막 데이터 

## 3.2 Pretraining

1B 버전의  EVA-02-CLIP 모델을 vision encoder 초기모델로 사용

멀티모달의 경우 13B LLaMA 모델을 사용

LLaMA는 Transformer Decoder 모델과 40-layer ViT 모델 사용 

 다 합해 Emu 모델은 14B 사이즈 

-> 24GB에서도 안돌아가는 사이즈 ㅠ

NVIDIA 80G-A100 GPU로 10k step 학습했다고 함 (2일 학습)

## 3.3 Visual Decoding

사전학습 후 LAION-COCO과 d LAION-Aesthetics 데이터셋을 이용해 fine-tuning 

LAION-Aesthetics 는 LAION-5B데이터셋 에서 미적 높은 퀄리티를 가진 image-text 데이터셋 



Stable Diffusion v1.5.을 이용해 학습 

visual encoder와 Emu를 freeze 시키고 U-Net만 학습시킴

[IMG]토큰을 마지막에 두고 텍스트를 입력해 이미지 생성을 유도함 

32개의 A100-40G gpu로 학습

# 4 Instruction Tunin

unseen 생성 task와 여러 테스크를 위해 공공 데이터셋을 이용해 Emu를 학습시킴

언어 모델인 language 인 ShareGPT과 Alpaca구조와 

image-text인 LLaVA 구조

video 인 VideoCaht, Video-ChatGPT 구조를 기반으로 만듦

 Instruction Tunng시 사전학습에 사용된 Emu의 모든 파라미터를 프리징 시키고 LoRA 모듈만 fine-tuning함

![f3](\img\2023\Generative_Pretraining_in_Multimodality\f3.PNG)

[USER]와 [ASSISTANT]는 특수 토큰이고 <System Message>는 task를 나타냄 

# 5 Evaluation

Vision Language : MS-COCO

Image QA : VQAv2, OKVQA, VizWiz

visual dialog : VisDial

video QA : MSRVTTQA, MSVDQA, NextQ

text2image generation : MS-COCO

데이터셋을 이용해 평가함 

## 5.1 Zero-shot Evaluation

![t_1](\img\2023\Generative_Pretraining_in_Multimodality\t_1.PNG)

학습 시 사용되지 않은 데이터셋만을 이용해 평가함을 다시 강조함 

-> 학습데이터가 이것저것 많다보니 다시 말한걸로 보임 

#### Multimodal Understanding

Emu-I : instruction-tuned model

Chain-of-Thought prompting 방식을 사용함 -> 이 방식은 이제 치팅으로 보지 않는건가?

두 가지 스텝을 사용 

step1 이미지를 입력하고 캡션을 생성하도록 함

step2  구체적인 테스크에 대한 설명과 step1에서 생성한 캡션 

Flamingo의 방식과 같이 평가함 

Table1에서 위방식을 사용한 경우 *을 붙임 

Emu-I는  14B 크기의 모델 

#### Text2image Generation

![t_2](\img\2023\Generative_Pretraining_in_Multimodality\t_2.PNG)

zero shot image generation을 평가함 

MS-COCO 데이터셋 사용 하고 랜덤으로 30k개의 prompt를 평가셋으로 사용 

PNDM 스케줄러를 사용(이미지 셈플링 방법)

## 5.2 Few-shot Evaluation

few shot 평가 방법은  task-specific prompts와 몇개의 입력 데이터(0, 2, 4, 8)를 사용함 

RICES접근 방법을 사용 

### 5.3 Qualitative Evaluation

![t_3](\img\2023\Generative_Pretraining_in_Multimodality\t_3.PNG)

- 결과 Figure

![f_9](\img\2023\Generative_Pretraining_in_Multimodality\f_9.PNG)

![f_4](\img\2023\Generative_Pretraining_in_Multimodality\f_4.PNG)

![f_5](\img\2023\Generative_Pretraining_in_Multimodality\f_5.PNG)

![f_6](\img\2023\Generative_Pretraining_in_Multimodality\f_6.PNG)

![f_7_8](\img\2023\Generative_Pretraining_in_Multimodality\f_7_8.PNG)



![f_10](\img\2023\Generative_Pretraining_in_Multimodality\f_10.PNG)

![f_12](\img\2023\Generative_Pretraining_in_Multimodality\f_12.PNG)







# 참고 지식

- raster

필셀로 구성된 이미지

- Q-Former

BLIP-2 논문에서 제안한 transformer 구조로 frezoen된 image encoder에서 정보를 뽑아 멀티모달에 사용될 수 있도록 하는 image encoder

-  diffusion model

generative 모델 중 하나로 data에서 noise를 조금씩 더해 data를 완전한 noise로 만드는 과정을 반대로 학습해 조금씩 복원해 가면서 data를 만들게 하는 모델 

-  Chain-of-Thought prompting

여러 단계의 추론 과정을 새성하도록 유도하여 언어 모델의 추론 능력을 향상시키는 기법

- Flamingo

VLM 모델 로 

프리트레이닝 모델과 교차배열된 image, text 데이터를 이용해 학습함 

- FID(Frechet Inception Distance)

실제 이미지와 생성된 이미지가 얼마나 유사한지 통계 측면세서 벡터 사이의 거리를 계산



Inception Score는 생성된 이미지만 사용해 평가하지만 FID는 실제이미지를 이용해 계산

 Inception v3 모델을 이용해 2048개의 output vector의 벡터의 거리를 구함 

-> 즉 거리값이 가까울수록 유사함
---
layout: post
title: "Semantic-Conditional Diffusion Networks for Image Captioning"
date: 2023-01-10 01:20:23 +0900
category: datascience
---

# Semantic-Conditional Diffusion Networks for Image Captioning

2022년 12월 6일

CVPR

code : https://github.com/YehLi/xmodaler/tree/master/configs/image_caption/scdnet

https://github.com/yehli/xmodaler

# Abstract

기존 NLP, VISION 멀티모달 테스크는 하나의 테스크만을 수행하거나, 여러 테스크를 수행 시  generation 테스크를 거의 수행하지 않음 

해당 논문에서는 image 생성, 변형 및 캡션까지 3가지의 멀티모달 테스크를 하는 Semantic-Conditional Diffusion Networks (SCD-Net) 모델을 제안 -> 이런 모델들을 diffusion model 이라고 지칭 

# 1. Introduction

![f1](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\f1.png)

기존의 이미지 캡셔닝은 이미지를 보고 의미있는 텍스트를 생성하는게 목표였지만 이미지에서 텍스트를 생성할 뿐 양방향의 테스크는 없었음 (텍스트에서 이미지도)

> Figure 1
>
> - a 
>
> word 단위의 이미지 캡션 생성 모델 
>
> auto-regressive model로 단방향
>
> - b 
>
> non-auto-regressive 방식으로 최근에 많이 사용되는 방법 
>
> 학습은 문장 전체를 한번에 하지만 역시 caption생성시에 autoregressive 하게 생성됨
>
> ex - bert에서 문장 생성시 결국 토큰하나씩 생성
>
> - c
>
> 가우시안 노이즈와 Markov chain을 이용해 이미지와 텍스트의 복원을 반복해 데이터 augmente 진행 



데이터셋은 COCO 데이터셋 사용 



# 2. Related Work

## 2.1. Autoregressive Image Captionin

- RNN-based Approaches
- Transformer-based Approaches

## 2.2. Non-Autoregressive Image Captioning



#  3. Method

![f2](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\f2.png)

SCD-Net은 transformers 레이어를 여러개를 사용하여 스택한 모델 

## 3.1. Problem Formulation

#### Notation of Diffusion Model

- Forward Process

![f_1](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\f_1.png)

Markov chain을 이용하고,

x : Gaussian noise를 이용한 sentence data

y t ∈ (0, T] : forward state transition

e : ∼ N (0, I)  - normal distribution

t :  ∼ U(0, T)  - uniform distribution

S : described Text

N : 텍스트의 각 워드 

γ(t') : 단조증가함수 monotonically increasing function

위 식에서  Diffusion Transformer - f(xt, γ(t'), V)는  x0를 복원하는 테스크를 수행하고 

V : L2 regression loss 사용

![f_2](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\f_2.png)

- Reverse Process

![f_3](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\f_3.png)

생성된 text로부터 주어진 image를 이용해 학습 

## 3.2. Diffusion Transformer

V : 이미지에서 detected objects

- Visual Encoder

Visnal Encoder는 N개의 Transformer encoder blacks의 stacked으로 이루어져잇음 

![f_4](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\f_4.png)

FFN : the feed-forward layer

MultiHead : Multi-head self-attention layer

norm : layer normalization

FC : fully-connected layer

δ : activation function

- Sentence Decoder

![f_5](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\f_5.png)

![f_6](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\f_6.png)

![f_7](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\f_7.png)

예측값을 수식6을 이용해 확률값처럼 이용할 수 있도록 변경하고 

 Bc의 representation과 곱 



로스는위 값의 Cross entropy를 사용한 Lxe와 Lbit을 합한 값을 사용 

## 3.3. Semantic Condition











# 참고 지식

1. Normal distribution and uniform distribution

   normal distribution

![normal_distribution](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\normal_distribution.png)

uniform distribution

![uniform_distribution](\img\2023\Semantic-Conditional_Diffusion_Networks_for_Image_Captioning\uniform_distribution.png)



2. FFN, FC 차이

FFN (Feed Forward Neural Network)

recurrent구조가 없는 텐서가 신경망의 앞으로만 전파되는 신경망을 의미

RNN가 대비되는 개념의 신경망 

RNN이 없기떄문에 gradient가 명확하게 정의되고, backpropagation을 쉽게 계산 가능 

FC(Fully Connected Neural Network)

각 layer의 각 뉴런들이 그 다음 층의 모든 노드들과 하나도 빼놓지 않고 모두 연결되어 있는 신경망 

다음층의 노드들과 듬성듬성 연결돼 있는 convolutional layer나 pooling layer와 대비되는 개념 

-> 모든 FC는 FFN이다





# 참고

- FFN, FC

https://heekangpark.github.io/ml-shorts/ffnn-vs-fc
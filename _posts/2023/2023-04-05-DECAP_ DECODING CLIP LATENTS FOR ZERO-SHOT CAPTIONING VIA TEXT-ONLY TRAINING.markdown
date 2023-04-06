---
layout: post
title: "DECAP: DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING"
date: 2023-04-05 00:05:23 +0900
category: paper
---

# DECAP: DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING

2023년 3월 6일 ICLR 게재

ByteDance 회사

paper : https://arxiv.org/abs/2303.03032

code : https://github.com/dhg-wei/DeCap



# ABSTRACT

CLIP(Large-scale pre-trained multi-modal models)는 강력한 zero-shot 분류, 생성등의 능력을 보여줌

하지만 large languagemodel은 분번별력 있는 설명을 만들지 못함

이를 해결하기 위해 lightweight의 DeCap 프레임워크를 제안

DeCap 프레임워크 특징

> - text 캡셧 데이터 쌍으로만 학습 
> - text only데이터 학습시 end-to-end 학습이 필요하지 않음

image와text 멀티모달 테스크시 데이터의 형식이 다른 이슈를 해결하기 위해 contrastive model을 주로 사용함

(같은 임베딩 공간에 배치)

-> 연구에서 이런 형식이 다른 이슈(modality gap)을 줄일 수 있는 방법을 제안



# 1 INTRODUCTION

Image Captioning의 목표는 이미지를 자동으로 설명하는것!

일반적으로 사람이 이미지를보고 설명한 데이터 셋을 가지고 학습하지만, 해당 데이터는 많지 않다는 문제를 가지고 있다.

-> 해당 연구에서는 text 데이터만을 사용함으로 이런 의존성을 줄임

또한 대규모 모델인 GPT, CLIP등이 있지만 모델이 크기 때문에 Infernece가 느린 단점이 있음

연구에서는 이러한 문제점을 해결하기 위해 

DeCap 모델인  zero-shot captioning를 제안

논문의 메인 컨트리뷰션

> 1. Zero Shot base 모델인 DeCap 프레임 워크를 제안
>
> 이 모델인 CLIP를 포함하고 있음
>
> (임베딩 영역 스페이스와 decoder를 가져와서 사용)
>
> 2. training-free projection mechanism 제안
>
> 이 방법은 vision text 의 CLIP에서 modality gap을 줄일 수 있음
>
> 또한 많은 메모리를 사용하지 않음
>
> 3. 여러 실험 케이스 설명
>
>  MSCOCO and NoCaps. 를 이용해 밴치마크 하고 
>
> MSCOCO and Flickr30k 데이터셋 에서 학습(Caption data인 Text 만 사용함)
>
> MSR-VTT and ActivityNet-Captions 과 비교해 SOTA 스코어 달성



# 2. RELATED WORK

#### CLIP in Captioning.

![f_1](F:\code\whtngus.github.io\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\f_1.PNG)

Vision-Language 모델로 contrastive loss를 사용 

-> 하지만 바로 generatino하기 때문에 프리 트레이닝 모델에 text decoder가 없음

해당 논문에서 제시하는 모델로 Text Incoder를 만들고 training free 메커티즘을 만듦

#### Zero-shot Captioning

Zero-shot Captioning은 사람의 도움 없이 이미지, 비디오의 캡션을 생성하는걸 목표로함

fine tuning 없이 프리트레이닝 모델로만 캡션을 생성

#### Text Reconstruction

pair 텍스트와 unpair 텍스트를구분하는 테스크



# 3. METHOD

위의 Fiugre 1이 해당 연구에서 제안하는 프레임워크

## 3.1 TEXT-ONLY DECODER PRE-TRAINING

기존에는 zero-shot 캡셔닝을 위한 PLM (Pretraining Language Model) 을 사용

-> 그러나 PLM은 웹공간의 다양한 이미지를 학습하여 caption된 좋은 데이터가 없어 이미지 캡셔닝 테스크에 적합하지 않음

![fm](F:\code\whtngus.github.io\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\fm.PNG)

> t : 문장  t = {word1, word2 , .... , wordt}
>
> Pθ : lanuage model - prefix로 프리징 시킴
>
> Etext(·) : CLIP 인코더의 L2-normalized embedding space

그냥 이전 문장을보고 다음 단어의 representation의 평균값? 인듯

-> 텍스트 임베딩을 이미지  임베딩에 최적화 시킴

## 3.2 INFERENCE STRATEGIES

위의 3.1을 통해 TEXT embedding 을 이용한 캡셔닝 생성 decoder 를 만듦

여기에서는 question을 이용해 어떻게 캡션을 생성하는지가 관건

### 3.2.1 PROJECTION-BASED DECODING (PD)





















# 참고

- CLIP

Learning Transferable Visual Models From Natural Language Supervision논문으로

인터넷에서 얻은 대규모 데이터셋을 이용, 이미지와 연관된 caption으로 사전학습

- web scale

아마존, 구글, 페이스북 등 대형 클라우드 서비스 제공업체들의 클라우드 운영 방식을 일컫는다
---
layout: post
title: "BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models"
date: 2023-04-28 00:05:23 +0900
category: paper
---

# BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models

Salesforce Research

paper : https://arxiv.org/abs/2301.12597

code : https://github.com/salesforce/LAVIS/tree/main/projects/blip2

-> 코드에 tutorial jupyter 도 있고 테스트 해보기 편함

2023년 1월 30일 게재

# Abstract

멀티모달 및 pre-training 모델 크기가 점점 커지고 있어서 효율적인 모델인 BLIP-2를 제안

-> 논문을 읽은 이유 

 bootstraps vision-language pretraining 전략을 제안함

-> 바로 실행하고 학습할 수 있는 느낌? 의 lightweight Querying Transformer

#  1. Introduction

Vision-language pre-training (VLP) 연구는 최근 몇년간 빠른속도로 발전하고 발전에 따라 모델의 크기가 빠르게 커져가고 있음 ... -> 개인이 pre-training은 거의 못해볼 만한 크기

해당 논문에서 포괄적이고(멀티모달) 효울적인 bootstrapping 기반의 높은 정확도의 VLP 모델을 제안

![f_1](\img\2023\BLIP-2 Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\f_1.PNG)

모델의 크기를 줄이기 위해 unimodal 사전학습 모델을 frozen 시킨 상태에서 pre-training  진행(해당 연구의 핵심 키)

-> 이방법을  Querying Transformer (QFormer)로 명칭

Figure 1에서  얼음모양 파란색이 frozen 시킨 상태 



- Q-Former pre-training 방법

> 1. visual representation 과 가장 관련인는 텍스트를 찾는 방식으로 학습 
> 2. vision-to-language 생성 학습 



- 컨트리뷰션

> 1. 2 stage pre-traininig
>
> 효율적인 모델 (작은 모델 크기 + 퍼포먼스)
>
> representation learning stage -> generative learning stage
>
> VL task에서 sota score 달성 (VQA, image caption, image-text retrival)
>
> 2. zero-xhot image-to-text generation
> 3. lightweigt Q-Former
>
> 연산량이 매우 효울적임



# 2. Related Work

## 2.1. End-to-End Vision-Language Pre-training

Vision-language pre-training의 목표는 멀티모달 성능의 향상이다.

-> 이를 증명하는 방법은 주로 downstream task

그러나 기존 연구들은 vision 과 nlp를 동시에 학습하다보니 모델의 크기가 너무 커져서 효율성이 떨어지는 문제 발생

## 2.2 Modular Vision-Language Pre-training

image encoder 부분을 freeze 시킨 후 학습시키는 방식 



# 3. Method

![f_2](\img\2023\BLIP-2 Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\f_2.PNG)

논문에서 제시한 bootstrap 기반의 fozen pre-train  BLIP-2 모델은 2 stage로 학습

1. vision-language representation learning

이때 image encoder를 frozen 시킴

2. vision-to-language gnerative learning

이때는 LLM을 frozen 시킴

## 3.1. Model Architecture

frozen 된 LLM과 image encoder의 gap 차를 줄이기 위한 Q-Former를 제안

위의 Figure2에서  Q-Former분을 보면 두개의 transfomer 부분으로 되어 있음

- iamge transformer

image transformer와 image encoder의 상호작용을 위한 레이어 

두 모델의 갭차를 줄여주기 위해 사용 

- text transformer

text encoder와  text decoder에 사용 



Q-Former는 Bert(base) 모델 weight로 initialize 시킴 -> 188M 파라미터

32 querie(output) 차원으로 768 차원 사용  -> Z (32 * 768)

-> ViT-L/14인 257*1024 에 비교하면 매우 작은 수치

## 3.2. Bootstrap Vision-Language Representation Learning from a Frozen Image Encoder

image-text pair 데이터를 이용해 pre-training을 진행

3개의 optimize pre-training 방법을 결합하여 사용 (위의 Figure 2참조)

- Image-Text Contrastive Learnig(ITC)

image text pair데이터가 들어온 경우 representation vecor가 유사하게 만드는 contrastive인듯

-> 이때 각 [CLS] 토큰의 represantaion vector를 사용 



leakage를 방지하기 위해 self-attention mask를 사용 (각각 이미지와 텍스트 부분)

-> 이때 image encoder는 frozen 시킴

- Image-grounded Text Generation (ITG)

ITG loss는 Q-Former의 Text generatio 로스로 일반적임  -> 이때도 image encoder는 frozen 

-> UniLM논문과 유사한 방식으로 학습한다고 함 

이때 querie가 있는경우 시작 부분에 [CLS] 대신 [DEC]토큰을 사용

- Image-Text Matching (ITM)

image, text representation 에서 fine-grain을 목표로 이진 분류 학습

-> 이미지와 텍스트가 pair인지 아닌지를 분류

## 3.3. Bootstrap Vision-to-Language Generative Learning from a Frozen LLM

![f_3](\img\2023\BLIP-2 Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\f_3.PNG)

Q-Former와 frozen 된 LLM모델을 결합 (위의 Figure 3 참조)

Figure 3에서 Fully Connected Layer로 embedding Z를 정사형 시킴 

-> 위와 같은 학습 방식으로 학습속도를 올리나 두 번쨰 학습으로 catastrophic forgetting문제가 발생

## 3.4. Model Pre-training

- Pre-training data

(COCO, Visual Genome, CC3M, CC12M, SBU, LAION400M(115M 사용))  데이터셋을 통해 BLIP 학습시  사용한 학습데이터를 그대로 129M 이미지 데이터 사용

CapFilt방식을 사용함 (web image에서 caption을 생성하는 방식)

BLIP large모델에서 사용한 방식대로 이미지당 10개의 캡션을 생성 후 캡션에 랭킹을 기반으로 학습 (상위 2개의 캡션을 선택하여 학습)

- Pre-trained image encoder and LLM

1. ViT-L/14 from CLIP
2.  ViT-G/14 from EVA-CLIP

위 2개의 모델에서 마지막 레이어를 제거하고 마지막에서 2번째 represantation vector 사용 

 

OPT model과 Flan T5를 비교 

- Pre0training settings

생략 .. 

A100  40GB 그래픽 카드 한장 사용해서 stage1 - 6일  stage2 - 3일 학습

 

# 4. Experiment

![t_1](\img\2023\BLIP-2 Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\t_1.PNG)

Table 1은 zero-shot vision task

## 4.1. Instructed Zero-shot Image-to-Text Generation

위의 Figure 4 에서 VQA에 대한 예시를 보여줌 

사진에 대한 지식, 상식, 토론 그리고 개인화된 답장을 할 수 있을을 보여줌 

- Zero-shot VQA

위의 Table 2 참조

지정된 템플릿을 통해 prompt로 질문 가능

->  “Question: {} Short answer:”

beam serach size 5를 사용 

OK-VQA dataset 에서 sota 달성

##  4.2~3 Image Captioning Visual Question Answering

![f_4](\img\2023\BLIP-2 Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\t_4.PNG)

Table 3 참조  Table 4참조 

...  생략 

#  5. Limitation

![f_7](\img\2023\BLIP-2 Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models\f_7.PNG)

image to text generation 에서  이미지에 대한최신 정보가 없는경우  정확도가 좋지 않을 수 있음 











# 참고

- fine-grained

세세하게 구분한 라벨을 의미 

꽃, 강아지, 고양이가 아닌 -> 꽃 종류, 강아지면 포메, 닥스훈트 등 

- catastrophic forgetting

인공신경망은 단일 작업에 대해선 뛰어난 성능을 보이나, 다른 종류의 작업을 학습하면 이전 학습 내용을 잊어버리는 현상


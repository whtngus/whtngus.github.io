---
layout: post
title: "VisionLLM: Large Language Model is also an Open-Ended Decoder for Vision-Centric Tasks"
date: 2023-09-09 02:05:23 +0900
category: paper
---

# VisionLLM: Large Language Model is also an Open-Ended Decoder for Vision-Centric Tasks

2023년 3월 25일 

상하이대학교

https://arxiv.org/pdf/2305.11175.pdf

Code: https://github.com/OpenGVLab/VisionLLM
Demo: https://github.com/OpenGVLab/InternGPT



# Abstract

최근 LLM으로 AGI(artificaial general interlligence)의 성능이 빠르게 올라감 

좋은 성능에더 불구하고 vision 모델에서는  open-ended task에 대해 한계가 있음 

4가지(System-centric, Content-centric, Visual-centric, Conversation-centric) 4가지중 visual-centric 테스크에서 많은 한계가 있음 

연구에서 제시하는 모델에서 COCO 데이터셋에서 60%의 mAP성능을 보임 



# 1 Introduction

![f_1](\img\2023\VisionLLM_Large_Language_Model_is_also_an_Open-Ended_Decoder_for_Vision-Centric_Tasks\f_1.PNG)

ChatGPT와 같은 LLM이 등장하면서 AGI의 큰 발전을 이룸 

그럼에도 불구하고 VL task에서는 좋은 성능을 아직 거두지 못하고 있음 

이전에는 pre-training 후 fine-tuning을 하는 방식으로 학습했지만 각각의 다운스트림 테스크를 위해 매번 학습해야 했음 (Figure 1 의 a)



![f_2](F:\code\whtngus.github.io\img\2023\VisionLLM_Large_Language_Model_is_also_an_Open-Ended_Decoder_for_Vision-Centric_Tasks\f_2.PNG)

이를 open-ended task를 통해 극복함

1. 논문에저 제시하는VisionLLM 모델을 통해 open-ended 와 customizable manner 방법을 제안 
2. LLM을 통한 vision-centric 문제를 해결함 
3. 여러가지 테스크를 지원함



# 2 Related Work

## 2.1 Large Language Model

LLM은 NLP와 AGI(artificial general intelligence)에서 상당한 능력을 보임 

GPT-3 ChatGPT GPT-4 InstructGPT 등등 

그 외에도 OPT, LLaMA, MOSS, GLM 등이 있음 



해당 논문에서 제안하는 vision-centric LLM인 Visual ChatGPT, MM-REACT, HuggingGPT, InternGPT, VideoChat이 있지만 그럼에도 불구하고 언어 기반의 모델이여서 vision 테스크를 전문적으로 다루지 못함

## 2.2 Vision Generalist Model

generalist model이 추구하는 바는 하나의 모델 파라미터로 여러 테스크를 수행할 수 있는것



## 2.3 Instruction Tuning

생략



# 3 VisionLLM

## 3.1 Overall Architecture

![f_3](F:\code\whtngus.github.io\img\2023\VisionLLM_Large_Language_Model_is_also_an_Open-Ended_Decoder_for_Vision-Centric_Tasks\f_3.PNG)

논문에서 제안하는 key 디자인

1. vision-centric task를정의하고 custom 함
2. image tokenizer를 제안함  (Language-Guided Image Token 이라고 정의)
3. LLM 기반의 open-task decoder 를 제안

## 3.2 Unified Language Instruction






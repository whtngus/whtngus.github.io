---
layout: post
title: "VisionLLM: Large Language Model is also an Open-Ended Decoder for Vision-Centric Tasks"
date: 2023-08-31 02:05:23 +0900
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

이를 open-ended task를 통해 극복함






---
layout: post
title: "Exploring Diverse In-Context Configurations for Image Captioning"
date: 2023-06-15 00:05:23 +0900
category: paper
---

# Exploring Diverse In-Context Configurations for Image Captioning

2023년 3월 26일

url : https://arxiv.org/pdf/2305.14800v2.pdf

code : https://github.com/mlfoundations/open_flamingo



# Abstract

VL를 위해 4가지 방법으로 나눠 분석을함

Image selection,  이미지 캡션

# 1 Introduction

NLP 테스크에서 강력한 모델을 VL도 합쳐 해결할 수 있는 방법을 제안함 

![f_1](F:\code\whtngus.github.io\img\2023\Exploring Diverse In-Context Configurations for Image Captioning\f_1.PNG)

위의 그림은 LM 과 VLM의 예시를 보여줌 

MSCOCO 데이터셋을 사용 해서 학습함

이미지 선택을 위해 4가지 방법 사용 

1. Random Sampling(RS)
2. Similarity-based Image-Image Retirival (SIIR)
3. Similarity-based Image-Caption Retrival (SICR)
4. Diversity-based Image-Image Retrival(DIIR)

4가지 타입의 이미지 캡션을 생성

1. Ground-Truth Captions (GTC)
2. Model-Generated Captions(MGC)
3. Interatively Prompting(IP)
4. Model-Generated Captions as Anchors(MGCA)

다양한 캡션 생성을 위해 MGC에서는 두 가지 모델을 사용 

# 2 Related Work

### Prompting Language Model (LM).

최근 몇년간 두 가지 방법론으로 NLP가 연구되고 있음

- GPT, BERT, BART 처럼 LM을 이용해 pre-training -> fine-tuning 방식
- prompt paradigm

GPT-3 가 나오면서 패러다임이 바뀜 

downstream task를 함에 있어서 fine-tuning을 하는것이 아닌 적절한 프롬프트를 만들어 채우는 방식으로 해결 

prompt-based techniques 기술이 필요해짐 

### Prompting Vision-Language Model (VLM).

Image Caption , VQA 등의 테스크가 있음 

### Exploring In-Context Configurations in NLP

- 생략

# 3 Configuring In-Context Sequences

















# 참고

- Chain-of-Thought 

추론 능력 사고 사슬

프롬프트를 이용해 사람이 사고하는 것과 비슷하게 추론 단계를 추가








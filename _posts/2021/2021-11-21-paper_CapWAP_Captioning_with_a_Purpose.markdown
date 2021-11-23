---
layout: post
title: "paper : CapWAP: Captioning with a Purpose"
date: 2021-11-23 19:20:23 +0900
category: paper
---



#  CapWAP: Captioning with a Purpose

학회 - EMNLP 2020

소속 - csail.mit.edu

게재 - 9 Nov 2020

url - https://arxiv.org/pdf/2011.04264.pdf



# Abstract

기존 이미지 캡션 작업은 일반적인 참조 캡션을 사용해 이미지에 대한 텍스트 정보를 제공한다.

즉 이미지의 다른 시각적 관점에만 집중하게 된다 (어떤의미진지는 뒤에서 이어서 설명)

-> 의도된 인구의 정보 요구에 맞게 조정될 수 있는 시스템을 개발하는 것

이를 해결하기 위해 CAPWAP(Caption with a Purpose)를 제안



 질문 답변 모델이 샘플링된 사용자 질문에 대한 정답을 제공할 수 있는 출력을 보상함으로써 강화 학습을 사용하여 의도된 정보 요구에 맞게 직접 최적화할 수 있음을 보여준다.



# 1. Introduction

![f_1](E:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\f_1.PNG)



일반 이미지 캡션의 경우 명확하지 않고 VQA는 질문에 대한 정보만을 제공함.

해당 논문에서는 

 (1) 일반 주석이 사용자의 정보 요구를 대표하지 않을 수 있고, 

(2) 사용자 질문이 정보 요구를 명확히 표현하는 더 자연스러운 방법이며, 

(3) 그러한 질문에 대한 정확한 답을 제공하기 위해 캡션을 최적화하면 훈련이 정보 요구에 집중할 수 있다고 주장

![t_1](E:\code\whtngus.github.io\img\2021\CapWAP_Captioning_with_a_Purpose\t_1.PNG)

1. 서로 다른 대상 사용자층이 표현하는 특정 정보 요구를 충족하기 위해 이미지 캡션을 생성하는 새로운 작업(CAPWAP)을 정의한다. 
2. 우리는 우리의 정보 중심 모델이 최첨단 기존 일반 캡션 시스템의 캡션보다 이 작업에 대해 훨씬 더 높은 품질의 캡션을 생성할 수 있음을 보여준다. 
3. 우리는 이 새로운 패러다임 하에서 강화 학습의 성능을 크게 향상시키는 새로운 합성 사전 훈련 루틴을 제안한다.

# 2. Related Work






















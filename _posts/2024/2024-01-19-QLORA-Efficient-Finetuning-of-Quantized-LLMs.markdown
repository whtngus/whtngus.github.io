---
layout: post
title: "QLORA: Efficient Finetuning of Quantized LLMs"
date: 2024-01-20 02:05:23 +0900
category: paper
---

# QLORA: Efficient Finetuning of Quantized LLMs

2023년 5월 23일 

NeurIPS 

washington 대학



url : https://arxiv.org/pdf/2305.14314.pdf

code : https://github.com/artidoro/qlora

# Abstract

QLORA는 메모리사용에 효과적인 finetuning 방법을 제안함 

65B 파라미터 모델을 48GB 하나의 gpu에서 학습할 수 있으며 16-bit 와 같은 성능을 냄 

QLORA는 백프로파게이션을 4비트로 양자화 시켜 학습하는 방식의 LoRa를 제공함

이름을 Guanaco로 명침함 -> 그냥 QLoRA쓰지 ...?

하나의 gpu 에서 24시간 학습 만으로 chatGPT 의 99.3% 성능을 달성했다고 함 



아래와같은 방법을 통해 정확도의 감소 없이 메모리를 최적화 시킴

1. 4-bit NormalFloat(NF4) -> 새로운 data type 적용 
2. 이중 양자화 사용 ->  ?? 아래 설명 봐야할듯
3. Paged Optimizers를 활용한 메모리 급증 관리 

QLoRA를 이용해 1000가지 이상 모델을 fine tuning 해보고 테스트해봤다고 함 

# 1 Introduction


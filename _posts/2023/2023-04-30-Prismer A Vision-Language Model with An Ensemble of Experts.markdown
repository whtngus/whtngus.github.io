---
layout: post
title: "Prismer: A Vision-Language Model with An Ensemble of Experts"
date: 2023-04-30 00:05:23 +0900
category: paper
---

# Prismer: A Vision-Language Model with An Ensemble of Experts

2023년 3월 4일 게재 
NVIDIA

code : https://github.com/NVlabs/prismer
paper : https://arxiv.org/abs/2303.02506



# Abstract

최근 멀티보달 기반의 좋은 성능의 알고리즘들이 많이 나오고 있음 

그러나 정현적으로 많은 학습 데이터를 필요로 함 

논문에서 제안하는 Prismer는 data와 parameter를 효율적으로 사용해 VLM 을 학습 

-> 쉽게 구할 수 있는 데이터와 frozen을 통한 학습을 진행

# 1 Introduction

최근 VLM 모델은 많은 데이터와 큰 모델을 피룡로 하고 yottaFLOP(10^24) scale 정도임 

![f_1](F:\code\whtngus.github.io\img\2023\Fcodewhtngus.github.ioimg2023Prismer A Vision-Language Model with An Ensemble of Experts\f_1.PNG)

Primer는 여러 테스크를 general하게 하는게 아닌 각각의 task를 독립적으로 학습시킴 

- 논문의 컨트리뷰션

> 1. 강력한 Vison-only 그리고 Language-only 모델 
>
> web-scale 지식 네트워크 구조를 기반
>
> 2. task 별 muliple type encoding 진행
>
> -> frozen시키고 상위 레이어를 통해 embedding vector로 classification 하는듯
>
> frozne 했기 때문에 lightweight 모델

13M의 공공 image/alt-text 데이터로 사용

# 2 Related Work

- Vision-Language Models (VLMs) 

transformers 모델이 나오면서 해당 테스크를 정복하기 시작함 









# 참고

- ALt Text

대체 텍스트는 alternative text의 축약

사진이나 동영상을 인공지능을 이용하여 분석한 뒤, caption을 생성한 데이터


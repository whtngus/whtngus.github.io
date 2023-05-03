---
layout: post
title: "Prismer: A Vision-Language Model with An Ensemble of Experts"
date: 2023-05-03 00:05:23 +0900
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

![f_1](F:\code\whtngus.github.io\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\f_1.PNG)

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

- Multi-task and Auxiliary Learning

하나의 입력에서 multiple modalities를 목적으로 학습함 

ex) emantic segmentation, object detection, and depth estimation)

-> 그러나 이렇게 한습하면 multi-task 에 대한 지도학습 (각 테스크에만) 집중함

Prismer 는 이를 해결하고자 함 

- Unifying Pre-trained Experts 

여러 multi-modal pre-trining을 이용해 다른 pre-training모델을을 이용하는 방법 



MoE와 "Ensemble of Experts"(논문에서 정의) 의 차이점을 분석



# 3 Prismer: Open-ended Reasoning with Multi-modal Knowledge

Vision-language generative model인 primer 모델 소개

## 3.1 Model Overview

![f_2](F:\code\whtngus.github.io\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\f_2.PNG)

모델은 Figure 2와 같이 설계됨 

transformer로 구성된 encoder - decoder 모델

Vision encoder는 RGB이미지와 multi-modal label을 입력받아 같이 학습함 (e.g. depth, surface normal, segmentation labels, predicted from the frozen pre-trained experts) 그리고 output으로 multi-modal feature를 출력

-> 도메인에 최적화 하기 위해 Expert Resampler를 도입

예를들어 Depth Parchify 테스크 뿐만아니라 그림에서 글자를 인식하는것도 필요하다면 저기에 OCR 모델의 결과를 추가해서 넣으면 됨 

각 task 별 모델의 결과를 결합해 종합적으로 쓰겠다는 뜻 (원본사진 + 각 task 모델 결합)



여러 모델을 잘 결합하기 위해 Expert Resampler와 Adaptor를 추가함 

Expert Resampler는 다양한 멀티모달 테스크의 결과값을 결합시키는데 사용 

Adaptor는 transformer레이어로구성되어 여러 테스크에 적용시킴

## 3.2 Pre-trained Experts

- Backbone Experts

각 트랜스포머 기반의 Vision과 Language 만을 학습한 유사한 모델 (single domain)을 사용 

-> 학습시에는 frozen 시킴

- Modaiity Experts



















# 참고

- ALt Text

대체 텍스트는 alternative text의 축약

사진이나 동영상을 인공지능을 이용하여 분석한 뒤, caption을 생성한 데이터

- Mixture of Experts (MoE)

참고 : https://chickencat-jjanga.tistory.com/5![moe_2](F:\code\whtngus.github.io\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\moe_2.PNG)

![moe](F:\code\whtngus.github.io\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\moe.PNG)

복잡한 문제를 단순화해 합쳐서 산출하는 방식의 아이디어 

g(x)는 softmax  (i번째 export를 몇%나 믿을지)

f(x)는 export network의 output




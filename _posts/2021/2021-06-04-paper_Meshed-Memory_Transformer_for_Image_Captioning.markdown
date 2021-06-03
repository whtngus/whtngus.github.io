---
layout: post
title: "paper : Meshed-Memory Transformer for Image Captioning"
date: 2021-06-03 19:20:23 +0900
category: paper
---

# 논문 정보 

논문 명 : Meshed-Memory Transformer for Image Captioning

2020년 3월 20일  CVPR 2020 게재


url : https://arxiv.org/abs/1912.08226

git url : https://github.com/aimagelab/meshed-memory-transformer



# Abstract

이미지캡션과 같은 멀티 모달 테스크를 위해 M2 모델에서는 이미지 캡션을 위한 메모리 모델을 제안

coco 데이터 셋을 이용해 테스트 

-> 결국 transformer 썻다고 보면 됨

#  1. Introduction

이미지 캡션은 이미지의 시각적 내용을 자연어로 설명해야 함으로 시각적 요소와 텍스트 요소의 관계를 이해하는 모델과 출력 시퀀스를 고려하는 모델이 필요

-> 그래서 이전에는 Recurrent 모델과 CNN 모델등이 사용됨

BERT에서 기술적 영감을 얻어 두 가지 캡션 알고리즘을 통합함

1.  이미지 영역과 각 객체들의 관계는 저수준 및 고수준 관계를 고려해 인코딩 된다.(이때 메모리 벡터를 사용해 사전 지식을 학습)
2. 문장 생성시에 낮은레벨과 높은 레벨을 모두 이용해야함. -> 인코더와 디코더 계층 사이에 메쉬 연결을 함으로 M2 Trasnformer 라고 함

![approach](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\approach.PNG)

위 그림은 아키텍처 인데 그냥 보면 이전의 일반 Transformer모델 사용과 크게 달라보이지 않는다 

COCO 데이터셋을 통해 학습하며 Karpathy 테스트 세트에서 소타 스코어 달성

논문에서 제시하는 컨트리 뷰션

- transformer 모델을 사용해 메쉬 구조로 학습(위 사진)
- 시각적 우선순위를 활용해 인코딩 영역과 영구 메모리 v를 사용
- sota 찍음
- nocaps 데이터셋 사용  (개인적으로 nocaps 데이터 사용이 마음에 든다) 
- 코드 공개 

# 2. Related work

초기에는 cross-entropy를 이용해 RNN, CNN 모델을 학습함

-> 그래프 서치를 사용하기 시작 

-> 인코딩을 위해 grid CNN features 를 사용하는등 임베딩 방법을 높임

-> 객체간의 관계를 설명하기 위한 모델을 향상 (역시 CNN베이스)

등등 .. 발전 순서 나열



# 3. Meshed-Memory Transformer

![architecture](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\architecture.PNG)

위 모델은 인코더와 디코더 모듈로 나눠서 볼 수 있다.

인코더는 입력 이미지에서 영역을 처리(attention - detection)하고 그들 사이의 관계를 파악

디코더는 각 인코딩 계층의 출력에서 단어별로 출력캡션을 생성

![modification_1](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_1.PNG)

수식은 일반적인 트랜스포머에서 쓰이는 수식과 같다.

Q 는 Nq의 query vector 이고 K, V는 nk를 포함하는(salf attention이여서 결국 같음) 같은 차원의 벡터 



### 3.1 Memory-Augmented Encoder

![modification_2](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_2.PNG)

X에 대한 재해석을 하는역할 S(X)인데 이미지가 정확히 어떤식으로 입력되는지는 코드를 확인해봐야 알것같다.

이미지의 관계에 대해서 파악할 수 있으나. 어텐션이 모든 쌍의 유사성에 의존하기 때문에 이미지 영역 간의 관계에 대한 사전지식을 모델링 할 수 없다고 한다 -> (논문에서 말하는 기존 트랜스포머 모델 적용시의 문제점)

예를들어 어떤 포지션에서 농구공 어떤 포지션에서는 사람에 집중할때 두 개체관의 관계를 집중할 수 있는 방법이 없기 때문에 사전 지식이 필요하다.

- Memory-Augmented Attention

![modification_3](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_3.PNG)

개체관의 관계성을 알수 없는 문제점을 해결하기 위해 memory-Augmented Attention 방식을 제안 

우선 순서 정보를 알 수 있는 추가 slots가 인코딩의 입력으로 추가된다.

우선순위 정보가 입력 데이터인 X에 의존해서는 안되기 때문에 단순한 학습 가능 벡터로 구현된다. 

Mk Mv 는 학습벡터, 위에서 학습 가능한 키를 추가하여 X에 포함되어 있지 않은 학습된 지식을 검색할 수 있다.

W와 M은 다른 프로젝션 레이어를 가지며 concatenate를 통해 다른 head의 결과를 얻는다. (M은 각 head에 대한 학습)

- Encoding layer








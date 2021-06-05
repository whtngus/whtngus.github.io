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

![modification_4](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_4.PNG)

memory-augmented 연산자를 트랜스포머형식의 레이어에 저장한다.

위 수식에서 Xi는 입력 벡터 셋이고, F(x)i는 i vector에 대한 output 이다 .

σ(·)는 ReLU V와 U는 학습 파라미터 b와 c는 바이어스 텀 이다. (그냥 일반 네트워크)

![modification_5](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_5.PNG)



위에서의 각 레이어는 residual connection과 노멀라이제이션으로 한번더 감싸진다.

위 식의 AddNorm은 residual connection + normalization

- Full encoder

여러 인코딩을 순차적으로 쌓아서 output을 계싼하는데 쓰인다 X² = (X²1, ..., X²N)  이전 타임까지 내용을 전부 고려 

### 3.2 Meshed Decoder

디코더에서는 인코더에서 출력된 모든 벡터를 사용해서 다음 토큰을 생성

multi-level representation을 사용해서 이미지에서 문장을 생성중에 인코딩 계층을 활용할 수 있는 mashed 구조 연산을 할 수 있도록 유도한다.

- Meshed Cross-Attention

![modification_6](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_6.PNG)

인코더의 출력 정보를 모두 사용해서 계산!

Y는 시퀀스 벡터이고, X는 인코딩 레이어  -> Y는 Masehd Attention 커넥션을 통해  X의 모든 요소를연결한다. 

그후 연산된 결과를 합침 

![modification_7](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_7.PNG)

C는 그냥 셀프어텐션인거 같은데 cross attention 이라고 명명 한다 

![modification_8](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_8.PNG)

ai는 cross attention 결과 이고 서로 다른 계층의 중요성을 나타낸다~  [] 는 attention을 나타내고 이를 뉴럴네트워크와 Lelu로 감싼다 

- Architecture of decodnig layers

![modification_9](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_9.PNG)

문장 생성은 이전에 예측된 단어에 의존해야 하므로, 디코더 계층의 입력 시퀀스 Y의 t번째 요소이전에 파생된 쿼리를 self attention 연산을 통해 계산한다.  Y는 입력벡터의 시퀀스, Smask는 시간에 따른 self-attention 결과 벡터이다. 그 결과로 뉴럴네트워크를 통과 후 softmax를 통해  t+1의 단어를 예측한다.

###  3.3 Trainig details

![modification_10](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\modification_10.PNG)

기존의 다른 이미지 캡션 모델들 처럼 word-level crossentropy loss (XE) 를 사용하여 학습을 한다. 

훈련시에는 이전 단어가 주어진 경우 다음 단어를 예측하는 방식으로 (일반적인 방식)예측을 통해 학습한다.

위처럼 강화학습을 통해 학습할때 빔서치 알고리즘을 사용 (연산량 ㄷㄷ) 이때, 출력 토큰을 계싼하는 데 사용되는 중간 key value는 병렬 연산이 가능!

메트릭스 평가는 CIDEr-D를 사용하는데 요건 정리가 따로 필요해보인다 ㅠ (인간의 판단과 가장 유사하다고 한다)

평균을 보상으로 삼았고(label 값) 이경우 스코어가 더 상승한다고 한다. ->  b = P i r(wi ) 

# 4. Experiments

COCO 데이터셋을 통해 모델을 평가하고 TextCaps로 모델을 평가(TextCaps로 평가하는 코드는 자세히 살펴보자!)

COCO는 이미지다 5개의 캡션 120,000개의 이미지가 있다.

![table_2](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\table_2.PNG)

![table_3](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\table_3.PNG)

![table_1](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\table_1.PNG)



![example_2](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\example_2.PNG)![example_1](D:\code\whtngus.github.io\img\2021\Meshed-Memory_Transformer_for_Image_Captioning\example_1.PNG)

결과와 예시드 설명 생략 (그림 을보면 M2가 다른모델애 비해 확실히 좋은지는 판단이 안된다 더 보면서 정리를 해야할듯!)
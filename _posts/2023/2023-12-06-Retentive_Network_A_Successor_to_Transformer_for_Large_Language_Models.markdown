---
layout: post
title: "Retentive Network: A Successor to Transformer for Large Language Models"
date: 2023-12-09 02:05:23 +0900
category: paper
---



# Retentive Network: A Successor to Transformer for Large Language Models

2023년 2월 9일 최초 아카이빙

Microsoft Research

code : https://aka.ms/retnet.



# Abstract

![f_1](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f_1.PNG)

LLM을 위한  Retentive Network (RETNET) 모델을 제안

이 모델을 통해 inference 성능 최적화(속도, 정확도)를 달성했다고 함 

모델에서 제안하는 retention mechanism 메커티즘은 attention + lstm 을 합친것으로 보임 

```
The only way to discover the limits of the possible is to go beyond them into the impossible
Arthur C. Clarke
```

#  1 Introduction

transformer가 사실상 LLM의 시대를 열었으나,  transformer의 명렬학습의 효율성이 매우 떨어지는 문제가 있음 

![f_2](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f_2.PNG)

위의 사진 2를 impossible triangle 이라고 함    코스트, 성능, 병렬학습

해당 아이디어를 위한 3가지 메인 리서치가 있음 

1. linearized attention approximates

attention을 exp(qk)의 커널 ϕ(q) · ϕ(k)을 recurrent 형식으로 바꿈 

-> 그러나 트랜스포머보다 성능은 안좋았다고 함 

2. 효율적인 inference를 위해 training parellelism을 버림 

??? -> 일단 성능이 너무 안좋았다고함

3. attention 대신 다른 메커즘을 사용 

S4,  방법이 있으나 Transformer와 비교 방식이 별로?



이를 해결하기 위해 

low-cost inference, 긴 토큰 임베딩이 가능한 RetNet(retentive networks)를 제안함

또한 multi-head attention을 대체할 multi-scale retention mechanism 을 제안 

multi-scael retention mechanism의 장점

1. gpu 를 최대한으로 사용
2. 메모리 복잡도 1의 inference 비용 (key-value cache trick을 사용했다고함)
3. chunkwise recurrent representation를 통해 long-sequence 임베딩 가능 

7B 모델로 8k의 시퀀스도 가능 (입력 길이에 구애받지 않음)

transformer decoder 모델에 비해 8.4배 빠르고 70%의 메모리를 절약할 수 있다고 함 

transformer와 비교하면 25~50%의 메모리 그리고 7배정도의 속도 향상을 얻을 수 있다고 함 



# 2 Retentive Networks

RetNet은 Transformer기반의 L 블럭을 쌓아서 만듦 (redidual connection과 비슷한 형식이라고함 )



RetNet block 은 두가지 모듈을 포함함 

1. MSR(multi-scale retention)
2. FFN(feed-forward network)



input sequence : x = x1 · · · x|x|

dmodel : hidden demention

X^l = RetNetl(X^(l−1)), l ∈ [1, L].  -> 해당 수식으로 봤을땐 transformer나 lstm의decoder와 같아보임



## 2.1 Retention

입력값에 대해 one-dimentional function을 수행

v(n) = Xn · wV

![f1](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f1.PNG)

sn : state vector 

다음 스테이터 벡터를 계산하기 위해 이전스테이터 벡터에 d*d 차원 메트릭과 전체 입력에 d차원곱을 더한값을 계산 -> 이러면 k의 d값은 결국 입력 시퀀스만큼 증가

아래 o 수식은 이전 m개의 시퀀스만 보고 계산  -> 이래서 필요한 파라미터 수가 적다고 말한듯 

![f2](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f2.PNG)

Q와 K를 만드는 방법은 기존 transformer와 같음 

Wq와 Wk는 d*d demention 학습 파라미터

![f3](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f3.PNG)

행렬분해를 활용해 on 의 n-m ~ n 을 계산 

![f4](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f4.PNG)

#### The Parallel Representation of Retention 

![f_3](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f_3.PNG)

![f5](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f5.PNG)

복잡해 보이는데 V K Q를 이용한 트랜스포머를 LSTM 형식으로 바꾼걸로 보임

#### The Recurrent Representation of Retention

![f6](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f6.PNG)

![f7](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f8.PNG)

특히 long sequence 데이터에서 빠른 학습이 가능하다고 함 

입력을 chunk 단위로 자름 - 위의 수식을 통해 recurrent한 모델을 만듦) 

위 수식에서  B는 chunk 사이즈

## 2.2 Gated Multi-Scale Retention

MSR(multi-scale retention)은 각각의 다른해드 r 값을 사용 

![f8](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f8.PNG)

![f_4](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f_4.PNG)

수도코드를 이렇게도 올려도 되는구나 

### Retention Score Normalization

QK, D, R 을 d, 합계, 합계로 normalize함 



## 2.3 Overall Architecture of Retention Networks

![f9](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f9.PNG)

redidual connection 같이 사용 



- Training

![t_1](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\t_1.PNG)

생략 .. 



# 3 Experiments

1.3B, 2.7B, and 6.7B. RetNet 모델을 비교함 -> 모델 사이즈가 기존 LLM대비 크진 않음

![t-2](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f_5.PNG)

![t-2](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\t-2.PNG)

![t_34](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\t_34.PNG)

일단 내꺼에서는 1.3B모델도 학습은 안되네 

8192 sequence length 로 512 chunk size,  a100-80gb 8개로 t_4 결과를 냄 

-> 해당 모델이 a100에 최적화 되었다고 함



![f_6](F:\code\whtngus.github.io\img\2023\Retentive_Network_A_Successor_to_Transformer_for_Large_Language_Models\f_6.PNG)

모델 속도가 입력 seq길이에 상관없이 동일하다는걸 보여주고 있음 


































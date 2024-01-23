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



하나의 gpu 에서 24시간 학습 만으로 chatGPT 의 99.3% 성능을 달성했다고 함 



아래와같은 방법을 통해 정확도의 감소 없이 메모리를 최적화 시킴

1. 4-bit NormalFloat(NF4) -> 새로운 data type 적용 
2. 이중 양자화 사용 ->  ?? 아래 설명 봐야할듯
3. Paged Optimizers를 활용한 메모리 급증 관리 



QLoRA를 이용해 1000가지 이상 모델을 fine tuning 해보고 테스트해봤다고 함 

# 1 Introduction

LLM을 fine-tuning하는건 성능을 향상시키고 바람직하지 않은 대답을 하는걸 막아줄 수 있다. 하지만 fine-tuning은 매우 많은 gpu를 소모함

LLaMA 65B의 경우 780GB gpu memory가 필요하다고 함 



해당 QLoRA에서 4bit로 양자화해도 성능이 내려가지 않음을 보이고 작은 학습 low-rank adapter weight를 추가함 -> 이때 backpropagation도 4bit를 사용



780GB 보다 더 사양되는 메모리를 48GB 이하로 사용하도록 내림  + 16bit와 비교해도 성능이 내려가지 않음을 보임 



Guanaco familiy model(중남미 낙타 4종류인 Llama, Alpaca, Vicuna, Guanaco) 과나코만 없어서 나머지 멤버로 부른듯

Guanaco familiy model 모델 메모리를 줄이고 97.8 %의 성능을 유지했다고 함 

하나의 gpu 모델에서 24시간 이상 학습시 99.3%성능을 달성함 



![t_6](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\t_6.PNG)

위의 table 6에서 최적화를 한 후 성능 비교로 전부 48gb이하로 보임 

-> 24gpu 에서 13B까지 학습 가능해 보임 ...  시도해볼 만 하겠는데



QLORA는 성능을 희생하지 않으면서 메모리를 줄이기 위한 혁신정인 방법 3가지를 제안함

1. 4-Bit NormalFloat

   이론적으로 최적의 양자화 유형이라고 함 

2. Double Quantization

   양자화 상수를 양자화함 -> 파라미터당 평균 0.37비트를 적약한다고 함 

   -> 65BG 면  3GB를 절약함

3. Paged Optimizers

   NVIDIA로 구성된 메모리에서 메모리가 spike되는 현상을 막기 위해 long sequence에 대한 mini-batch를 사용함 

    -> squence 가 길어지면 gpu 터지는경우가 많았는데 꼭 활용 해야할듯



# 2 Background

### Block-wise k-bit Quantization

양자화 처리는 입력에 대한 정보를 유지하며 discretize(연속적인 공간을 나눔)

일반적으로 fewer-bit로 양자화 하기 위해 32-bit floats 을 8-bit integers로 나누는 작업이 있음

![f1](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\f1.PNG)

방법은 위 수식 1과 같음

float32 에서 [-127, 127]범위의 int8로 양자화 하기 위해서 maximum값으로 나눠서 -> 127로 곱해주고 round 시킴 

![f2](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\f2.PNG)

c는 quantization constant or quantization scale로 불리며 위의 수식은 역양자화를 진행(Dequantization)

수식1에서 양자화를 위해 곱해줬던 값을 반대로 나눠줌 



여기에서 문제는 큰 규모의 값이 입력으로 들어노는 경우 (아웃라이어) quantization bins의 일부 bin에서 숫자가 거의 없어 잘 작동하지 않는 문제가 발생함 

이러한 아웃라이어 이슈를 해결하기 위해서 일반적인 접근 방법인 chunk 방식을 사용함 

input tensor block에 대해서 독립적인 양자화 상수를 갖는 블록으로 청킹함 



b는 input tensor의 크기이고, n은 size B의 연속된 값 이고 n = (b*h)/B  Blocks로 이루어짐 

X 는 R^b*h 차원의 연속된 B 블록으로 슬라이스하여 청킹함 위의 수식1을 이용하여 독립적으로 n개의 양자화를 진행 

설명은 없지만 -> b는 bining 수 h는 hidden state vector로 추정됨

### Low-rank Adapters 

Low-rank Adapter (LoRA) finetuning은 작은 학습 파라미터를 사용함으로써 학습메모리를 감소시킨다.

-> 모델을 전부 업데이트 하지 않고 기존 모델을 fix 시킴 

![f3](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\f3.PNG)

원래의 모델 xw = y 에서  입력을 autoencoder 방식으로 사용하는 L1L2를 추가함 

### Memory Requirement of Parameter-Efficient Finetuning

![f_6](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\f_6.PNG)

LoRA의 메모리가 요구하는 학습량은 중요한 포인트임 

-> LoRA의 메모리 footprint는 매우 적기 때문에  메모리를 크게 늘리지 않고 성능을 향상시키기 위해 adpater를 사용할 수 있음 

7B LLaMA 모델에서 LoRA는 학습하기 위해 567MB의 gradient 메모리를 필요로 하고 자체적인 모델 크기는 26MB로 매우 적음 

여기에서 4-bit 양자화를 통해 5,048 MB 메모리를 아낌 



# 3 QLORA Finetuning

### 4-bit NormalFloat Quantization

 NormalFloat (NF) data type을 만듦  -  Quantile Quantization(분위 양자화)를 사용함 

위에서 설명한 대로 Quantile Quantization를 진행 시 양자화에 많은 비용이 듦 그래서 빠른 최적화 알고리즘을 적용함

최적화 양자화 알고리즘 예시로 SRAM quantiles가 있는데  -> 추정치를 사용하기 때문에 큰 데이터의 양자화의 오류에서 벗어나지 못함 

 

이러한 비싼 연산비용의 오류는 양자화 상수와 분포가 고정되면 피할 수 있음 



그런데 pretrained 된 모델의 경우학습 wights가 zero-centered normal distribution 분포의 성향을 띈다고 함 - standard deviation σ

-> 그래서 그냥 양자화 범위를 [-1, 1]로 임의로 정함 

(모든 범위를 다 커버할수 있다를 아래에서 설명 ~~~ 생략 ) + 특별한 이유들이 있지만 이해를 못함 ㅠ

### Double Quantization

Double Quantization (DQ)를 제안함 

양자화 상수를 양자화 하면 메모리를 절약할 수 있음 

4비트 양자화를 위해선 small blocksize가 필요하지만 이또한 메모리 오버헤드를 가짐 

 ex) 64비트 크기의 w에 32비트 양자화 상수를 이용하면 파라미터 당 32/64 = 0.5 비트 메모리를 더 소모하게됨 

   이를 최적화 하기 위해 DQ를 적용  (weight 2개당 상수 공간 하나 사용)

8비트 양자화 상수 적용 후  256 블럭 사이즈의(8-bit) 32비트 양자화 상수를 두번째 이용함 

이렇게 하면 소모되는 메모리 양이 32/64 = 0.5  에서  

블록사이즈 64를 기준으로 8/64 + 32/(64*256) = 0.127  

   ->  8/64는 블럭사이즈 64당 8비트 양자화 상수를 사용해서

 -> 뒤는 블럭사이즈 256에 64bit개의 비트에서 32bit양자화를 사용함

그럼 weight ekd 0.373 비트를 아낄 수 있음 

### Paged Optimizers

NVIDIA 통합 메모리 기능을 사용

cpu gpu간의 스왑을 사용함 

### QLORA. 

![f5](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\f5.PNG)

기존 입력에 LoRA를 활용하기전 doubleDequat를 이용해 4비트로 양자화 함

-> 위의 식 5는 LoLA에서 사용하는 학습 weight는 양자화를 시키지 않음 

![f6](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\f6.PNG)

doubleDequat 에 대한 설명  

# 4 QLoRA vs. Standard Finetuning

![f_2](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\f_2.PNG)

4bit 스코어가 오히려 더 높은거같네? 

RougeL은 최장길이 매칭 스코어로 매칭이 잘 될수록 높은 스코어 



이하 스코어 월등함... 생략









# 참고

1. FLAN

https://learn-ai.tistory.com/entry/Paper-Review-FLAN-Finetuned-Language-Models-Are-Zero-Shot-Learners

instruction tuning의 결과 모델을 *FLAN*이라 함



in-context learning을 적용하여 few-shot 성능을 향상시키는 대신에 instruction tuning을 사용해 zero-shot 성능을 향상시키는 method에 대해 다룬다. 

![flan_1](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\flan_1.PNG)

![flan_2](F:\code\whtngus.github.io\img\2024\QLORA-Efficient-Finetuning-of-Quantized-LLMs\flan_2.PNG)

nlu, nlg를 포함한 62개의 데이터샛에 대해 각 10개의 instruction templte를 구성함 (구중 3개는 데이터셋과 상관 없는 template를 만듬 )

템플릿은 랜덤으로 생성하여 사용 




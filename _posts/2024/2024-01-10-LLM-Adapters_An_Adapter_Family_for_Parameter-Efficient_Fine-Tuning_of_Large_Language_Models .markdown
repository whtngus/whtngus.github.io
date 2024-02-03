---
layout: post
title: "LLM-Adapters: An Adapter Family for Parameter-Efficient Fine-Tuning of Large Language Models"
date: 2024-02-03 02:05:23 +0900
category: paper
---

# LLM-Adapters: An Adapter Family for Parameter-Efficient Fine-Tuning of Large Language Models

2023년 10월 9일 

url : https://arxiv.org/abs/2304.01933

EMNLP 2023

학생 



# Abstract

GPT-4와 ChatGPT가 나오면서 fine-tunig 대신 open-access LLM 방식이나  instruction data 방식을 사용하게 됨 

PEFT 방식은 일부 파라미터만 학습하는 좋은 방식이고 계속해서 연구되고 있다.



LLM은  LLaMA, BLOOM, and GPT-J등 

-> 최근 게재된 논문이지만 참조되는 논문은 오래된 논문이 많음을 감안해야할듯

2가지 테스크의 14개의 테스크 데이터셋을 이용해 PEFT와 smaller-scale LLM(7B)를 학습하고 평가함 

# 1 Introduction

Chat-GPT와 GPT-4가 NLP에서 엄청난 퍼포먼스를 보임

-> 이렇게 되면서 대규모 모델과 비공개 코드가 다시 많이지게됨 (공개해줘 ㅠ)



이를 해결하기 위해 비용효율이 높은 학습 방법이 연구되었고 예시로 LLaMA모델이 나오게됨

(LLaMA는 ChatDoctor, instructional data 를 통해 학습)

그래도 FFT(Full-model Fine-Tuning)을 하기엔 모델이 매우 큼... (BERT때도 프리트레이닝 하기엔 충분히 컸는데)

이렇게 되면서 현실적인 최적화 연구가 시작됨

![t_1](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\t_1.PNG)

PEFT 방법은 위의 4가지 기본 방법에 의해 분류됨 



해당 연구에서는 3개의 오픈소스를 기반으로 PEFT를 비교함  

-> BLOOM, GPT-J, LLaMA

# 2 PEFT Overview

![f_1](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\f_1.PNG)

### Prompt-based learning.

프롬프트 기반 학습은 최적의 결과를 찾는 discrete optimization과 이산 최적화 문제를 찾는연속적인 soft promp가 존재함 



input embedding에 학습 가능한 레이어를 삽입 - Prefix Tuning

그 외에도 autoencoder를 사용하는 prompt tuning 이 있음 

![f1](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\f1.PNG)

Hi : input      -> T*d 차원

Ho : output    -> T*d 차원

T : 입력 최대 길이 

Pk, Pv : PEFT의 학습 벡터  -> L*d 차원 벡터 

L : 학습 토큰 번호 

### Reparametrization-based method.

![f2](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\f2.PNG)

low-rank technique 방식을 사용 

학습 파라미터를 효과적으로 줄인 방법

W0 : MLP Layer를 포함한 pre-trained weight 

B, A : r*d 차원으로 lower-rank metric 

-> 아래 참고에서 추가 정리함

### Series Adapter.

![f3](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\f3.PNG)

위의 그림1 참조 

### Parallel Adapter.

![f4](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\f4.PNG)

요거도 그림참조 

# 3 Experiment Setup

## 3.1 Benchmarks

![t2](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\t2.PNG)

14개의 데이터셋을 가지고 테스트를 수행함 

- 산술 추론

GSM8K - 고품질 언어로 수학 단어 문제

SVAMP -  하나의 산술 단어를 블럭처리하고 맞추는 작업 

MultiArith - multiple reasoning steps

AddSub - 더하기 빼기 산술 문제 

AQuA - 유리수 대수학 문제 

SingleEq - 초등학교 수준의 수학 문제 

- 상식  추론
- ​

... 이하 생략 - 테이블 참조

## 3.2 Fine-tuning Data Collection

GSM8K과 AQuA 데이터셋만 수학 training 셋트를 제공함 

다양성을 향상시키기 위해 AQuA 에서 1000개의 데이터 추출 

.. 생략

### 3.3 Implementations

편한 실험을 위해 프레임워크를 만들었다고함 

실험 모델 크기는 아래와 같음 

 LLaMA (7B, 13B) , BLOOMz (7B), GPT-J (6B), 

# 4 Experiment Results

## 4.1 Placement and Configuration (다음 목차부터 생략)

![f_2](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\f_2.PNG)

실험 결과 LLaMA-7B 모델이 optimal 하기에 최적이라고함 (아래 t3참조) 그냥 llama가 다른 두 모델보다는 확실히 잘함

![t_3](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\t_3.PNG)



![t_4](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\t_4.PNG)







# 참고지식

- BLOOM

약 1,000명 정도의 학술 자원봉사자로 구성된 공개 협업 프로젝트인 빅사이언스(BigScience)에서 개발 

-> 2022년도 개발됨 

- GPT-J

마찬가지로 2022년도 모델

GPT-3의 오픈소스 버전

 60억 개 파라미터 (6B)

- PEFT 기법들

adapater : 기존에 이미 학습이 완료된 모델의 사이사이에 학습 가능한 작은 feed-forward network를 사입하는 구조

LoRA(**Lo**w-**R**ank **A**daptation)의 개념을 간단하게 설명하자면, 고정된 weights를 갖는 pretrained model에 학습이 가능한 rank decomposition 행렬을 삽입한것 -> 적은수의 파라미터로 학습용이

- rank decomposition

![LoRA](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\LoRA.PNG)

f레이어 중간에 존재하는 hidden states h 값을 더해줄 수 있는 파라미터를 추가해 모델의 출력 값을 원하는 타겟 레이블에 맞게 튜닝 하는 개념 

- Prompt Tuning

![prompt_tuning](\img\2024\LLM-Adapters_An_Adapter_Family_for_Parameter-Efficient_Fine-Tuning_of_Large_Language_Models\prompt_tuning.PNG)

모델에게 전달되는 입력 프롬프트를 정제/조정하여 더 정확하고, 관련성 높은 답변을 유도하는 과정

양한 프롬프트 조합을 반복적으로 조합해서 모델의 출력을 향상 ->각각의 테스크 데이터를 섞어서 사용 

- **Reparametrization-based Method**

낮은 순위 표현을 활용하여 훈련 가능한 매개변수 수를 최소화







# 참고

- PEFT 기법들

https://devocean.sk.com/blog/techBoardDetail.do?ID=164779&boardType=techBlog

https://blog.kubwa.co.kr/peft-%ED%9A%A8%EC%9C%A8%EC%A0%81-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-%ED%8C%8C%EC%9D%B8-%ED%8A%9C%EB%8B%9D-%ED%99%9C%EC%9A%A9%ED%95%9C-%EC%84%B1%EB%8A%A5-%EC%B5%9C%EC%A0%81%ED%99%94-%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8-%ED%8A%9C%EB%8B%9D-%EB%94%A5%EB%8B%A4%EC%9D%B4%EB%B8%8C-573339ea21b2
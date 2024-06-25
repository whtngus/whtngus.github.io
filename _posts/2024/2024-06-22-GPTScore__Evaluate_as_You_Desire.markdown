---
layout: post
title: "GPTScore: Evaluate as You Desire"
date: 2024-06-25 02:05:23 +0900
category: paper
---

# GPTScore: Evaluate as You Desire

github : https://github.com/jinlanfu/GPTScore

paper : https://arxiv.org/abs/2302.04166

2023년 2월 8일



# Abstract

생성모델은 텍스트 뿐만아니라 이미지 등 다양한 생성을 잘 하고 있으나 생성품질을 측정하기는 매우 힘듦

본 논문에서 이를 해결하기 위해 GPTSCORE 프레임워크를 제안함 

 19 pre-trained models로 평가함  

80M(FLANT-T5-small) 부터 175B(GPT3까지 다양한 모델 사용)

22개의 관점에 해당하는 37개의 데이터셋을 통해 보여줌 

# 1. Introduction

![f_1](\img\2024\GPTScore__Evaluate_as_You_Desire\f_1.PNG)

GPT3 이후 텍스트 생성 기술이 빠르게 증가함에 따라 위의 그림 1과 같은 평가 방법들이 생김

- (그림1 좌측) a

기존 연구로 제한된 측면으로 텍스트 품질을 평가함 

- (그림1 가운데) b

몇개의 소수 연구중에서 다중 관점에 대한 평가를 진행

그러나 평가 시 latent relationship에 대한 관계를 평가하지 못함



위 두 평가 방법으로 복잡한 훈련 절차와 데이터 생성에 비용이 많이 필요함 

- (그림1 우측) c

논문에서 제한하는 평가 방법으로 GPT-3 와 같은 모델을 사용해 

학습을 하지않고 평가할 수 있는 방법 

![f_2](\img\2024\GPTScore__Evaluate_as_You_Desire\f_2.PNG)

그림 2와 같은 프로콜을 사요함 

(a) Task Specification : 전형적으로 어떻게 텍스트를 새성할지를 명시 

(b) Aspect Definition : 문서에 대한 바람직한 평가 방법

그 후 각 평가에대한 셈플을 제시함 (왼쪽 그림의 우축 위)

마지막으로 이정보를 GPT 모델을 통해 계산함



생성형 pretrained 모델을 아래와 같은 경우 더 신뢰할 수 있음 

1. 다양한 평가 기준을 수용할 수 있는 유연성을 제공함 

2. 다른 평과측면과 함께 정의들을 고도로 결합하여 상호 연관된 측면의 성능평가가 가능 

3. 사람의 피드백을 기반으로 튜닝된 GPT3-text-davinci-003는  GPT3-text-davinci-001보다 성능이 떨어짐 

   이와같은 깊은 탐색이 필요 

# 2. Preliminaries

## 2.1. Text Evaluation

텍스트를 평가하는 목표는 생성된 텍스트 h에 대한 a관점에서의 평가를 하는것임 

![f1](\img\2024\GPTScore__Evaluate_as_You_Desire\f1.PNG)

h : 평가 될 텍스트

a : 평가 관점 (예시 : 유창성)

S : 다른 시나리오를 기반으로 선택적으로 사용되는 추가 텍스트 모음 

### 2.2. Meta Evaluation

meta evaluation은 사람이평가한 y_human 과 자동으로 평가한 y_auto가 유사하게 나오는걸 목표로함 

평가 지표는

1. Spearman(p)

스피어먼 상관 계수는 [순위가 매겨진 변수](https://ko.wikipedia.org/wiki/%EC%88%9C%EC%9C%84) 간의 [피어슨 상관 계수](https://ko.wikipedia.org/wiki/%ED%94%BC%EC%96%B4%EC%8A%A8_%EC%83%81%EA%B4%80_%EA%B3%84%EC%88%98) 로 정의

2. Pearson(r)

두 변수간의 선형 상관관계를 계량화한 수치

으로 평가 

## 2.3. Evaluation Strategy

#### Sample-level

![f2](\img\2024\GPTScore__Evaluate_as_You_Desire\f2.PNG)

g 는 Spearman or Pearson 상관계수

결국 각 상관계수를 하나씩 비교하겠다는소리

#### Dataset-level 

![f3](\img\2024\GPTScore__Evaluate_as_You_Desire\f3.PNG)

n개의 셈플에 대해 상관계수를 구함 

# 3. GPTSCORE

## 3.1. Generative Pre-trained Language Model

Pretrained 된 LM을 3가지 기준으로 분류 진행 

a : encoder-only model (bert)

b :  encoderdecoder models (bart, t5)

3 :  decoder-only models (gpt-2, 3 , PaLM)

![f4](\img\2024\GPTScore__Evaluate_as_You_Desire\f4.PNG)

주어진 프롬프트 입력 x와 순차적으로 생성되는 y 의 확률값을 수식으로 표현하것

## 3.2. Generative Pretraining Score (GPTScore)

GPTScore 아이디어는 모델에 주어진 명령과 컨텍스트에 따라 고푸질 텍스트가 생성될 확률이 높기 때문

![f5](\img\2024\GPTScore__Evaluate_as_You_Desire\f5.PNG)d : description

a : aspect definition

h : 평가받을 텍스트

w_t : 토큰 위치에 t 대한 weight

T() : 프롬프트 템플릿

#### Few-shot with Demonstratio

GPT는 몇개의 정의된 셈플이 있으면 더 성능이 좋아짐 

그걸 위해 템플릿 T 에 설명을 추가 

#### Choice of Prompt Templat

프롬프트 템플릿은 테스크,  관점을 정의하고 컨텍스트를 구성함 

NaturalInstruction을 사용함

#### Selection of Scoring Dimension

프롬프트로 다양한 기준을 설정하기에 따라 원하는 scoring을 할 수 있음 

# 4. Experimental Settings

## 4.1. Tasks, Datasets, and Aspects

![t_8](\img\2024\GPTScore__Evaluate_as_You_Desire\t_8.PNG)

natural language generation tasks: Dialogue Response Generation, Text Summarization, Data-toText, and Machine Translation, which involves 37 datasets

과22 evaluation aspects in total 로 평가함 

#### (1) Dialogue Response Generation

아래는 cahtgpt 로 가볍게 번역해서 끝냄

**대화 생성 (Dialogue Generation)**:

- **FED (Mehri & Eskénazi, 2020)** 데이터셋을 사용하여 대화 생성 모델을 평가합니다. 여기서는 턴 수준(turn-level)과 대화 수준(dialogue-level) 평가를 모두 고려합니다.

**텍스트 요약 (Text Summarization)**:

- 주어진 긴 텍스트에 대해 정보가 풍부하고 유창한 요약을 자동으로 생성하는 작업입니다. 여기서 고려된 데이터셋은 다음과 같습니다:
  - **SummEval (Bhandari et al., 2020)**
  - **REALSumm (Bhandari et al., 2020)**
  - **NEWSROOM (Grusky et al., 2018)**
  - **QAGS_XSUM (Wang et al., 2020)**: 이 데이터셋들은 10가지 측면을 다룹니다.

**데이터-텍스트 생성 (Data-to-Text Generation)**:

- 주어진 표에 대해 유창하고 사실적인 설명을 자동으로 생성하는 작업입니다. 여기서 고려된 데이터셋은 다음과 같습니다:
  - **BAGEL (Mairesse et al., 2010)**
  - **SFRES (Wen et al., 2015)**

**기계 번역 (Machine Translation)**:

- 한 언어에서 다른 언어로 문장을 번역하는 작업입니다. 여기서는 다차원 품질 측정(MQM, Multidimensional Quality Metrics) 데이터셋의 하위 데이터셋인 **MQM-2020 (중국어->영어)**를 고려합니다.

## 4.2. Scoring Models

![다t_2](\img\2024\GPTScore__Evaluate_as_You_Desire\t_2.PNG)

다양한 모델과 ROUGE-1, ROUGE-2, ROUGE-L, PRISM 방법등 다양한 방법을 이용해 평가함 

* PRISM은 뭔지 모르겠음..

## 4.3. Scoring Dimension

??

## 4.4. Evaluation Dataset Construction

생략

# 5. Experiment Results

생략..













# 참고

- NaturalInstruction

![NaturalInstruction](\img\2024\GPTScore__Evaluate_as_You_Desire\NaturalInstruction.PNG)

Definition : task 수행을 위한 instruction

Positive examples : input / correct output / 관련 설명으로 구성

Negative examples : input / incorrect output / 관련 설명으로 구성◦

Evaluation instances : Tk-Instruct 및 mTk-Instruct 모델 학습에는 사용하지 않고 evaluation에만 사용하는 테스트 데이터. Task별 밸런스를 맞추기 위하여 최대 6500개로 제한

참고 : https://blog.sionic.ai/super_naturalinstructions
















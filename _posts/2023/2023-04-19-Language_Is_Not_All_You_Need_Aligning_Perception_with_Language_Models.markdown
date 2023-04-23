---
layout: post
title: "Language Is Not All You Need: Aligning Perception with Language Models"
date: 2023-04-24 00:05:23 +0900
category: paper
---

# Language Is Not All You Need: Aligning Perception with Language Models

2023년 2월 27일(최초) -> 3월 1일

Microsoft

paper : https://arxiv.org/pdf/2302.14045.pdf

code : https://github.com/microsoft/unilm

# Abstract

Multimodal Large Language Model (MLLM)로 이미지 이해, 멀티모달, 생성등 다양한 AI 테스크를 수행하는 모델 

여기서 제안하는 이 모델을 KOSMOS-1 로 이름을 정의

인터넷상의 이미지 텍스트 데이터를 이용해  이미지 캡션 페어 데이터를 학습



KOSMOS-1의 컨트리뷰션 내용

1. NLU, generation, OCR-free NLP 등의 테스크
2. perception-languge task

멀티모달 다이얼로그, 이미지 캡션, VQA등의 테스크

3. vision task

이미지 인식, description등 

머티모달간  지식 전이에서 강한 특징을 보임

(Raven IQ test dataset) 등



아래는 실행 결과

![f_2](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\f_2.PNG)

![f_3](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\f_3.PNG)

# 1 Introduction: From LLMs to MLLMs

![f_1](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\f_1.PNG)

최근 LLM은 NLP general-purpose를 성공적으로 잘 수행하고 있다.

그럼에도, 멀티모달 데이터에서는 아직 부족함을 보임 (Text, Image, Audio)

해당 논문을 통해 KOSMOS-1 모델로 이를 해결함

![t_1](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\t_1.PNG)

위 테이블은 그 결과로 거의 모든것을 zero shot 러닝을 통해 지원(실행 결과는 더 위에 figure 2, 3 참조)

-> vision, nlp, 그리고 멀티모달 까지 다양한 테스크를 지원

또한 IQ test benchmark를 통해 모델의 높은 이해도를 보임

### From LLMs to MLLMs

LLM은 상식이나 지식에대한 설명을 할 수 있고 여러 기계적인 테스크 수행 가능하며 여러 API를 제공할 수 있음

MLLM은 screen이나 영수증등을 직접적으로 읽고 처리할 수있으며(멀티모달) web-scale, 그리고 다양한 지식 정보를 web-scale로 학습함으로 써 다양한 정보에도 강함



KOSMOS-1은 대규모 corpora 뿐만 아니라 인터넷 상의 잘 절제된 문서의 image-caption pair 데이터도  학습

### New capabilities of MLLMs

Table1 에서 이미 보임(멀티모달, 다양한 테스크 등)



# 2 KOSMOS-1: A Multimodal Large Language Model

Figure 1에서 생성 general modality를 위해 특정 방식의 템플릿을 정의 

다른 모델과 비슷하게 KOSMOS-1 역시 Transformer-based causal language model 임

KOSMOS-1은 monomodal(다붕분포)를 포함한 데이터를  학습

## 2.1  Input Representation

![t_21](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\t_21.PNG)

general modality를 위해 특정 포맷을 정의

flatten 입력을 받으며 

\<s\> 와 \</s\> 토큰으로 문서를 구분  

\<image\> 와 \</image\> 토큰으로 embedding image를 구분

-> 이미지 임베딩의 경우 pooling mechanism을 통해 Resampler함 (입력차원 크기 때문인듯)

## 2.2 Multimodal Large Language Models (MLLMs)

2.1에서 입력 스퀀스를 임베딩한 후 디코더의 입력으로 줌 (여기도 역시나 Transformer-base) 

학습을 위해 casual masking을 사용하고 토큰 생성시에 softmax 사용

대규모 데이터 학습시 TorchScale을 사용 

- MAGNETO

transfomer backbone architecture로 MAGNETO 사용

안정적인 학습을 지원한다고 함

MAGNETO 설명으로 extra LayerNorm to each sublayer

그리고 효율적인 initialization 지원으로 빠른 optimization을 도움

- xPos(Extrapolatable Position Embedding)

xPos position encoding을 사용 

긴 context의 데이터가 들어온경우의 모델링시 훨씬 안정적이라고 함 

또한 보간법 extrapolation에 효율적이라고 함

## 2.3 Training Objective

multimodal corpora 뿐만 아니라 monomodal 데이터도 학습

monomodal - ex  text corpus

cross-modal paired data  - ex image-caption pair

interleaved multimodal data  - ex 임의의 문서에서 interleave한 텍스트와 사진



모델은 next-token prediction 을 통해 학습 (디코더)

training objective : maximize log-likelihood (각 다음 토큰 예측시)

# 3 Model Training

## 3.1 Multimodal Training Data

학습 데이터는 text corpora, image-caption pair, 이미지와 텍스트의 interleaved data로 구성됨

- Text Corpora

![t_20](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\t_20.PNG)

Pile과 Common Crawl(CC)를 통해 데이터 수집 

Pile은 영어 데이터를 대규모로 수집 -> 여기에 github, arxiv, stack Exchange, pubmed central 데이터를 확장함

Common Crawl은  snapshots 데이터셋, + CC-Stories, RealNews dataset을 사용

여기에서 중복 혹은 거의 비슷한 문서는 삭제함 

- Image-Caption Pairs

English LAION-2B, LAION-400M,  COYO-700M, Conceptual Captions 사용

(위의 데이터 중 앞의 3개는 Common Crawl web 을 통해 추출된 iamge 와 all text 데이터)

- Interleaved Image-Text Data

Common Crawl snapshot을 통해 데이터를수집

71M web page를 수집(전체 2B web page에서 정제한 데이터)

## 3.2 Training Setup

24 layers with 2,048 hidden dimensions 그리고 8192사이즈의 FFN 사용

32 attention heads

총 1.3B parameter 

(gpt2 small(117M), medium(345M), large(762M), extra-large(1,542M) 와 비교해서 보면 될듯)

## 3.3 Language-Only Instruction Tuning

![t_19](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\t_19.PNG)

위는 Language-Only 학습시

Unnatural Instructions과 FLANv2를 조합하여 데이터셋을 사용

자연스럽지 않은 데이터에서 자연스러운 데이터를 생성(68,478 instruction-input-output
triplets in its core dataset)

FLANv2는 NLU 테스크(reading comprehension, commonsense reasoning, and closed-book
question answering)  -> 이중 랜덤으로 54K개를 선택해 사용

# 4 Evaluation

## 4.1 Perceptin Language Tasks

- Image Caption

MS COCO Caption과 Filckr30k dataset을 활용해 평가 진행

few shot learning 방법을 사용해도 높은 정확도를 보임 (테이블이 많아 생략)

Flamingo-3B (비교대상)

- IQ Test

![f_4](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\f_4.PNG)

흥미로운건 이미지와 텍스트가 같이있고 사람도 쉽게 판별하기 어려운 IQ 테스트 내용인데 

정확도가 좋진 않지만 랜덤보다는 높은 스코어로 유의미한 결과가 나옴

![t_6](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\t_6.PNG)

약간 의심이 가는건 저정도 스코어면 그림이나 결과에 약간의 편향이 있다면 그걸로 랜덤보다 높은 스코어가 나올수 있지 않을까 싶음 

- OCR-Free Language Understanding

정확도가 높은 수준 

내용 생략

- Weg Page Question Answering

기존 LLM보다 높은 정확도를 보임 (WebSRC dataset 사용)

- Multimodal Chain-of-Throught Prompting

![f_5](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\f_5.PNG)

정확도를 올리기 위해 두 가지 스텝을 사용

step 1 : 이미지가 들어온 경우 텍스트와 이유를 생성 

step 2 :  step1을 통해 tasks를 이해시켜 최종 결과를 생성 

(결과 좋음 생략)

- Zero-Shot Image Classification

![f_6](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\f_6.PNG)

beam size 2 이며 image는 224*224로 resoution 후 사용 

- Zero-Shot Image Classification with Descriptions

분류와 설명을 동시에하는 테스크로 CUB 데이터셋 사용 

bird classification dataset을 통해 새를 분류하고 (3개의 그룹)

설명 생성

- Language Tasks

생략

- Cross-modal Transfer

: COCO, Flickr30k, VQAv2, and VizWiz 데이터셋을 사용 : CIDEr scores for COCO/Flickr30k and VQA
accuracy for VQAv2/VizWiz. 테스트

![t_14](\img\2023\Language_Is_Not_All_You_Need_Aligning_Perception_with_Language_Models\t_14.PNG)

대락적으로 language-only 보다 멀티모달 학습의 정확도가 더 높음

당연한 것 같은데 coco dataset에서 정확도가 더 안나온건 ...

# 5 Conclusion

해당 논문에서 multimodal large language model 인 KOSMOS-1을 발표

web-scale multimodal corpora 학습 이며 MLLM 용어 사용 -> 높은 성능을 보여 멀티모달 최적화 시킴

부록에 재미있는 내용이 많아 중간중간 구경하기 좋아 보임



-> chatGPT(GPT3.5 GPT4)가 나오면서 기존 연구를 어서 논문화 시키고 털어 내는 줄 알았는데 버전을 명시한걸 보니 지속 연구의지가 보임

-> 모델 사이즈가 전부다 커져서 걱정 ... 



# 참고 지식

- Chain of Thought(COT)

few shot prompting의 일종으로

한 개의답을단계별로 차근차근 나눠 예시를 제공하는 것

- web-scale

대형 클라우드 서비스 제공업체들의 클라우드 운영 방식

글로벌 수준의 대규모 환경에서도 좋은 품질을 제공

- Causality Masking

transformer는 모든 단어를 병렬적으로 처리하기 때문에 연속적 특징이 없기 때문에 

→ 목표하는 문장의 일부를 가려서 인위적으로 연속성을 학습하게 함

- TorchScale

microsoft에서 pytorch 기반으로 Transformer 모델을 효율적으로 학습할 수 있도록 해주는 라이브러리

대규모 모델을 잘 학습하기 위해 만들어졌다고 함

- interleave(인터리브)

데이터가 서로 인접하지 않도록 배열하는 방법 



# 참고
  
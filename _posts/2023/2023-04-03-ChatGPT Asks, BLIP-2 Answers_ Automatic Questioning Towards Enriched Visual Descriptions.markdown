---
layout: post
title: "ChatGPT Asks, BLIP-2 Answers: Automatic Questioning Towards Enriched Visual Descriptions"
date: 2023-04-03 00:05:23 +0900
category: paper
---

# ChatGPT Asks, BLIP-2 Answers: Automatic Questioning Towards Enriched Visual Descriptions

2023년 3월 12일 

kaust 학생

url : https://arxiv.org/abs/2303.06594

code : https://github.com/Vision-CAIR/ChatCaptioner

# Abstract

통찰력 있는 질문은 세상에대한 이해를 높이기 위해 매우 중요함 그러나 AI qa 테스크에서는 이러한 점이 많이 간과되고 있다.

ChatGPT는 높은 수준의 질문 능력을 가지고 있음으로 ChatGPT를 이용해서 자동 question system을 만듦

해당 연구에서는  

ChatCaptioner :  자동 질문 생성방법을 제안 

-> 질문 ChatGPT 답변  BLIP-2 모델을 사용

기존 모델들은 정답 captino을 잘 생성하지만 해당 연구를 통해 중요한 정보를 생성함을 보임 

WordNet synset matching 방법으로 평가함

#  1. Introduction

![f_1](F:\code\whtngus.github.io\img\2023\ChatGPT Asks, BLIP-2 Answers_ Automatic Questioning Towards Enriched Visual Descriptions\f_1.PNG)

질문을 잘 하는것은 모델이 세상을 이해하기 위한 가장 핵심적인 요소.

ChatGPT를 이용해 자동으로 질문하는 시스템과 BLIP-2의 Vision Language모델을 이용해 학습

논문에서 제안하는 이 방식을 ChatCationer라고 명칭

COCO, WikiArt, CC datasets을 이용해 평가 진행  

#  2. Related Works

### Learning to Ask Questions

Question generation -> Visual Question Generation 테스크는 이미지를 보고 질문을 생성 

그러나 답변을 알지 못하고, 답변을 위한 테스크는 아님.

-> 이러한 문제가 있어 해당 연구에서 제안하는 방법은 차이점을 가지고 있음 

- 정보를 더 획득하기 위해 질문을 생성 

VQG에서는 그냥 질문을 위해서만 질문을 생성

- 해당 연구에서는 연속적인 질문을 허용

VQG테스크 에서는 매번 독립적인 질문만을 사용 

### Large Language Model and Prompting

GPT-3, 4 나 PaLM에서 Large Language Model  and Prompting 연구를 진행하고 있음 

이미지에 대한 질의응답도 가능해짐



### Image Captioning and Visual Question Answering

VQA capability of BLIP-2

여기서 베이스라인으로 사용하는 BLIP-2 모델 

# 3. ChatCaptioner

![f_2](F:\code\whtngus.github.io\img\2023\ChatGPT Asks, BLIP-2 Answers_ Automatic Questioning Towards Enriched Visual Descriptions\f_2.PNG)

ChatGPT를 사용해 자동적으로 질문을 생성하고 BLIP-2 Vision-Language model을 이용해 새로운 정보 답을 생성

마지막으로 ChatGPT는 대화 내용을 요약함을써 이미지에 대한 디테일한 캡션을 생성  

-> Figure 2 참조 

## 3.1. Automatic Questioning

ChatGPT의 질문능력을 향상시키기 위해서 3가지 컴포턴트를 포함

Figure 2에서 1 - 구조를 설명, 2- 질의응답, 3- 요약 부분 

> 1. ρtaskQ
>
> 과제를 설명하는 테스크
>
> 2. ρchat
>
> 이전 대화 내요을 이용해 질문과 답변을 하는 시스템 
>
> 3. ρq
>
> 높은 퀄리티의 질문 를 생성



해당 연구에서는 문맥학습을 위해  ρtaskQ + ρchat + ρq   모두 사용 

그후에 자동화된 프로세스로 요약 작업을 통해 캡셔닝을 생성

### ChatGPT Task Instruction 

ρtaskQ는 ChatGPT에서 개요를 설명하기 위해 사용

- ρtaskQ 내용 

```
I have an image. Ask me questions about the content of this image. Carefully asking me informative questions to maximize your information about this image content. Each time ask one question only without giving an answer. Avoid asking yes/no questions. I’ll put my answer beginning with “Answer:”.
```

직접적으로 어떤 질문을 만들어야 할지 셋팅을 진행 

-> 여기에서는 ChatGPT의 GPT-4 버전이 나오기 전에 사용해서 이미지 없이 설명을 한걸로 보임 

* *단점 포인트로 이미지를 이용한 GPT-4를 사용하지 않음*

### Chat Log ρchat

대화 로그 ρchat를 이용해 질문과 답변 형식의 내용을 진행 

```
Question: <question> Answer: <answer>
```

위와 같은 질의응답 후 

직접적으로 "Describe the image in detail" 라는 내용을 입력해 요약 텍스트를 생성 

![f_3](F:\code\whtngus.github.io\img\2023\ChatGPT Asks, BLIP-2 Answers_ Automatic Questioning Towards Enriched Visual Descriptions\f_3.PNG)

Figure 3는 위의 방법을 통해 캡션을 생성한 예시

### Question Instruction ρq 

ChatGPT의 질문 생성을 가이드하기 위해 질문 구조를 ρq로 셋팅 

- 디자인 예시

```
Next Question. Avoid asking yes/no questions. Question:
```

답변이 예 아니오로 나오는걸 방지해서 계속해서 질문을 이어나갈 수 있도록 유지함 

### Question Trimming 

ChatGTP는 가끔 답변을 날조하기 때문에 정제가 필요 

다음과 같은 셋팅을하고 질문을 했을때 날조된 데이터를 답변 하면 

"Answer:"을 시작으로 답변을 하는 패턴을 보임  해당패턴만 제거 

* 단점 2 : 다양한 패턴의 날조 답변이 있을것이고 이것만을 차단한다는 점에서 신뢰성이 많이 떨어짐 

## 3.2. Question Answering

 ρtaskA + ρchat + ρa을 통해 Question Answering 진행 

### BLIP-2 Task Instruction  ρtaskA

ρtaskA는 BLIP-2 answering task 

ρtaskA는 사진에 없는 불확실한 정보를 사용하는걸 완화시켜 준다. 

- Answer Instruction  ρa

> ρchat(챗 로그)를 기반으로 BLIP-2의 응답은 아래와 같은 구조로 이어짐
>
> Question: <question> Answer:

- Answer Trimminig  ρa

> ChatGPT, BLIP-2 와 같은 생성 모델이 만든 텍스트를 이용해 작성 
>
> ChatGPT의 답변이 "Question:" 으로 시작하는경우 자동으로 차단 

### 3.3. Context Summarizing

아래와 같은 질문으로 그전 대화 질의응답을 요약해 이미지 캡셔닝을 생성

```
Now summarize the information you get in a few sentences. Ignore the questions with answers no or not sure. Don’t add information. Don’t miss information. Summary:
```

#  4. Experiments

![f_4](F:\code\whtngus.github.io\img\2023\ChatGPT Asks, BLIP-2 Answers_ Automatic Questioning Towards Enriched Visual Descriptions\f_4.PNG)

ChatCaptioner 으로 생성된 캡션과 비교, 결과의 퀄리티가 다름을 볼 수 있음

- Details of Model Deployment.

여기에선 chatGPT 모델 “gpt-3.5-turbo”를 사용 

- Limitation of Traditional Metrics.

ROUGE, METEOR 로 metric 사용 

## 4.1. Information Analysis

- Does ChatCaptioner extract more information from the image?

![t_1](F:\code\whtngus.github.io\img\2023\ChatGPT Asks, BLIP-2 Answers_ Automatic Questioning Towards Enriched Visual Descriptions\t_1.PNG)

BLIP-2 를 단독으로 사용하는것 보다 ChatCApioner를 사용하는것이 더 욱 많은 정보를 생성해냄 COCO, WikiArt의 ArtEmis, CC 데이터에서 랜덤으로 100개를 추출해 평가를 진행

-> information을 저렇게 정의할 수 있을까?

위의 테이블에서 정확도가 높음을 보임

- How many objects in images can ChatCaptioner discover?

![t_2](F:\code\whtngus.github.io\img\2023\ChatGPT Asks, BLIP-2 Answers_ Automatic Questioning Towards Enriched Visual Descriptions\t_2.PNG)

Pascal VOC 200개의 이미지를 추출해서 캡션을 생성후

WordNet의 NLTK를 이용해 유사한 의미를 가진 단어를 찾은 경우 총 1154개의 단어가 나오는것을 확인.  

제안한 방식에서는 이중 584개의 단어의 종류가 나왔으나 BLIP-2 모델에서는 383개만 발생

## 4.2. Correctness Analysis

- How accurate are the captions from ChatCaptioner?

![t_3](F:\code\whtngus.github.io\img\2023\ChatGPT Asks, BLIP-2 Answers_ Automatic Questioning Towards Enriched Visual Descriptions\t_3.PNG)

ChatCaptioner를 평가하기 위해 human evaluation 을 수행

-> 이 이유는 해당 논문에서 제시하는 모델의 캡션들의 길이가 길고 정보가많아서 스코어 비교가 안되는듯

사람이 보고 부정확한지 정확한지를 판단 

COCO, WikiArt, CC 데이터셋을 기반으로 테스트

*문제점 이 스코어가 의미를 가질 수 있을까?



- Does BLIP-2 know it doesn’t know?

BLIP-2는 answer를 만들 수 있지만 









-> 특정 모델이 캡션을 가지고 해당 이미지가 맞는지 아닌지의 정확도로 평가 



# 참고지식

- WordNet synset matching





# 참고






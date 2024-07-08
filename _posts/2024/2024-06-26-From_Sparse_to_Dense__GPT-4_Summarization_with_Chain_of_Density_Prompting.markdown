---
layout: post
title: "From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting"
date: 2024-07-08 02:05:23 +0900
category: paper
---

# From Sparse to Dense: GPT-4 Summarization with Chain of Density Prompting

mit, salesforce, columbia.edu 

url : https://arxiv.org/abs/2309.04269

2023년 9월 8일 게재 





# Abstract

옳바른 양의 정보를 유지하면서 요약본을 만드는 일은 어려움 

좋은 요약은 상세하고 실질적이여야하며, 중복과 어려움이 없어야함 

GPT-4 를 통해 CoD(Chain of Density)  prompt를 사용 

기본적으로 gpt-4는 길이를 늘리지 않고 누락된 주요 개체를 반복적으로 사용함 

CoD로 생성시 추상적이지 않고 바닐라 프롬프트보다 평향이 적다고함 

NN DailyMail 기사 100개에 대해 인간 선호도 연구를 수행함 



500개의 주석이 달린 CoD 요약과 추가적으로 5,000개의 비주석 요약은 HuggingFace에서 무료로 이용 가능하다고 함

# 1 Introduction

![f_1](\img\2024\From_Sparse_to_Dense__GPT-4_Summarization_with_Chain_of_Density_Prompting\f_1.PNG)

자동 요약은 지난 오랫동안 연구되어 옴

최근 몇년 사이 학습을 하지 않는 LLM을 사용한 zero-shot prompting 방법의 요약 방법이 사용됨  

-> 주제 길이 스타일등을 원하는 방식으로편하게 변경 가능함 

적은 단어로 많은 정보를 커버하는건 실시간 서비스의 목표임



정해진 토큰 안에 얼마나 많은 정보와 설명을 압축해서 넣을지를 알아야하며 얼마나 많은 요약공간을 만들지도 정의해야함 



해당 논문에서 점점 내용을 조밀하게 그리고 사람의 선호도를 요청해 하여 한계를 알아보고자 함 

이때 gpt-4 를 사용  

토근당 평균 개체 수를 밀도로 판단하여 요약을 생성



연구의 컨트리뷰션

- Develop a prompt-based iterative method (CoD) 개발
- 요약의 자동화된평가 방법 제안  CNN/Dailymail 데이터를 기반으로함
- GPT-4를 이용해 5000개의 요약, 레이블링을 CoD 방법으로 작업 

# 2 Chain of Density Prompting

#### Prompt.

![f_2](\img\2024\From_Sparse_to_Dense__GPT-4_Summarization_with_Chain_of_Density_Prompting\f_2.PNG)

연구의 목표는 GPT-4를 사용해 생성 길이를 조절함으로 써 다양한 수준의 정보를 생성하는것

엔티티 유형에서 누락된 엔티티를 정의 

- Relevant : 메인 스토리
- Specific : 설명적이면서 간결함 (5개 이하의 단어)
- Novel : 이전 요약에는 없는 내용
- Faithful : 내용에 충실한지
- Anywhere : 기사 내용의 위치를 전부 커버

#### Data

100개의 CNN/Daily Mail 을 랜덤으로 샘플링해서 요을 생성해서 테스트함

#### Reference Points

CoD 와 사람이 요약한 내용을 사용하여 비교 

GPT-4 의 템플릿은 아래와 같은 형식을 다룸

![t_1](\img\2024\From_Sparse_to_Dense__GPT-4_Summarization_with_Chain_of_Density_Prompting\t_1.PNG)

```
“Write a VERY short summary of the Article. Do not exceed 70 words."
```

# 3 Statistics

토큰, 객체, 객체밀도의 통계정보는 CoD로 조절 가능함 

#### Direct Statistics.

위의 테이블 1에서 NLTK 라이브러릴 통해 토큰화하고 수를 계싼하고 entities의 경우 Spacy 라이브러리를 사용 



CoD는 앞의 토큰수가 있어 고정된 예산을 사용 

두 번째 단계에서는 장황한 단어들을 삭제하기 때문에 (제약사항으로) 오히려 불필요한 길이를 감소시킴 



#### Indirect Statistics

![f_3](\img\2024\From_Sparse_to_Dense__GPT-4_Summarization_with_Chain_of_Density_Prompting\f_3.PNG)

Abstractiveness은 각 CoD 단계에서 스텝이 증가살수록 증가함

abstractiveness를 평가하기 위해서  추출된파편들을 통해 평가 (추출 조각의   평균 제곱 길이)

그리고 ROUGE를 사용

cod 요약이 사람이 작성한 내용보다 더 추강적으로 잘 작동했다고함(figure 3)



4 결론 생략



.. 음..

원하던 내용이 아님












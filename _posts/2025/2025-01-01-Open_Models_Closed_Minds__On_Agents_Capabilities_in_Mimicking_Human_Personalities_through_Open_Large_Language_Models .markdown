---
layout: post
title: "Personas within Parameters: Fine-Tuning Small Language Models with Low-Rank Adapters to Mimic User Behaviors"
date: 2025-01-01 02:05:23 +0900
category: paper
---

# Personas within Parameters: Fine-Tuning Small Language Models with Low-Rank Adapters to Mimic User Behaviors

2024년 1월 13일

url : https://arxiv.org/abs/2401.07115

켈리포티아 대학교 



# Abstract

사람과 비슷하게 행동하는 LLM의 등장은 nlp와 사람의 심리학과 매우 가까워짐

LLM과 사람의 특성을 연결하기 위해 많은 연구가 되고 있으나 대부분의 연구가 상업적이용에 집중되어 있음 



해당 연구에서는 12 LLM Agents를 통해  MyersBriggs Type Indicator (MBTI)와  Big Five Inventory (BFI) 대해 조사함

위를 통해 밝혀냄 

1. 각 Open LLM 에이전트는 도특한 특성을 보임
2. 프롬프트는 특성에 다양한 영향을 미침, 몇개만이 성격을 성공적으로모방하고 대부분은 폐쇄적으로 남아 성격 모방에 실패함
3. 롤과 성격의 조합은 사람을 따라하는 능력을 향상시킬 수 있음 

# 1 Introduction

llm의 개인적 특성을 알 수 있는 Myers-Briggs Type Indicator (MBTI) and Big Five Inventory (BFI) 테스트를 진행함 

RQ0: Open LLM agent가 MBTI와 BFI 를 인지하고 있는가

RQ1: Open LLM agent가 일관되게 MBTI BFI를 나타내는가

RQ2: Open LLM agent가 구체적인 내면을 프롬프팅으로 따라할 수 있는가

RQ3: Open LLM agent는 모방시 구체적인 역할에 따라 행동을 지시받은 경우 모방 성능을 향상시킬 수 있는가 

위의 내용을 12개의 LLM 에이전트로 실험함

# 2 Background

## 2.1 The MBTI and BFI Personality Tests

 ![t_1](F:\code\whtngus.github.io\img\2025\Open_Models_Closed_Minds__On_Agents_Capabilities_in_Mimicking_Human_Personalities_through_Open_Large_Language_Models\t_1.PNG)

MBTI는 BFI 상당히 자주 널리 사용됨 

MBTI는 Table1 처럼 16로 페르소나를 구분할 수 있음

 BFI는 5개의 핵심 요소로 구성됨 

개방성(Openness), 성실성(Conscientiousness), 외향성(Extraversion), 친화성(Agreeableness), 신경증(Neuroticism)



MBTI는 유형을 그룹화 하는데 사용되며 BFI는 학문적심리학에서 널리 사용되고 있음

## 2.2 Related Work

#### LLM Agents.

LLM 기술이 빠르게발전되고 있다 ...

#### Personality and LLMs

텍스트에서 성격을 추출하는 것은  오랜 도전과제였음 

* 관련 연구 내용들체크해보기 

# 3 Methodology

## 3.1 Awareness Check

RQ0 체크: MBTI와 BFI를 LLM 이 답변할 수 있는지 없는지를 반정략적으로 평가를 수행

1. mbti가 4개의 양극성을 가진 16개의 성격유형
2. BFI 5가지 지수가 정의와 예제 행동

어휘의 의미와 의미의 유사성을 평가함

- mbti는 themyersbriggs.com BFI는 John et al., 2008

## 3.2 Administering the tests

각 모델은 질문에서 질문과 옵션에 따른 답변이 정의되어 있음 

MBTI는 60개의 질문인 Q^MBTI가 있음 (16Personalities.com)

LLM은 질문에 대해서 선택해야됨 

Q^MBTI = {Agree, Generally Agree ,Partially Agree ,Neither Agree, Disagree}

BFI test는 44의 질문의로 구성됨 

마찬가지로 아래중 하나를 답변해야됨

O^BFI ={Disagree strongly, Disagree a little, Neither agree nor disagree, Agree a little, Agree strongly}.

두가지 다 1~5의 같은 스케일 범위를 가지고 있음 

## 3.3 Personalities of Open LLMs

RQ1~RQ3을 하기위해 3가지 프롬프트 전략을 사용함 

#### Unconditioned Prompting

![f_1](F:\code\whtngus.github.io\img\2025\Open_Models_Closed_Minds__On_Agents_Capabilities_in_Mimicking_Human_Personalities_through_Open_Large_Language_Models\f_1.PNG)

RQ1에 대답하기 위해 Q^MBTI, Q^BFI 질문들을 훈련받지않은 구조의 프롬프트를사용함 

질문 형식은 위의 그림1과 같음 

#### Personality-Conditioned Prompting.

![f_2](F:\code\whtngus.github.io\img\2025\Open_Models_Closed_Minds__On_Agents_Capabilities_in_Mimicking_Human_Personalities_through_Open_Large_Language_Models\f_2.PNG)

RQ2를 위해서는 구채적인 페르소나를 위한 내용들이 제공됨

MTBI 는 PBFI의 각 요인에 대해 연관된 언어적 라벨, 개념적 정의, 행동적 예시를 가져옴

모든 성격과 그 특성 또는 세부 사항을 사용해 모델이 특정 성격을 효과적으로 모방할 수 있는 조건화된 맥락을 정의

#### Role- and Personality-Conditioned Prompting.

![f_3](F:\code\whtngus.github.io\img\2025\Open_Models_Closed_Minds__On_Agents_Capabilities_in_Mimicking_Human_Personalities_through_Open_Large_Language_Models\f_3.PNG)

RQ3를 평가하기 위해서 사람의역할이 llm 모방 능력을얼마나 향상시켰는지 이전 연구를 조사해야됨 

이를 확인하기 위해 잘 엄선된 StereoSet dataset인 120개의 전문직과 역할을 활용함 

 심리학자 그룹에게 MBTI 성격과 BFI 요인 각각에 대해 해당 목록에서 가장 관련성이 높은 역할 3가지를 선택하도록 요청함

## 3.4 Temperature and Repetitions

평가가 충분히 만족되기 위해서 MBTI 와 BFI테스트를 방복해서 실험함

temperature 값을 테스트 τ = {0.01, 0.7}

총 12 × 2 × 16 × 30 = 11, 520 번을 테스트함 

12개의 모델, T 2가지, 30번씩 반복,  MBTI 16가지

12 × 2 × 5 × 30 = 3, 600 BFI 테스트 

## 3.5 Models

![t_2](F:\code\whtngus.github.io\img\2025\Open_Models_Closed_Minds__On_Agents_Capabilities_in_Mimicking_Human_Personalities_through_Open_Large_Language_Models\t_2.PNG)

HuggingFace Model에서 Table2와 같은 다양한 모델을 가지고 실험함

## 3.6 Agent Creation and Models Deployment

llm 페르소타를 셋팅하기 위해 면접자와 면접대상자 인터뷰 진행자 에이전트로 간주함

실험에서 오픈소스인 AutoGen을 사용함 시스템 메시지와 롤 페르소나를 각 에이전트한테 전달할 수 있고 일관된 테스트를 할 수 있음 

top_p와 top_k를 기본값은 50, 1을 사용함 

A30 gpu 8대(24 gb) - 764RAM  서버에서 테스트함 

# 4 Results and Discussion

## 4.1 RQ0: Models’ awareness of the tests

Open LLM은 MBTI와 BFI 테스트에 대해 인지하고 음을 나타냄

## 4.2 RQ1: LLM-inherent Personalities

#### MBTI test.

![f_4](F:\code\whtngus.github.io\img\2025\Open_Models_Closed_Minds__On_Agents_Capabilities_in_Mimicking_Human_Personalities_through_Open_Large_Language_Models\f_4.PNG)

그림4의 윗 부분을 보면 temperature가 0.01일때 단봉분포를 보임 

위 그림에서 LLM 에이전트는 ENFJ을 대부분 보임

#### BFI test

![f_5](F:\code\whtngus.github.io\img\2025\Open_Models_Closed_Minds__On_Agents_Capabilities_in_Mimicking_Human_Personalities_through_Open_Large_Language_Models\f_5.PNG)

특별한 특징은 없어보임 

#### RQ1 — Summary

temperature가 0에 가까운경우 mbti는 j나 ENFJ성향을 보이며 BFI의 경우 Neuroticism(신경질)을 제외하면 높은 수치를 보임

그리고 temperature를 높이면 당연하게도 다양해짐

## 4.3 RQ2: Prompt-conditioned Personalities

#### MBTI test. 

![t_3](F:\code\whtngus.github.io\img\2025\Open_Models_Closed_Minds__On_Agents_Capabilities_in_Mimicking_Human_Personalities_through_Open_Large_Language_Models\t_3.PNG)

Table 3의 왼쪽 테이블로 MBTI 정확도 평가를 함 

SOLAR가 가장 높은 점수가 나옴 

#### BFI test.

Table 3 의 오른쪽 역시 SOLAR 가 가장 높은 점수대가 나옴 

#### RQ2 — Summary.

instructing LLM을 통해 특정인간을 모방하는것을 지시함으로써 높은 temperature일 수록 조건을 무시함

## 4.4 RQ3: Role&Prompt-conditioned Personalities

페르소타랑 role 조건을 같이 조합하여 제공함 

생략..



# 5 Conclusions

생략















# 참조 

- StereoSet dataset

데이터셋 확인하기 

- AutoGen

프레임워크 확인하기 










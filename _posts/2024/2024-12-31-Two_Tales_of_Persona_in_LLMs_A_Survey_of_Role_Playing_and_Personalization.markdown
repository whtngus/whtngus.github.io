---
layout: post
title: "Social Life Simulation for Non-Cognitive Skills Learning"
date: 2025-1-2 02:05:23 +0900
category: paper
---

# Two Tales of Persona in LLMs:A Survey of Role-Playing and Personalization

2024년 10월 5일 

url : https://arxiv.org/pdf/2406.01171

git : https://github.com/MiuLab/PersonaLLM-Survey -> 코드없음

타이완 대학교, 중국 중앙연구원

# Abstract

페르소나 컨셉은 대화문헌에서 주로 채택되며 LLM에 의해 금증하고 있음 (e.g., personalized search, LLM-as-a-judge)

그러나 llm을 사용한 연구는 체계적이지 않거나 분류체계가 부족하다고 함 

이를 쳬계적으로 하기 위해 2가지를 명명하고 제안함

1. LLM Role-Playing

LLMs에게 persona를 할당

2. LLM Personalization

LLMs에게 persona를 할당하고, 평가함

# 1 Introduction

![f_1](F:\code\whtngus.github.io\img\2024\Two_Tales_of_Persona_in_LLMs_A_Survey_of_Role_Playing_and_Personalization\f_1.PNG)

해당 연구에서는 기존 연구의 포괄적인 조사와 치계적인 분류 쳬계에 포커스를 맞춤 

그림1과 같이 현재의 연구를 2개의 main streams인 LLM Role-Playing과 LLM Personalization으로 정의함 정의함 

주요 차이점은 역할 수행에서는 페르소타가 LLM에 속하는 반면, 개인화에서는 페르소나가 사용자에게 속함 

role-playing은 LLM role-playing이 어떻게하면 좋은 성능을 낼 수 있는지 

personalization은 사용자의 기대를 충족하는 방법

- LLM Role-Playing:

LLM에게 페르소나를 할당하는 테스크를 수행하고

환경의 피드백에 따라행동하고 환경에 적응을 수행함

- LLM Personalization

사용자(사용자의 정보 및 이전 행동을 기반)의 페르소나를 개별적으로 만족하기 위한 만족하기 위한 임무

![f_2](F:\code\whtngus.github.io\img\2024\Two_Tales_of_Persona_in_LLMs_A_Survey_of_Role_Playing_and_Personalization\f_2.PNG)

기존 연구들을 조사하고 위의 그림 2와같이 분류함

# 2 LLM Role-Playing

![f_3](F:\code\whtngus.github.io\img\2024\Two_Tales_of_Persona_in_LLMs_A_Survey_of_Role_Playing_and_Personalization\f_3.PNG)

llm을 통한 role-playing은 계획, 반성에서 인상적인 성능을 보임 

학습하지 않는 페러다임은 간단하고 효과적임

또한 LLM role-playing은 multi-agent 셋팅까지 확장되고 다양한 페르소타를적용할 수 있음 

## 2.1 Environments

### 2.1.1 Software Development

software development는 프로그램 디자인, 코딩 프로젝트와 관련 있음 

ex) “Create a snake game.” or “Create a Python program to develop an interactive weather dashboard.” 

### 2.1.2 Game

마인크래프트, 구매자 판매자 환경 등 에서 강력한 백본성능을 보임 

게임환경은 넓은 정보와, 설정값, 사용도구 , 근처 상황들이 필요함 

-> 이에따라retrieval-based memory  접근방법이 중요한 요소가 됨

### 2.1.3 Medical Application

의료 도메인 환경에서  DR-CoT 프롬프트가 제안됨 

-> 의료 진단 롤플레잉 

의사 모방(mimicking doctor)가 근본적인 사고과정에 대해 DR-CoT는 프롬프팅을 통해 확고히 향상시킴



또한  MedAgent으로 image-based diagnosis 도 제안됨 

### 2.1.4 LLM-as-Evaluator

llm을 평가자로 사용하는 방식은 표준 프레임워크가 됨 

이것은 LLM의 성능이 사람과 비슷함을 증빙함

## 2.2 Role-Playing Schema

2가지 스키마를 분류함: single-agent and multi-agent.

#### Single-Agent

하나의 에이전트에서 도움없이 동시에 독립적인 여러개의 에이전트가 존재할 수 있는지 

예시로 Voyager agents가 있음 ->Minecraft의 에이전트에서 마인크래프트 여러개를 하나의환경에서 구동

#### Multi-Agen

여러 에이전트에서 Supports(collaborate and communicate)를 수행

## 2.3 Emergent Behaviors in Role-Playing

3개지 협동 방식을 소개함 

#### Voluntary Behavior

협력적 협업 패러다임, 에이전트가 능동적으로

자발적인 행동을 통해 LLM은 팀의 효율성을 높이고 정의된 환경 내에서 결속력을 보여줌 

#### Conformity Behavior

에이전트가 비평이나 다른 질문으로인해 팀 목표를 벗어난 경우 이를 개선함 

#### Destructive Behavior

때떄로 llm은 설계되지않은행동을 수행함(원치않는 대답이나 유해한 답변)

# 3 LLM Personalization

![f_4](F:\code\whtngus.github.io\img\2024\Two_Tales_of_Persona_in_LLMs_A_Survey_of_Role_Playing_and_Personalization\f_4.PNG)

사람에 맞는 개인화된 추천같은 테스크를 할 수 있어야함

## 3.1 Personalized Recommendation

생략.



# 4 LLM Personality Evaluation

A line of works has carried out the evaluation leveraging human personality assessments, including Big Five (Jiang et al., 2023; Sorokovikova et al.,2024) and MBTI (Pan and Zeng, 2023; Song et al., 2024). For example, Sorokovikova et al. (2024);Jiang et al. (2024)

-> 이 논문들은 찾아봐야될듯 

Big Five Personality Inventory (BFI), MBTI를 이용한 평가를함 ..



# 5 Challenges and Future Directions

생략

# 6 Broader Implications

생략



# **관련** 키워드

mimicking human 

 Persona llm 














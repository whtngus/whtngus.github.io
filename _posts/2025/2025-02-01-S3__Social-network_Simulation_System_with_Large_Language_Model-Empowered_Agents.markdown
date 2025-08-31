---
layout: post
title: "S3: Social-network Simulation System with Large Language Model-Empowered Agents"
date: 2025-2-1 02:05:23 +0900
category: paper
---

# S3: Social-network Simulation System with Large Language Model-Empowered Agents



url : https://arxiv.org/pdf/2307.14984



중국 청화대

2023년 10월 19일



# Abstract

시뮬레이션은 사회과학 내에서 다양한 문제를 해결하는 데 상태 예측, 현상 설명, 정책 결정 지원 등 광범위한 응용을 제공해 중요한 역할을 함 

 대형 언어 모델(LLM)의 인간과 유사한 감지, 추론, 행동 능력을 활용하여 S3 시스템(Social network Simulation System의 약어)을 구축했다고 함 

-> 파인튜닝 프롬프트 두개 다 했다고함 



구체적으로 감정, 태도, 상호작용 행동이라는 세 가지 측면을 시뮬레이션함 

-> 데이터는 쇼셜 네트워크 데이터를 활용해 두 가지 수준의 시뮬레이션을 수행하는 평가를 진행함 

# 1 Introduction

sns 는 사회 내에서 상호 연결결된 개인들로 구성되어 현대 세계의 초석을 다루고 있으며

컴퓨터시뮬레이션은 수학적인 분석과 달리 사회적 네트워크 형성과 진화를 이해할 수 있는 새로운 접근 방법임 



1996년에는 이미 *Social Science Microsimulation*책을 통해  사회과학적 관점에서 시뮬레이션에 대한 귀중한 통찰을 제공함



사회 시뮬레이션은 개인 및 집단의 사회적 활동을 포함하는 다양한 영역을 포괄함

사회 시뮬레이션의 핵심은 2가지 관점이 있다고 함

1.  개인 간의 동적 피드백 및 상호작용
2. 집단의 상태 변화

2번은 집단 전체 또는 개별 그룹의 형태로 나타날 수 있음



시뮬레이션은  **미시적 수준의 시뮬레이션**과 거시적 수준의 시뮬레이션으로 구현될 수 잇음 



거시적 시뮬레이션(시스템 기반 시뮬레이션이라고도 함)에서는 연구자들이 집단의 상태 변화를 설명하는 방정식을 활용하여 시스템의 동적 변화를 모델링히고 미시적 시뮬레이션(에이전트 기반 시뮬레이션)은 연구자들이 인간이 만든 규칙이나 매개변수화된 모델을 사용하여 개별 행위자(에이전트)의 행동을 묘사함



LLM을 이용한 사회 시뮬레이션은 다음 세 가지 주요 능력에 기반함

1. **세계 인식 및 이해 능력**
   - 텍스트로 충분히 기술될 수 있는 환경에서 정보를 인식하고 이해할 수 있습니다.
2. 추론 및 작업 계획 수립 능력**
   - 작업 요구사항과 이에 따른 보상을 고려하여 작업 계획을 수립하고 조직할 수 있습니다.
   - 이 과정에서 LLM은 기억을 유지 및 갱신하며, 인간과 유사한 추론 패턴을 기반으로 적절한 프롬프트를 활용합니다.
3. 텍스트 생성 및 상호작용 능력**
   - 인간이 생성한 것과 유사한 텍스트를 작성할 수 있으며, 이를 통해 환경에 영향을 미치고 다른 에이전트와 상호작용할 수 있습니다.





연구에서는 Social-network Simulation System(S³, 사회 네트워크 시뮬레이션 시스템)를 제안함 

1. 환경의 현실성을 보장하기 위해, 프롬프트 엔지니어링과 프롬프트 튜닝을 결합한 **사용자 인구 통계 추론 모듈**을 개발
2. 사용자는 자신이 팔로우하는 사람들의 콘텐츠를 관찰하며, 이로 인해 자신의 태도, 감정, 행동이 변화할 수 있음 -> 행동 및 감정 변화 시뮬레이션
3. 집단 수준에서의 정보 및 감정 전파 모델링 -> 정보 전파, 태도 형성, 감정 확산 등 



두 가지 대표적인 시나리오를 측정해봤다고함 성차별, 워낮려 ㄱ에너지

# 2 Related Works

**사회 시뮬레이션(social simulation)**과 **대규모 언어 모델(LLM) 기반 시뮬레이션**에 대해 논의

## 2.1 Social Simulation

 사회 시뮬레이션은 **경제 시뮬레이션(socio-economic simulation)**을 수행하는 경제학자들에게 훈련 환경을 제공할 수 있습니다 [34]. 이 맥락에서 경제학자는 인공지능 프로그램을 활용하여 경제 정책을 수립하는 디지털 페르소나(digital persona) 역할을 할 수 있습니다. 더 나아가, 사회 시뮬레이션은 메타버스에서 등장한 **디지털 아바타(digital avatar)**와 같은 인간 대체 요소로 활용될 수도 있음



초기 시뮬레이션은 이산 사건 기반 시뮬레이션(discrete event-based simulation) 또는 시스템 동역학(system dynamics)을 널리 사용했다고함 

-> 뭔지 모르겠다..  -> 일련의 방정식을 통해 여러 변수의 시간적 변화를 근사적으로 예측하는 방법

이후 에이전트 기반 시뮬레이션(agent-based simulation이 본격적으로 활용되기 시작함 대표적으로 렐룰러 오토마타가 있음

## 2.2 Large Language Model-based Simulation

LLM 을 이용한 많은 시뮬레이션들이 있었음 

-> 관련 논문 많음

# 3 S^3: Social Network Simulation

##  3.1 System Overview

**사회 네트워크 프레임워크(social network framework)** 내에서 구축하여 LLM을 활용하여 에이전트 역량을 강화함



**개별 수준 시뮬레이션(individual-level simulation)**

- 사용자 특성, 사회 네트워크 내 정보적 맥락(informational context), 그리고 **사용자의 인지적 지각(cognitive perception)과 의사결정(decision-making)을 조정하는 복잡한 메커니즘**을 활용하여 **행동(behavior), 태도(attitude), 감정(emotion)**을 재현하는 것을 목표로 합니다.



**집단 수준 시뮬레이션(population-level simulation)**

- 에이전트 기반 시뮬레이션(agent-based simulation)을 활용하여, **집단 수준에서의 동적 변화(population-level dynamics)**를 분석합니다.

- 이를 위해, 

  사회적 주요 현상(social phenomena) 세 가지

  를 중점적으로 시뮬레이션합니다.

  1. **정보의 전파 과정(propagation process of information)**
  2. **태도의 변화(attitude shift)**
  3. **감정(emotion)의 확산**

## 3.2 Social Network Environment

**원자력 에너지(nuclear energy) 연구**

- 연구의 핵심은 **일반 대중이 원자력 에너지를 지지할 것인지, 아니면 화석 연료에 의존할 것인지에 대한 태도를 분석하는 것**입니다.

**성차별(gender discrimination) 연구**

- 본 연구에서는 **성차별과 관련된 사건이 개인 및 집단 차원에서 유발하는 감정적 반응(emotional experiences)**을 심층적으로 분석합니다.
- 특히, **분노(anger)와 같은 감정이 어떻게 촉발되는지**에 초점을 맞춥니다.



![t_1](F:\code\whtngus.github.io\img\2025\S3__Social-network_Simulation_System_with_Large_Language_Model-Empowered_Agents\t_1.PNG)

실제 데이터수집은 sns에서 사용자, 사회적 연결, 텍스트 게시물을 수집함 -: table1 참조 



**소셜 미디어에서는 사용자에 대한 정보가 제한적**으로 제공되므로, 이를 보완하기 위해 **사용자 게시물 및 자기소개 등의 텍스트 데이터에서 인구통계 정보를 추출** 해야함 

-> 즉 원본 데이터를 가져온게 아니라 연령, 성별 ,직업 정보를 예측해서 가져옴  (table 2의 정확도 참조)

### 3.3.1 Emotion Simulation

사용자가 특정 사건에 대해 가질 수 있는 잠재적 감정(potential emotions)을 세가지 수준으로 모델링함

**차분한 상태(Calm)**

- 사용자가 해당 사건을 **인지하기 전**의 기본 감정 상태(default emotion level)입니다.

**중간 수준(Moderate)**

- 사용자가 사건을 인식하고, 어느 정도 감정적 반응을 보이는 상태입니다.

**강한 감정(Intense)**

- 사용자가 사건에 대해 **강렬한 감정적 반응**을 나타내는 상태입니다.

그리고 감정의 변화는 마르코프 과정을 활용함



마르코프 과정은 사용자의 감정 변화를 예측하는 데 있어 다음과 같은 요소를 고려합니다.

1. **현재 감정 상태(Current emotion level)**
2. **사용자 프로필(User profile)**
3. **사용자의 과거 경험(User history)**
4. **현재 시점에서 받은 메시지(Messages received at the present time step)**

-> 이러한 방법을 사용해 table2 정확도가 나옴 





### 3.3.2 Attitude Simulation

사용자의 **태도(attitudes)**는 **행동(actions), 의견(opinions), 및 다양한 주제에 대한 결정(decisions)**을 결정짓는 핵심 요소임

사람의 감정을 2가지로 이진부류함 -> like unlike 두가지 인듯..

이진 분류:

- **부정적 태도(Negative stance)**
- **긍정적 태도(Positive stance)**





**태도 시뮬레이션 과정**

1. **초기 태도(Initial Attitude) 설정**

   - 사용자의 **프로필(profile)** 및 **과거 기록(user history)**을 활용하여, 사용자의 **기본적인 태도(predisposition)**를 설정합니다.
   - 이는 사용자가 **과거 상호작용 및 행동을 통해 형성한 태도**를 반영하는 과정입니다.

2. **태도 변화(Attitude Change) 모델링**

   - 태도의 변화는 **마르코프 과정(Markov Process)**을 통해 모델링됩니다.
   - 다음과 같은 요인들이 태도 변화에 영향을 미침
     - 사용자의 현재 태도(Current attitude)
     - 사용자 프로필(User profile)
     - 사용자 과거 기록(User history)
     - 현재 시점에서 받은 메시지(Messages received at the current time step)

   대부분 마르코프 과정으로 사용함

### 3.3.3 Content-generation Behavior Simulation

![t_3](F:\code\whtngus.github.io\img\2025\S3__Social-network_Simulation_System_with_Large_Language_Model-Empowered_Agents\t_3.PNG)

사용자들이 특정 사건에 대해 **자신의 태도(attitudes)와 감정(emotions)**을 반영하여 콘텐츠를 생성

LLM에 태도 감정상태 등을 입력값으로 넣어서 유사한 컨텐츠를 생성하는 능력을 갖추게 했다고 함 

**실제 사용자 생성 콘텐츠(real user-generated content)와 비교하여 높은 정확도를 보였습니다.**

#### **1. 성차별(Gender Discrimination) 시나리오 성능**

- **Perplexity Score**: 19.289
- **Cosine Similarity (평균 유사도)**: 0.723

#### **2. 원자력 에너지(Nuclear Energy) 시나리오 성능**

- **Perplexity Score**: 16.145
- **Cosine Similarity (평균 유사도)**: 0.741

-> 이건 어떻게 한거지?  Perplexity는 낮을수록 좋은값임 (엔트로피 정도라고 대충 이해하면 쉬움)

### 3.3.4 Interactive Behavior Simulation



시뮬레이션 과정에서, 사용자는 **팔로우(followee)한 다른 사용자로부터 메시지를 수신**하게 됩니다.
이때, 사용자는 **세 가지 행동 옵션 중 하나를 선택**해야 합니다.

1. **게시물 공유(Forwarding)**
2. **새로운 콘텐츠 게시(Posting new content)**
3. **아무것도 하지 않음(Doing nothing)**

-> 우선 액션부터 취함 



## 3.4 Population-level Simulation

1. **정보 전파(Information Propagation)**
   - 사회적 환경(social environment)에서 발생하는 **사건(events)에 대한 뉴스(news) 및 정보의 전파 과정**을 시뮬레이션합니다.
   - 사용자가 **어떤 정보를 공유하고 확산시키는지**를 모델링하는 것이 핵심입니다.
2. **감정 전파(Emotion Propagation)**
   - 특정 사건이나 주제에 대해 **사람들의 감정이 전염되는(social contagion) 과정**을 분석합니다.
   - 예를 들어, **부정적인 뉴스가 확산될 때, 분노(anger)나 슬픔(sadness)이 어떻게 퍼지는지**를 시뮬레이션합니다.
3. **태도 전파(Attitude Propagation)**
   - 사용자가 **사회 네트워크 내에서 서로의 태도(attitudes)나 견해(viewpoints)를 교환**하는 과정을 모델링합니다.
   - 특정 이슈에 대한 **의견 변화 및 사회적 영향(social influence)의 작용을 반영**하는 것이 목표입니다.

### 3.4.1 Information Propagation

![f_3](F:\code\whtngus.github.io\img\2025\S3__Social-network_Simulation_System_with_Large_Language_Model-Empowered_Agents\f_3.PNG)

**"여덟 아이를 둔 어머니 사건 (Eight-child Mother Event)"**

- 2022년 1월 말, **성폭력(sexual assault)과 페미니즘(feminism) 등 여러 논란이 얽힌 사건**이 공론화됨.

**"일본 원전 오염수 방류 사건 (Japan Nuclear Wastewater Release Event)"**

- 일본 정부가 **원전 오염수를 해양에 방류하기로 결정하면서**
- **전 세계적인 관심과 논란(global scrutiny and interest)을 불러일으킨 사건**

두 가지 사건을 시뮬레이션 함 



특정 시간 단계(time step)마다 **해당 사건을 인지한 사람들의 수(the overall number of people who have known the events)를 측정**.

-> 정확히 어떻게 한거지?



퍙기 빙법이 이상함  => 알림을 다 본건 아닐탠데 이렇게되면 계속 연락을 받고 반응할지 여부를 결정해야함 

figure 2, 3 를 비교하면 실제데이터와 비교해서 예측할 수 있을거라고 함 -> 신기하네..

### 3.4.2 Emotion Propagation

### 



이후 부분 생략
























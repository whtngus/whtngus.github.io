---
layout: post
title: "On the Multi-turn Instruction Following for Conversational Web Agents"
date: 2024-08-05 02:05:23 +0900
category: paper
---

# On the Multi-turn Instruction Following for Conversational Web Agents

Alibaba 및 대학교

url : https://arxiv.org/pdf/2402.15057v1

dataset : https://github.com/magicgh/self-map



# Abstract

웹기반 환경에서 LLM덕분에 복잡한 환경에서도 광범위한 웹 탐색과 탁월한 작업 수행능력을 보임 

그러나 현실적인 연속된 질문 시나리오에서 효과적으로 적용할 수 있는방법은 없음ㅐ 



해당 연구에서 Conversational Web Navigation 라는 테스크를 만들어, 유저와  에이전트간의 정교한 multi turn 대화를 지원하기 윈한 데이터셋 MT-Mind2Web을 만들어서 제안함 

또한 LLM의 토큰 제한 문제와 문맥 기반의 대화 기능을 해결하기 위한 self-reflective memory-augmented planning (Self-MAP)를 제안함 

# 1 Introduction 

![f_1](\img\2024\On the Multi-turn Instruction Following for Conversational Web Agents\f_1.PNG)

AI의 지금까지의 목표는 복잡한 테스크들을 수행하는 AI agent를 개발하여 사람의 노력을 최소화하는것

Figure 1의 (a)는 사용자의 입력을 해석하여 키보드와 마우스를 이용해 티켓을 예약하는 테스크를 수행하는것 

사용자의 지시를 그대로 행동하는건 아직 제대로 구현되지 않음

Figure 1의 (c)는 대화형 웹 세션에서 사용자가 이전의 정보를 새로 기반으로 이전 정보를 생략하고 말하는 경향이 있음 

여기에서도 간략한 정보와 생략된 구조에 대한 답변을 해야함 



이러한 것을 측정하기 위해 Conversational Web Navigation 테스크와 새로운 데이터셋을 제안함 

Figure 1의 (b)처럼 LLM은 대화영 질문에 대한 답변을 할 수 있음 

 이때 사전 학습된 데이터와 외부 데이터 검색 기술을 통해 답변 가능함



문맥 기반의 대화는 매우 킨 문맥과 노이즈를 해결해야 한다는 전통적인 문제가 있음



논문에서 제안하는 Self-MAP프레임워크는 제한된 메모리 내에서 작동하도록 설게됨(입력 길이 제한)

-> 대화 내용 기록을 기반으로 메모리 뱅크를 구성하고, 대화의 각 순서마다 상호작용 단계를 저장함 



컨트리뷰션 

(이해 안가서 그냥 chatgpt로 번역)

**다중 턴 지시를 따르는 웹 에이전트의 연구**:웹 에이전트가 여러 차례의 지시를 따라가며 작업을 수행하는 능력을 연구하기 위해, 저자들은 대화형 웹 탐색 문제를 정의하고 새로운 데이터셋인 MT-Mind2Web을 도입합니다.

**자기 성찰 메모리 증강 계획 방법 (Self-MAP) 제안**:저자들은 대화형 웹 탐색 과제의 기본적인 도전 과제를 해결하기 위해 메모리 활용과 자기 성찰을 결합한 Self-MAP이라는 방법을 제안합니다.

**MT-Mind2Web 데이터셋에 대한 벤치마킹**:저자들은 다양한 기준선을 사용하여 MT-Mind2Web 데이터셋을 벤치마킹하고, 다양한 설정에서 종합적인 평가를 제공합니다. 실험 결과는 제안된 방법의 효과도 확인해줍니다.

# 2 Related Works

#### Web Agents

최근 web agents 기반의  multi-domain, real-time 상호작용, visual UI understanding 등 다앙한 연구가 활성화 되고 있음 

이런 문제를 해결하기 위해 LLM을이용하여 강력한 에이전트를 만들어 사되며 웹 에이전트 기반으로 LLM 성능을 향상시키기 위해 다양한 프롬프트 기반의 방법들이 제안됨 

그러나 프롬프트 기반의 방법들은 fine-tuning하는 방법에 비교하여 실패한 결과를보이고 있음 

#### Multi-turn Interactions with Environment 

현실의 여러 환경에서 multi-turn 문제를 적용하기 위해서는 여러 문제들을 해결해야함

우선 사용자들이 하나의 테스크에서만 질문하는경우는 거의 없음 

#### Multi-turn Interactions with Users 

광범위한 연구로 기존 LLM이 multi-turn에 탁월한 성능을 입증함 

 MT-Bench 는 고품질의 80개의 멀티턴 데이터로 평가됨 (8개의 도메인으로 글쓰기, 열할극, 추리능력등)

그러나 이 데이터셋은 llm의 고유지식에 의존하는 테스크임 

# 3 MT-Mind2Web Dataset

## 3.1 Annotation & Quality Control

![f_2](\img\2024\On the Multi-turn Instruction Following for Conversational Web Agents\f_2.PNG)

Mind2Web(single-turn interaction data) 데이터셋을 기반으로 MT-Mind2Web 데이터를 만듦 

### 1) Organize Conversation Sessions

Mind2Web데이터의 같은 문맥인 같은 도메인과 웹사이트에서 연속적 주제의 테스크 구조를 만듦

-> multiple individual task 구조 

두 개의 instructions이 같은 의도나 객체를 가지고 대화를 하는 경우 같은 의도로 분류함

그림 2와 같이 Mind2Web데이터의 Insturction 1과 Instruction 2의 티켓 예약에 관한 같은 TicketCenter website의 Event 도메인을 공유함

이 경우 데이터를 결합하면 자연스러운 대화세션으로 사용할 수 있다고 함



-> 자연스럽진 않을거같은데 ...

### 2) Decompose Complex Instructions

  Mind2Web는 이상생활에서 볼 수 없는 복잡한 연속된 액션이 필요한 경우가 있음 

이런 복잡한 instruction의 경우 여러번 상호작용을 위한 좋은 지침이 될 수 있음 



복잡한 지시문을 멀티턴으로 분해하기 위해서 AI와 사람이 직접하는 방법을 같이 사용하여 annotation함

AI가 긴 시퀀스를 짧은 시퀀스로 나누는 결정을 내리는데는 사람보다 더 능숙했다고 함 

![t_1](\img\2024\On the Multi-turn Instruction Following for Conversational Web Agents\template_1.PNG)

chatgpt를 통해 N개의 서브 테스크로 나누게 시킴 

그림2의 예시에서 위에는 2개 아래는 3개의 서브테스크로 나뉜것을 볼 수 있음 

chatgpt를 통해 시키고 사람이 검수했을때 98.5%가 잘 뉘었다고 함

### 3) Rewrite Conversational Instructions

원래 독립실행하는 명령을 대화형 명령으로 개선함 

이때 anaphora(첫머리 어구 반복)와 ellipsis(생략)를 사용했다고 함 



예시

T2는 T1에서 언급된 WWE 티켓을 지칭하기 위해 'one'을 사용함

T3는 티켓을 예약하는 동일한 행동과 함께 다른 작업으로 전화하며, 이때 동사 'book'을 생략함

T4에서도 반복된 내용은 생략됨 



#### Quality Verification

오류나 실수등을 확인하기 위해 품질 검사를 진행함 

이때 사람이 직접 확인하며 대화가 일관성이 없거나 이해가 되지 않는경오 이를 수정하며 검증을 통과할때 까지 반복함





## 3.2 Dataset Statistics

![t_1](\img\2024\On the Multi-turn Instruction Following for Conversational Web Agents\t_1.PNG)

720개의 웹 대화 센셩을 확보하였으며, 3,525개의 대응하는 지시 및 행동 시퀀스 쌍이 포함되어 있고, 각 대화 세션마다 평균 5회의 사용자-에이전트 상호작용

위의 테이블 1과 같은 데이터셋을 생성함 

## 3.3 Problem Definition

Conversational WebNavigation 테스크

Ct : 상호작용 히스토리로 {q1, A1, ... qt, At}

Ai : Ct에 들어있는 행동 세트

Et : 환경 상황 (ex 현재 HTML web page)

# 4 Method

![f_3](\img\2024\On the Multi-turn Instruction Following for Conversational Web Agents\f_3.PNG)

Self-MAP framwork는 memory-augmented planning과 slef-reflection의 결합으로 되어있음 

위의 그림 3과 같이 메인 요소는 Memory, Reflection, Planning Modules 3가지 로 이루어짐

## 4.1 Memory Module

웹 에이전트기반을 위한 memory bank는 대화 히스토리를 Ct를 구조화함 

![ff1](\img\2024\On the Multi-turn Instruction Following for Conversational Web Agents\ff1.PNG)

위처럼 진행하려면 많은 크기의 토큰이 주입되어야하며 모델에 따라 최대 입력 길이의 제한이 있음 

몇몇의 메모리 조각은 환경 설정, 지침, 행동의 불일치로 인해 에이전트가 이후의 행동하는데 유요한 지침을 제공하지 못함 

그래서 메모리뱅크에서 관련있는 top-K개의 액션만 가져와서 사용함 

Ckt={q1,A1,…,qt,Ak−1t}

-> 이때 text-embedding-ada-002 모델을 사용하여 임베딩 모델 사용 

## 4.2 Reflection Module

메모리공간을 제한하기 위해 아래 2가지 스텝으로 최대 메모리 공간을 설정함 

1) Memory Simplification

2) Memory Refinement

#### Memory Simplification

MINDACT framework는 작은 모델인 BERTa를 이용해 ranking top-N을 추출함 

이를통해 노이즈나 관계가 없는 데이터를 제거함 

#### Memory Refinement

대화영 웹 탐색 도메인을 위한 특화된 메모리 정제 접근 방법을 설계함 

전통적인 방법과 달리 모델이 잘못된 경로를 수집하지 않음 



LLM의 중간 추론 근거를 생성하고 이전 메모리조각정보를 LLM에게 다음 행동의 ㅢㅇ사 결정 과정에 대한 이유를 설명하는 심층 근거를 생성하도록 함 (근거 - r)

#### Self-reflective Memory

위 두가지 스텝으로 노이즈 제거와 필터링을 완료 했으며 아래와 같이 표기함

![ff2](\img\2024\On the Multi-turn Instruction Following for Conversational Web Agents\ff2.PNG)

## 4.3 Planning with Self-reflective Memory

현재 대화 차례에서 사용자 쿼리 qt와 이전행동 시퀀스 ak-1을 고려해 

상위 k개의 피렅링 된 메모리조각 으로 M과 e를 얻음 

이후 입력을 기반으로 LLM을 finetuning하여 다음 행동 a를 결정함



# 5 Experiment

![t_2](\img\2024\On the Multi-turn Instruction Following for Conversational Web Agents\t_2.PNG)



생략...







# 참고

- Mind2Web

Mind2Web은 언어 지시에 따라 모든 웹사이트에서 복잡한 작업을 완료할 수 있는 웹용 일반 에이전트를 개발하고 평가하기 위한 데이터 세트

Mind2Web은 31개 도메인에 걸쳐 137개 웹사이트에서 수집한 2,000개 이상의 개방형 작업과 작업에 대한 크라우드소싱된 작업 시퀀스를 통해 일반 웹 에이전트를 구축하는 데 필요한 세 가지 요소를 제공합니다. 

1. 다양한 도메인, 웹사이트 및 작업
2. 시뮬레이션 및 단순화된 웹사이트 대신 실제 웹사이트 사용
3. 광범위한 사용자 상호 작용 패턴. 데이터 세트 구조 데이터 필드

https://paperswithcode.com/dataset/mind2web
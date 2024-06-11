---
layout: post
title: "Simulating Human Strategic Behavior: Comparing Single and Multi-agent LLMs"
date: 2024-06-11 02:05:23 +0900
category: paper
---



# Simulating Human Strategic Behavior: Comparing Single and Multi-agent LLMs

Columbia University, USA

2024년 2월 13일 아카이빙



# Abstract

계획을 세우거나 행동을 할때 사람의 행동을 전략적으로 파악하기는 어려움 

 최근 llm이 등장하면서 사람을 시뮬레이션 할 수 있을정도의 성능의 모델이 나오기 시작함 

해당 논문에서는 LLM이 인간의 전략적 행동을 시뮬레이션할 수 있는지 조사함 

논문에서는 최후통첩 게임을 통해 사람의 행동을 이해하는 연구를 함 

1. 최후통첩에서 사람과 비슷한 행동을 하는 행동을 비교
2. 두 플레이어 간의 탐욕과 공정한 성격을 시뮬레이션 
3. 논리적으로 완벽한 전략과 성격을 생성하는 능력을 평가함 

사람의 전략과 성격 쌍에 대해 행동 시뮬레이션이 더 정확하다고함 (88% vs 50%)

-> 자세한 내용은 아래 내용 보면서 확인 



이를통해 계획자와 정책 입안자 등 시스템에서 사람들이 어떻게 행동할지를 예비적으로 참구할 수 있음 



# 1 INTRODUCTION

시뮬레이션은 빌딩의 지진안전 설계, 계획을 평가, 경제 정책 등 많은 부분에서 도움을 줄 수 있음 

논문에서 물리적 시뮬레이션은 많이 발전했지만 사람의 행동을 시뮬레이션하는건 악명 높을정도로 어렵다고 함

 최근 LLM은 사람의 페르소나를 시뮬레이션 할 수 있는것으로 나타났으며 과거 대법관들의 판결을 모방하기도 했음 

논문에서는  LLM simulations 실험을 통해 사람의 행동 전략에 대해 영구함 

최후통첩은 사람의 사회적인 행동을 알 수 있는 기본적인 경제학 실험임 



두 플레이어가 제안자와 수신자로 나뉘어서 게임을 진행

제안자에게 먼저 특정 양의 돈이 주어짐 (ex 1$)

그리고 수신자에게 얼마를 나누어 줄지를 결정함 

수신자는 동의하거나 거절할 수 있으며  동의시 돈을 나눠서 받으며 거절시 두 플레이어는 아무돈도 받지 못함

 

경제학 이론에 따르면 가장 합리적인 최대 배분 값은 0.01$라고 함 

-> 나눌 수 있는 최솟값 이기 때문에, 그리고 수신자는 비동의하면 아무것도 받지 못하기때문에 무조건 동의해야함

그러나 실험적으로 사람은 관계적인 행동을 함 그리고 수신자는 공평하지 않은 돈을 제안하면 벌을 주기 위해 거절하기도 함  -> 제안자는 이를 알기때문에 공평함과 가까운 돈을 주는 전략을 세워야함 



40번의 시뮬레이션에서 Multi-agent 구조로 사람의 행동 88%정도가 일치했으며 LLM의 행동 50%가 일치함 

LLM과 인간의 행동이 일치하지 않는 이유는 아래와 같다.

1. 생선된 전략이 불완전함 
2. 생성된 전략이 지정된 성격과 일치하지 않음 
3. 플에이어가 게임 플레이 중에 생성된 전략에서 벗어난다.



총 40번의 시뮬레이션에서 1번만 오류가 플레이어가 생성된 전략을 따르지 않아서 문제가 발생함 



# 2. RELATED WORK

## 2.1 Ultimatum Game Background and Experiments

McCabe(2014)에 따르면 제안자들은 40% 또는 50%를 제안한경우 수락하지만 제안 금액이 20%일때 50%까지 하락하고 10%는 더 많이 하락한다고 한다.



## 2.2 LLM Reasoning

ext-davinci-003. 모델을 사용 나머지는 간단해서 생략

## 2.3 Using LLMs to Simulate Strategic Behavior

생략

## 2.4 Multi-Agent Paradigms of LLMs

기존 게임 시뮬레이션에서 단일 LLM을 사용했지만 새로운 에이전트 기반 구조는 사람의 행동을 더욱 효과적으로 예측할 수 있음 

아키텍처는 자기 지식, 기억, 계획, 반응, 성찰 다섯가지 구성요소를 포함함 

# 3 EXPERIMENTAL SET-UP

최후통첩 게임에서 llm이 사람의 행동을 시뮬레이션할 수 있는지를 테스트하기 위해 5라운드의 게임을 진행함 

이때 단일 llm과 멀티 에이전트 llm 기반의 아키텍처로 구성됨 

단일 llm은 프롬프트로 각각의 플레이어의 전략을 생성하고 실행을 함 

멀티 에이전트 llm은 각각의 플레이어를 각각 llm이 담당함 



탐욕, 공평한 두개의 성격을 테스트함 

단일 다중 에이전트에 대해 40개이ㅡ 시뮬레이션을 진행 (각 성격상 10개씩 단일 다중 진행함)



실험에서 GPT3.5, GPT4를 둘다 사용함

## 3.1 Research Questions

RQ1. 최후통첨 5라운드 동안 LLM이 사람과 비슷하게 행동할 수 있는가

RQ2. LLM이 사람의 성격을 그대로 모사할 수 있느가

RQ3. LLM이 최적화된 전략을 만들 수있는가 



단일 다중 에이전트는 각각의 장단점이 있다고 함 

single LLMs :  LLM이 모든 플레이어에 대한 모든 기록을 가지고 있음  -> 일관성 있는 게임을 진행 함 

Multi-agent : global context는 없지만 하나의 agent를 충분히 이해하고 선택할 수 있음 

## 3.2 Single LLM and Multi-Agent Architecture

### 3.2.1 Inputs

single-LLM structure

1. 5라운드 동안 각 플레이어들에게 최후통첩 게임 전략을 생성하고 표시함
2. 설정된 전략에따라 5라운드 동안 게임을 진행함

수령인은 제안자가 제안한 경우에만 판단 

 프롬프트 디자인에서는 원하는 행동을 생성하는 가장 간단한 프롬프트를 목표로 함

### 3.2.2 Outputs

![f_1](\img\2024\Simulating_Human_Strategic_Behavior__Comparing_Single_and_Multi-agent_LLMs\f_1.PNG)

그림 1과 같이 제안자가 제안을하고 수신자가 제안을 받거나 거절하는 방식으로 진행이됨 

다중 에이전트는 별돌의 행동이 기록됨 ->  여러 가능한 전략을 고려한 후 하나의 전략을 선택하거나 여러 전략을 결합하여 메모리에 기록

제안자는  제안을 통해 수락을 계속 받으면 가격을 낮춰서 제안하는 방식

## 3.3 Evaluation

### 3.3.1 Evaluation of Game play

![f_2](\img\2024\Simulating_Human_Strategic_Behavior__Comparing_Single_and_Multi-agent_LLMs\f_2.PNG)

각 에이전트를 게임에서의 역할(제안자 또는 수령인)에 따라 이름을 지정하고 각 플레이어의 초기 계획을 그들의 역할에 따라 5라운드 궁극의 게임을 위한 전략을 생성하고 그것을 메모리에 저장하도록 설정

각 플레이어 성격을 설정함 (ex 제안자는 욕심이 많음)



제안자들은 주로 0.5$ ~ 0.4$ 사이의 동등한 분할을 제안하며 공정한 수령인들을 제안을 받아들이고 욕심 많은 수령인들은 일반적으로 제안을 거절함 

욕심 많은 제안자들은 0.7$ 이상을 가저가기도 함 





첫 라운드 가정 

공정한 제안자는 제안이 $0.40에서 $0.60 사이

욕심 많은 제안자는 제안이 수령인에게 유리하게 편향되거나 엄격히 $0.50 미만이면 일관된 성격으로 행동한 것으로 간주됩니다. 공정한 수령인은 제안이 $0.40 미만인 경우 거부하고 $0.40 이상인 경우 수락한 경우에 일관된 성격으로 행동한 것으로 간주

등.. .이런식으로 간주함 

-> 이러면 그냥 룰기반 아닌가???



## 3.3.2 Evaluation of Strategies. 

llm 출력에서 수집된 정보를 가지고 3가지 구성 요소에 대한 전략을 평가함 

1. 전략의 완전성
2. 전략이 지정된성격 특서과 일관성 
3. 다음 게임 플레이에서 전략을 준수하는 정도

 전략은 모든 게임 상태에 대한 조치가 있는 경우 완전한 것으로 간주

제안자의 전략이 완전하려면 초기 제안 계획이 포함되어야 하며, 그 다음 라운드에서의 행동 계획이 수령인이 이전 제안을 수락하거나 거부하는지에 따라 결정되어야함

제안자의 전략이 불완전한 경우, 수령인이 전략의 나머지 부분이 의존하는 행동을 하지 않을 때 제안자가 부적절하게 행동할 수 있음 -> 예시 0에서1달러 사이로만 제안해야함 



불안전한 전략

제안자가 욕심이 많다고 가정하고 처음에 0.1 달러를 제안하고 걸저하면 조금씩 올려가면서 제안하는걸 전략에 넣음   하지만 이전략은 초기에 수령자가 무조건 걸저해야만 함 . 초기에 수락을 해버리면 그다음 전략이 사라져버림 

# 4 RESULTS

총 4가지에 대해서 실험을 함 

multi-agent 와 singe 별로 llm모델을 GPT-3.5와 GPT-4 조합 

### RQ1. Which LLM architecture more accurately simulates human-like actions in the five-round ultimatum game?

![t_1](\img\2024\Simulating_Human_Strategic_Behavior__Comparing_Single_and_Multi-agent_LLMs\t_1.PNG)

실험 결과, 다중 에이전트 LLM 아키텍처는 단일 LLM보다 인간 실험 데이터와 일관된 행동을 훨씬 더 자주 보여줌   

-> 당연한 내용인듯 ...그보ㅗ다 전략 에러가 거의 전부라는게 신기하네 ..



오류 분석 결과, 두 아키텍처 모두 전략 생성이 게임 플레이 실수보다 오류의 큰 원인이 됨 



 표 2에는 네 가지 조건에 대한 전략, 게임 플레이 또는 둘 다의 오류 백분율중에서 

다중 에이전트 아키텍처에서는 시뮬레이션의 모든 오류가 전략 생성 오류로 인한 것으로 나타났으며, 게임 플레이 오류는 없음



이런 검증이 의미있나 싶음 ...



### RQ2. Which LLM architecture more accurately simulates the actions of player personalities?

![t_3](\img\2024\Simulating_Human_Strategic_Behavior__Comparing_Single_and_Multi-agent_LLMs\t_3.PNG)

 MultiAgent-4가 두 가지 성격 유형을 모델링하는 데 가장 잘 수행

-> 이것또한 gpt -4 가 성능이 좋고 multi agent여서 당연한 결과라고 생각됨 



공정-공정 시뮬레이션에서는 100%의 인간과 유사한 게임 플레이를 달성했지만, 욕심-욕심 조건에서는 단 10%만 인간과 유사한 게임 플레이를 달성

-> 대화없이 딜만하는데 되는게 신기한 방법인듯 

### RQ3. Which LLM architecture more often creates robust strategies: both logically complete and consistent with personality?

![t_4](\img\2024\Simulating_Human_Strategic_Behavior__Comparing_Single_and_Multi-agent_LLMs\t_4.PNG)

생략





# 4 RESULTS

생략

---
layout: post
title: "Human Simulacra: Benchmarking the Personification of Large Language Models"
date: 2025-1-7 02:05:23 +0900
category: paper
---

# Human Simulacra: Benchmarking the Personification of Large Language Models

2024년 2월 28일

중국 대학교들 

git : https://github.com/hasakiXie123/Human-Simulacra


# Abstract

LLM 시스템은 사람을 흉내내는 지능을 가짐 

이러한 능력으로 연구에 필요한 비용과 복잡도를 감소시킬 수 있음 

본 연구에서 멀티 에이전트 기반 언어모델의 의인화를 보여줌

# 1 Introduction

심리학과 사회학 연구는 사람의 행동에 관한 연구를 계속 해왔음 

이러한 연구는 참여자를 구하는것과, 높은 비용, 윤리적 고려사항 등 여러 문제를 가지고 있음

이러한 이유로 LLM을 통해 사람을 따라하는 방법에 관한 연구는 점점 관심을 받고 잇음 

연구에서 질문하고자 하는 내용은

```
Can LLMs simulate human cognitive processes, thereby assisting researchers in exploring human interactions without involving real human participants?

LLMs이 사람의 인지를 시뮬레이션 하고, 사람의 상호작요에 대한 연구를 사람대신할 수 있는가
```

해당 질문은 이미 심리학과 사회학자들에게 논의되고 있으며 LLM을 사용해 사람을 대체하는 방법이 옹호되고 있음 

그럼에도 불구하고 사람을 시뮬레이션 하는건 그룹단위로만 연구되고 있으며 답변에 대한 개개인의 미묘한 정확도는 재현할 수 없음 

 computer science분야에서 연구는 role-playing 테스크에서 집중하고 있음

이러한 연구는 특정한 전문적인 능력, 대화 스타일, 개인의 페르소나를 목적으로 하고있으나 롤플레잉 테스크는 인물의 외적인특성을 통해 단편적인 정보로  시뮬레이션 하는 역할밖에 못함



이러한 문제를 해결하기 위해 llm의 의인화를 목표로 LLM의 내적 특성을 정의함 

를 통해 특정한 성격을 시뮬레이션하며 인간처럼 외부 세계와 상호작용할 수 있게 하는 것으로 정의



virtual character dataset을 제공하며 멀티에이전트 기반 인지 모델과 심리학적 평가 방법을 제안함 



그사람의 서사에서 시작하는 광범위한 정보를 활용하여 반자동화된 서브테스크를 제안함 



멀티 에이전트 기반의 사람을 시뮬레이션한 데이터 셋을 생성함 11명의 사람과 129k의 텍스트로 이루어짐 

이때 생성된 캐릭터는 각각의 서사와 행동 특징이 있음 



논문의 컨트리뷰션

1. 생생한 가상 캐릭터의 서사를 통해 semi-automated 전략을 제안함 

2. 멀티 에이전트 기반 메커티즘을 제안함  MACM(Multi-Agent Cognitive Mechanism)

   이를 통해 복잡한 사람 시뮬레이션을 달성했다고 함 

3. 2차원의 심리학적인 평가 방법을 제안함 

   self-reporting, external observation 



# 2 Related Work

### Memory Systems in Cognitive Psychology.

인지 심리학에서 정보처리 접근 방법은 감각의 입력이 변혀오디고, 축소되고, 정교화되고, 저장되고, 회복되는 전체과정을 통해 이루어진다고 주장함 

이러한 인지는 사람의 뇌와 컴퓨터는 순차적으로 정보를 처리하는 유사성을 강조함 



사람의 기억을 단기기억과 장기기억에 따라 행동이 바뀌는데 이는 LLM의 롱텀메모리 저장방식알고리즘이 따라하기 때문에 시뮬레이션 할 수 있음

# 3 Human Simulacra Dataset

![f_1](\img\2024\Human_Simulacra__A_Step_toward_the_Personification_of_Large_Language_Models\f_1.PNG)

정보체인의 계측적 구조로 가상 캐릭터 데이터를 생성함 

위의 그림 1에서 3개의 레이어와 2개의 서브 레이어로 모델의 캐릭터를 정리함

왼쪽에서 오른쪽으로 갈수록 정보를 얻는 난이도와 데이터 양이 상승함 

반대로 오른쪽에서 왼쪽으로 갈수록 정보는 간결해지고 정보에대한 근본적인 사실 위주가 됨 

기존의 롤플레잉을 통한 연구는 사람의 간단한 정보를 통해 얕게 시뮬레이션하는것에는 성공함

연구에서는 사람을 시뷸레이션하기 위해 사람의 life story를 사용함 사람의 life story는 매우 복잡한 데이터로 다양한 정보 파편을 포함함

LLM을 사용하여 일관성 있는 life story를 만드는건 매우 어렵다고 함

![f_2](\img\2024\Human_Simulacra__A_Step_toward_the_Personification_of_Large_Language_Models\f_2.PNG)

캐릭터의 life story를 생성하기 위해 여러 테스크로 분해하여 semi-automated 전략으로 변경함 

해당 내용은 위으 그림2에서 볼 수 있음 



## 3.1 Character Attributes

Character attributes는 가상 캐릭터의 핵심 정보를 포함하며 life story를 만들기 위한 기준점이 됨 

attributes를 설계하는 동안 합리적은 연관성과 자연 법칙에 부합하도록 보장하는 것이 필요함

진짜 사람을 따라하기 위해 종합적인 특성을 만듦 

 {name, age, gender, date of birth, occupation, personality traits, hobbies, family background, educational background, short-term goals, and longterm goals}

the International Standard Classification of Occupations (ISCO-08)를 기반으로 해서 76개의 일반적인 직업을 수작으로 선택함 



## 3.2 Personality Modeling

개인화시 그사람의 생각, 기분, 행동을모두 고려해야함

모델의 개인화정확도를 높이기 위해서 타겟 캐릭터의 특성을 디자인해야함 

간단한 방법으로는 Five Factor Model 나 MBTI 방법등이 있음 

그러나 이런 방법들은 피할수 없는 단점이 있음

1. LLM은 블랙박스 모델임 내부에서 이해하는 방식은 잘못된 방식일 수 있음
2. 특정 타입으로는 사람의 복잡한 특성을 다 정의할 수 없음 

8가지 겅향을 높은 순부터 순서대로 나타내고 높은 순일수록 많이 나타다노록 지침을 마련함 

이렇게 해서 서로 다른 스크립트를 생성할 수 있음 

## 3.3 Character Profile and Biography

캐릭터의 프로필을 조합하기 위해 프로파일을 우선 랜덤을 선택하고 상응하는 특성들을 고름

이런 방법은 빠르나 속성의 충돌 문제를 가지고 있어서 Profile Selection module을 도입함

Profile Selection module의 품질과 정교함을 보장함 

## 3.4 Life Story

![t_1](\img\2024\Human_Simulacra__A_Step_toward_the_Personification_of_Large_Language_Models\t_1.PNG)

간단한 biography정보를 통해서 반복적인 생성을 통해 biography정보를 풍부하게 만듦 

T번의 반복 생성을 한다고 함 

1. Quality Check

   biography를 메뉴얼 적으로 합리성과 일관섬을 검사함

2. Chunking:  전기를 여러 청크로 분리함

3. Scoring : 각각의 청크의 Importance (전기에서 중요한 내용의 청크인지 여부), Elaborateness(청크 내부의 세부 수준), Redundancy(청크의 중복성 정도)를 계산함

이렇게 해서 높은 importance 와 낮은 elaborateness, redundancy의 청크를 확장해감

4. Expanding: LLM프롬프트를 통해 청크를 선택하고 새로운 life experience를 생성함 

위 과정으로 생성된 정보는 Table1 데이터임 

# 4 Multi-Agent Cognitive Mechanism

![f_3](\img\2024\Human_Simulacra__A_Step_toward_the_Personification_of_Large_Language_Models\f_3.PNG)

3에서 설명한 방법으로 가상 캐릭터의 life story를 정교하게 만듦 

그러나 제한된 context로 LLM이  고유한 감정적 성향을 적화하게 포착하지 못할 수 있음

그림3과 같이 인지심리학을 기반으로 한 Multi-Agent Cognitive Mechanism를 통해 이런 문제를 해결하고자 함 

4개의 LLM 에이전트를 사용함

탑 에이전트는 테스크를 할당하고 다른 에이전트로 부터 받은 정보를 조합하는 역하을 함

이는 두가지 핵심 과정이 있는데 장기 기억 구축과, 다중 에이전트 협력 인지 임

## 4.1 Long-term Memory Construction

사람은 성격은 유전적인 이유 뿐 아니라 환경, 문화, 개인적인 겸험 등 다양한 영향ㅇ르 받으며 뇌에 기록으로 저장됨 



... 4번 생략



# 5 Psychology-guided Evaluation

시뮬레이션을 평가하기 위해서 psychology-guided manner을 사용함

![f_4](\img\2024\Human_Simulacra__A_Step_toward_the_Personification_of_Large_Language_Models\f_4.PNG)

그림 4에서와 같이 2가지 방법을 사용함 (self report, observer report)

self-report는 자기 인식을 형성하는 능력을 평가함 

observer report는 신뢰할 수 있는 행동을 하는 능력에 초점을 맞춤 (목표하는 캐릭터와 ㅇ리치하는지를 비교)

## 5.1 Self Report

자기자신을 잘 알고있는지평가하기 위해 사전 질문을 준비함 

가상 캐릭터는 single, multiple  선택 질문에서 balnk를 채워야 함 

예시 질문은 아래와 같음 

“What is your name?”, “What do you think of your father?”, and “What were the reasons behind not
going through formal schooling for you?”.

## 5.2 Observer Report

self-report 평가 후 시뮬레이션이 스스로를 잘 이해하는지를 평가한 결과를 얻음

실제 상황에서 감정과 행동을 제3자의 관점에서 평가하는 것은 시뮬레이션이 대상(캐릭터)을 진정으로 이해하는지, 즉 내부에서 외부로 확장되는 시뮬레이션을 달성하는지 판단하기 위함입니다. 따라서 자기 보고 외에도, 우리는 인간 심판에 기반한 교차 평가인 관찰자 보고를 도입하여, 인간의 시각에서 시뮬라크럼(시뮬레이션된 복제물)을 평가하려고 합니다.
구체적으로는 Mussel et al. (2016)을 참고하여, 우리는 인간의 감정적 반응이나 성격 특성을 이끌어낼 수 있는 여러 가상의 시나리오를 만들었습니다. 각 시뮬라크럼은 주어진 시나리오 속에 자신이 있다고 상상하고, 그들이 어떻게 느끼고 어떤 행동을 취할 것인지 설명하도록 요구됩니다. 모든 응답은 수집되어 교차 평가를 위해 제출되며, 이는 그림 4의 오른쪽 하단에 나타나 있습니다.

cross-evaluation을 함 

1. 사람이 Q A에 대해서 

   1과 2 시나리오를 분석하고 응답자의 성격을 응답함

   성격이 불일치가 나오면 시뮬레이션 오류를 의미함 

2.  3과 4에게 대상 캐릭터의 생애 이야기를 철저히 읽고, 그들이 그 캐릭터라면 시나리오에서 어떻게 느끼고 어떤 행동을 할 것인지를 답하게 합니다. 그런 다음, 심판 1과 2는 인간의 응답과 시뮬라크럼의 응답 간의 유사성을 비교합니다. 높은 유사성은 시뮬라크럼이 캐릭터에 대한 외부의 기대에 부합하는 행동을 채택했음을 증명하며, 이를 통해 고품질의 시뮬레이션을 달성했음을 나타냅니다.
   평가 과정 전반에 걸쳐, 우리는 심리학에 대한 기본적인 이해를 가진 다양한 심사 위원을 선정하고, 편향을 줄이기 위해 그들이 필요한 경우에만 대상 캐릭터에 대한 정보를 제공하도록 보장합니다.

# 6 Experiments

## 6.1 Implementation Details












































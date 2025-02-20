---
layout: post
title: "How Far Are LLMs from Believable AI? A Benchmark for Evaluating the Believability of Human Behavior Simulation"
date: 2025-02-20 02:05:23 +0900
category: paper
---

# How Far Are LLMs from Believable AI? A Benchmark for Evaluating the Believability of Human Behavior Simulation

url: https://arxiv.org/abs/2312.17115

홍콩대



# Abstract

LLM이 시뮬레이션한 행동에 대한 체계적인 평가가 부족하기 때문에, LLM이 인간 사이에서 얼마나 신뢰할 수 있는지에 대한 명확한 결론을 내리기 어렵습니다. 즉, 어떤 LLM의 행동이 설득력 있게 인간과 유사한지, 그리고 어떤 부분이 추가 개선이 필요한지가 불분명합니다



**SimulateBench**를 설계하여 LLM이 인간 행동을 시뮬레이션할 때의 신뢰성을 평가함

1. **일관성(Consistency)**: LLM이 시뮬레이션하려는 인간의 주어진 정보를 바탕으로 얼마나 일관되게 행동할 수 있는가.
2. **견고성(Robustness)**: LLM의 시뮬레이션된 행동이 다양한 요인의 변화(교란)에 직면했을 때 얼마나 견고하게 유지되는가.

SimulateBench는 65개의 캐릭터 프로파일과 총 8,400개의 질문을 포함하여 LLM이 시뮬레이션한 행동을 검증함

이를 바탕으로,  10개의 널리 사용되는 LLM을 대상으로 캐릭터 시뮬레이션 성능을 평가



. 실험 결과, 현재의 LLM은 할당된 캐릭터와의 행동 정렬(align)에 어려움을 겪으며, 특정 요인에 대한 교란에 취약하다는 사실이 드러남



# 1 Introduction

AI의 사람 시뮬레이션은 사회 이론의 프로토타입 제작(Aher et al., 2023; Horton, 2023; Kovac et al., 2023), 합성 연구 데이터 생성(Hämäläinen et al., 2023; Wang et al., 2023a), 비플레이어 캐릭터 제작(Laird and VanLent, 2001) 등 다양한 응용 분야에서 활용될 수 있음



기존 AI기반 사람 시뮬레이션의 문제점 

주요 문제

1. **프로파일의 복잡성**: 시뮬레이션에서 사용하는 프로파일은 종종 길고 복잡하며, 신원 정보, 사회적 역할(Wasserman, 1994), 관계(Hinde, 1976) 등의 개인 데이터를 포함하여 포괄적인 시뮬레이션을 가능하게 합니다.
2. **LLM의 견고성 부족**: 입력 데이터가 교란(perturbation)을 받을 때 LLM은 이를 효과적으로 처리하지 못합니다(Perez and Ribeiro, 2022). 이는 동일한 시나리오에서 다른 행동을 생성하게 만들 수 있습니다. 특히 LLM이 배치된 환경이 동적으로 변화하면서 프로파일 정보가 지속적으로 업데이트되면, LLM이 이를 효과적으로 처리하지 못할 경우 신뢰성이 손상될 수 있습니다.

기존 연구의 한계점

**짧은 프로파일 정보의 평가**: 기존 연구는 LLM이 매우 간략한 프로파일 정보를 시뮬레이션하는 능력만 평가하며, 이는 사람을 효과적으로 시뮬레이션하기에 충분하지 않습니다.

**교란의 영향 평가 부족**: 교란이 LLM의 신뢰성에 미치는 잠재적 영향을 철저히 조사하거나, 이러한 교란이 신뢰성에 구체적으로 어떤 영향을 미치는지 탐구하는 메커니즘이 거의 없거나 아예 없습니다.



#### 주요 도전 과제:

- **긴 입력 문맥 처리의 비효율성**: 현재 LLM은 긴 입력 문맥을 효과적으로 처리하지 못합니다(Liu et al., 2023). 이는 LLM이 프로파일에서 중요한 정보를 포착하지 못하게 할 수 있으며, 신뢰성을 저하시킬 위험이 있습니다.
- **환경 변화 대응력 부족**: LLM이 시뮬레이션하는 동안 환경이 동적으로 변화하며, 프로파일 정보가 지속적으로 갱신되는 상황에서 이를 효과적으로 처리하지 못할 경우, 시뮬레이션의 신뢰성이 심각하게 손상될 수 있습니다.





![f_1](F:\code\whtngus.github.io\img\2025\How_Far_Are_LLMs_from_Believable_AI__A_Benchmark_for_Evaluating_the_Believability_of_Human_Behavior_Simulation\f_1.PNG)

LLM이 긴 프로파일 입력을 처리하지 못하거나 견고성이 부족함으로 인해 발생하는 부정적인 영향을 평가하기 위해, 우리는 LLM의 신뢰성을 평가하는 두 가지 차원을 제안함

**일관성(Consistency)**: 생성된 인간 행동이 긴 프로파일 입력에 제시된 신원 정보, 사회적 역할, 관계를 얼마나 정확하게 묘사하는가?

**견고성(Robustness)**: 프로파일의 업데이트나 교란이 발생했을 때, LLM의 행동이 얼마나 견고하게 유지되는가?

위 2개를 측정하기 위해 캐릭터 데이터수집 및 일관성과 견고성을 평가하기 위한 SimulateBench 벤치마크를 도입함 



그림 1을 보면 프로파일 업데이트 후 같은 질문을 함 (robust) , consistency는 어떻게하는지 아래설명을 더 들어봐야 알듯





- SimulateBench 구서용소

> **프로파일 설명 프레임워크**: 사람에 대한 정보를 포괄적으로 문서화하기 위해 설계된 구조입니다.
>
> **캐릭터 프로파일 데이터셋**: 65명의 캐릭터 프로파일을 포함한 데이터셋입니다.
>
> **일관성 데이터셋**: LLM이 프로파일 정보를 바탕으로 논리적 추론을 통해 다중 선택 질문을 정확히 답할 수 있는지를 평가합니다.
>
> **견고성 데이터셋**: 프로파일의 교란(perturbation)을 적용하고, LLM의 일관성 능력이 어떻게 변화하는지 비교합니다.



# 2 Related Work

## 2.1 Human behavior Simulation

많은 연구들이 사회과학, 경제학, 심리학, 인간-컴퓨터 상호작용 분야에서 LLM을 활용하여 인간 행동과 사회적 상호작용을 시뮬레이션하고, 이론 프로토타이핑과 합성 연구 데이터를 생성하려고 노력하고 있음



 LLM을 프로파일로 프롬프트하여 역할극(role-playing)과 개인화된 대화에서 인간 대화를 시뮬레이션하려고 시도했습니다(Zhang et al., 2018; Zheng et al., 2019, 2020; Wang et al., 2023b).

-> 그러나 프로필이 간결하며, 개인정보 양이 제한적 이라고함 

## 2.2 Evaluation of LLMs in Human Behavior Simulation

Aher et al. (2023)은 LLM이 인간 실험 연구에서 대표적인 참가자 샘플의 행동을 시뮬레이션할 수 있는지를 평가하기 위해 **튜링 실험(Turing Experiment)**을 도입

Park et al. (2023)은 에이전트의 사회적 상호작용을 평가하기 위해 샌드박스 및 온라인 소셜 네트워크를 제안



그러나 LLM의 신뢰성을 체계적이고 세밀하게 평가할 수 있는 벤치마크는 존재하지 않

# 3 SimulateBench

![t_1](F:\code\whtngus.github.io\img\2025\How_Far_Are_LLMs_from_Believable_AI__A_Benchmark_for_Evaluating_the_Believability_of_Human_Behavior_Simulation\t_1.PNG)

 **SimulateBench**를 도입하여 캐릭터 프로파일 수집 및 신뢰성 평가를 수행함

65개의 캐릭터 프로파일과 8,400개의 질문을 포함하여 LLM의 사람행동 시뮬레이션 시 일관성과 견고성을 평가한다고함 

->발화 정보가 없는게 아쉬움 

## 3.1 Profile Descriptive Framework and Character Dataset

LLM이 인간 행동을 정확하게 시뮬레이션하기 위해서는 포괄적인 프로파일 정보가 필요함

 **프로파일 설명 프레임워크(profile descriptive framework)**를 제안하고, 이를 기반으로 캐릭터 데이터셋을 수집

#### Profile Descriptive Framework

캐릭터 정보를 세 가지 측면에서 포괄적으로 문서화하는 설명 프레임워크를 제안

> **변경 불가능한 특성 (Immutable Characteristic)**: 이름, 성별, 나이와 같이 쉽게 변경될 수 없는 특성(Stein, 2001)을 의미합니다.
>
> **사회적 역할 (Social Role)**: 특정 사회적 상황에서 사람들이 개념화한 일련의 연결된 행동, 의무, 신념, 규범(Wasserman, 1994; Eagly and Wood, 2012)을 나타냅니다.
>
> **관계 (Relationship)**: 사회 과학 분야의 기본 연구 요소로, 두 명 이상의 개인 간의 모든 대인 관계를 의미합니다(Sztompka, 2002).

Relationship의 경우 친숙도, 판단, 애정, 행동 패턴, 관계 상태, 의사소통 기록 등의 측면이 포괄적으로 사용

#### Character Dataset

다음과 같은 인기 장르의 TV 드라마에서 캐릭터를 선정했습니다:

- **The Simpsons** (애니메이션)
- **Friends** (코미디)
- **Breaking Bad** (범죄)
- **The Rings of Power** (SF)



팬덤(fandom) 웹사이트에서 캐릭터 프로파일 정보를 추출함

-> 애이메이션 tv의 가상 캐릭터를 사용한것으로 보임 



프로파일은 평균적으로 **3,277개의 토큰**을 포함하고 있어, 이전 연구보다 포괄적이라고함 이전 연구 Park et al. (2023)는 203개의 평균적인 토큰을 가짐 

->사람이 직접 에러여부를 레이블링을 하고, 주석자가 익숙한 캐릭터만을 레이블링함 

 네 명의 인간 주석자(annotator)를 모집하여 수집된 데이터를 신중하게 검증하고, 프로파일이 오류가 없도록 보장했습니다. 각 주석자는 프로파일 설명 프레임워크의 작동 방식과 데이터 오류 감지 방법을 다루는 **10시간의 집중 교육**을 이수

## 3.2 Measuring Consistency

#### Consistency Dataset 

일관성 데이터셋은 다중 선택 질문으로 구성되어 있으며, 각 캐릭터당 평균적으로 **150개의 질문**을 포함하며 질문에 정확한 답을 하기 위해 LLM 프로파일 정보를 분석하고 논리적인 추론을 적용함

**질문 생성**: GPT-4를 활용하여 다양한 프로파일 정보 유형에 기반한 질문을 자동으로 생성

**질문 유형**: 프로파일 설명 프레임워크에 따라, 질문은 **변경 불가능한 특성(Immutable Characteristics)**, **사회적 역할(Social Roles)**, **관계(Relationships)**와 관련된 세 가지로 구성

**정답 생성 및 검증**: 모든 질문에 대해 정답(gold answer)을 수동으로 생성하고, 답변의 정확성을 두 번 검토하여 오류를 방지

모든 질문에는 "이 질문에 답하기에 충분한 정보가 없습니다"라는 선택지를 추가했습니다.

-> 결국 가상 캐릭터에 질문 답변의 경우 가상으로 생성됨

이를 실질적인 평가로 활용할 수 있는가는 고민해봐야됨 



질문은 모든 질문은 정답(gold answer)을 기준으로 다음 답할수 있는 Known, 답하기에 정보가 부족한 Unknown으로 분류함

일관성을 측정하기 위해, LLM이 일관성 데이터셋의 질문에 답하도록 하고, 정답의 정확도를 계산합니다. 이 정확도를 **일관성 능력(Consistency Ability, CA)**이라 명칭함



![f_3](F:\code\whtngus.github.io\img\2025\How_Far_Are_LLMs_from_Believable_AI__A_Benchmark_for_Evaluating_the_Believability_of_Human_Behavior_Simulation\f_3.PNG)

그림3은 생성된 데이터 예시  2개의 질문 수준은 메타데이터를 읽고 그대로 답하는 수준으로 보임 ..





## 3.3 Measuring Robustness

#### Robustness Dataset

캐릭터의 프로파일에 교란을 가하고 이에 따라 일관성 데이터셋의 질문을 수정함으로써 구성됨 

캐릭터의 **인구통계적 요소(demographic factors)** 내용을 수정함, 교육수준, 성, 인종, 나이 등 

교란으로 인해 비합리적인 결과가 발생하지 않도록, 초기 프로파일에 대한 모든 수정의 결과 검토했다고함





**프로파일 수정 반영**: 캐릭터 프로파일의 특정 요소를 수정하면, 일관성 데이터셋의 질문을 복제한 후 해당 변경 사항에 맞게 질문과 정답(gold answer)을 수정

나이를 20->30으로 변경한 경우 일관성 데이터셋에서 해당 캐릭터 질문을 가져와 나이 변경사항에 맞게 질문과 정답을 수정함 

이렇게 수정된 데이터셋은 견고성 데이터셋에 포함됨 

#### Measuring Metrics: RA and RCoV

견고성의 목적은 **프로파일에 약간의 수정(slight modifications)**을 가했을 때, LLM의 일관성(CA, Consistency Ability) 성능 변동을 평가하는 것

-> 이렇게 만든 데이터셋으로 견고성을 평가하는게 의미가 있는지... 추가로 변형후에 다시 데이터를 기존 일관성과 같이 만든다면 어떻게 평가할지 봐야될듯



를 달성하기 위해, 우리는 **CA의 변동치(variation)**와 **CA 점수의 변동 계수(coefficient of variation)**를 견고성 성능으로 사용하며, 이를 각각 **RA**와 **RCoV**로 나타냄



ex

> GPT-3.5를 사용해 특정 캐릭터를 시뮬레이션한다고 가정했을 때, 프로파일에서 **나이 속성(age property)**을 **10, 15, 20, 25, 30**으로 변경하면 다섯 가지 변형(variants)이 생성
>
> 다섯 변형에 대해 견고성 데이터셋을 실행하면, 다섯 개의 CA 점수 s1,…,s5s_1, \dots, s_5s1,…,s5가 생성
>
> 이 점수들의 평균과 편차를 구함 
>
> RA=σ
>
>  RCoV=RA/μ
>
> -> RA를 μ로 나누는 것은 **다른 모델 간의 견고성 성능 비교**를 가능하다고 함 -> 그냥 평균을 기준으로 정규화 후 하면 안되나?



예시

**모델 A**

- 평균 성능(μ): **0.3**
- RA(σ): **0.04**

**모델 B**

- 평균 성능(μ): **0.9**
- RA(σ): **0.08**



RA만 보면 모델B의 RA가 더 커서 불안정해보임  그래서 편차도 더 커보임(자체 값이 커서)

**모델 A의 RCoV**:

RCoV=RA/μ=0.040.3≈0.13

**모델 B의 RCoV**:

RCoV=RAμ=0.080.9≈0.089

모델 B의 값이 오히려 안정적임 



# 4 Baseline Methods for Human Behavior Simulation



LLM이 인간 행동을 시뮬레이션하도록 유도하기 위해서는 다음 세 가지 구성 요소가 중요함

**I**: 인간 행동을 어떻게 시뮬레이션할지 설명하는 지침(Instruction).

**II**: 특정 캐릭터의 프로파일(Profile).

**III**: LLM이 완료해야 할 작업(Task)에 대한 설명.

#### I: Simulate Human Behavior

GPT-3.5와 같이 **RLHF**를 거친 모델은 특정한 언어적 선호와 습관을 가지게됨

-> ex) "나는 언어 모델입니다"라고 자신을 소개하는 습관은 신뢰성(believability)에 부정적인 영향을 미칠 수 있음

이러한 문제를 극복하기 위해, 우리는 LLM이 인간 행동을 시뮬레이션하는 방법을 지시하는 **지침 프롬프트 템플릿(instruction prompt template)**을 설정함

#### II: Profile of Specific Characters

**3.1절**에 따라, 우리는 지침 프롬프트 템플릿에 해당 정보를 채워 넣습니다.
예를 들어, **{person}**은 캐릭터의 이름으로 대체

#### III: Prompting for Consistency Dataset

일관성 평가가 **질문-답변 형식(question-answering format)**으로 수행되기 때문에, 작업 프롬프트는 다음과 같이 설정

"Answer the below question; you should only choose an option as the answer.{example}. {question}" .

다섯 가지 조합의 프롬프트 전략과 학습 설정을 고려한다고함

**Zero**

**Zero+CoT**

**Few**

**Few+CoT**

**Few+Self-Ask**

#### III: Prompting for Robustness Dataset

견고성 데이터셋에 사용되는 프롬프트는 일관성 데이터셋에 사용되는 프롬프트와 유사
차이점은 **지침 프롬프트 템플릿(instruction prompt template)**에 **교란된(perturbed) 캐릭터 프로파일**을 제공한다는 점
LLM은 캐릭터의 변형(variants)을 시뮬레이션할 수 있으며, 이러한 변형을 시뮬레이션할 때 **RA(Robustness Ability)**와 **RCoV(Coefficient of Variation)**를 계산하여 LLM의 견고성을 평가합니다.



# 5 Experiment

## 5.1 Experimental Setup

상용 모델과 오픈 소스 모델을 포함하여 10개의 LLM을 종합적으로 평가함

GPT-3.5와 GPT-4는 상용 모델이고, 다른 모델은 hugging face의 오픈 소스 모델

## 5.2 Consistency Evaluation Results

#### GPT series perform better than open-source models; longer context size does not necessarily mean better consistency performance

![t_2](F:\code\whtngus.github.io\img\2025\How_Far_Are_LLMs_from_Believable_AI__A_Benchmark_for_Evaluating_the_Believability_of_Human_Behavior_Simulation\t_2.PNG)

표 2는 캐릭터를 시뮬레이션할 때 모든 질문 유형에 걸쳐 다양한 모델의 CA 점수를 보여줌 

모델의 입력 컨텍스트 길이가 길다고 모델 정확도가 올라가는건 아니고 기본적으로 모델 크기가 큰 gpt-4 3.5가 정확도가 더 높다고 함 

정확도가 의외로 높을 수 있는데 그건 위의 그림3 질문 예시를 보면 어느정도 감이온다.

#### Models demonstrate severe simulation hallucination

모델들은 심각한 시뮬레이션 환각을 보여줌 Unknown 정확도는 엄청 낮은것을볼 수 있음 

프로필에서 이용 가능한 정보가 질문에 답하기에 불충분할 때, 이러한 모델들이 규정된 프로필을 준수하기보다는 터무니없는 응답을 제공하는 경향이 있으며, 이는 그들의 신뢰성을 훼손한다는 것을 나타냄 

-> 다른 해석도 가능할듯 .. 꼭 메타정보에 있는 정보만 대답하는게 맞을까? 그게 본인이라고 했는데 

## 5.3 Robustness Evaluation Results

![f_2](F:\code\whtngus.github.io\img\2025\How_Far_Are_LLMs_from_Believable_AI__A_Benchmark_for_Evaluating_the_Believability_of_Human_Behavior_Simulation\f_2.PNG)

모델이 캐릭터를 시뮬레이션하도록 지시받고 해당 캐릭터의 프로필에 변형(교란)이 가해졌을 때 RCoV, RA, CA 점수를 그림2에서 볼 수 있음 

#### Better consistency performance does not necessarily mean better robustness performance (일관성이 좋다고 견고성이 좋은건 아니다)

그림 2에서 볼 수 있듯이, 강력한 일관성 성능을 보이는 모델도 여전히 부적절한 견고성 성능을 보일 수 있음 

Vicuna-13B-16K(0.621)는 Age Variants 그룹에서 Vicuna-7B-16K(0.457)보다 일관성 측면에서 더 나은 성능을 보이지만, Vicuna-13B-16K는 더 나쁜 견고성을 나타낸다(Vicuna-7B-16K의 0.006보다 RCoV가 0.024 더 크고, RA가 0.003보다 0.015 더 큼). 

##### Open-source models show poor robustness performance; models exhibit similar robustness to different profile perturbations(오픈 소스 모델은 견고성 성능이 떨어지는 경우가 많으며 프로필 변동성엔 유사한 견고성을 보임)

![t_3](F:\code\whtngus.github.io\img\2025\How_Far_Are_LLMs_from_Believable_AI__A_Benchmark_for_Evaluating_the_Believability_of_Human_Behavior_Simulation\t_3.PNG)

일부 오픈 소스 모델은 프로필 변형에 직면할 때 견고성 성능이 크게 저하됨

# 6 Influential Factors for Believability

신뢰성에 중대한 영향을 미치는 네 가지 요인에 대해 더 깊이 살펴봄 

#### Simulation hallucination

표 2에서 볼 수 있듯이, 모델은 알려진 질문보다 알 수 없는 질문에 대한 CA가 상당히 낮은 심각한 시뮬레이션 환각을 보여줌

논문에서는 모델이 프로필의 정보가 없지만 관련 등장인물에 대한 정보를 미리 알수도 있다고 이야기함

 character.ai 및 npc.baichuan-ai 같은 상업용 시뮬레이션 제품의 신뢰성을 저하시킬 수 있다고 함 

#### Bias of models towards specific demographic traits

![t_4](F:\code\whtngus.github.io\img\2025\How_Far_Are_LLMs_from_Believable_AI__A_Benchmark_for_Evaluating_the_Believability_of_Human_Behavior_Simulation\t_4.PNG)

 어떤 프로필 정보가 다양한 LLM에 대해 높은 신뢰성을 가져올지 조사하기 위해 프로필의 다른 인구 통계 정보를 교란하여 LLM의 일관성을 비교함

심슨가족의 호머의 데이터를 변경한 경우 table 4를 보면 모든 LLM은 특정 인구 통계학적 요인을 가진 프로필에 대한 다양한 수준의 선호도를 나타냄

 예를 들어, LongChat7B-32K는 백인 인종에 대해 유의미하게 더 높은 일관성 점수를 나타냄

연령 그룹의 5개 모델은 출생 연도가 2000일 때 우수한 성능을 보여줌

여러 모델이 겹치는 코퍼스에서 훈련되기 때문에 코퍼스 편향이 이러한 모든 모델에서 동시에 나타나고 있다는 사실을 시사한다고 함 

=> 학습 데이터가 많이 겹친다는걸 이렇게 증명하네 ;;

-> 하나의 캐릭터만 대상으로 한게 이상함 

#### Position in the profile

긴 택스트의 경우 프로필 내부 정보 배치에 성능 영향을 받음 

이 문제를 조사하기 위해 프로필 정보의 순서를 조정하는 실험을 수행

원래 프로필은 불변 특성, 사회적 역할, 관계 순서로 정보를 제공하며, 이를 "정상(Normal)"이라고 표시합니다. 조정된 순서는 "역순(Reverse)"으로 표시되며, 사회적 역할, 관계, 불변 특성 순서로 LLM을 평가함 

-> 즉 프로필의 역순으로 질문 순서를 바꿔서 다시 평가 

![t_5](F:\code\whtngus.github.io\img\2025\How_Far_Are_LLMs_from_Believable_AI__A_Benchmark_for_Evaluating_the_Believability_of_Human_Behavior_Simulation\t_5.PNG)

순서를 변동하니까 성능 차이가 심해짐

이러면 앞의 실험이 다 무효가 되는건 아닐까?   프로필 기반으로 대답을 하는게 아니라 순서의 영향을 받고 있으니 모델은 메타정보를 인지하지 못함

#### Reasoning prompting

![t_6](F:\code\whtngus.github.io\img\2025\How_Far_Are_LLMs_from_Believable_AI__A_Benchmark_for_Evaluating_the_Believability_of_Human_Behavior_Simulation\t_6.PNG)

COT를 적용한 경우 성능이 높아지기 때문에 이를 적용해서 테스트해봄

Few, Few+CoT, Few+Self-Ask, Zero, Zero+CoT의 프롬프트 조합을 사용하여 시뮬레이션을 수행

고려된 모든 프롬프트 조합 중에서 다른 프롬프트와 비교했을 때 모든 모델의 성능에서 일관된 개선을 보이는 프롬프트 조합은 없는 것으로 나타남

-> 의외임 



논문에서 해석한 이유는  CoT 및 Self-Ask와 같은 이러한 프롬프트 기법의 효능이 주로 해결, 의사 결정 및 계획과 같은 추론 능력을 포함하는 작업의 성능을 향상시키는 능력에 있다는 것

몇몇 sllm 모델은 fewshot의 예시때문에 프롬프트가 길어져서 예시답변을 따라하거나 문제를 이해하지 못하는걸로 보인다고 함  -> sllm 의 경우 이미 해당 케이스를 많이 봄 

# 7 Conclusion

LLM의 신뢰성 수준을 측정하기 위한 두 가지 새로운 차원인 일관성과 강건성을 제안

프로필 수집과 LLM의 일관성 및 강건성 측정을 위한 벤치마크인 SimulateBench를 도입

SimulateBench를 통해 인기 있는 LLM의 신뢰성 수준을 평가

# 8 Limitations

간 행동을 시뮬레이션할 때 LLM의 신뢰성 수준을 측정하기 위한 두 가지 차원을 제안함

인간 행동을 시뮬레이션하는 것은 캐릭터 프로필에 대한 광범위하고 자세한 정보를 필요로 하는 복잡한 작업으로 데이터가 부족함

많은 유명 모델에 대한 철저한 평가에도 불구하고 Anthropic의 Claude와 같은 특정 상용 모델은 평가에 포함되지 않음

이러한 누락은 이러한 모델을 사용하기 위한 자격 심사 요구 사항 때문이며, 저희는 이에 접근할 권한이 없었다고함
















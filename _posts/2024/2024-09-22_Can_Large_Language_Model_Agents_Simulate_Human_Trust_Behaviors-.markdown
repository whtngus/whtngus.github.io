---
layout: post
title: "Can Large Language Model Agents Simulate Human Trust Behaviors?"
date: 2024-08-21 02:05:23 +0900
category: paper
---

# Can Large Language Model Agents Simulate Human Trust Behaviors?

2024년 3월 10일 

Bernard Ghanem

url : https://arxiv.org/abs/2402.04559

# Abstract

LLM은 사럼울 시뮬레이션 방법으로 채택되고 있음

그러나 아래와 같은 근본적인 질문은 아직 해결 못하고 있음

```
can LLM agents really simulate human behaviors?
```

해당 연구에서는 사람에게 신뢰받을 수 있는 LLM 에이전트를 만드는걸 목표로 함 



연구에서 진행하는 프레임워크에서  agent trust에 초점을 맞춤

이를 연구하면서 특히 GPT-4 LLM agent가 사람과 비슷한 행위를 할 수 있다고 함

-> 사람을 시뮬레이션 할 가능성이 있음을 확인함

# 1. Introduction

agent-based simulation 에서 LLM을 사용한 연구가 계속 증가하고있음 

많은 LLM을 통한 연구에서 신뢰성과 복잡한 사회적 상호작용을 할 수 있음을 보여주지만 사람을 시뮬리이션 하는 연구는 찾아볼 수 없다고 함 

해당 연구에서는 사람을 시뮬레이션 하고  agent trust(사람의 신뢰)를 모방할 수 있는지를 탐구함 

->  agent trust는 다른사람의 긍정적인 기대에 기반하여 위험성이 있는 행동에도 긍정적인 반응을 함 (경제학에서 확립된 방법론)



Belief-Desire-Intention(BDI) 프레임워크를 채택하고 LLM 에이전트를 테스트함 

-> 신념-욕구-의도 프레임워크 에이전트의 의사결정 과정을 설명하는 모델 



연구에서 4가지 시나리오에 대해서 검증함 

1. 상대플레이어의 인구통계학 정보가 바뀐 경우 신뢰도에 영향이 있는지를 조사함 
2. 다른 에이전트에 대한 신뢰도를 비교함 
3. 상대에 대한 신뢰성을 조작하여 실험함(상대를 신뢰한다, 상대를 신뢰하지 않는다)
4. CoT를 사용해 이유를 zero-shot을 추론함



연구 결과는 상대의 인구통계학 정보에 따라 신뢰성이 바뀌는것을 추론했으며, 에이전트보다 사람을 더 선호함

신뢰성은 강화되는것 보다 약회되는것이 더 쉬우며 이는 추론 전략에 영향을 받을 수 있음 



연구 요약

- LLM이 사람을 시뮬레이션 할 수 있는지와 BDI프레임워크에서 신뢰관계를 구축할 수 있는지에 대해 보여줌
- LLM 에이전트가 일반적으로 신뢰 행동을 보여줌을 발견함  특히 GPT-4가 높은 신뢰를 받음을 확인했다고함
- 신뢰성에 대한 직접적인 조작을 사람과 대조하여 실험함
- LLM 에이전트를 사용하여 응용프로그램에 미치는 영향에 대해 논의함

# 2. LLM Agents in Trust Games

## 2.1. The Setting of Trust Games

![f_1](F:\code\whtngus.github.io\img\2024\Can_Large_Language_Model_Agents_Simulate_Human_Trust_Behaviors\f_1.PNG)

Trust Game을 기반으로 실험함 위의 그림1과 같이 플레이어가 처음으로 돈을 보낼지에 대한 결정을 내림 

 trustor : 신뢰자 - 처음 돈을 보낼지 결정하는 사람 

trustee : 수탁자, 신라죄의 행동에 응답하는 사람 - trustor의 결과를 보고 응답하는 사람

이를 기반으로 6개의 타입의 게임을 만듦

### Game 1: Trust Game

trustor는 10$를 받고 시작함 

그리고 N$를 보낼 수 있음  -> 이걸 trust behavior이라고 명칭함 

그리고 trustee는 $3N을 받음 그리고 이중 일부를 되돌려줄 수 있음 -> 이걸 reciprocation behavior 라고함

### Game 2: Dictator Game

game 1과같이 시작함 10$를 받고, N\$를 보낼 수 있음 그리고 trustee는 \$3N을 받음

다른점은 trustee는 돈을 돌려줄 수 있는 옵션이 없음. 그리고 이 내용을  trustor도 알고 있음

### Game 3: MAP Trust Game

MAP Trust Game (MAP represents Minimum Acceptable Probabilities) 

trustor는 trustee를 신뢰할지 말지를 결정해야함 

신뢰를 안하는 경우 각각 10$씩을 받음

둘다 신뢰하는 경우 15$씩을 받음 

trustor가 신뢰하고 trustee가 신뢰하지 않는 경우  trustor는 8$ 그리고 trustee는 22\$를 받음

이때 trustor가 신뢰할 가능성을 P 로 정의하고  trustee가 신뢰할 수 있는 최적의 P값을 찾음 

### Game 4: Risky Dictator Game

MAP에서 한가지 관점을 추가함 

trustee는 존재하지만 신뢰여부를 선택하지 못하고 순수하게 P의 확률로 신뢰, 신뢰안함여부가 결정됨 

### Game 5: Lottery Game

2가지 게임이 있음 

1. Lottery People Game

trustor는 trustee가 신뢰를 선택할 확률을 알게됨 

그리고 trustor는 신뢰할지 혹은 고정된 돈을 받을지를 결정함 

2. Lottery Gamble Game

MAP게임과 비슷함 

승리확률 P를 보고 도박을 할지 고정된 금액을 받을지를 결정

### Game 6: Repeated Trust Game

 Trust Game을 여러 라운드를 실행함 

매 실행시 마다 초기 10$로 시작함



## 2.2. LLM Agent Setting

CAMEL framework로 실험환경을 구성함 (코드 공개 안됨)

그리고 테스트한 llm 모델은 figure1 에 나와있음 

### Agent Persona.

실제 사람의 연구 설정을 잘 반영하기 위해 LLM 에이저느를 다양한 페르소나 프롬프트를 반영함 

GPT-4를 통해 53가지 타입으 페르소나를  템플릿을 생성 하고 각각의 페르소나는 이름, 나이, 성별, 주소, 직업, 그리고 background를 포함하고있음 

### Belief-Desire-Intention (BDI)

BDI 프레임 워크는 에이전트 지향 프로그래밍에서 확립된 접근 방식이며, 최근 언어모델을 모델링하는데 사용됨 



LLM 에이전트가 의사결정을 내리는 과정에서 신념, 욕구, 의도를 출력하도록함 

# 3. Do LLM Agents Manifest Trust Behavior?

LLM 에이전트가 신뢰성있게 행동하는지를 조사함

1. 양의 정수를 보내는지 (마이너스는 보낼 수 없기 때문에)와 가진돈을 초과해서 보내는지 
2. 각 결정에 대해서 추론할 수 있는지 

## 3.1. Amount Sent

![f_2](F:\code\whtngus.github.io\img\2024\Can_Large_Language_Model_Agents_Simulate_Human_Trust_Behaviors\f_2.PNG)



Valid Response Rate (VRR) 평가 지표를 제안함 - 초기 보내는 돈이 10$내에 속하는지를 확인하여 llm모델이 게임을 이해했는지를 확인함 

그림 이에서 Llama2-7b를 제외하고 VRR이 높다고 함 

-> x 검은색바가 뭘 의미하는지 몰라서 해석이 잘 안됨 



## 3.2. BDI

3.1 에서 증명된 내용은 신뢰성 있는 행동이라고 충분히 증명할 수 없음. 범위 내에서 랜덤으로 보낼 돈을 선택할 수 있기 때문 

대문에 BDI output에서 왜 그만큼 돈을 보냈는지 이유를 추론하여 random으로 출력한게 아니라는걸 반박함



많은 금액을 주는 페르소나에서 하나의 BDI를 선택하고 적은 금액을 주는 페르소나에서 또 하나의 BDI를 선택 후 긍정적인 요소는 파란색 부정적인 요소는 빨간색으로 표시함 

![prompt_1](F:\code\whtngus.github.io\img\2024\Can_Large_Language_Model_Agents_Simulate_Human_Trust_Behaviors\prompt_1.PNG)

![prompt_2](F:\code\whtngus.github.io\img\2024\Can_Large_Language_Model_Agents_Simulate_Human_Trust_Behaviors\prompt_2.PNG)

## 3.3. Basic Analysis of Agent Trust

1. Vicuna-7b 모델이 높은 신뢰성을 보여줬다고함 

으외로 gpt-3.5-turbo는 낮은 성능을 보여줌

2. 사람은 평균적으로 5.97$를 보내지만 gpt-4나  Vicuna-7b은 더 많은 돈을 보냄  

그리고 gpt-3.5-turbo는 더 낮은돈을 보냄

=> Figure2 참조 (위에)

Vicuna-33b는 또 낮은돈을 보낸걸 봐서는 모델별 특성이 있음을 보임 

3. Llama2-70b and Llama2-13b는 보내는 돈이 거의 수렴함 

# 4. Does Agent Trust Align with Human Trust?

에이전트의 신뢰성이 사람고 비슷한지 아닌지를 탐구하고자 함 

1. 새로운 컨셉의 behavioral alignment을 제공하고 기존 방법과 차의점을 명시함
2. 신뢰 행동이 사람과 일치함을 보임 



## 4.1. Behavioral Alignment

기존에는 가치 측면과 LLM의 무해함을 강조함 

그러나 이정보만으로는 사람과 다면적으로 일치함을 보일 수 없음 

이를 해결하기 위해 behavioral alignment를 제안함 

사람과 유사성을 평가하기 위해 영향도인 behavioral factors 와 복잡도인 behavioral dynamics 으로 판단 



에이전트는 사람의 신뢰와 일치하는지를 평가함 

이대 3가지 요소 사용

1.  reciprocity anticipation : 사호성 기대 (도움받을 준경우 상대도 나에게 도움을 줄것이다)
2. risk perception : 위험 인식 (어떤 행동이나 결정이 위험이 얼마나 큰지 인식)
3. prosocial preference : 친사회적 선호 (다른 사람들에게 이익이 되는 방식으로 행동하려넌 선호)

위 세가지 요소로 정량적인 평가가 가능함 

또한 BDI를 사용해 LLM 에이저트가 사람과 유사한 기본적 추론과정을 가지는지 판단할 수 있음 

## 4.2. Behavioral Factor 1: Reciprocity Anticipation

![f_3](F:\code\whtngus.github.io\img\2024\Can_Large_Language_Model_Agents_Simulate_Human_Trust_Behaviors\f_3.PNG)

Trust Game 게임에서 사람은 Dictactor Game 보다 높은 금액을 보냄 

-> Dictator Game 의 경우 돈을 돌려받지 않음으로 더 적은 돈을 보내주는걸로 보임 

아래 여러 해석이 있지만 LLM 에이전트 들은 사람과 비슷하지 않은 경우가 많으며 둘다 비슷하게 돈을 주는것으로 보임 ...

BDI 분석 결과에서 gpt-4의 경우 사람과 비슷한 의견을 냈다고함, 그리고 dictator game에서 돈을 더 조금 보냄 -> 그러나 비율차이가 너무 많이난다...

## 4.3. Behavioral Factor 2: Risk Perception

![f_4](F:\code\whtngus.github.io\img\2024\Can_Large_Language_Model_Agents_Simulate_Human_Trust_Behaviors\f_4.PNG)

Risky Dictator Game에서 확률 p가 높을수록 신뢰 행동에 대한 위험이 낮아지고, 더 많은 인간이 신뢰를 선택됨

LLM은 신뢰에 대해 큰 영향을 받지 않으며 그나마 gpt-4가 영향을 받는걸로 보임 

## 4.4. Behavioral Factor 3: Prosocial Preference

![f_5](F:\code\whtngus.github.io\img\2024\Can_Large_Language_Model_Agents_Simulate_Human_Trust_Behaviors\f_5.PNG)

Lottery Game는 GPT-4와 굉장히 비슷함 

그림 5는 같은 확률에서 다른 사람을 신뢰한다는 것을 보임 

그냥확률 29 , 사람 54 

## 4.5. Behavioral Dynamics



...

생략

...

# 6. Implications

### Implications on Human Simulation

GPT-4와 인간의 신뢰 행동 간의 높은 행동적 일치를 발견한 우리의 연구는, 인간 상호작용과 사회 전체에서 가장 중요한 행동 중 하나인 인간의 신뢰 행동이 LLM 에이전트에 의해 시뮬레이션될 수 있다는 가설을 검증하는 중요한 경험적 증거를 제공

...













# 참고 

- BDI 프로세스

Deliberations와 Means-ends reasoning두 가지 프로세스를 사용 

BDI 3가지 개념 예시 

- B(Beilive)  : 열심히 출근하면 월급이 나올거다.
- D(Desire) : 월급을 받길 바란다 
- I(Intend) : 열심히 출근할거다






---
layout: post
title: "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment"
date: 2024-06-24 02:05:23 +0900
category: paper
---

# G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment

url : https://arxiv.org/abs/2303.16634



# 1 Introduction

LLM 모델 평가 방법은 

사람의 개입 없이 평가하는 방법과 사람이 평가하는 Human Evaluation 평가 방법이 있음 



태스크에 대한 정답이 있는 경우 사용할 수 있는 reference-based 평가에서 gold label에 대한 기계적인 평가 매트릭인 BLEU, ROUGE와 같은 지표는 창의성이나 다양성이 필요한 태스크에서 인간의 판단 혹은 선호도와 낮은 상관관계를 보여 사용하기 힘듦

 모든 태스크에 대해 Gold label이 존재하는 것이 아니므로 최근에는 정답 없이도(reference-free) 생성 결과물의 품질을 평가하는 LLM 기반의 평가 방법들이 제안되고 있음 



G-Eval인 자연어 생성(NLG) 시스템이 생성한 텍스트의 품질을 자동으로 평가하는 방법으로  Chain-of-Thought(CoT)과 form-filling을 제안함 

논문의 컨트리뷰션

1. 개방형 및 창의적 자연 언어 생성 작업에서 인간 품질 판단과의 상관관계 측면에서 참조 기반 및 참조 없는 기본 메트릭보다 성능이 뛰남
2. 사고의 연쇄(chain-of-thought)는 더 많은 맥락과 지침을 제공함으로써 LLM 기반 평가자의 성능을 향상시킬 수 있음
3. 토큰 확률에 따라 이산 점수를 재가중하여 더 세분화된 연속 점수를 제공할 수 있음
4. LLM 기반 평가를 하는 경우 사람이 작성한것보다 LLM이 작성한 텍스트를 선호하는 편향을 보임을 확인 



# 2. Method

![f_1](\img\2024\G-Eval__NLG_Evaluation_using_GPT-4_with_Better_Human_Alignment\f_1.PNG)



G-EVAL은 세 가지 주요 구성 요소를 가진 프롬프트 기반 평가 도구

1. 평가 작업의 정의와 원하는 평가 기준을 포함하는 프롬프트
2. LLM이 생성한 중간지침 세트 -> 상세한 평가 단계를 설명하는 CoT
3. LLM을 호출하고 반환된 토큰의 확률을 기반으로 점수를 계산 

### Prompt for NLG Evaluation

```
You will be given one summary written for a news article. Your task is to rate
the summary on one metric.
Please make sure you read and understand these instructions carefully. Please keep this document open while reviewing, and refer to it as needed.
-> 번역
뉴스 기사에 대한 요약 하나가 주어질 것입니다. 당신의 임무는 한 가지 기준으로 요약을 평가하는 것입니다. 이러한 지침을 주의 깊게 읽고 이해했는지 확인하십시오. 검토하는 동안 이 문서를 열어 두고 필요할 때 참고하십시오.
```

프롬프트로 평가 작업과 원하는 평가 기준을 정의함 



다양한 언어 생성 기준으로  일관성, 간결성, 문법이 있어 다양하게 생성가능하며 아래와 같이 설정 가능

```
Evaluation Criteria:
Coherence (1-5) - the collective quality of all sentences. We align this dimension with the DUC quality question of structure and coherence whereby ”the summary should be well-structured and
well-organized. The summary should not just be a heap of related information, but should build from sentence to sentence to a coherent body of information about a topic.”
-> 번역
평가기준:
일관성 (1-5) - 모든 문장의 종합적인 품질. 우리는 이 차원을 DUC 품질 질문의 구조와 일관성과 맞추어 "요약은 잘 구성되고 잘 조직되어야 합니다. 요약은 단순히 관련 정보의 집합이 아니라, 문장에서 문장으로 이어지며 주제에 대한 일관된 정보의 본문을 형성해야 합니다"
```

### Auto Chain-of-Thoughts for NLG Evaluation

 chain-of-thoughts (CoT)는 텍스트 생성 과정에서 LLM이 생성하는 중간 표현들의 연속임 (한 토큰씩 생성)



평가 작업의 경우, 일부 기준은 단순한 정의를 넘어서 더 상세한 평가 지침이 필요하며, 각 작업에 대해 이러한 평가 단계를 수동으로 설계하는 것은 시간 소모적

->  LLM이 이러한 평가 단계를 스스로 생성할 수 있음을 발견함 

CoT는 LLM이 생성된 텍스트를 평가하는 데 더 많은 맥락과 지침을 제공할 수 있으며, 평가 과정과 결과를 설명하는데도 도움이 될 수 있음 

텍스트 요약에서 “Evaluation Steps:”스텝을 추가하고 LLM이 CoT를 자동으로 생성하도록함

```
1. Read the news article carefully and identify the main topic and key points.
2. Read the summary and compare it to the news article. Check if the summary covers the main topic and key points of the news article, and if it presents them in a clear and logical order.
3. Assign a score for coherence on a scale of 1 to 5, where 1 is the lowest and
5 is the highest based on the Evaluation Criteria
-> 번역
1. 뉴스 기사를 주의 깊게 읽고 주요 주제와 핵심 요점을 식별합니다.
2. 요약을 읽고 뉴스 기사와 비교. 요약이 뉴스 기사의 주요 주제와 핵심 요점을 다루고 있는지, 이를 명확하고 논리적인 순서로 제시하는지 확인합니다.
3. 평가 기준에 따라 일관성에 대해 1점에서 5점 사이의 점수를 부여합니다. 여기서 1점은 가장 낮은 점수이고 5점은 가장 높은 점수입니다.
```

### Scoring Function 

채점 함수는 아래의 세 가지를 인풋으로 LLM을 호출

1. 생성 결과물 평가를 위한 프롬프트
2. 자동으로 생성된 CoT
3. 입력 컨텍스트와 평가해야 할 대상 텍스트



최정 평가점수는 아래와 같음



![f1](\img\2024\G-Eval__NLG_Evaluation_using_GPT-4_with_Better_Human_Alignment\f1.PNG)

s는 미리 정의된 점수 집합이고 각 점수의 확률 p(si) 로 스코어를 합계하여 계산

위 수식을 통해 품질과 다양성을 더 잘 반영할 수 있음 



* G-eval은 양식채우기 방식으로 평가 작업을 수행함 (1~5점까지)

직접적인 체점 함수에는 두 가지 문제가 있다고함 

1. 일부 평가 작업의 경우, 하나의 숫자가 점수 분포를 지배하는 경우가 많습니다. 예를 들어 1-5 점수 척도에서 3점이 그렇습니다. 이는 점수의 분산이 낮아지고 인간 판단과의 상관관계가 낮아질 수 있습니다.

2. LLM은 프롬프트에서 소수 값을 명시적으로 요청하더라도 보통 정수 점수만 출력 

   -> 생성된 텍스타간의 미묘한 차이를 구분하지 못하고 정수로 같은 등급으로 평가되버림 

# 3 Experiments

GPT-3.5(text-davinci-003) 및 GPT-4를 포함한 OpenAI의 GPT 제품군을 LLM으로 활용하여 평가를 수행

-> 아래부분 부터 블로그 정리 그대로 따옴 

● 벤치마크

- **SummEval** : 요약에 대한 다양한 평가 방법을 비교하는 벤치마크 데이터셋. 요약문에 대해 유창성(fluency), 일관성(coherence), 일치성(consistency), 관련성(relevance) 네 가지 측면에 대한 사람의 평가를 제공한다. 데이터는 CNN/DailyMail 데이터 세트를 기반으로 한다.
- **Topical-Chat **: 지식을 필요로 하는 대화 응답 생성에 대한 다양한 평가자에 대한 meta evaluation을 위한 테스트베드. 자연스러움(naturalness), 일관성(coherence), 참여성(engagingness), 근거성(groundedness) 네 가지 지표를 사용한다.
- **QAGS** : 요약 태스크에서 hallucination을 평가하기 위한 벤치마크. 두 개의 요약 데이터셋에 대해 일관성(consistency) 측면을 평가하는 것을 목표로 한다.

● 베이스라인

G-eval을 다음과 같은 SoTA 방법론들과 비교한다.

- **BERTScore** - BERT 임베딩을 기반으로 두 텍스트 간의 유사성을 측정
- **MoverScore** - BERTScore에 soft alignment를 추가하고 새로운 집계 방법을 사용하여 보다 강건한 유사도 측정
- **BARTScore **- 사전 학습된 인코더-디코더의 평균 likelihood를 활용한 통합 평가기. 소스와 타깃의 평태에 따라 다른 점수를 예측할 수 있음.
- **FactCC와 QAGS** - 생성된 요약의 사실적 일관성을 측정.
  - FactCC: 요약이 원본과 일치하는지 여부를 예측하는 BERT 기반 분류기.
  - QAGS : 질문-답변 기반의 평가기. 요약문에 대해 질문을 생성하고 그 답변을 소스 문서에서 찾을 수 있는지 확인하는 방식
- **USR** - 다양한 관점에서 대화 응답을 평가하는 평가기로, 각 타겟 응답에 대해 서로 다른 점수를 할당하는 각기 다른 버전이 존재함
- **UniEval** - 텍스트 생성의 다양한 측면을 QA 작업으로 평가하는 통합 평가기. 사전 학습된 T5 모델을 사용하여 평가 과제, 소스 및 대상 텍스트를 질문과 답변으로 인코딩한 다음 QA 점수를 평가 점수로 계산함. 또한 질문 형식을 변경하여 다양한 평가 과제를 처리할 수 있음
- **GPTScore** - GPT-3과 같은 생성적 사전 훈련 모델로 텍스트를 평가하는 새로운 프레임워크. 생성형 사전 학습 모델이 주어진 지시문과 콘텍스트에 따라 고품질의 텍스트를 생성할 확률을 더 높게 할당한다고 가정함. G-EVAL과 달리 GPTScore는 평가 작업을 양식 채우기 문제가 아닌 조건부 생성 문제로 보고 점수를 측정함.



![t_1](\img\2024\G-Eval__NLG_Evaluation_using_GPT-4_with_Better_Human_Alignment\t_1.PNG)

- ROUGE 스코어와 같이 모델 아웃풋과 reference 요약문의 토큰 단위 유사성을 비교하는 매트릭은 사람의 평가 결과와 상관관계가 매우 낮음


- BERTScore 등 뉴럴네트워크를 활용한 매트릭의 경우 ROUGE보다 개선된 결과를 보이며, BARTScore, UniEval과 같은 프레임워크에서 상관관계가 향상됨
- 논문에서 제안한 G-EVAL 방식이 GPT 기반의 평가 방식인 GPTScore을 비롯한 다른 방법론을 능가하는 성능을 보이고, GPT-4를 사용한 결과가 사람의 평가와 더 높은 상관도를 보임.

### 해당 논문에 두번째 관점 G-EVAL은 LLM이 생성한 텍스트를 선호하는가

![f_2](\img\2024\G-Eval__NLG_Evaluation_using_GPT-4_with_Better_Human_Alignment\f_2.PNG)

1) 사람이 평가했을 때 GPT-3.5가 작성한 요약보다 사람이 작성한 요약이 더 높은 점수를 받은 경우

2) 사람이 평가했을 때  GPT-3.5가 작성한 요약보다 사람이 작성한 요약이 더 낮은 점수를 받은 경우

3) 사람이 평가했을 때 GPT-3.5가 작성한 것과 사람이 작성한 요약이 같은 품질이라고 평가한 경우 

논문에서 추정한 이유

1. 품질이 좋은 시스템이 생성한 결과물은 평가가 어렵다. 사람이 생성한 요약문과 LLM이 생성한 요약문에 대한 사람 평가조차도 평가자 간의 의견 합의의 정도가 낮았다 (Krippendorff's alpha = 0.07)
2. 모델이 생성과 평가에 있어 같은 평가 기준에 대한 개념을 가지고 있기 때문에 LLM 기반의 요약을 선호하도록 편향되었을 수 있다.







# 참고 

- G-Eval

https://littlefoxdiary.tistory.com/123

---
layout: post
title: "Quantifying the Persona Effect in LLM Simulations"
date: 2025-08-31 02:05:23 +0900
category: paper
---

# Quantifying the Persona Effect in LLM Simulations

url: https://arxiv.org/pdf/2402.10811

ACL 2024 Main

Cambridge 대학교 

# Abstract

LLM은 사람 행동 시뮬레이션에서 뛰어난 성능을 보이고 있음

해당 연구에서는 persona의 인구통게학, 사회적, 행동적 요인 팩터의 다양성을 통합하는 연구를 하고 있음

그리고 LLM이 다양한 관점에서 어떤 영향을 미치는지 탐구함 

연구에서는 페르소나 분포가 기존 nlp 데이터셋의 주석 분산의 10%미만만 설명한다는것을 발견했다고함  -> 어떻게 측정하는지 확인해보자

그러나 llm에 persona 변수를 프롬프트에 포함시키면 통계적으로 유의미한 개선이 나타났다고함

persona prompting은 여러 annotator들이 의견 불일치를 보이지만, 그 차이가 비교적 작을 때 가장 효과적이라고함, 그리고 연구에서 persona 변수와 인간주석 간의 상관관계까 강할수록 persona prompting을 사용한 LLM 예측정확도가 높아진다는 섢여적인 관계까 있다고 함

70b 모델을 쓸대 제로샷 셋팅 에서 학습한 경우 프롬프팅은 81%를 설명할 수 있었다고함

대부분의 주관적인 NLP 데이터셋은 persona 변수가 제한적임으로 설명하기 어려움 

# 1. Introduction

“이 텍스트를 읽고 나서 당신은 감정적으로 어떻게 느끼나요?”와 같은 주석은 정답이나 오답이 명확하지 않음  -> 이러한 주관성(subjectivity)이 NLP학계에서 인식되고 있다고 함

주관적인 NLP 테스크는 전혁적으로  low inter-annotator agreement를 보인다고 함  그리고 라벨을 평균 내거나 합치는 방식은 적절하지 않다고함

기존 연구에서는 사회인구학적 변수가 중요한 영항을 미친다고 함 

LLMs는 롤플레잉과 시뮬레이션 사람의 행동을 효과적으로 사용되었고, LLM이 사람 피실험자를 대체할 수 있는가에 대한 논쟁을 불러일으켰다.

![f1](G:\code\whtngus.github.io\img\2025\Quantifying_the_Persona_Effect_in_LLM_Simulations/f_1.png)

그러나 그림1과 같이 프롬프트에 페르소나 프롬프팅 방버볼ㄴ에 대한 우려도 존재함 생태학적 오류(ecological fallacy), LLMs가 고정관념적 과장(캐리커처)에 쉽게 영향받는 점, 하위집단의 다양성을 왜곡(misportrayal)하거나 지워버리는 문제가 지적되고 있음

기존 연구들은 종종 페르소나 변수 효과를 측정하려고 했으나, 전체적(holistic) 영향력을 분석하는데 소흘이함



해당 연구에서는 아래의 Research Question을 탐구함

### RQ 1 How much variance in human annotation could persona variables explain?

인간 주석의 분산을 persona 변수가 얼마나 설명할 수 있는가?

### RQ2: Can incorporating persona variables via prompting improve LLMs’ predictions?

프롬프트를 통해 persona 변수를 포함하면 LLM의 예측이 향상되는가?

### RQ3: For what types of samples is persona prompting most useful?

어떤 유형의 샘플에서 persona prompting이 가장 유용한가?

### RQ4: How effectively can LLMs simulate personas when the importance of persona variables varies?

persona 변수의 중요성이 달라질 때, LLM은 얼마나 효과적으로 페르소나를 시뮬레이션할 수 있는가?

# 2 Related Work

## 2.1 The Relationship between Persona Variables and Annotation Outcome













 






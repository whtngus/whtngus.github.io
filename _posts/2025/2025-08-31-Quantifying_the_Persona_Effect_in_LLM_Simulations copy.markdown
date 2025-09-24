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

많은 연구들이 페르소나가 혐호 발언 탐지나, 감정분석, 풍자 탐지에 영향을 미치는지 강조해왔다.

많은 연구 과제들이 NLP 주석의 주관성을 밝히긴 했찌만, 페르소나 변수가 주석의 변동을 얼마나 섬령할수 있을지에 대한 전체적 설명까지는 미치지 못함

반대로 사회과확에서는 페르소나 변수가  태도에 미치는 영향이 오랫동안 연구되었고, 정량하됨

 -> 연구에서는 주석 결과를 섬령하는데 있어 페르소나 변수의 유용성을 분석

## 2.2 Modeling Persona Variables and LLM for Simulation

일부 연구들은 페르소나 변수를 단지 출력의 다양성을 높은데만 사용됨, 

다른 연구에서는 페로스나 표현의 정확성을 강조하며, 그룹 수준의 속성과 개별 주석자간의 차이를 반영하려고 시도함

이는 개인또는 그룹별 layer를 추가하거나 프롬프트를 통한 방식으로 이루어짐

-> 이때 결과는 엇갈린다고함 그룹 수준의 페르소나변수를 사용했을때 성공적이라고하는경우도 있고 의문을 제기하는 경우도 있다고함 

## 2.3 Persona Prompting and AI Alignment

AI 정렬(AI alignment) 의 맥락에서 페르소나 프롬프트(persona prompting)를 다룸

LLM을 활용해 사회적 가치(societal values)와 태도(attitudes)에 관한 객관식 설문조사(multiple-choice survey questions) 에 답변하게 하고, LLM이 생성한 답변 분포(answer distribution) 와 실제 인간 응답 분포(human response distribution)를 비교함

해당 연구는 연구는 LLM의 응답이 특정 인구 집단의 설문 응답과 얼마나 유사한가를 보는 것이 아니라, LLM이 과제 예측(task predictions)을 수행하는 데 있어 페르소나 변수를 얼마나 효과적으로 활용할 수 있는가를 탐구한다고 함

# 3 RQ1: How much variance in human annotation could persona variables explain?

- Methodology

페르소나 변수가 인간 주석의 변동을 어느 정도까지 설명할 수 있는지 조사한다고 함 

해당 연구에서는 "혼합효과 선형 회귀 모델(mixed-effect linear regression model)" 방법을 사용한다고 함 

페르소나 변수(persona variables)는 고정 효과(fixed effect) -> 텍스트 샘플의 특성에서 비롯되는 변동성(text-specific variability)은 무작위 효과(random effect) 로 두어 각 텍스트에 대한 무작위 절편(intercept)을 추가  

주석 결과에 미치는 텍스트 자체의 변동성과 페르소나 변수의 영향을 분리한다고 함

주석이 집계되지 않은(unaggregated) 주관적 NLP 데이터셋 10개를 평가 -> 10개만 해도 되는구나... 

미국 2012년 선거 조사(ANES 2012 survey) 의 대통령 투표 질문도 고려했다고함 

- Results

![t1](G:\code\whtngus.github.io\img\2025\Quantifying_the_Persona_Effect_in_LLM_Simulations/t_1.png)



과제, 데이터 출처, 주석 방식, 데이터 크기, 포함된 페르소나 정보 유형, 그리고 회귀 R² 값을 비교 Table 1을 인하라고함 

데이터는 주로 소셜 미디어에서 수집되었고 주석은 직접 크라우드소싱을 했다고함 => 여기에서 컨트리뷰션 요소가 있는듯

페르소나 변수(고정 효과)는 주석 결과의 일부 변동을 유의미하게 설명하지만, 전체 변동 중 단지 1.4% ~ 10.6% (한계 R², Marginal R²) 만을 차지함 

면 텍스트 자체의 변동성(무작위 효과)은 최대 70% 까지도 설명할 수 있다고함

ANES 데이터셋에서는 페르소나 변수가 70% 이상의 인간 응답 변동을 설명함

한계 R² 값은 페르소나 변수가 설명할 수 있는 변동의 기본선을 보여줌

모든 과제에서 주석 변동의 상당 부분(25%~70%)이 텍스트나 페르소나 변수로도 설명지 않는다고함

ANES 데이터셋에서 높은 R² 값을 보이는 이유는 최근 미국 정치의 양극화(polarization) 가 심화되었기 때문일 수 있다고함

# 4 RQ2: Can incorporating persona variables via prompting improve LLMs’ predictions?

- Methodology

페르소나 프롬프트(persona prompting) 가 실제로 LLM의 예측 성능을 향상시킬 수 있는지를 탐구함

그림1의 제로샷 프롬프트 설저에서  LLM 성능 향상이 가능한지를 확인

동일한 텍스트에 대해 LLM을 두 번 프롬프트함

1. 페르소나 변수를 포함 안함
2. 페르소나 변수를 포함 함

실험은 Annotator-withAttitude (Sap et al., 2022), Kumar et al. (2021), EPIC (Frenda et al., 2023), 그리고 POPQUORN 데이터셋의 공손함 평가(politeness rating; Pei and Jurgens, 2023)에서 수행

주석자의 원래 페르소나 설명 언어를 최대한 보존했고, 객관식(multiple-choice) 형식으로 질문과 답변 선택지를 포함시킨 뒤, 모델이 다음 토큰을 예측하는 방식으로 응답하도록함

비용 제약으로 인해 각 데이터셋에서 600개 샘플만 추출하여 실험함 => 나도 이걸 고려해서 해봐야 될듯

- Results

![t2](G:\code\whtngus.github.io\img\2025\Quantifying_the_Persona_Effect_in_LLM_Simulations/t_2.png)

첫 번째 행은 “목표(Target)” R² 값으로, 이는 표 1과 동일한 방식으로 혼합효과 회귀를 적용해 산출한 값

-> 별표(*)는 페르소나 변수를 포함했을 때 성능 개선이 통계적으로 유의함

그러나 개선 폭은 대체로 크지 않고, 미묘함. 큰차이가 없음

-> 여기에선 ACC 로만 표시하는게 아니라 R^2랑  MAE로 사용하는걸 따라할 필요 있을듯 

# RQ3: For what types of samples is persona prompting most useful?

페르소나 프롬프트(persona prompting) 기법을 더 잘 이해하기 위해, 우리는 주석 데이터가 가지는 특성(엔트로피와 표준편차) 에 따라 효과성을 조사

특히 Kumar et al. (2021) 데이터셋에 집중했는데, 이 데이터셋에서는 페르소나 변수가 주석 변동을 설명하는 비율이 비교적 높기 때문 

엔트로피와 표준편차의 높고 낮음은 각 데이터의 중앙값(median)을 기준으로 나눔

각 범주에서 평균 주석 값에 따라 다시 4개의 구간으로 세분화하고, 각 구간에서 무작위로 150개 샘플을 추출하여 총 600개 샘플을 구성

- Results



각 범주별로, 페르소나 프롬프트를 적용했을 때와 하지 않았을 때의 평균 MAE(평균 절대 오차) 개선치를 보여준다. 색이 짙을수록 개선 효과가 크다는 의미

POPQUORN-Politeness 데이터셋(Pei and Jurgens, 2023) 에 대해서도 반복하였고, 그 결과는 그림 2b에 제시



# 6 RQ4: How effectively can LLMs simulate personas when the importance of persona variables varies?







-> 탑 컨퍼런스를 위해서는 분석결과가 다양해야하며, 다채로운 해석 필요. .. 
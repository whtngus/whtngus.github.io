---
layout: post
title: "Synthetic Replacements for Human Survey Data? The Perils of Large Language Models"
date: 2024-08-16 02:05:23 +0900
category: paper
---

# Synthetic Replacements for Human Survey Data? The Perils of Large Language Models

url : https://www.cambridge.org/core/journals/political-analysis/article/synthetic-replacements-for-human-survey-data-the-perils-of-large-language-models/B92267DC26195C7F36E63EA04A47D2FE

Published online by Cambridge University Press

밴더빌트 대학 



# Abstract

LLM은 사회과학자들에게 새로운 연구를 가능하게  함 그러나 “synthetic data"는 아직 잘 모르는 영역 

ChatGPT api를 통해 여론을 복원하고자함 그리고 11개 서로다른 사회적 그룹이 호감도를 평가를 함

ChatGPT가 만든 스코어는 베이스라인 설문조사와 굉장히 유사하다고함 

-> 2016–2020 American National Election Study(ANES)

그럼에도 불구하고, ChatGPT를 통한 샘플링은 통계적 추론에 신뢰할 수 없음

응답의 변동성이 실제 설문 조사보다 적고, 회귀 계수는 종종 ANES 데이터를 사용하여 얻은 동일한 추정치와 크게 다름



해당 연구에서는 프롬프트의 사수한 문구에 따라 응답 분포가 어떻게 달라지는지를 기록하고, 동일한 프롬프트가 3개월동안 어떻게 다른 결과를 가져오는지를 보여줌 



그리고 해당 논문에서 함성데이터에 대한 품질, 신뢰성을 갖기 어렵다고함 



# Introduction

설문조사는 비용증가, 응답 비율 감소 등과 이로인한 부정확한 설문조사결과에 위기에 처해있음 

잘 수행된 여론조사는 학자들, 정책 입안자들, 언론이들이 전체 대중의 의견을 평가할 수 있도록 해줌 



사라들의 응답과 인터뷰의 어려윰이 증가함에 따라 연구자들은 다른 방법들을 활용하기 시작함

비조사 데이터를 활용하거나 정교한 가중치 바법들을 적용하기 시작



LLM 합성 데이터를 이용하여 막대한 데이터를 합성하여 전통적인 설문조사 방식을 대채하고자함 

합성된 유저는 사람의 응답을 대체할 수 있다는 연구가 있으나 해당 연구에서는 과연 실제 사람의 응답과 의견을 정확하게 생성할 수 있는지 의무을 제기함 

이를 실험하기 위해 "ChatGPT 3.5 Turbo"를 사용 하여 다양한 사람의 통계학정 정보와 사회적 그룹을 고려하여 평가함 -> 이렇게 인공적으로 생성된 답변 데이터를 "silicon samples"이라 명칭함

실험을 위해 실제 응답 데이터 2016 and 2020 American National Election Study (ANES)를 활용함 



기본적으로 ChatGPT의  페르소나 답변 데이터와 ANES 데이터와 아래 3가지 지표로 비교함 

1. ChatGPT가 평균과 분산이 그룹별로 잘 복원 했는지

2. 페르소나 특성과 설문 응답 사이의 (조건부) 상관관계가 ANES에서 얻은 추론과 얼마나 유사

3. 프롬프트와 LLM 데이터 수집 시점 변화에 대한 민감도 비교


간단한 분석 결과 ANES의 응답과 ChatGPT의 응답과 상당히 비슷함을 확인함 

그러나 전체 평균 응답을 비교하더라도 분포를 복원하는데에 문제를 발견함 

 높은 관계 분석을 하는경우에도 다른 결론을 도출할 수 있게 나왔다고함 



그리고 2023년 4월과 7월 chatgpt 알고리즘 교체에 따라 답변 결과도 바뀜 

# 1. Research Design and Data

LLM은 다음토큰을 예측하는데 최적화된 모델로 질문에 설득력있게 일관된 답변을 하기 위해 학습

사전학습된 LLM은 사람의 의견을 다시 생성할 때 개인의 페르소나를 생성하는건 명확하지 못함

![prompt](\img\2024\Synthetic_Replacements_for_Human_Survey_Data_The_Perils_of_Large_Language_Models\prompt.PNG)

위는 메타 정보를 넣어주기 위해 사용한프롬프트 

아래는 질문 

```
How do you feel toward the following groups?
The Democratic Party?
The Republican Party?
Democrats?
Republicans?
Black Americans?
White Americans?
Hispanic Americans?
Asian Americans?
Muslims?
Christians?
Immigrants?
Gays and Lesbians?
Jews?
Liberals?
Conservatives?
Women?”
```

ANES 설문조사 데이터에서 7,530 명의 응답자 에게서 30개의합성 응답을 요청함 

최종적으로  모든 경우의수로 3,614,400 데이터를 생성 

(480개의 조합으로 보임)

이때 주요 분석시에는평균 데이터, 불확실성 계산 시에는 첫 번째 응답만을 사용함 

다양한 그룹에 대한 개읜의 감정에 대해 물어봄 응답은 0(냉정한 감정) ~ 100(따드뜻한 감정) 척도 이고 50이상이면 호의적임을 의미 

# 2. Results

3가지 방식으로 평가를함 

평균 및분산 비교와

ChatGPT는 종종 실제 인간 설문 응답의 근사에서 편향되거나 과도한 자신감을 보이며 공변량간의 주변 관계를 회복할 수 있는지 테스트함 

 합성 응답이 데이터 생성 시점과 각 프롬프트가 나타내는 페르소나에 따라 상당히 민감하다는 것을 정리함

American political opinion surveys 를 벤치마크함 + gpt 학습기간 전에 설문조사가 완료되었다고함

## 2.1. Accuracy of Average and Standard Deviations

![f_1](\img\2024\Synthetic_Replacements_for_Human_Survey_Data_The_Perils_of_Large_Language_Models\f_1.PNG)

위의 Figure 1 은 chatgpt와 실제 투표의 분포 

ANES설문조사 결과와 ChatGPT의 설문 결과가 평균점이 크게 다르다고 함

그리고 chatgpt의 경우  분포가 작은 편이며 특히 인종 및 종교 집단에대한 관점을 물어보는경우 그렇다고 함 



# 참고

- ANES(American National Election Study) 데이터

https://electionstudies.org/data-center/

선거연구 

더 자세한 내용 확인 필요 






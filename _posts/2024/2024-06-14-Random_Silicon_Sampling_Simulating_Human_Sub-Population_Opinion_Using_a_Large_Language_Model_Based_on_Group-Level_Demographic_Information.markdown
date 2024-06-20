---
layout: post
title: "Random Silicon Sampling: Simulating Human Sub-Population Opinion Using a Large  Language Model Based on Group-Level Demographic Information"
date: 2024-06-18 02:05:23 +0900
category: paper
---

# Random Silicon Sampling: Simulating Human Sub-Population Opinion Using a Large Language Model Based on Group-Level Demographic Information 

성균관대학교 

2025년 2월 28일 

github : https://anonymous.4open.science/r/RSS-1D4D

url : https://arxiv.org/pdf/2402.18144



# Abstract

llm을 통해 인종 성별 등 인구통계학 정보와 관련된 사회적 편견을 의견을 생성할 수 있음 

논문에서 random silicon sampling을 제안함 

논문에서 분석하는 내용 

1. lm이 생성하는 설문 답변과 사람의 답변의 그룹의 인구통계학 분포를 비교함 
2. 인구 통계 하위 그룹과 주제별 질문에 걸쳐 적용 가능하다는 점을 확인



인구 통계 정보만을 사용하여, 언어 모델의 미국 여론 조사와 유사한 분포를 생성할 수 있음을 밝힘 



# 1 Introduction

llm을 이용한 사회의 편향성에 대해 광범위하게 연구되고 있음 

 llm은 사람의 같은 인족, 민족, 성별 그리고 사람의 데이터(텍스트)의 바이어스를 학습함 

많은 연구에서 사람의 의견을 이해할 수 있는 방법을 시도하고 있음 

사람의 관점을 llm 모델을 생성될 수 있음 

논문에서 제안하는 silicon sampling는 방법은 설문자소 답변을 생성할 수 있음 그리고 그 llm은 설문조사를 대신할 수 있음 

그러나 개개인의 정보는 대신할 수 없으며 통계정보만을 생성할 수 있음 



논문의 컨트리뷰션

1. LLM을 통한설문조사 설계와 사전조사 설문비용 감소
2. 인구통계학 정보를 통해 개개인의 데이터 없이 의견을 추출
3. 언어모델을 통해 인구 그룹의 설문조사 연구를 뚜력하며 일반화 할 수 있음 

## 2 Related Work

### Simulate human opinion

성별 인종, 국가, 사회적 맥락을 통해 연구된 내용이 있으며 

사람의 의견에 영향력에 대해 연구된 바도 있음 

등등... finetuning을 통해 개인을 학습하는 연구 도 있음

### Silicon sampling

llm이 사람의 통계학정 정보를 가지고 의견을 예측하는것을 보여줌 

 해당 연구에서는 llm 모델이 사람의 적절하게 큰 그룹단위의 의견을 시뮬레이션 할 수 있는지를 연구하고자 함 

-> 해당 연구에서는 개개인의 의견을 수집해서 반환하는건 의 없다고 함 

사람의 의견을 subgroup  시뮬레이션 을함 

# 3 Methods 

![f_1](\img\2024\Random_Silicon_Sampling_Simulating_Human_Sub-Population_Opinion_Using_a_Large_Language_Model_Based_on_Group-Level_Demographic_Information\f_1.PNG)

위의 그림 1에서와 같이  층화 샘플과 다운샘플링, 다중 질문을 통해 생성에 대해 의견을 샘성

데이터셋은  [American National Election Studies (ANES)](https://electionstudies.org/data-center/).을 사용함

## 3.1 Data

ANES은 미국의 공공 의견을 담고있음 

여기에서 2020년 사전선거 샘플 데이터를 사용함  (2020 8월 18일 11월 3일 데이터 사용 )

그리고 인구통계학 정보를 통해서 5,441건의 응답결과를 생성하고 분포를 비교함 

인구통계학 정보는 인종/민족, 성별, 나이, 관념, 직업,  정치적 과점, 정치적 관심, 종교, 정치토론 정보를 사용 

-> 사용 정보가 설문조사와 직접적인 데이터들이 많이 있는걸로 보임 

## 3.2 Random silicon sampling

인구통계학 정보들을 랜덤으로 선택하여 인구통계 그룹 분포를 만듦 그리고 ANES 응답 정보와 비교함 

## 3.3 Evaluation

ANES와 RSS 와 비교 

심플

#### Chi-Square Test for Homogeneity

통계를 활용해서 응답 부포가 P<0.05 인것을 확인 

#### Kullback-Leibler Divergence

KL-divergence 평가를 통해 시뮬레이션이 현실과 같게 사용 

# 4 Experimental Settings

![t_2](\img\2024\Random_Silicon_Sampling_Simulating_Human_Sub-Population_Opinion_Using_a_Large_Language_Model_Based_on_Group-Level_Demographic_Information\t_2.PNG)

![t_1](\img\2024\Random_Silicon_Sampling_Simulating_Human_Sub-Population_Opinion_Using_a_Large_Language_Model_Based_on_Group-Level_Demographic_Information\t_1.PNG)

GPT3.5-turbo API를 통해 시뮬레이션을 함 

위의 Table A2와 같이 프롬프트 를 사용 

## 4.1 Response generating process

2020 U.S. 대선을 생성해서 평가함 

프롬프트는 생략   위의 table 과같이 생성함 

## 4.2 Further analysis

#### Stratified sampling

8개의 인구통계학 정보를 바탕으로 분류를 하고 23개의 서브그룹을 생성 

(남자 여자 백인 흑인 등)

#### Down sampling

5,441 개의 샘플 중에서 90%에서 10%까지 줄였고 9% 에서 1%까지 줄여가면서 테스트르 ㄹ진행 

#### Multiple questions

10개의 질문을 추출해 (5지선다)

대통령 선거 외에 다른곳에 활용가능한지를 테스트 

maxtoken을 1로 설정하여 답변을 제안함 

# 5 Results










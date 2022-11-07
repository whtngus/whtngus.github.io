---
layout: post
title: "paper : Deep learning for depression recognition with audiovisual cues"
date: 2022-11-07 01:01:01 +0900
category: paper
---

# Deep learning for depression recognition with audiovisual cues

url : https://www.sciencedirect.com/science/article/abs/pii/S1566253521002207

Information Fusion Volume 80, April 2022, Pages 56-86



# Abstract

재택근무로 인해 pace of work의 수가 많이 늘고있고, 그와 동시에 우울증 환자도 같이 늘고 있다. 

우울증 진단은 의사에 의해서 판단되지만 기준이 일정하지 않다.

이러한 점에서 오디오와 시각적인 정보를 Deep Learning을 통해서 해결하고자 한다.

해당 연구에서는 위와 같은 문제를 다루는 데이터셋과 연구 모델을 정리해서 보여줌 

# 1. Introduction

우울증은 정신질환의 일환이고, 개인적인일, 가족, 사회적인 이유 등에서 발생한다.

World Health Organization (WHO)에 따르면 2030년의 정신질환중 대부분은 우울증이라고 한다.

우울증은 자살을 유도하고, 자살자중 50%는 우울증을 가지고 있다고 한다.

그러나 우울증은 한가지 유형이 아니라 다양한 유형이고 오랜시간 관찰이 필요함,  최근 이를 해결하기 위해 Deep Learning based 방법론들이 사용되고 있다.

# 2. Current diagnostic methods

우울증 탐지에 대한 이해를 위해 audivovisual 케이스, 우울증의 정의, 우울증 진단 방법에 대한 이해가 있어야 한다.

## 2.1. The definition of depression

![f1](\img\2022\Deep_learning_for_depression_recognition_with_audiovisual_cues\f1.png)

- 1980년에 Russell은 감정의 차원인 2차원의 연속형 차원인 Valence–Arousal (VA)를 제안함


- Diagnostic and Statistical Manual of Mental Disorders (DSM) of the American Psychiatric Association(APA)의 정의에 따르면 우울증은 다음과 같이 분류된다.

>  Major Depressive Disorder (MDD) - 주요 우울증
>
> Persistent Depressive Disorder (Dysthymia) - 지속적인 우울증
> Disruptive Mood Dysregulation Disorder (DMDD) - 파괴적 기분조절장애
>
> Premenstrual Dysphoric Disorder (PDD) - 월경전 불쾌장애
>
> Substance/Medication-Induced Depressive Disorder (S/M-IDD) - 물질/의약품에 의한 우울증장애
>
> Depressive Disorder Due to Another Medical Condition (DDDAMC) - 다른 의학적 질환
>
> Other Specified Depressive Disorder (OSDD) - 특정 우울장애
> Unspecified Depressive Disorder (UDD) - 지정되지 않은 우울증

DMS는 위와 같이 우울증에 분류에 대한 기준을 제안함 



우울증은 정확한 원인을 규정할 수 없지만 대체로 cortical-limbic system의 기능장애로 이야기 된다 

 (대뇌 변연계 - **변연계**는 [대뇌피질](https://ko.wikipedia.org/wiki/%EB%8C%80%EB%87%8C%ED%94%BC%EC%A7%88)과 [뇌량](https://ko.wikipedia.org/wiki/%EB%87%8C%EB%9F%89) 그리고 [시상하부](https://ko.wikipedia.org/wiki/%EC%8B%9C%EC%83%81%ED%95%98%EB%B6%80) 사이의 경계에 위치한 부위) 

## 2.2. Diagnosing depression

기본적인 진단 방법에서 우울증 진단은 매우 어렵고, 잘못 진단되기 쉽다. 

오랜 시간이 지나야 보이는 특성과 우울증 실험자가 우울증 징후를 직접적으로 보여주지 않기 때문 (무력감, 절망감 등)

최근에는 HAMD, BDI 방법에 의해서 체크 를 많이 한다. 

그 외에 여러가지 진단 방법이 있지만 생략 ...

## 2.3. Objective markers for depression assessment

Objective markers는 심리학에서 진단시에 많이 사용된다. 

... 생략

# 3. Depression databases

## 3.2. Databases reviewed

| 이름         | 특징                                       |
| ---------- | ---------------------------------------- |
| BlackDog   | 21 ~ 75세 ,   DSM-IV 기준,  음성 상담 데이터 녹음(8개의 그룹) 7개의 감정그룹으로 label |
| AVEC2013   | audiovisual 우울증, 340 비디오 및  292사람 데이터 , 18~63세,  BDI-II 기준 label, 총 150개의 비디오 클립 |
| AVEC2014   | AVE2013에서 100개의 데이터인 Freeform와  Northwind 추가됨, |
| DAIC       | 4개의 타입의 인터뷰(화상회의), 189개의 데이터(https://dcapswoz.ict.usc.edu/ - 신청) |
| CHI-MEI    | 혐오, 두려움, 슬픔, 놀라움, 분노, 행복에 대한 비디오 ()      |
| Pittsburgh | 34명의 여성, 23명의 남성 우울증 데이터셋, 19~65세,   DSM-IV criteria for MDD(https://www.di.ens.fr/willow/research/netvlad/ - ) |
| BD         | 46명의 참가자,  AVEC2018                      |
| MODMA      | audio, EEG signals,                      |



그 다음부터는 알고리즘 .. 생략 















# 참고 지식 

- HAMD(The Hamilton Rating Scale for Depression)

우울증 진단은 증상을 묘사하는 주체의 학력, 인지 능력, 정직성뿐만 아니라 임상의의 경험과 동기 등에 따라 분류

그러나 전형적인 증상인 불면증, 기분 저하, 동요, 불안, 체중감소 등은 HAMD에서 무시되는 문제가 있음.

20~30분의 인터뷰 타임

| 평가          | 점수      |
| ----------- | ------- |
| Normal      | ~7      |
| Midl        | 8 ~ 13  |
| Moderate    | 14 ~ 18 |
| Severe      | 19 ~ 22 |
| Very Severe | 23 ~    |



- ADE(automatic depression estimation)

우울증 추정 시스템

- LBP (Local binary patterns)

이미지의 질감(texture) 표현 및 얼굴 인식 등에 활용되는 아주 간단하면서도 효율적인 방법

- BDI(Beck Depression Inventory)

정신 치료를 받고 있는 우울 증 환자에게 많이 나타나는 증상과 환자들의 태도를 종합 정리하여 21개 문항을 추출하고 이것을 척도화 한 것

5~10분의 인터뷰 타임 

| 평가                       | 점수(0~63) |
| ------------------------ | -------- |
| no or minimal depression | ~ 13     |
| Midl                     | 14 ~ 19  |
| Moderate                 | 20 ~ 28  |
| Severe                   | 29 ~ 63  |





| 이름        | 설명                                       | url                                      |
| --------- | ---------------------------------------- | ---------------------------------------- |
| GRID-HAMD | 평가척도만 있고 실 데이터 없음                        | [ISCDD - 스케일](https://iscdd.org/Resources.aspx) |
| AVEC      | Audio–VisualEmotion Recognition Challenge <br /> 우울증 포함 - 데이터 다운 링크가 다 막혀있음 | https://sites.google.com/view/avec2019/home |
|           |                                          |                                          |

https://github.com/chkche1/avec2013
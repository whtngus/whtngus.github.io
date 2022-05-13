---
layout: post
title: "paper : SMOGN_a_Pre-processing_Approach_for_Imbalanced_Regression"
date: 2022-04-23 01:01:01 +0900
category: paper
---

# SMOGN_a_Pre-processing_Approach_for_Imbalanced_Regression



url : http://proceedings.mlr.press/v74/branco17a/branco17a.pdf

LIDTA 2017

code :  https://github.com/paobranco/SMOGN-LIDTA17.

# Abstract

불균형 도메인의 문제는 많은 실제 응용 분야에서 관련이 있다

불균형 회귀를 처리하기 위한 새로운 전처리 접근 방식을 제안

SMOGN은 두 가지 모두에서 탐지된 문제를 해결하려는 두 가지 기존 제안을 통합



# 1. Introduction

불균형 도메인은 주로 분류 작업의 맥락에서 연구된 관련 문제 그러나 불균형 도메인은 회귀 작업, 데이터 스트림 또는 시계열 예측과 같은 다른 예측 컨텍스트에서도 발생

불균형 도메인은 두 가지 요인의 동시성으로 인한 문제를 나타낸다

1. 대상 변수 도메인에 걸친 사용자의 불균일한 선호도
2. 데이터가 절대적으로 부족한 경우

실제로 회귀 데이터 집합에서 대상 변수의 연속성은 처리할 수 있는 값의 수가 무한하기 때문에 작업에 복잡성을 더하고, 대상의 관련 값을 더하거나 덜 지정하는 것도 간단하지 않다

언더 샘플링 전략과 두 가지 오버 샘플링 전략을 결합

# 2. Problem Definition

목표는 알려지지 않은 함수 Y = f(x)에 근접한 모델을 얻는 것

 모델을 찾기 위해 N개의 예를 가진 훈련 세트 D = {hxi,  yii} i=1 N  N개의 예제를 사용 

불균형 회귀 작업은 두 가지 특성으로 특징지을 수 있는 회귀 문제의 특정 클래스

> 1. 사용자가 대상 변수 도메인에 걸쳐 불균일한 선호도를 가지고 있다.
> 2. 가장 중요한 범위가 제대로 표현되지 않는다
>
> 불균형 회귀 분석에서 사용자는 다른 더 빈번한 범위와 비교하여 대상 변수의 잘 표현되지 않은 범위에서 달성되는 예측 성능에 더 많은 중요성을 부여

이 두 요소의 결합은 사용자에게 가장 중요한 경우에서 성능 저하를 초래

![f_0](E:\code\whtngus.github.io\img\2022\SMOGN_a_Pre-processing_Approach_for_Imbalanced_Regression\f_0.PNG)

![f_0](E:\code\whtngus.github.io\img\2022\SMOGN_a_Pre-processing_Approach_for_Imbalanced_Regression\dn.PNG)

DR : rare cases

DN : normal and uninteresting case불균형 회귀 문제를 다루기 위해 성능 평가 문제와 학습 알고리듬을 관련 사례로 편향시키는 문제를 모두 고려 해야함 

Branco(2014)가 제안한 F1-measure e (Fφ1)  를 사용 

# 3. Related Work 

생략

# 4. SMOGN Algorithm

SMOGN이라고 하며 무작위 언더샘플링과 두 가지 오버샘플링 기법을 병행해서 사용 

즉, SmoteR 및 가우스 노이즈 도입과 결합

SmoteR이 발생할 수 있는 위험을 가우시안 노이즈로 제한하는 전략을 가짐 

*** k-근접 이웃이 "충분히" 가까울 때만 SmoteR로 새로운 합성 예제를 생성하고, 두 예제가 "더 멀리" 있을 때 가우스 노이즈의 도입을 사용 ***

1. 보간 과정에서 가장 먼 예를 사용하지 않기 때문에 SmoteR을 사용할 때 발생하는 위험의 한계,
2. 가우스 도입으로 달성하기 어려운 일반화 능력을 증가시키는 드문 경우에 대한 결정 경계를 확장

![a_1](E:\code\whtngus.github.io\img\2022\SMOGN_a_Pre-processing_Approach_for_Imbalanced_Regression\a_1.PNG)

위 알고리즘 하나로 논문이 제시하는 방법을 모두 설명

```
Bin R - 중요한 부분 (Rare)  -> 오버 셈플링 대상
Bin N - 일반적인 부분  	-> 언더 셈플링 대상

오버샘플링은 SmoteR 또는 가우스 노이즈 전략을 도입하여 시드와 선택된 k-가장 가까운 이웃 간의 거리에 따라 새로운 사례를 생성 - 선택된 이웃이 안전한 경우 SmotR  안전하지 않은 범위의 경우 가우스 노이즈를 도입

안전성 여부는 시드와 고려 중인 파티션의 나머지 모든 사례 사이의 거리에 따라 달라진다.  
(시드 예제와 동일한 파티션에 있는 다른 예제 사이의 거리의 중위수의 절반을 사용)
```

![f_1](E:\code\whtngus.github.io\img\2022\SMOGN_a_Pre-processing_Approach_for_Imbalanced_Regression\f_1.PNG)

그림 1에서 safe 종은 5개의 near list 의 거리들의 중앙값 

점 - rare bin

십자가 - nomal bin

#  5. Experimental Evaluation

생략!





# 관련 지식

- Gaussian Noise

정규분포를 가지는 노이즈.







# 참고
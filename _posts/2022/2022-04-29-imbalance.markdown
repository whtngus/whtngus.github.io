---
layout: post
title: "imbalance"
date: 2022-05-11 16:20:23 +0900
category: datascience
---

# imbalance

# 불균형 분류에 대한 성능 측정

![How-to-Deal-With-Imbalanced-Classification-and-Regression-Data_29-3372336075-1643136560469](\img\2022\imbalance\How-to-Deal-With-Imbalanced-Classification-and-Regression-Data_29-3372336075-1643136560469.webp)

F1 score

ROC, AUC(ROC커브 하단 넓이)

Precision, Recall

Confusion Matrix



# Under Sampling

![undersampling](\img\2022\imbalance\undersampling.webp)

## Random Sampling

다수 클래스에서 몇 개의 샘플을 무작위로 선택하여 데이터 균형을 맞추는 가장 쉽고 빠른 방법

### NearMiss

1~3가지 N을 통해 언더 샘플링 진행

![nearmiss](\img\2022\imbalance\nearmiss.PNG)



 네거티브 클래스의 가장 가까운 샘플까지의 평균 거리가 가장 작은 포지티브 샘플을 선택

포지티브 샘플이 majority class

위의 사진은 n이 1이고 n이 2인경우  2개의 네거티브 샘플링에서 가장 가까운 포지티브 샘플링을 선택

즉 NearMiss-n 은 n개의 minority class에서 가장 가까운 majority class를 선택하는 방법 

### Tomek Link

 두 샘플 A와 B가 있을 때, A의 `nearest neighbor`가 B이고(=B의 `nearest neighbor`가 A) A와 B가 다른 class에 속할 때를 제외

이러한 방식으로 minority class와 가까운 majority class를 제외하면서 다소 모호할 수 있는 `decision boundary`가 명확히 구분될 수 있도록 한다.

![tomek](\img\2022\imbalance\tomek.PNG)





# Over Sampling

![oversampling](\img\2022\imbalance\oversampling.webp)

## 1. Classification OverSampling

## **Random oversampling**

가장 간단하게 생각해볼 수 있는 방법으로 minority class에서 샘플을 랜덤으로 뽑아서 복사하는 방법이다.

### smote(**Synthetic Minority Over-sampling Technique**)

![smote](\img\2022\imbalance\smote.gif)

합성을 기반으로 하는 방법으로, minority class의 샘플을 가져와 이들을 잇는 선에서 중간값을 택하여 만들어내는 방식



### SMOTE-SVM

SVM classifier에 의해 만들어진 support vectors(경계선과 가까운 vectors)에 속하는 인스턴스들에만 SMOTE algorithm을 적용하는 방법

맨 처음, SVM를 학습시키고 support vectors에 속하는 샘플들이 나오면 SMOTE를 이용하여 oversampling하는 방식

-> 경계선을 더 뚜력하게 만드는 효과가 있음



### **WEMOTE/CWEMOTE**

일반적인 SMOTE는 minority class 샘플들의 nearest neighbours를 결정

 O(n2)의 시간이 소모되는데, 이와 달리 WEMOTE를 통해 좀 더 효율적으로 샘플들을 만들어낼 수 있다.

WEMOTE는 두 개의 랜덤 벡터를 뽑아내고 평균을 계산

하지만 같은 class라 하더라도 데이터들의 특성은 제각각이기에 in-class imbalance가 있다. 이를 위해 CWEMOTE는 minority class 내에서 학습 샘플들을 clustering한 후 WEMOTE를 적용하는 것( clustering은 k-means를 사용)

### ADASYN: Adaptive Synthetic Sampling Approach

기존의 `SMOTE`는 모든 minority class로부터 동일한 개수의 synthetic 샘플을 생성

 **ADASYN**은 각 관측치마다 생성하는 샘플의 수가 다르다는 점이 특징

 `weight`로 synthetic 샘플 수를 결정하고 이 `weight`는 `knn` 범위 내로 들어오는 majority class의 개수에 비례하도록 한다. 

-> 더 훈련시키기 어려운 관측치에 집중하여 근방의 synthetic 샘플을 더 많이 생성하는 것

![adasyn](\img\2022\imbalance\adasyn.PNG)

위는 `k-nearest neighbors`내 majority class 비율을 나타내는 ᴦ hat이 더 큰 경우에 더 많은 synthetic 샘플을 생성한다는 점을 그림으로 표현

-> 즉 minarity 근처에 majority가 많으면 더 많이 생성

### SMOTE-Tomek

`Oversampling`과 `Undersampling`을 함께 수행하는 방법

 `SMOTE`로 `Oversampling`   `Tomek Links`로 `Undersampling`을 수행



## 2. Regression OverSampling



### SMOTER

SMOTER는 잘 알려진 SMOTE 알고리즘의 회귀에 대한 적용 방법

백분률로 나눠서 가장 적은 데이터를 기준으로 over sampling을 함 (보간법 사용)

k-nearest neighbors 방식 사용해 가중 평균 사용

그러나 백분위로 나눈 후 minority 데이터의 경우 데이터가 적어 잘 복원 될지 ...

와 같은 minority한 경우 특징값들이 같은 값을 가진 경우가 많아 upsampling 이 잘 되지 않는경우 많음 

### SMOGN

SMOGN은 SMOTER에서 가우시안 노이즈를 추가

- 논문으로 따로 정리함 

논문 제목으로 다시 접속 !



### Delving into Deep Imbalanced Regression (ICML 2021, Long Oral)

- 논문으로 따로 정리함 

논문 제목으로 다시 접속 !























# 참조

- uner sampling

https://imbalanced-learn.org/stable/under_sampling.html#mathematical-formulation

- over sampling

https://givitallugot.github.io/articles/2021-07/Python-imbalanced-sampling-copy

https://simonezz.tistory.com/92

https://neptune.ai/blog/how-to-deal-with-imbalanced-classification-and-regression-data

towardsdatascience.com/how-i-handled-imbalanced-text-data-ba9b757ab1d8

- Strategies and Tactics for Regression on Imbalanced Data - Delving into Deep Imbalanced Regression (ICML 2021, Long Oral)

https://towardsdatascience.com/strategies-and-tactics-for-regression-on-imbalanced-data-61eeb0921fca
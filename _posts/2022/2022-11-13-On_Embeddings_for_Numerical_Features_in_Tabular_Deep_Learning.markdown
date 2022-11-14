---
layout: post
title: "paper : On Embeddings for Numerical Features in Tabular Deep Learning"
date: 2022-11-14 01:20:23 +0900
category: paper
---

2022년 3월 15일

# Abstract

piecewise linear encodig(정규화), periodic activations(활성함수)을 제안하며 데이터 별 어떤 딥러닝 방법을 사용해야 할지 실험적으로 정리한 논문

 GBDT와 비교해서 DL이 tabular에서 사용할 수 있도록 연구를 진행

# Indroduction

기존에는 tabular data에서 deep learning을 쓸 필요가 없다는 인식이 많았다. (

deep models (Goodfellow et al., 2016), their success in the tabular domain
is not convincing yet)  → lgbm 등 트리계열 모델의 성능이 잘나오기 때문에 

많은 기존 연구들은 layer에 초점을 맞추고 있어 중요한 전처리 activation function등을 상대적으로 신경쓰지 않음

→ 위 같은 이유로 기존 연구들은 최적의 성능을 보여주지 못하고 있음 

- piecewise linear encoding

 scalar values 와 feature binning 을 해결하기 위한 제안 방법

이 방법 사용시 Transformer 방법론에서도 잘 작동한다고 함 

- contribution
1. numerical features를 효율적으로 임베딩하는 방법을 제안 
2. tabular deep learning에서 Transformer-like architectures 보다 고전적인 모델들이 더 작동이 잘함을 보임
3. sota 달성
4. 여러 데이터 별 실험 결과 제공 

# Related Work

### Tabular deep learning

최근 몇년간 tabular data에서 활용하기 위한 딥러닝 방법들이 많이 연구되고 있음

그러나 비교 대상으로 GBDT를 포함한 체계적인 평가가 제시되지 않고 있다

→ 논문에서는 이런 문제를 해결하기 위해 평가 모델과 수치형 데이터의 전처리에서 놓치고 있는 부분까지 파악해서 보여준다고 함 

### Transformers in tabular DL

transformer 방법론은 nlp vision voice 등의 도메인에서 엄청난 성과를 내고 있음 

tabular 데이터에 적용된 FT-Transformer architecture 연구가 있으나 성능을 최대한으로 발휘하지 못하고 있다(introduction 에서 설명) 이를 실험 

### CTR Prediction

ctr 예측은 수치형 데이터와 카테고리형 데이터인 높은 차원의 임베딩을 해야한다.

그러나 전통적인 activation 과 linear layer만을 사용하고 있음 …

(그럼 ??? )

### Feature binning

binning은 수치형 데이터를 불연속화 변환 방법이다. 

값의 범위를 지정하고 bins으로 분할한다. (이때, 변수들은 별개의 설명인자로 변화됨) 

→ piecewise linear representations 제안

### Periodic activations

nlp vision에서 많이 사용되고 있지만 tabular 에서는 많이 사용되고 있지 않다.

해당 논문에서는 tabular데이터 에서도 효과적으로 사용 가능하다는것을 보여줌

 

# 3. Embeddings for Numerical Features

대상으로 하는 데이터 설명

![f1](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f1.png)

![f2](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f2.png)

전부 지도학습 이며, 다양한 데이터셋에 대한 평가를 학고 있음 

## 3.1. General Framework

- 일반적인 임베딩

![f3](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f3.png)


f : 임베딩 함수

x : 수치형 특징

z : 임베딩된 변수 

임베딩 방법도 테스트 대상에 포함 

![f4](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f4.png)

임베딩된 z들을 mlp에 태움 

## 3.2. Piecewise Linear Encoding

![f5](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f5.png)

e one-hot encoding algorithm 에서 영감을 얻음 

![f6](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f6.png)

특정 간격으로 bin을 생성 

![f7](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f7.png)

PLE : peicewise linear encoding

코드를 실행해봐야 알듯.. 모르겠다…

## 3.3. Periodic Activation Functions

![f8](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f8.png)

c : 학습 파라미터      N(0, σ) 로 초기화 되며 σ는 하이퍼 파라미터 

# 4. Experiments

실험 결과들 

![f9](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f9.png)

실험 모델 설명 

![f10](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f11.png)

![f12](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f12.png)



각 모델별 결과와 xgboost와 비교 결과 

![f13](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f13.png)

모델 크기 및 파라미터 

# 관련 지식

## Implicit Neural Representation

**INR (Implicit Neural Representations)**는 모든 종류의 신호들(signals)을 Neural Network 를 통해 **패러미터화(paremeterize)** 하는 방법이다.

→ INR 은 데이터를 Nueral Network 를 통해 Continuous 한 좌표 값으로 매핑시켜 하나의 함수로 작동하도록 표현

![f14](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f14.png)

패러미터화 : 하나의 표현식에 대해 다른 parameter를 사용하여 다시 표현하는 과정 

→ 위 사진이 예시 인데 딱봐도 어려워 보인다

즉, 신호를 입력으로 받아 encoding해 더 간결하거나 parameter조작이 용이한 represnation을 output으로 출력하는 일종의 regression task

- 장점
- 
    1. 해상도의 영향을 안 받는다(agnostic) - 그리드 포인트가 엄청나게 밀집해도 적용 가능 
    2. model scales with complexity of object, not with resolution 
    3. High Frequncy Data

## **Periodic Activation**

**ReLU position encoding과 같이 데이터의 좌표에 시그널 값을 주는 방법이나, Sine activation을 사용하는 방법이 주로 사용됨**

![f15](\img\2022\On_Embeddings_for_Numerical_Features_in_Tabular_Deep_Learning\f15.png)

위 예시는 sine activation 방법이 왜 좋은지를 설명 

모델의 구조는 linear transformation + Sine Activation을 반복하는 구조 

모델의 레이어를 지나감에 따라서 초기값은 1번 분포를 따르며, **나머지는 2,3번을 반복하는 형식으로 분포가 생성됩니다.** 논문의 저자는 weight의 분포를 적절한 uniform distribution으로 초기화함으로써, activation의 분포가 standard normal distribution이나 interval이 고정된 arcsin으로 강제시킵니다.

→ 딥러닝은 미분으로 학습하기 때문에 미분의 변화량도 같이 학습하면 더 좋은 효과를 낼 수 있음 Lelu같은 경우 미분값이 고정이지만 sine activation 같은 경우 이러한 점을 해결할 수 있음 

# 참고

- Implicit Neural Representation

[https://velog.io/@perla0328/Implicit-Neural-Representations](https://velog.io/@perla0328/Implicit-Neural-Representations)

- **Periodic Activation**

[https://jrc-park.tistory.com/m/286](https://jrc-park.tistory.com/m/286)

[https://tskim9439.github.io/blog/ai/2022-06-16-SIREN/](https://tskim9439.github.io/blog/ai/2022-06-16-SIREN/)
---
layout: post
title: "paper : Delving into Deep Imbalanced Regression"
date: 2022-05-12 01:01:01 +0900
category: paper
---

# Delving into Deep Imbalanced Regression

url : https://arxiv.org/abs/2102.09554
ICML 2021 
code :  https://github.com/YyzHarry/imbalanced-regression  

-> 블로그 정리를 따라서 정리하다가 이해가 안가서 논문으로 다시정리  블로그 정리는 아래 참조 



# Abstract  

실제 데이터는 특정 목표값의 관측치가 유의하게 적은 불균형 분포를 보이는 경우가 많음

기존 imbalanced 해결 방법은  classification 에 초점을 맞춤

나도 regression을 찾고있고 논문도 regression에 관심을 가지고있으니 정리 시작

regressino에서의 불균형 문제를 해결하기 위해 e Deep Imbalanced Regression(DIR) 을 제안 

- 실험 데이터 셋

 CIFAR100  : 100 개의 카테고리 분류 데이터셋(강아지, 차, 비행기 등) 

IMDB-WIKI  : 시각적 외모로 연령 추정을 위한 이미지 데이터 셋

# 1. Introduction

 데이터는 각 범주에 대해 이상적인 균일한 분포를 보존하기보다는 특정 목표 값이 훨씬 적은 긴 꼬리를 가진 왜곡된 분포를 보이는 경우가 많다

# ![f_1](\img\2022\Delving_into_Deep Imbalanced_Regression\f_1.PNG)

DIR을 자연 불균형 데이터에서 연속 대상을 학습하는 것으로 정의(위의 Figure 1 참조)

정 목표 값에 대한 잠재적으로 누락된 데이터를 처리하고 연속 목표 값의 전체 범위에 걸쳐 균형 잡힌 테스트 세트로 일반화

- 연속(잠재적으로 무한) 대상 값이 주어지면 클래스 간의 경계까 존재하지 않음으로 불균형 분류 방법을 직접 적용할 때 모호성을 유발

ex) t1, t2 에 훈련 데이터의 관측치 수가 적다고 가정  그러나 t1근처에는 데이터들이 많고 t2근처에 데이터들이 없다면 t1과 t2의 예측 정도가 달라짐 ( t1은 불균형을 겪지 않음 )



이러한 문제를 해결하기 위해 

label distribution smoothing (LDS)  와 feature distribution smoothing (FDS)를 제안

두 접근 방식의 기초가 되는 핵심 아이디어는 커널 분포를 사용하여 레이블 및 특징 공간에서 명시적 분포 평활을 수행하여 인근 대상 간의 유사성을 활용하는 것

두 가지 방식은 딥러닝에 적용 가능하며 불균형에 대해 성공적으로 보정할 뿐만 아니라 다른 방법과 결합할 때 크고 일관된 이득을 제공

논문의 컨트리 뷰션

-  DIR 작업을 연속적인 대상을 가진 불균형 데이터에서 학습하고 전체 대상 범위로 일반화하는 것으로 공식적으로 정의
- 레이블과 특징 공간 모두에서 인근 대상 간의 유사성을 활용하는 DIR, LDS 및 FDS에 대한 두 가지 간단하고 효과적이며 해석 가능한 알고리듬을 개발
- 벤치마크 DIR 데이터 세트를 컴퓨터 비전, 자연어 처리 및 의료 등 다양한 영역에서 큐레이션

#  2.Related Work

#### Imbalanced Classification

많은 선행 연구는 불균형 분류 문제(긴 꼬리 인식이라고도 함)에 초점을 맞추고 있다

데이터는 각 범주에 대해 이상적인 균일 분포를 유지하는 대신 긴 꼬리가 있는 치우친 분포를 나타내는 경우가 많으며, 여기서 특정 대상 값은 관측치가 훨씬 적습니다.

과거 해결 방법

> - data-based
>
> 동일한 클래스의 샘플을 선형으로 보간하여 소수 클래스에 대해 합성 샘픙르 생성하는 방법
>
> smote알고리즘 같이 소수 클래스를 over-sampling 하거나 majority 클래스를 under-sampling 하기도 함
>
> - model-based
>
> re-weighting, adjusting the loss function, and leveraging relevant learning paradigms, such as transfer learning, meta-learning, and two-stage training.
>
> 

리그레션에서 이를 해결하기 위해

해당 논문에서는 Label distribution smoothing (LDS) 와 feature distribution smoothing (FDS)를 제안

#### Imbalanced Regression

이 주제에 대한 대부분의 연구는 SMOTE 알고리듬을 회귀 시나리오에 직접 적응시키는 것

배깅이나 앙상블 기반 방법들이 고려됨

# 3. Methods

![f_2](\img\2022\Delving_into_Deep Imbalanced_Regression\f_2.PNG)

- Problem Setting

왼쪽 데이터는 classification 오른쪽 데이터는 regression

간단하게 두 데이터의 분포를 일치화 시킴(정규화 및 데이터 컷)

## 3.1. Label Distribution Smoothing

Figure2 에서 불균형이 나타날 때 분류와 회귀 사이의 차이를 보여주는 예를 보여주는 것으로 시작

그림 2(a)를 통해 오차 분포가 라벨 밀도 분포와 상관관계가 있음을 관찰

림 2(b)에서 알 수 있듯이, 라벨 밀도 분포가 CIFAR-100과 동일하더라도 연속적인 라벨 공간을 갖는 IMDB-WIKI의 경우 오차 분포가 매우 다르다.

-> . 이 예가 흥미로운 이유는 직간접적으로 모든 불균형 학습 방법이 경험적 레이블 밀도 분포의 불균형을 보완하여 작동하기 때문

클래스 불균형에는 잘 작동하지만 연속 레이블의 경우 경험적 밀도가 신경망에 의해 보이는 불균형을 정확하게 반영하지 못한다.

#### LDS for Imbalanced Data Density Estimation.

인근 레이블(예: 근연령 이미지)의 데이터 샘플 간의 의존성 때문에 연속적인 경우 실제 레이블 밀도 분포를 발영하지 못함.

레이블 분포 스무딩(LDS)은 연속 대상에 해당하는 데이터 세트의 효과적인 불균형을 학습하기 위해 커널 밀도 추정의 사용



LDS는 대칭 커널을 경험적 밀도 분포와 결합하여 인근 레이블의 데이터 샘플 정보에서 중복을 설명하는 커널 평활 버전을 추출

>  대칭 커널은 
>
> k(y, y^) = k(y^, y) 
>
> ∇k(y, y^) + ∇y^k(y ^, y) = 0,
>
>  yy, y^  ∈  yY
>
> 를 만족시키는 커널 (k(y, y^) /= yy^ 인 경우)

즉 대칭터널은 목표값 y^과 목표 공간에서의 거리 y 사이의 유사성을 특징 짓는다.

따라서 LDS는 유효 레이블 밀도 분포를 다음과 같이 계산합니다.

![f1](\img\2022\Delving_into_Deep Imbalanced_Regression\f1.PNG)

 p(y)는 훈련 데이터

 y 레이블의 출현 수

p˜(y^)는 y 레이블의 유효 밀도



![lds](\img\2022\Delving_into_Deep Imbalanced_Regression\lds.gif)

위 그림은 LDS가 어떻게 라벨 밀도 분포를 매끄럽게 하는지를 보여준다. 

 LDS에 의해 계산된 결과 레이블 밀도는 오차 분포(-0.83)와 잘 상관된다는 것을 보여준다.

이는 실제 불균형 문제를 포작할 수 있음



효과적인 레이블 밀도를 사용할 수 있게 되었으므로 클래스 불균형 문제를 해결하기 위한 기술을 DIR 컨텍스트에 직접 적용할 수 있다.

es) 간단한 적응은 비용에 민감한 재가중 방법, 손실함수 가중치 등 

## 3.2. Feature Distribution Smoothing

학습된 feature 공간의 z에 대해서 집중함 

모형이 제대로 작동하고 데이터가 균형을 이루면 주변 표적에 해당하는 형상 모수 통계량이 서로 가까울 것으로 예상

![f_4](\img\2022\Delving_into_Deep Imbalanced_Regression\f_4.gif)

- 그림

> 모든 feature의 평균, 분산 의 코사인 유사도로 비교
>
> - 상단
>
> 특정 연령에서 형상 평균의 코사인 유사도는 고정 지점의 값을 기준으로 한다.
>
> - 하단
>
>  특정 연령에서 특징의 코사인 유사성은 고정 지점의 값에 따라 달라진다
>
>  
>
> 배경색은 특정 대상 범위의 데이터 밀도
>
> 그림은 가까운 연령이 가까운 유사성을 가지고 있다는 것을 보여준다.
>
> 또한 데이터 불균형으로 인해 0세에서 6세까지의 이미지와 30세 사이의 부당한 유사성이 있음을 보여준다.

25세에서 35세 사이의 모든 빈에 대한 형상 평균과 형상 분산의 코사인 유사도는 30세(고정 연령)의 값으로부터 몇 퍼센트 이내, 앵커 주변의 범위가 좁을수록 유사도가 높짐

#### FDS Algorithm.

위의 관찰에서 연감을 받아 공간에 대한 분포 평활을 수행하는 형상 분포 평활화(FDS)를 제안

-> 주변 대상 빈 간에 형상 통계를 이용



FDS는 먼저 각 빈의 통계를 추정

일반성의 손실 없이, 우리는 z 내의 다양한 특징 요소들 사이의 관계를 반영하기 위해 분산을 공분산으로 치환

![f2](\img\2022\Delving_into_Deep Imbalanced_Regression\f2.PNG)



Nb 데이터에서 bin의 총 표본의 수 

k(yb, yb' ) t : 대상 빈 B에 대한 형상 평균과 공분산의 분포를 매끄럽게 함 - 커널함수 사용 

![f4](\img\2022\Delving_into_Deep Imbalanced_Regression\f4.PNG)

{µb, Σb} and {µ˜b, Σeb} standard whitening and re-coloring 방법을 사용 

![f6](\img\2022\Delving_into_Deep Imbalanced_Regression\f6.PNG)

 최종 형상 맵 다음에 형상 보정 계층을 삽입하여 FDS를 심층 네트워크에 통합

모델을 훈련시키기 위해, 우리는 각 에포크에서 실행 통계 {αb, βb}의 모멘텀 업데이트를 사용

실행 중인 통계의 지수 이동 평균(EMA)을 수행하는 모멘텀 업데이트를 통해 훈련 중에 특징 통계를 보다 안정적이고 정확하게 추정할 수 있다.

보정된 형상 z²는 최종 회귀 함수로 전달되고 손실을 계산하는 데 사용

![fds](\img\2022\Delving_into_Deep Imbalanced_Regression\fds.gif)

# 4. Benchmarking DIR

## 실험 환경

- loss function

로지스틱에 맞는 임벨런스 로스를 사용하기 위해 Focal-R loss를 이용

- Focal-R loss

> L1 distance에 기초함  
>
> ![focal-r](\img\2022\Delving_into_Deep Imbalanced_Regression\focal-r.PNG)
>
> ei :  i번째 샘플에 대한 L1 오차
>
> σ : sigmoid
>
> β, γ : 하이퍼 파라미터
>
> -> 손실을 추정된 라벨 밀도의 역으로해서 곱함 

```
https://github.com/YyzHarry/imbalanced-regression/blob/main/sts-b-dir/loss.py

def weighted_focal_l1_loss(inputs, targets, weights=None, activate='sigmoid', beta=20., gamma=1):
    loss = F.l1_loss(inputs, targets, reduce=False)
    loss *= (torch.tanh(beta * torch.abs(inputs - targets))) ** gamma if activate == 'tanh' else \
        (2 * torch.sigmoid(beta * torch.abs(inputs - targets)) - 1) ** gamma
    if weights is not None:
        loss *= weights.expand_as(loss)
    loss = torch.mean(loss)
    return loss
    
def weighted_focal_mse_loss(inputs, targets, weights=None, activate='sigmoid', beta=20., gamma=1):
    loss = F.mse_loss(inputs, targets, reduce=False)
    loss *= (torch.tanh(beta * torch.abs(inputs - targets))) ** gamma if activate == 'tanh' else \
        (2 * torch.sigmoid(beta * torch.abs(inputs - targets)) - 1) ** gamma
    if weights is not None:
        loss *= weights.expand_as(loss)
    loss = torch.mean(loss)
    return loss
```


- Two-stage training 

regressor re-training (RRT)을 제안 

> - first stage
>
> 인코더를 정상적으로 훈련
>
> - second stage
>
> 인코더를 동결하고 역 재가중으로 회귀기 g(·)를 재훈련
>
> DS를 첨가할 때, 2단계에서의 재가중치는 LDS를 통해 추정된 라벨 밀도를 기준



![t_1](\img\2022\Delving_into_Deep Imbalanced_Regression\t_1.PNG)

![t_2](\img\2022\Delving_into_Deep Imbalanced_Regression\t_2.PNG)



# 5. Conclusion

 연속적인 대상을 가진 자연 불균형 데이터에서 학습하고 전체 대상 범위로 일반화하는 DIR 작업을 소개

이블과 특징 공간 모두에서 주변 대상 간의 유사성을 활용하는 DIR에 대한 두 가지 간단하고 효과적인 알고리듬을 제안

 DIR 벤치마크 5개에 대한 광범위한 결과는 우리 방법의 우수한 성능을 입증





# 관련 지식

## Kernel Density Estimation(KDE)

Kernel Density Estimation(커널 밀도 추정)이란 히스토그램(histogram) 등을 smoothing(스무딩)하는 것

#### **Density Estimation**(밀도 추정)

데이터는 어떤 변수가 가질 수 있는 다양한 가능성 중의 하나가 현실 세계에 구체화된 값 ->  이렇게 관측된 데이터들을 통해 그 변수(random variable)가 가지고 있는 본질적인 특성을 파악

하나의 데이터는 변수의 일면에 불과하기 때문에 변수의 진면목을 파악하기 위해서는 많은 수의 데이터가 필요

그리고 이렇게 얻어진(관측된) 데이터들의 분포로부터 원래 변수의 (확률) 분포 특성을 추정하고자 하는 것이 density estimation(밀도추정)이다.

```
위의 예시
-  육교 밑을 통과하는 차량의 일일 교통량을 파악하는게 목적
 변수(random variable)는 '일일 교통량'이다.
 실제 육교 위에서 매일 매일 관찰한 값이 데이터
 
 이데이터를 수집해 나가면 '일일 교통량'이란 변수가 어떤 값의 분포 특성을 갖는지 좀더 정확히 파악
 그리고 어떤 변수가 가질 수 있는 값 및 그 값을 가질 가능성의 정도를 추정 하는것이 density estimation
```

밀도(density)는 수학적으로는 mass/volume으로 정의되지만, 밀도추정(density estimation), 기계학습, 확률, 통계 등에서 말하는 밀도(density)는 확률밀도(probability density)를 의미

- 밀도 추정 방법

> 1. Parametric
>
> Parametric 밀도추정은 미리 pdf(probability density function)에 대한 모델을 정해놓고 데이터들로부터 모델의 파라미터만 추정하는 방식
>
> ```
>  '일일 교통량'이 정규분포를 따른다고 가정해 버리면 관측된 데이터들로부터 평균과 분산만 구하면 되기 때문에 밀도추정 문제가 비교적 간단한 문제가 됌
> ```
>
> 1. Non-parametric
>
> 그러나 현실에서 모델이 미리 주어지는 경우는 많지 않다.
>
> 사전 정보나 지식 없이 순수하게 괸측된 데이터만으로 확률밀도함수를 추정하는 방식
>
> 간단한 예시로는 histogram이 있음 

#### kernel function

![kerner_1](\img\2022\Delving_into_Deep Imbalanced_Regression\kerner_1.PNG)



우선 kernel function는 수학적으로 원점을 중심으로 대칭이면서 적분값이 1인 non-negative 함수로 정의(Gaussian, Epanechnikov, uniform 함수등이 대표적)

#### Kernel Density Estimation(커널 밀도 추정)

히스토그램 방법은 bin의 경계에서 불연속성이 나타난다는 점, bin의 크기 및 시작 위치에 따라서 히스토그램이 달라진다는 점, 고차원(high dimension) 데이터에는 메모리 문제 등으로 사용하기 힘들다는 점 등의 문제점을 갖는다.

*** Kernel Density Estimation (커널 밀도 추정) 방법은 non-parametric 밀도추정 방법 중 하나로서 커널함수(kernel function)를 이용하여 히스토그램 방법의 문제점을 개선한 방법 ***

![pdf_1](\img\2022\Delving_into_Deep Imbalanced_Regression\pdf_1.PNG)

 x를 변수(random variable), x1, x2, ..., xn을 관측된 샘플 데이터, K를 커널 함수라 하면 KDE에서는 랜점 변수 x에 대한 pdf(확률 밀도 함수)는 다음과 같이 추정됨

위 식의 h는 커널 함수의 bandwidhtm (첨도가 높으면 h는 작은 값, 첨도가 낮으면 h는 큰 값)를 조절하는 파라미터

```
1. 관측된 데이터 각각마다 해당 데이터 값을 중심으로 하는 커널 함수를 생성한다: K(x-xi)
2. 이렇게 만들어진 커널 함수들을 모두 더한 후 전체 데이터 개수로 나눈다.
```

![kerner_2](\img\2022\Delving_into_Deep Imbalanced_Regression\kerner_2.PNG)

히스토그램을 이용한 밀도추정 방법과 KDE 방법을 비교해 보면, 히스토그램 방법은 이산적(discrete)으로 각 데이터에 대응되는 bin의 값을 증가시킴으로써 불연속성이 발생하는 반면 KDE(커널밀도추정) 방법은 각 데이터를 커널 함수로 대치하여 더함으로써 그림 4 오른쪽 그래프와 같이 smooth한 확률밀도함수(pdf)를 얻을 수 있는 장점을 갖는다.

![kerner_3](\img\2022\Delving_into_Deep Imbalanced_Regression\kerner_3.PNG)

```
KDE(Kernel Density Estimation)를 통해 얻은 확률밀도함수는 히스토그램 확률밀도함수를 스무딩(smoothing)한 것으로도 볼 수 있으며 이 때, 스무딩(smoothing) 정도는 아래 그림처럼 어떤 bandwidth 값의 커널 함수를 사용했으냐에 따라 달라진다.
```

실제 KDE를 사용할 때, 중요한 이슈는 어떤 커널 함수를 사용할지와 커널 함수의 bandwidth 파라미터인 h 값을 어떻게 잡을지이다. 위키피디아에 의하면 가장 최적의 커널함수는 Epanechnikov 커널이며 계산의 편의상 Gaussian 커널함수도 많이 사용된다고 한다. 그리고 Gaussian 커널함수를 사용할 경우 최적의 bandwidth 파라미터 값은 다음과 같다고 한다.

![kerner_4](\img\2022\Delving_into_Deep Imbalanced_Regression\kerner_4.PNG)

 n은 샘플 데이터의 개수, σ는 샘플 데이터의 표준편차.



## whitening 

 whitening 또는 Sphering이라고 불림

입력값을 더 쓸모있게 만드는 작업

각 Feature간에 (1) 서로 작은 상관관계 correlation를 지니도록, 그리고  동일한 분산 variance을 가지도록 하는 작업이다.

























# 참고 

- Kernel Density Estimation

https://darkpgmr.tistory.com/147

- whitening

https://withkairos.wordpress.com/2015/06/13/ufldl-tutorial-8-whitening/


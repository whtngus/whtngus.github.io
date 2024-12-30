---
layout: post
title: "A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization"
date: 2024-12-30 02:05:23 +0900
category: paper
---

# A Unified Anomaly Synthesis Strategy with Gradient Ascent for Industrial Anomaly Detection and Localization

2024년 10월 26일 

상하이 교통 대학 

url : https://arxiv.org/abs/2410.20047

code : https://github.com/xcyao00/ResAD.

# Abstract

class-generalizable anomaly detection 문제에 대해 탐구함 

-> 정의된 AD 모델은 별도의 학습과 데이터 없이 이상치를 탐지할 수 있음 

기존 연구된 one-for-one AD 모델은 학습시 사용되지 않은 클래스가 온경우 성능이 급격하게 떨어짐 

연구에서는 간단하지만 효과적으로 새로운 클래스에 대해 탐지할 수 있는 ResAD를 제안함 

ResAD는 초기 feature분포 보다 residual feature의 분포를 학습하는 것임 

그리고 feature의 variations을 상당히 줄였다고 함 

ResAD는 3개의 요소로 구성됨

1. Feature Convert : 초기 feature를 residual feature로 변환 
2. Feature Constra: normal residual features를 spaital hypersphere로 제한해, feature의 scale과 변화를 더욱 줄이고 일관데게 유지하는 간단하고 얕은 feature constrainor 제안 
3. Feature Distribution Estimator는 normal residual의 분포를 최적화함 

# 1 Introduction

Anomaly detection (AD)는 많은 도메인에서 빠른 성취를 달성함, 특히 산업 검사, 비디오 감시, 의학적 병변산업군에서 사용됨

그러나 현실에서 적용할때 많은 문제에 직면하고 있음 

다양한 클래스와 새로운 클래스가 계속 생성됨 



대부분의 사전 one-for-one 그리고 one-for-many AD(learning one AD model for multiple classes) 모델들은 실제로 적용하기에는 아직 불충분함 

-> 새로운 클래스가 발생한경우 다시 학습해야 되기 때문에 

그리고 또하나의 치명적인 점은 데이터 프라이버시 이슈로 학습하지 못하는 경우가 있음 



그래서 class-generalizable 능력이 중요하지만 아직 연구되지 않음 

해당 연규에서는 학술적 가치와, 활용적 가치 task를 목적으로 함 

few-shot class generalizable anomaly detection 과 하나의 모델이 알고있는 클래스로 학습된 경우 few-shot으로만 새로운 클래스에 대해 학습하지 않고 탐지할 수 있는 지

현재 존재하는 one-for-one/many AD는 대부분 이런 능력이 없다고 함 

논문의 메인 도전 - "the normal patterns from different classes are significantly different"

 residual features을 상당히 분산히 큰 feature인 class-invariant representation 로 간주할 수 있음

![f_1](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f_1.PNG)

figure 1의 를 보면 b를 보면  새로운 클래스는 원래 학습 분포(정상과 비정상)의 차이가 크지 않을거라고 가정 

-> 이를 유사한 특징으로 정상 비정상을 구분하려는 걸로 보임 -> 그렇다면 few-shot 시 정상데이터가 많이 필요할걸로 보임 

이를 이용해 ResAD(Residual Feature Learning based Class-Generalizable Anomaly Detection)를 제안함 



1. residual features를 이용해 클래스 feature의 분산을 감소시킴 

이 과정으로 관련있는 데이터(하나의 클래스는) origin-centered region이 될 가능성이 높음

2. residual feature space를 감소기킴

one-class-classification(OCC) 아이디러를 적용함 

3.  hypersphere-constrained feature space

 feature distribution estimator  

normal residual feature 분포를 사용해 이상치



contributions

1. ResAD를 제안하고 class-generalizable anomaly detection을 달성함 
2. 이전 one-forone/many AD 방식의 새로운 클래스에 대한 해결을 residual feature learning으로 해결
3.  6개의 AD 데이터셋에 대해 4-shot 에서 sota 성능 다성 

# 2 Related Work

#### One-for-One/Many AD Methods

대부분 AD 방식은 one-for-one/many 체계임 

1. Reconstruction-based methods

   가장 인기있는 AD 방식이라고함  이때 주로 auto-encoders를 사용함 

   UniAD는 transformer 기반의 recontruction 모델이나 one-for-many AD로 쓰기엔 "identical shorcut" 이슈가 있음

2. Distillation-based methods 

student networks를 teacher networks의 reconstruct를 학습함 

3.  Embedding-based method

#### Few-Shot AD Methods.

해당연구와 비슷한 방법

별도의 학습 없이 거리 기반의 접근 방식으로 few-soht 을 진행함



논문에서는 few-shot ad와 class-generalizable ad가 다르다고함 (논문의 타당성을 위해서 인듯)

Class-generalizable AD는 새로운 클래스의 normal samples의 feature만을 추출함

few-shot ad의 경우 여전히 새로운 클래스의 경우 학습을 해야한다고함

# 3 Method

#### Problem Statement.

I_train = I^n ∪ I^a

트레인 데이터셋은 일반 이미지와 이상치 이미지로 구성됨 

![f1](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f1.PNG)

![f2](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f2.PNG)

일반 임지와 이상치 이미지는 위와 같으 구성됨 

-> 위 변변수에 대한 설명이 없음 ...

unknown class는 C_u로 표기함  그리고 known class는 C_k로 표기함 

#### Overview

#### ![f_2](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f_2.PNG)

ResAD은 3개의파트로 구성됨 

1. Feature Extractor
2. Feature Constraintor
3. Feature Distribution Estimator

## 3.1 Residual Feature Generating

Residual feature learning은 class-generalizable AD를 하기위한 논문의 핵심 아디이어임 

![f3](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f3.PNG)

ϕ : Feature extraction 네트워크(각각 다른 레벨로 추출)

L: feature extraction 의 레벨의 총 수 

![f4](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f4.PNG)

여기서 H_l, W_l, C_l은 높이, 너비, 채널 차원을 가진 feautre map 임 

![f5](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f5.PNG)

l : level

(h,w) : 위치

#### Reference Feature Pools.

새로운 클래스를 예측하는 경우 few개의 normal 셈플을 같이 입력함 

(이때는 랜덤 추출로 데이터셋을 만들어서 고정)

pre-trained 네트워크인 ϕ 이 일반 이미지로부터 계층적으로 feature를 추출함 

![f6](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f6.PNG)

l은 각 레벨을 의미 

i는 일반 이미지 셈플 

N_fs 는 일반 이미지 수

#### Residual Features.

![f7](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f7.PNG)

x^l_h,w 는 초기 feature 

참조 feature pool P_l에서 가장 가까운 feature를 찾는 작업 을함 

식에서 l은 참조 pool 

![ff1](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\ff1.PNG)

x^l_h,w 는 representation 임 

즉, 가장 가까운 벡터거리를 구한걸로 보임 



![f_3](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f_3.PNG)



새로운 class에 대해서 분류할 수 있는 능력이 떨어지는 것은 다른 클래스의 feature는 일반적으로 다른 feature 도메인에 있기 때문임 



## 3.2 Feature Hypersphere Constraining

class들은 상당히 다른 스캐일들을 가졌을 거고, 이로 인해 다른 클래스간의 결정 경계값이 매우 달라질 것임



feature 분산을 줄이고 class간의 일관성을 유지하기 위해 one-class-classification (OCC) learning 아이디어인 Feature Constraintor를 제안함 

Feature Constraintor는 초기 residual feature 공간을 제한함

C_θ_1 는 Featrue Constrainor 이고     projects 초기 residual feature는 x^l,r_h,w 임

제약된 constrain feature는 

![f8](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f8.PNG)

위와 같이 정의함 

이때 사용한 네트워크는 Conv+BN+ReLU로 분포가 바뀌는걸 원치않아서 간단한 레이어로 사용했다고 함 

복잡한 네트워크는 알고있는 feature에대해 overfitting되기 쉽고,일반화가 어렵다고함

#### Abnormal Invariant OCC Loss

![ff2](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\ff2.PNG)

y^l_h,w = 1은 이상치의 위치

y^l_h,w = 0은 정상 위치 

-> low-resolution mask를 사용

첫 파트의 로스함수는  pseudo-Huber loss

정상성이 0이기 때문에 바이어스에 제한을 두게 됨 

-> 이게 스케일을 제한하기는 어려운데 더 봐야될듯 그리고 해당로스는 잘못된 부분이 보임 

* 모든 representation vector가 0인경우 loss는 0이됨 

## 3.3 Feature Distribution Estimating

 normalizing flow (NF) model 을 사용해서 represent를 변환함

![f9](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\f9.PNG)

NF 모델로 위와 같은 수식을 사용함 

변한된 representation 벡터를 z로 이동 

![ff3](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\ff3.PNG)

J는 x에대한 z의 미분값이고Jacobian matrix를 사용함 

![ff4](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\ff4.PNG)

C를 NF 모델에 씌움 

BGAD를 통해 알고있는 클래스에 오버피팅되지 않도록 막음

![ff5](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\ff5.PNG)

b_n은 바운더리 τ 마진값

바운드리값은 BGAD 방식을 사용하고 

τ는 0.1 을 사용 (스케일을 낮게 잡음)  -> τ값에 따른 실험결과 첨부되어있음

![ff6](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\ff6.PNG)

loss fuction 3개를 합함 

## 3.4 Inference and Anomaly Scoring



![ff7](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\ff7.PNG)

새로운 클래스에서 해당 논문은 학습 없이 오직 few-shot normal 샘플을 필요로함

 테스트 특성 xilx^l_ixil를 **Feature Constraintor** Cθ1C_{\theta_1}Cθ1와 **Feature Distribution Estimator** ϕθ2\phi_{\theta_2}ϕθ2에 입력하여 잠재 특성 zilz^l_izil를 얻습니다



s(x)를 bilinear interpolation를 이용해 업셈플링함 

# 4 Experiments

## 4.1 Experimental Setup





# 참고

- Reconstruction-based

예측과 달리 주어진 시계열 그 자체를 그대로 복원하여 그 차이를 시계열 이상 탐지에 사용하는 방법 

- identical shortcut

reconstruction 기반의 이상치 탐지 방법론에서 대두되는 문제가 정상 데이터, 이상치 데이터 모두 복원이 잘 되는 점

- CLIP (Contrastive Language-Image Pre-training)

OpenAI에서 2021년에 발표한 논문

Text와 Image간의 관계성을 모델링한 연구

이미지와 해당 이미지에 대한 설명 Text를 pair로 두고 학습데이터셋으로 구성한 후, 각각을 인코더로 임베딩하여 같은 pair에 대해 거리를 가깝게하고 다른 pair에 대해 거리가 멀어지도록 텍스트/이미지 인코더를 학습

- Huber loss

L1과 L2의 장점을 취하면서 단점을 보완하기 위해 제안된 것

L2는 제곱이여서 이상치에 취약

![huber_loss](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\huber_loss.PNG)

이상치에 취약한걸 해결하게 위해 특정 값보다 큰 경우 로스함수를 제곱을 제거

l2와 유사하지만 그외부분은 l1과 유사한 형태를 가져감 

-  normalizing flow model



참고 : https://wikidocs.net/229977![normalizing_flow_model](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\normalizing_flow_model.PNG)

- Jacobian matrix

비선형 변환을 미분으로 선형변환으로 근사시키는것

-> 변환해야 되는 스케일을 선형으로 맞춰 버림 

![jacobian](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\jacobian.PNG)

참고:  https://angeloyeo.github.io/2020/07/24/Jacobian.html

- bilinear interpolation

참고 : https://blog.naver.com/aorigin/220947541918

![bilinear_interporation](\img\2024\ResAD__A_Simple_Framework_for_Class_Generalizable_Anomaly_Detection\bilinear_interporation.PNG)
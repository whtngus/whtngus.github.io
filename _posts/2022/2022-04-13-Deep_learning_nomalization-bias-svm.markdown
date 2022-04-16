---
layout: post
title: "normalization gan kl-divergence 기초 다시 정리"
date: 2022-04-13 16:20:23 +0900
category: deep_learning
---



# Normalization

- 공변량(covariate)

공변량이라는 변수는 독립변수라기 보다는 하나의 개념으로서 여러 변수들이 공통적으로 함께 공유하고 있는 변량을 뜻한다. 

공변량의 분포가 학습과 테스트에 다른 상황을 공변량 변화라고 부른다.

- internal covariate shift (ICS)

![nomalization_3](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\DS기초\nomalization_3.png)

input layer에서 정규분포를 가지는 입력을 줘도 hidden layer를 지나면서 그 분포가 점점 정규분포를 벗어나 ( ex - sigmoid 인 경우 거의다 1이 여서 back propagation이 0이됨) gradient vanishing 현상이 발생

Back-propagation에 의해서 트레이닝이 진행이 되면, 특정 레이어는 해당 레이어보다 낮은 레이어가 변함에 따라 영향을 받게 됨. Network 가 깊어질수록, 더욱 스노우볼이 굴러감.

-> 특정 레이어는 인풋이 새로운 Distribution으로 계속해서 변해가늦ㄴ 것에 적으하며 학습해야하는 점 때문에 필요

## Normalization 비교

### 기본적인 nomazliation

1. normalization

정규화 라고 불리며 값 범위의 차이를 왜곡시키지 않고 데이터 세트를 공통된 scale로 변경하는 것 

ex ) Min-Max Scaler

2. Regularization

일반화, 정규화로 불림  (학습 제약 기법)

ex) weight decay, droptou, pruning

3. Standardization

표준화 라고 불리며, 기존 데이터를 평균 0 표준편차1인 표준분포의 꼴 데이터로 만드는것을 의미

Standard Scaler, z-score normalization

###  weight 

![nomalization](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\DS기초\nomalization.png)

4. Batch Normalization

batch 단위로 평균을 구함, 각 데이터들으 분산을 구함,  scanle and shift

activation function이 작용하기 전에 진행됨  

샘플을 standard noralize -> variance와 bias를 조절할 수 있는 y, b를 부과해서 parameterize를 함 

=> y와 b를 다시 조절하는 이유는 sigmoid는 중앙에 몰려있는 분포가 학습하지 좋지만 다른 activate 는 안좋음 

단점 : batch size가 작을경우 안좋음 

5. Layer Normalization

Feature 차원에서 정규화를 진행 , batch가 1인 경우에는 batch normalization을 수행하지 못하기 때문에 + rnn같은경우 각 단계마다 적용시 모델을 더 복잡하게 만듦

rnn 에서 좋은성능을 냄 

![nomalization_2](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\DS기초\nomalization_2.png)

6. Instance Normalization

(image 데이터를 타겟으로 함)layer normalization과 유사하지만 각 데이터마다 normalization을 하고 fiter들의 종류와 관계없이 (layer norm과의 차이점)다 따로 normalization을 진행 

7. Group Normalization

Instance Normalization과 유사함. 다만 여기서는 채널들을 그룹으로 묶어 평균과 표준편차를 구한다. 마치 , Layer Normalization과 Instance Normalization의 중간정도라고 생각할 수 있다.

만약, 모든 채널이 하나의 그룹으로 묶여있다면 Layer Normalization 이고 모든 채널이 각각의 그룹이 되어있다면 Instance Normalization이다.

8. Weight Normalization

 mini-batch를 정규화하는 것이 아니라 layer의 가중치를 정규화



# gan vs vae

## GAN

gan은 두 가지 구성요소 가 있음 - generator discriminator

GAN loss function

![gan_1](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\DS기초\gan_1.png)

D(x) - discriminator output -> classification image

G(z) - generator output -> generation image



## VAE

![gan_2](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\DS기초\gan_2.png)

우측항 negative KL divergece 를 사용 

p_pi(x|z) : normal prior N(0, 1)

장점 : 모델 평가 기준이 명확함(원본 데이터를 잘 복구 햇는지)



## 	비교

최종적으로 컨셉과 동일하다는 것 

VAE : 입력 데이터를 만드는것을 목표로 함,  차원 축소용으로 많이 사용 

GAN :  새로운 이미지를 만들어 낼 때 많이 사용 





# KL divergence

풀 네임 : Kullback-Leibler divergence (쿨백 라이블러 발산)

- P 분포와 Q 분포가 얼마나 다른지를 측정하는 방법

 통계적으로 P는 사후, Q는 사전분포

두 [확률분포](https://ko.wikipedia.org/wiki/%ED%99%95%EB%A5%A0%EB%B6%84%ED%8F%AC)의 차이를 계산하는 데에 사용하는 함수로, 어떤 이상적인 분포에 대해, 그 분포를 근사하는 다른 분포를 사용해 샘플링을 한다면 발생할 수 있는 [정보 엔트로피](https://ko.wikipedia.org/wiki/%EC%A0%95%EB%B3%B4_%EC%97%94%ED%8A%B8%EB%A1%9C%ED%94%BC) 차이를 계산

![kl](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\DS기초\kl.png)

![![img](file:///C:/Users/whtng/OneDrive/%EB%AC%B8%EC%84%9C/src/whtngus.github.io/img/2022/DS%EA%B8%B0%EC%B4%88/kl_2.png?lastModify=1650104625)kl_2](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\DS기초\kl_2.png)

- KL(p|q)≥0KL(p|q)≥0
- KL(p|q)≠KL(q|p)

-> 거리개념 처럼 쓰려면 Jensen-Shannon divergence 를 사용 

![kl_3](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\DS기초\kl_3.png)

. KL-divergence를 2가지를 구하고는 평균을 내는 방식입니다. 이렇게 간편하게 쓸 수 있지만 Jensen-Shannon divergence는 KL-divergence만큼 자주 쓰이지 않습니다.













# 참조

- nomalization

https://wingnim.tistory.com/92

https://sonsnotation.blogspot.com/2020/11/8-normalization.html

- gan vs vae

https://medium.com/@lishuo1/which-one-should-you-choose-gan-or-vae-part-i-da92acb4ab3e

- kl divergence

https://hyunw.kim/blog/2017/10/27/KL_divergence.html
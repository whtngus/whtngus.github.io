---
layout: post
title: "paper : Controlling Length in Image Captioning"
date: 2021-09-21 19:20:23 +0900
category: paper
---
# Controlling Length in Image Captioning

2020 Computer Vision and Pattern Recognition

url :   https://arxiv.org/abs/2005.14386

github : 	https://github.com/ruotianluo/self-critical.pytorch/tree/length_goal

논문 짧음 ? 

# Abstract

이미지 캡션의 길이를 조절해 다른 스타일의 캡션을 생성할 수 있도록 유도 

# 1. Introduction

Transformer와 LSTM을 통한 Image Captioning은 이미 많이 존재하고 있음

하지만 일반적으로 이미지 캡션의 마지막을 나타내는 <eos> 테그로 캡션을 generate 하기 때문에 

이미지 캡션의 output을 변경 조정하는것은 매우 어렵다.

해당 연구에서는 이미지 캡션 생성 학습시 이미지 캡션 라벨의 길이의 정보를 제공해 이미지 캡션 길이를 조정하고자 한다.

그리고 7 ~ 28 단어의 길이의 캡션을 조정 및 생성하는데 성공했고 길이를 컨트롤하지 못하는 캡션 모델에 비해 높은 성능을 달성했다.

# 2. Models

![f_1](\img\2021\Controlling_Length_in_Image_Captioning\f_1.PNG)

```
c : caption
I : image
l : caption length
```

일반적인 이미지 캡션 모델은 이미지 정보만을 가지고 캡션을 생성한다.

하지만 해당 연구에서는 이미지 캡션의 길이를 조절하기 위해 캡션의 길이 정보를 모델에 주입하여 학습한다.

##  2.1 LenEmb

해당 연구에서는 LenEmb를 통해 모델애 간단한 변화를 준다.

![f_2](\img\2021\Controlling_Length_in_Image_Captioning\f_2.PNG)

```
t : time 
위 수식에서 길이 임베딩을 추가하는 방식은 현재 이미지 캡션의 전체 길이에서 현재 토큰의 길이를 뺀 차후 남은 토큰 수를 입력으로 추가한다.
```

위의 방식으로 학습한 후 predict 시에 원하는 캡션 길이를 이미지에 추가로 모델에 주입하여 캡션 생성을 컨트롤 한다.

## 2.2 Marker

두 번재로 Marker 모델을 구현한다.

첫 번째 단어로 특수 토큰(길이 정보를 제공하는)으로 제공하여 훈련 시 모형은 첫 번째 단계에서 다른 단어와 동일한 방식으로 길이를 예측하는 방법을 배운다.

-> test 시에 원하는 길이를 지정하지 않은 경우 다른 단어와 동일한 방식을 생성하게 만듦

# 3. Experiments

COCO evaluate 모델을 사용

## 3.1 Generation with predicted lengths



![t_1](\img\2021\Controlling_Length_in_Image_Captioning\t_1.PNG)

공정한 성능평가를 위해 caption의 길이를 label을 보고 주는게 아닌 캡션의 길이또한 예측하여 모델의 입력으로 비교한 결과이다.

위의 결과에서 점수는 비슷해 보이지만 길이분포는 상당히 다른 결과를 보여준다.

일반 회귀 모델보다 해당 연구에서 제시하는 모델이 더욱 긴 캡션을 생성하는 경향을 보임 

(but 두 모델다 실제 caption test 데이터의 길이 분포에 근접하진 않음)

## 3.2 Generation with controlled lengths

원하는 길이까지 eos 토큰 생성을 피하기 위해 확률을 변경하는 fixLen 방법을 사용

CIDEr-D 는 생성과 참조 사이의 평균 유사성을 계싼하기 때문에 짧은 캡션과 일반 캡션을 만들게 된다. 수정된  CIDEr  (길이 페널티를 제거or 모든 기준 캡션에서 n-gram 카운트를 결합)하는 방식을 제안한다.

![c_1](\img\2021\Controlling_Length_in_Image_Captioning\c_1.PNG)

### Fluency

Attn2in 모델에서 문장의 마지막 캡션을 정상적을 생성하지 못해  유창한 문장을 생성할 수 없는 문제가 있어 Beam 크기를 늘려 해결 (?!? 그냥 리소스 많이사용???)

길이 모델의 경우 20보다 작을 때 성능이 우수하지만 LenEmb는 일관돠게 우수함 

### Accuracy 

위 그림의 Figure 2 에서 

캡션의 길이가 10 이하인 경우 기본 모델보다 성능이 우수 

기본 모델은 데이터 세트에가 가장 일반적인 길이인 10~16 사이의 캡션 길이에서 우수한 성능을 보임 

길이가 클수록  LenEmb는 mCIDer와 SPICE 모두에서 최고의 성능을 보이며 더 많은 정보를 포함한다.

### Controllability

원하는 길이와 실제 길이(LenMSE) 사이의 평균 제곱 오차를 사용하여 제어 가능성을 평가한다.

예측 길이를 사용하는 경우, 길이 모형은 예측 길이를 완벽하게 달성

하는 길이를 입력했을 때, 그림 2는 LenEmb가 길이를 완벽하게 준수할 수 있는 반면 마커는 좋지 않은 장기적 의존성으로 인해 긴 캡션에 대해 확률적으로 실패

-> 즉 길이를 무작위로 조작하면 실패한다는 소리??  길이를 조절할 수 있지만 학습데이터인 caption의 길이와 크게 벗어나면 잘 생성 못한다는것 같다.

### Quatlitative results

긴 캡션을 생성할 때 LenEmb 모델이 캡션 구조를 변경하고 보다 자세한 내용을 다루는 반면 Marker 모델은 길이와 반복에 대해 동일한 접두사를 갖는 경향이 있음

# 3.3 Failure on CIDEr optimization

SCST를 적용한경우 성능평가에선 점수가 좋아졌지만 'a a a' 같이 잘못된 단어를 반복 하는 경향을 발견하여 사용하지 않음

# 4. Conclusions

해당 연구에서는 길이를 제어할 수 있고 다양한 길이의 캡션을 생성하는 효과를 보여준다.

두 가지 캡션 모델을 제시하고 코드 또한 제공한다.




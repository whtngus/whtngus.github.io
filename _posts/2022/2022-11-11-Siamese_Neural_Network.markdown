---
layout: post
title: "paper : Siamese Neural Network"
date: 2022-11-07 01:01:01 +0900
category: paper
---
2005년

[Learning a Similarity Metric Discriminatively, with Application to Face Verification](http://yann.lecun.com/exdb/publis/pdf/chopra-05.pdf)

라는 논문으로 Yann LeCun 교수 연구팀에 의해 발표

Siamese Network 는 (이하 샴 네트워크) 다루어야하는 클래스의 종류가 매우 많고, 특정 클래스에 대한 사진을 대량으로 구할 수 없을 때 머신러닝을 활용하여 그 클래스를 구분해내기 위하여 고안된 네트워크

![f1](\img\2022\Siamese_Neural_Network\f1.png)

축구공, 코끼리, 악어 3가지 클래스로 같은지 다른지를 모델을 학습 시키고 입력 feature를 이해해서 얼마 보지 못한 데이터 클래스를 예측

![f2](\img\2022\Siamese_Neural_Network\f2.png)

이러한 방법을 적용하는 모델중 하나가 샴 네트워크 이고 두 입력간의 feature를 합쳐서 사용하는 방법

기본적으로 샴 네트워크는 모델의 웨이트를 공유함

![f3](\img\2022\Siamese_Neural_Network\f3.png)

이렇게 정의된 네트워크에 두 사진이 같을 경우 유사도(Similarity)를 1로 주고, 두 사진이 다를 경우 유사도(similarity)를 0 으로 주어서 모델을 학습

![f4](\img\2022\Siamese_Neural_Network\f4.png)

이때 각 입력에서 나온 embedding vector를 이용해 classification, regression 등 다양하게 활용 가능

## vector 학습 만드는 방법

이것을 similarity learning 혹은 metric learning이라고 부름

![f5](\img\2022\Siamese_Neural_Network\f5.png)

### similarity learning or metric learning 방법

### contrastive loss function

![f6](\img\2022\Siamese_Neural_Network\f6.png)

Y = 0 같은 셈플인 경우 : 거리만큼 loss가 발생

Y = 1 다른 셈플인 경우 : 입력 파라미트 margin값 보다 작은 경우 loss가 발생

contrastive loss는 같은 데이터 다른 데이터 한 번씩 사용해 학 습 함으로 한번에 둘 다 학습시킬 수 있는 방법은 없을까? 

### triplet loss function

![f6](\img\2022\Siamese_Neural_Network\f6.png)

데이터를 하나 가지고 와서(anchor) 기준으로 삼고, 같은 클래스(positive)에 데이터 하나 다른 클래스(negative)에 데이터 하나를 가지고 온 후,

(같은 클래스와의 거리) - (다른 클래스와의 거리) 만큼 손실이 발생

- 여기에서 중요한 포인트는 a(alpha)

a가 없다면 anchor-posirive, anchor-negative pair간의 거리가 모두 같게하면 loss가 0이되는 문제가 발생 

그래서 a를 추가해 같은 고객의 거리가 a 만큼 더 가까워야해! 를 추가해 준다.

위치간의 차이를 보는건 ok 근데 .. 3가지 위치를 동시에 보지는 못하네 … 차이값만 봐야하나?

### angular loss function

![f8](\img\2022\Siamese_Neural_Network\f8.png)

한 쪽을 optimize 하면서 다른 한 쪽의 적합한 거리가 보장받지 못하는 경우가 발생하였는데, 세 가지 데이터 포인트 간 거리를, 삼각형의 각(angle) 의 관점에서 보면서, negative data point 가 가지고 있는 내각에 조건을 주는 방식을 사용

anchor/positive/negative 세 데이터 포인트가 요구하는 거리 조건을 동시에 충족시키면서 모델을 최적화 할 수 있게 만듦

# 참고

- siamese network 설명

[https://blog.mathpresso.com/샴-네트워크를-이용한-이미지-검색기능-만들기-f2af4f9e312a](https://blog.mathpresso.com/%EC%83%B4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EA%B2%80%EC%83%89%EA%B8%B0%EB%8A%A5-%EB%A7%8C%EB%93%A4%EA%B8%B0-f2af4f9e312a)

[https://tyami.github.io/deep learning/Siamese-neural-networks/](https://tyami.github.io/deep%20learning/Siamese-neural-networks/)

- metric learning

[https://techy8855.tistory.com/18](https://techy8855.tistory.com/18)

[https://dongkyuk.github.io/study/metric-learning/](https://dongkyuk.github.io/study/metric-learning/)
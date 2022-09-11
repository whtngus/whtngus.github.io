---
layout: post
title: "few-shot learning"
date: 2022-09-11 16:20:23 +0900
category: datascience
---

# few-shot learning

Few shot learning이란, 말 그대로 “Few”한 데이터도 잘 분류할 수 있다는 것이다. 그런데, 헷갈리지 말아야 할 것은 “Few”한 데이터로 학습을 한다는 의미는 아니라는 것

기존 딥러닝은 고도의 데이터를 통해 테스크를 수행해야 함으로 많은 비용이 소모됨. 최근 몇 년간 데이터 의존성을 줄이기 위한 많은 연구가 진행됨

1. Domain Adaptation

2. Semi-supervised learning

3. self-supervised learning

4. Meta-learning(학습을 잘 하는 방법을 학습하는 것에 대한 연구)

   ![스크린샷 2022-09-01 오후 4.20.23](\img\2022\fewshot_learning\스크린샷 2022-09-01 오후 4.20.23.png)

   → Few-Shot Learning(적은 데이터만을 가지고 좋은 성능을 뽑아내기 위한 방법론들) - Meta Learning의 하위 분야 

![스크린샷 2022-09-01 오후 4.31.39](\img\2022\fewshot_learning\스크린샷 2022-09-01 오후 4.31.39.png)

그중 few shot learning을 공부해 보자 

few shot learning은 supervised learning(학습 시 사용한 클래스)를 바탕으로 Training Set 에 없는 클래스를 맞추는 문제이다.

![스크린샷 2022-09-01 오후 4.02.07](\img\2022\fewshot_learning\스크린샷 2022-09-01 오후 4.02.07.png)

### N-way, K-shot

일반적으로. few shot learning 은 k-way n-shot 이라는 표현을 씀 

| 명칭     | 설명               | 특징          |
| ------ | ---------------- | ----------- |
| N-way  | class 수          | 클수록 정확도 상승  |
| K-shot | class당 example 수 | 작을수록 정확도 상승 |

ex) 10-way few shot learning인 경우 랜덤의 정확도는 10%

# Few shot learning의 Siamese Network

![스크린샷 2022-09-01 오후 4.04.28](\img\2022\fewshot_learning\스크린샷 2022-09-01 오후 4.04.28.png)

siamese는 입력에 대한 hidden representation을 각각 구한 뒤 이 차이를 구하는 형식

거리 값이 아닌 layer 를 이용해 loss를 구하는 방법 도 있음 



# Siamese Neural Network

2005년 [Learning a Similarity Metric Discriminatively, with Application to Face Verification](http://yann.lecun.com/exdb/publis/pdf/chopra-05.pdf)라는 논문으로 Yann LeCun 교수 연구팀에 의해 발표

Siamese Network 는 (이하 샴 네트워크) 다루어야하는 클래스의 종류가 매우 많고, 특정 클래스에 대한 사진을 대량으로 구할 수 없을 때 머신러닝을 활용하여 그 클래스를 구분해내기 위하여 고안된 네트워크

![스크린샷 2022-09-06 오후 3.02.39](\img\2022\fewshot_learning\스크린샷 2022-09-06 오후 3.02.39.png)

축구공, 코끼리, 악어 3가지 클래스로 같은지 다른지를 모델을 학습 시키고 입력 feature를 이해해서 얼마 보지 못한 데이터 클래스를 예측

![스크린샷 2022-09-06 오후 3.04.43](\img\2022\fewshot_learning\스크린샷 2022-09-06 오후 3.04.43.png)

이러한 방법을 적용하는 모델중 하나가 샴 네트워크 이고 두 입력간의 feature를 합쳐서 사용하는 방법

기본적으로 샴 네트워크는 모델의 웨이트를 공유함

![스크린샷 2022-09-06 오후 3.45.11](\img\2022\fewshot_learning\스크린샷 2022-09-06 오후 3.45.11.png)

이렇게 정의된 네트워크에 두 사진이 같을 경우 유사도(Similarity)를 1로 주고, 두 사진이 다를 경우 유사도(similarity)를 0 으로 주어서 모델을 학습

![스크린샷 2022-09-06 오후 3.20.48](\img\2022\fewshot_learning\스크린샷 2022-09-06 오후 3.20.48.png)

이때 각 입력에서 나온 embedding vector를 이용해 classification, regression 등 다양하게 활용 가능

## vector 학습 만드는 방법

이것을 similarity learning 혹은 metric learning이라고 부름

![스크린샷 2022-09-06 오후 5.09.43](\img\2022\fewshot_learning\스크린샷 2022-09-06 오후 5.09.43.png)

### similarity learning or metric learning 방법

### contrastive loss function

![스크린샷 2022-09-06 오후 3.49.21](\img\2022\fewshot_learning\스크린샷 2022-09-06 오후 3.49.21.png)

Y = 0 같은 셈플인 경우 : 거리만큼 loss가 발생

Y = 1 다른 셈플인 경우 : 입력 파라미트 margin값 보다 작은 경우 loss가 발생

contrastive loss는 같은 데이터 다른 데이터 한 번씩 사용해 학 습 함으로 한번에 둘 다 학습시킬 수 있는 방법은 없을까?

### triplet loss function

![스크린샷 2022-09-06 오후 3.51.53](\img\2022\fewshot_learning\스크린샷 2022-09-06 오후 3.51.53.png)

데이터를 하나 가지고 와서(anchor) 기준으로 삼고, 같은 클래스(positive)에 데이터 하나 다른 클래스(negative)에 데이터 하나를 가지고 온 후,

(같은 클래스와의 거리) - (다른 클래스와의 거리) 만큼 손실이 발생

- 여기에서 중요한 포인트는 a(alpha)

a가 없다면 anchor-posirive, anchor-negative pair간의 거리가 모두 같게하면 loss가 0이되는 문제가 발생

그래서 a를 추가해 같은 고객의 거리가 a 만큼 더 가까워야해! 를 추가해 준다.

위치간의 차이를 보는건 ok 근데 .. 3가지 위치를 동시에 보지는 못하네 … 차이값만 봐야하나?

### angular loss function

![스크린샷 2022-09-06 오후 5.04.32](\img\2022\fewshot_learning\스크린샷 2022-09-06 오후 5.04.32.png)

한 쪽을 optimize 하면서 다른 한 쪽의 적합한 거리가 보장받지 못하는 경우가 발생하였는데, 세 가지 데이터 포인트 간 거리를, 삼각형의 각(angle) 의 관점에서 보면서, negative data point 가 가지고 있는 내각에 조건을 주는 방식을 사용

anchor/positive/negative 세 데이터 포인트가 요구하는 거리 조건을 동시에 충족시키면서 모델을 최적화 할 수 있게 만듦











# 참조

- few shot learning 개념 및 사진

[https://zzaebok.github.io/machine_learning/FSL/](https://zzaebok.github.io/machine_learning/FSL/)

[https://velog.io/@sjinu/Few-Shot-Learning](https://velog.io/@sjinu/Few-Shot-Learning)

- 나중에 확인해보기

[https://sebastianraschka.com/blog/2022/deep-learning-for-tabular-data.html](https://sebastianraschka.com/blog/2022/deep-learning-for-tabular-data.html)

[Siamese Neural Network](https://www.notion.so/Siamese-Neural-Network-a9664502196345b5b0890695f4ce5f5b)

[tabular data for deep learning](https://www.notion.so/tabular-data-for-deep-learning-98f5c99db7f747f78e1039691603a9f1)

- siamese network 설명

[https://blog.mathpresso.com/샴-네트워크를-이용한-이미지-검색기능-만들기-f2af4f9e312a](https://blog.mathpresso.com/%EC%83%B4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EA%B2%80%EC%83%89%EA%B8%B0%EB%8A%A5-%EB%A7%8C%EB%93%A4%EA%B8%B0-f2af4f9e312a)

<https://tyami.github.io/deep> learning/Siamese-neural-networks/

- metric learning

<https://techy8855.tistory.com/18>

<https://dongkyuk.github.io/study/metric-learning/>
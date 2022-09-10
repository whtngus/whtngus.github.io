---
layout: post
title: "paper : Switchable Novel Object Captioner"
date: 2022-08-31 01:01:01 +0900
category: paper
---

# Switchable Novel Object Captioner

Switchable Novel Object Captioner 2022

IEEE 2022

url : https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9693277



# Abstract

이미지 캡션은 학습 데이터셋으로 이미지를 입력을 받아 설명을 하는 caption을 생성하는 테스크

그러나 입력 데이터에서 새로운 도메인의 단어가 나오는 경우 이미지 캡션은 제대로 작동할 수 없어 새로운 데이터를 필요로 한다. 

해당 연구에서는 이를 해결하기 위해 데이터 셋을 새로 구축하는것이 아닌 zero-shot 기법을 제안함.

언어 생성을 훈련 개체에서 완전히 분리하는 방법을 학습하며, 새로운 개체를 설명하는 데 훈련 문장이 필요하지 않다.

3가지의 학습 데이터 셋을 사용함

# 1. INTRODUCTION

 최근 몇 년 동안 이미지 캡션 연구의 중추적인 연구 방향은 테스트 시간에만 발생하는 새로운 객체를 설명하기 위해 캡션 모델을 일반화하는 것

![f1](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f1.png)

위의 그림의 예시 처럼, 기존의 캡션 모델은 객체 "트럭"에 대한  캡션을 올바르게 생성할 수 있지만, 훈련 문장이 버스 단어를 포함하지 않는다는 이유만으로 유사한 객체 "버스"에 대해 실패

-> 즉 학습 데이터에 편향적으로만 캡션을 생성할 수 있음 

기존 연구에서는 이러한 문제를 해결하기 위해 외부 언어 지식(새로운 object 들)을 학습

그러나 이 데이터들을 결합 하는것도 한계점을 가지고 있음으로 해당 연구에서 zero-shot 기븝을 통해 아기들의 말하는 방식을 모방한 객체 캡션러(SNOC)라는 프레임워크를 제안

-> 새로운 객체에 대한 학습을 따로 하지 않는 방식

특수토큰 <PL>을 이용해 해당 객체 단어 키워드를 DNOC의 아디어를 기반으로 함 



해당 논문의 컨트리뷰선

- 이미지 캡션의 제로샷 소설 객체 캡션 작업을 소개한다. 
- 올바른 어순을 가진 문장을 생성하기 위해, 우리는 다음 세 가지 측면에서 노력을 기울였다. 
  1. 객체 단어를 어디에 배치해야 하는지 알아내기 위해 전환 가능한 LSTM을 설계한다. 
  2. 그런 다음 LSTM 숨겨진 상태에서 의미 정보를 가져와 인식된 모든 객체 메모리로부터 여기서 언급되어야 하는 시각적 객체를 찾는다. 
  3. 문장의 일관성을 보장하고 어휘 부족 문제를 완화하기 위해 프록시 시각적 단어를 설계하고 가져온 새로운 객체 레이블이 LSTM에 미치는 알려지지 않은 영향을 피한다.

-> 이렇게 보면 이해가 안가니 3번 챕터에서 다시 다루기로...



# 2. RELATED WORK

거의 생략...

#### 2.1 IMAGE CAPTIONING

#### 2.2  Novel Object Captioning

Novel object captioning은 훈련 중인 새로운 객체에 대한 쌍체 시각적 문장 데이터가 없는 어려운 작업 ->  즉 사진과 sentence 연결된 데이터가 없는 경우 

#### 2.3 Zero-shot Novel Object Captioning

 제로샷 학습은 외부 데이터 소스에 대한 개념 검출기 사전을 학습하여 시각적 의미론과 텍스트 의미론 간의 격차를 해소한다



# 4. THE PROPOSED METHOD

## 3.1 Preliminaries

```
I : 입력 이미지 
s : 입력 문장
N : 입력 문장 s의 각 단어 - 모두 유니크함
w : 각 단어의 represents
P : 이미지 문장 페어 {(I1,S1), ...}
xi = ϕw(wi) : ϕw()는 linear transformation
f : CNN을 통해 추출된 Feature 
M : 객체 메모리 object feautre-class pair
N(d) : 사진에서 예측한 object 수
o-th : O번째 객체 범주
```

- The Encoder

ILSVRC12 dataset을 16-layer VGG를 통해 학습된 모델을 사용

pre-trainined 모델

- The decoder

![f_1](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_1.png)

decoder 모델은 위 수식과 같이 입력 이미지의 represantation vector와 이전 단어들의 벡터값을 통해 다음 단어를 예측하는 방식으로 진행 

![f_2](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_2.png)

ot−1 of the model as the input xt at the t-th step ...

그냥 lstm. ....

- Zero-Shot Novel Object Captioning.

해당 연구에서 모델이 개체에 대한 추가 훈련 문장 데이터 없이 새로운 개체에 대한 캡션을 수행해야 하는 제로샷 신규 개체 캡션 작업을 연구

또한 중요한건  어휘 부족(OOV) 단어를 처리하는 것

## 3.2 Building the Key-Value Object Memory

각 object를 추출한 f를 통해서 예측된 클래스와 key-value pair 를 만들어 객체 메모리 M을 구축

![f_3](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_3.png)

처음보는 객체 테그가 나온 경우 feature-name pairs 쌍을 메모리에 다시 사용 

위 수식은 새로운 슬롯을 메모리에 등록하는 과정

- The proxy visual words

새로운 객체의 경우 어휘 부족 문제를 완화하기 위해  대리 단어를 대신 사용할 것을 제안

![f_4](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_4.png)
새로운 객체의 feature와 object의 feautre의 cosine 유사도를 통해 정의 

![f_5](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_5.png)

이를 통해 새로운 객체 범주 category를 찾아 적용하고 메모리에 추가로 삽입

## 3.3 Switchable LSTM

기존 지식과 외부 지식을 모두 활용해야 한다. 따라서 두 가지 지식 소스를 모두 활용할 수 있는 두 가지 작동 모드를 갖춘 전환 가능한 LSTM을 제안한다.

기존 LSTM 방식과 키 값 객체 메모리 M에서 명사를 검색하는 검색 모드 사이에서 전환을 수행 후 생성 모드에서는 표준 LSTM의 메모리 셀을 사용하여 기존 지식을 기반으로 문장을 생성

###  3.3.1 Standard LSTM Revisit

![f_6](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_6.png)

h caption hidden state는 시작시 <GO>의 special token으로 initilized 되며 하나씩 문장을 생성하기 시작 

### 3.3.2 Retrieving Nouns from External Knowledge

표준 LSTM 생성 시 외부 지식 정보를 고려하지 않고, 객체 메모리 M의 지식을 문장 생성에 통합하기 위해 attention-based방법을 사용 

![f_7](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_7.png)

Retrieving mode 라고 명명하고, 검색 모드에서는 숨겨진 상태 ht-1을 의미론적 쿼리로 사용하여 객체 메모리 M을 검색 후  t번째 시간 단계에서, 우리는 쿼리 qt를 이전의 숨겨진 상태 ht-1의 선형 변환으로 정의

![f_8](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_8.png)

위의 커리 q를 사용해 관련 객체 정보를 찾는 것을 목표로 객체 메모리 M에서 콘텐츠 기반 주소 지정 작업을 수행

K와 V는 각 메모리에 있는 모든 k v의 concatenate

### 3.3.3 Modes Switching

![f2](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f2.png)

우측 그림이 제안된 LSTM 인데 가장 아래부분의 KV Memory와 우측 아래의 Swich가 추가 됐다.

 t번째 단계의 스위치 표시기는 숨겨진 상태 ht-1을 기준으로 수행

![f_9](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_9.png)

w b는 학습 파라미터 

스위치는 현재 시간 단계에서 검색 모드를 선택할 확류을 추정하도록 설계 됨 

그 후 생성 모드의 예측과 비교

![f_10](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f_10.png)

a가 ptl보다 작으면 Generating 모드를 기반으로 단어를 예측 크면 Retriveving 모드로 고유 명사를 찾아 교체 (수식8번)

## 3.4 Framework Overview

새로운 당너의 존재에 관계 없이 모든 입력 토큰을 인코딩 할 수 있게 된다.  따라서 새로운 객체에 대한 문장을 생성할 수 있게 된다. 

1. 외부 객체 감지 모델을 사용하여 입력 이미지에 대한 키 값 객체 메모리 M을 구축. 어휘 부족 문제를 피하기 위해 보이지 않는 객체에 대해 가장 유사한 보이는 객체의 레이블을 프록시 시각적 단어로 사용
2. 전환 가능한 LSTM을 활용하여 캡션 문장을 생성한다. 이 모델은 내부 지식과 외부 지식을 모두 활용하기 위해 두 가지 작업 모드로 공동으로 작동한다. 메모리 셀 내부의 스위치 표시기는 두 모드를 제어하기 위해 사용된다. 검색 모드에서, 예측된 단어는 메모리 M의 소프트 콘텐츠 기반 어드레싱에 의해 생성된다. 
3. t의 자리 표시자를 교체 (그전에는 스페셜 토큰)

![f3](\whtngus.github.io\img\2022\Switchable_Novel_Object_Captioner\f3.png)

그림 3의 예시로 테니스 라켓이라는 객체가 기존에 없었다면, 메모리 M을 구성하고 유사한 후보를 찾아 교체한다 위의 예시에서는 가장 유사한 baseball bat 으로 교체함. 두 번째 단어 person의 경우 검색모드를 사용함(기존에 나왔던 객체 이기 때문에)

## 3.5 Training

연구에서는 학습시 모든 대상 객체를  교체 방식을 사용할 것을 권장함 

즉, 모든것을 새로운 객체로 간주

이러한 방식을 통해 처음보는 객체가 등장하는 경우에도 이미지 캡션을 생성 할 수 있도록 유도함



# 4 EXPERIMENTS

## 4.1 Datasets

##### The held-out MSCOCO dataset.

![t_1](\img\2022\Switchable_Novel_Object_Captioner\t_1.png)

데이터셋은 MSCOCO 데이터 세트를 사용

MSCOCO 데이터 세트는 8개의 MSCOCO 개체 중 적어도 하나를 포함하는 모든 이미지를 제외

 8개의 객체는 MSCOCO 탐지 챌린지의 모든 80개의 객체에 대해 word2vec 임베딩을 클러스터링하여 선택

최종 평가 대상인 "병", "버스", "카우치", "마이크로웨이브", "피자", "라켓", "가방", "제브라"의 8가지 새로운 객체가 만들어짐 

-> 테스트 분할에서만 사용

이미지 캡션에서 매우작은 물체의 경우 무시하게 됨, label 된 캡션에서도 작은 물체 혹은 뒤에있는 물체는 언급되지 않음

이러한 예는 해당 연구가  모델이 훈련에서 이러한 새로운 물체의 시각적 존재에 의존하지 않는다는 것

##### Scaling to the ImageNet dataset

MSCOCO 데이터 세트에 없는 646개의 개체를 포함하는 ImageNet의 동일한 하위 집합을 사용

##### The nocaps dataset.

nocaps 데이터 세트에는 Open Images 검증 및 테스트 세트에서 소스된 이미지가 포함

## 4.2 Experimental Settings

##### The Object Detection Model

공개적으로 사용 가능한 사전 훈련된 객체 감지 모델을 사용하여 키 값 객체 메모리를 구축

InceptionResNet-V2과 FasterR-CNN 모델을 사용하여 object detection의 상자와 점수를 생성 

##### Evaluation Metrics

Meteor과 F1 점수를 사용 

## 4.3 Comparison to the State-of-the-art Results
















---
layout: post
title: "paper : Towards Accurate Scene Text Recognition with Semantic Reasoning Networks"
date: 2021-05-21 19:20:23 +0900
category: book
---

# 논문 정보 

논문 명 : Towards Accurate Scene Text Recognition with Semantic Reasoning Networks

2020년 3월 27일 게재

Baidu Inc

url : https://arxiv.org/abs/2003.12294

git url : https://github.com/chenjun2hao/SRN.pytorch



# 1. Abstract and Introduction

OCR의 장면 텍스트인식은 몇년간 많은 향상을 이루었지만, 텍스트 인식을 지원하기 위한 의미적인 해석을 하는 연구는 RNN과 유사한 구조의 탐색만 사용되어 왔다. 

-> 즉, 트랜스포머 시대에? RNN말고 트랜스포머를 써보자 라고 해석 가능

위의 한계를 안화하기 위해  

1. 장변 텍스트 인식인 semantic reasoning network (SRN)
2. 사진의 문맥 이해를 위한 global semantic reasoning module (GSRM) 

위 두 가지 학습 모델로  semantic reasoning network (SRN) 프레임워크를  제안하고, 7가지 벤치마크 테스크에서 state-of-the-art를 달성함 

![example_image](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\example_image.PNG)

OCR에서도 텍스트는 많은 의미를 가지고 있으며 장면 텍스트 인식은 비전 기반 응용프로그램에서 중요한 단계이다. 위의 예시 사진에서 그냥 단어만을 인식한다면 "HOUSE"의 "S"는 글자를 알아볼 수 없어 예측이 불가능하다. 하지만 의미적인 컨텍스트를 이해한다면 "S"를 유추할 수 있다.

또한 이러한 문맥 정보를 기존 RNN 방식으로 해결한다면 런타임 시간, 롱 텍스트 디펜던시, 그리고 RNN구조상 한번의 잘못된 디코딩으로 연속된 잘못된 정보를 축혀갛는 문제들이 발생하게 된다.

![rnn_transformer](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\rnn_transformer.PNG)

위 그림은 트랜스포머는 연속으로 잘못된 정보를 전달하지 않는다.  정도로 이해하고 넘어가자

-> 해당 논문에서는 GSRM, PVAM등 트랜스포머를 사용 하는 방식을 적용하여 sota를 찍음

# 2. Related Work

해당 논문에서는 OCR의 semantic context-free 와 semantic context-aware로 나누어서 정리를 함.

-  semantic context-free

> 의미론적인 정보를 명시적으로 사용하지 않고 장면 텍스트 인식을 순수하게 분류로만 사용
>
> 예시로 CRNN(CNN + RNN 과 CTC decoder, ACE 사용), FCN을 사용해 각 위치의 문자범주를 필셀단위로 분류
>
> 해당 연구는 불규칙한 텍스트에 대해 효과적인 특징을 추출하는 방법에 초점을 맞춰서 연구가 되고 있음
>
> -> 노이즈 처리(원근, 왜곡,  분포 곡면성 등)

- Context modeling structures

> 특정 시간범위 공간범위의 정보를 캡처하도록 설계됨
>
> 기존에는 ByteNet, ConvS2S등 CNN을 인코더로 사용  -> 글로벌 관계를 유추하기에는 어려움이 있음 (입력 필드의 한계점)
>
> -> 트랜스포머가 이러한 문제에 대해 효과적임을 많은 연구논문에서 검증함  *(SRN 논문에서 트랜스포머를 채용하는 이유)*



# 3. Approach

![SRN](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\SRN.PNG)

4가지 부분으로 구성된 모델

백본 네트워크에서 2D V를 추출하고, PVAM은 각 기능에 해당하는 G를 생성 해서 텍스트의 오류와 정렬된 시각적 정보를 캡처

N개의 병렬 1-D 를 GSRM에공급하여 의미정보인 S를 얻고 VSFD에 의해 융합되어 N자를 예측 

N의 남은 부분 패딩은 'EOS' 토큰을 사용



### 3.1 Backbone Network



















# 참고

- FPN(Feature Pyramid Network)

> 1. Featurized Image Pyramid
>
> 각 라벨에서 독립적으로 특징을 추출하여객체를 탐지하는 방법 
>
> 연산량과 시간 관점에서 비효율적, 적용하기 어려운 담점 있음
>
> 2. Single Featur Map
>
> Conv layer를 이용해서 특징을 압축하는 방식
>
> 멀티 스케일을 사용하지 않기 때문에 성능이 떨어지는 단점 발생
>
> 3. Pyramidal Feature Hierarchy
>
> 서로 다른 특징 맵을 이용해 멀티 스케일 특징을 추출하는 방식
>
> 각 레벨에서 독립적으로 특징을 추출하여 객체를 탐지
>
> 4. Feature Pyramid network
>
> Top-down 바잇ㄱ으로 특징울 추출
>
> 각 추출된 결과들인 low-resolution 및 high-resolution 들을 묶는 방식
>
> 

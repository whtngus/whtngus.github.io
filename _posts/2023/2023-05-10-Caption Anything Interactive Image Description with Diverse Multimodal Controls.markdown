---
layout: post
title: "Caption Anything: Interactive Image Description with Diverse Multimodal Controls"
date: 2023-05-11 00:05:23 +0900
category: paper
---

# Caption Anything: Interactive Image Description with Diverse Multimodal Controls

tencent 

2023년 3월 4일 공개

url : https://arxiv.org/pdf/2305.02677v1.pdf

code url : https://github.com/ttengwang/caption-anything

  -> pytorch colab등 정리 잘 돼있는듯 

# Abstract

최근 멀티모달 에서 Controllable image키워드가 많이 언급되고 있음

sota 모델은 이미지-텍스트 페어 데이터를 학습해 캡션을 생성함 그러나 이런 캡션 데이터는 모델의 유용성과 확장성을 크게 제안함 

이를 해결하기 위해 다른 광범위한 데이터가 필요함 

논문에서 제안하는 Caption AnyThing (CAT)를 통해 아래와 같은 내용을 해결하고자 함

1. visual control

점 박스 궤도등 시각적인 컨트롤

2. language control

감정, 길이, 언어, 사실성등을 컨트롤

vision, language 두 개의 다른 조정을 지원해 유연하게 사용 가능하다고 함 

caption 생성을 컨트롤 한다는 의미로 보임 

-> 무슨 말인지 아래서 확인해보자 

# 1 Introduction

![f_2](F:\code\whtngus.github.io\img\2023\Caption Anything Interactive Image Description with Diverse Multimodal Controls\f_2.PNG)

vanilla 이미지 캡션의 특징은 이미지의 가장 중요한 특지점을 잡아 캡션을 생성하는것

그러나 image caption task에서 실용적인 텍스트를 생성하는게 필요함

기존 모델의 caption은 지나치게 간결하거나 너무 복잡한 문장을 생성하고  사용자가 캡션 생성하는걸 조정할 수 있어야함 

![f_1](F:\code\whtngus.github.io\img\2023\Caption Anything Interactive Image Description with Diverse Multimodal Controls\f_1.PNG)

연구에서 제안하는 모델은  일관성 있는 캡션 생성과 사용자는 object중 원하는 객체를 선택해 캡션을 생성할 수 있다.

거기에 OCR, VQA 테스크 지원 

# 2 Related Work

- Image Captioning and Dense Captioning

이미지에서 일반적인 캡션을 생성하는 테스크 

주로 인코더와 디코더 영역이 있는 모델을 통해 해결함 

하지만 기존 모델은 이미지에서 일반적인 설명이나 중요한 특징들을 설명하는데에만 집중함 

또, 사용자의 의도에 맞는 캡션을 생성하지 못함 

- Controllable Image Captioning

object detection 결과를 이용해 사용자의 의도에 맞는 캡션을 생성하는것을 목표로한 연구

혹은 text 의 스타일을 유연하게 생성하는 연구 가 있음 

- Interactive Image Segmentation.

유저의 의도를 반영한 멀티모달 테스크

# 3 Caption Anything

![f_3](F:\code\whtngus.github.io\img\2023\Caption Anything Interactive Image Description with Diverse Multimodal Controls\f_3.PNG)

사용자와 상호작용을 통한 caption을 생성하기 위해 model augmentation strategy을 제안함

위의 Figure3에서 처럼  {segmenter, captioner, text refiner} 3개의 테스크를 수행

segmenter는 픽셀 단위로 마스킹된 (points, boxes, trajectory) 를 예측

-> 이렇게 되면 이미지의 지역기반의 캡션을 새성하게 됨

captioner는 mask가 씌어진 오리지널 이미지에서 캡션을 생성

 -> 유저가 선택한 객체에 집중하게 됨

text refiner는  생성된 캡션을 사용자의 조절에 의해 다시 정제함 

- Segmenter

이미지를 분할해서 컨트롤 하고자 함 

SA-1B dataset을 통해 pre training 진행 (1 billion 마스크가 있는 11M image segmentation 데이터셋 ) 

- Captioner

유저에 따른 캡션을 생성하기 위해 강력한 zero-shot captioning 이 필요 

various novel objects와 다른 이미지의 분포에 대한 묘사가 필요

BLIP2를 사용함 (이미지 encdoder를 frezen 시키는 방식)

- Text Refiner

 ChatGPT API를 사용하여 정제함

- Visual Chain-of-Thought.

실험적으로 image caption은 background information에 따라 쉽게 영향을 받음을 찾음 

chain-of-thought를 따라 만듬 

관심있는 객체에를 기준으로 자른 백그라운드를 prmpt에 넣어 prompt 를 진행 

- Extension to Object-Centric Chatting

위의 그림3의 우측을 보면 원하는 객체를 물어보고 그다음 객체를 이용한 다음질문을 만들어서 캡션을 생성함

-> (사용자 선택)지역 기반의 캡션을 새성하게 됨

=> 이미지 캡션 모델이 최근에 ChatGPT를 사용하는 방식이 많음 ...

- Extension to Paragraph Captioning.

 CAT 파이프라인으로 각 개체에 캡션을 지정하여 조밀한 캡션들을 생성

-> 생성한 캡션을 합칠때 텍스트 식별을 위해 EasyOCR를 이용

# 4 Experiments



![f_4](F:\code\whtngus.github.io\img\2023\Caption Anything Interactive Image Description with Diverse Multimodal Controls\f_4.PNG)



# 참고

- chain-of-thought 

문제의 인과 관계에 대해서 차근차근 풀어서 전개하다 보면, 정답에 더 잘 도달할 수 있다는 개념

‘문제-답’ 대신에 ‘문제-풀이-답’ 형태로 프롬프트를 구성하는것.




---
layout: post
title: "Prismer: A Vision-Language Model with An Ensemble of Experts"
date: 2023-05-03 00:05:23 +0900
category: paper
---

# Prismer: A Vision-Language Model with An Ensemble of Experts

2023년 3월 4일 게재 
NVIDIA

code : https://github.com/NVlabs/prismer
paper : https://arxiv.org/abs/2303.02506



# Abstract

최근 멀티보달 기반의 좋은 성능의 알고리즘들이 많이 나오고 있음 

그러나 정현적으로 많은 학습 데이터를 필요로 함 

논문에서 제안하는 Prismer는 data와 parameter를 효율적으로 사용해 VLM 을 학습 

-> 쉽게 구할 수 있는 데이터와 frozen을 통한 학습을 진행

# 1 Introduction

최근 VLM 모델은 많은 데이터와 큰 모델을 피룡로 하고 yottaFLOP(10^24) scale 정도임 

![f_1](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\f_1.PNG)

Primer는 여러 테스크를 general하게 하는게 아닌 각각의 task를 독립적으로 학습시킴 

- 논문의 컨트리뷰션

> 1. 강력한 Vison-only 그리고 Language-only 모델 
>
> web-scale 지식 네트워크 구조를 기반
>
> 2. task 별 muliple type encoding 진행
>
> -> frozen시키고 상위 레이어를 통해 embedding vector로 classification 하는듯
>
> frozne 했기 때문에 lightweight 모델

13M의 공공 image/alt-text 데이터로 사용

# 2 Related Work

- Vision-Language Models (VLMs) 

transformers 모델이 나오면서 해당 테스크를 정복하기 시작함 

- Multi-task and Auxiliary Learning

하나의 입력에서 multiple modalities를 목적으로 학습함 

ex) emantic segmentation, object detection, and depth estimation)

-> 그러나 이렇게 한습하면 multi-task 에 대한 지도학습 (각 테스크에만) 집중함

Prismer 는 이를 해결하고자 함 

- Unifying Pre-trained Experts 

여러 multi-modal pre-trining을 이용해 다른 pre-training모델을을 이용하는 방법 



MoE와 "Ensemble of Experts"(논문에서 정의) 의 차이점을 분석



# 3 Prismer: Open-ended Reasoning with Multi-modal Knowledge

Vision-language generative model인 primer 모델 소개

## 3.1 Model Overview

![f_2](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\f_2.PNG)

모델은 Figure 2와 같이 설계됨 

transformer로 구성된 encoder - decoder 모델

Vision encoder는 RGB이미지와 multi-modal label을 입력받아 같이 학습함 (e.g. depth, surface normal, segmentation labels, predicted from the frozen pre-trained experts) 그리고 output으로 multi-modal feature를 출력

-> 도메인에 최적화 하기 위해 Expert Resampler를 도입

예를들어 Depth Parchify 테스크 뿐만아니라 그림에서 글자를 인식하는것도 필요하다면 저기에 OCR 모델의 결과를 추가해서 넣으면 됨 

각 task 별 모델의 결과를 결합해 종합적으로 쓰겠다는 뜻 (원본사진 + 각 task 모델 결합)



여러 모델을 잘 결합하기 위해 Expert Resampler와 Adaptor를 추가함 

Expert Resampler는 다양한 멀티모달 테스크의 결과값을 결합시키는데 사용 

Adaptor는 transformer레이어로구성되어 여러 테스크에 적용시킴

## 3.2 Pre-trained Experts

- Backbone Experts

각 트랜스포머 기반의 Vision과 Language 만을 학습한 유사한 모델 (single domain)을 사용 

-> 학습시에는 frozen 시킴

- Modaiity Experts

task-specific 한 모델 

Primer는 비전에서 6가지의 전문가 모델을 사용 

그리고 블랙박스를 예측하는 object labels, segmentation labels, text labels 모델을 학습

## 3.3 Key Architectural Components

- Modality-Specific Convolutional Stem

![t_1](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\t_1.PNG)

3*3 커널 사이즈즈의 5개의 conv layer를 사용함

- Experts Resampler

![f_3](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\f_3.PNG)

여러 다운스트림 테스크들의 input과 label을 합칠 방법 필요

multi-modal features를 attention을 통해 resample 하지만 엄청난 메모리를 차지함 

- Lightweight Adaptor

Figure 3의 Adaptor를 보면 down projection, up projection 총 두변의 layer만 사용해 training free 라고함

-> 이해를 잘못한거같은데 왜 free?

그후 cross attention bloc와 결합됨 

## 3.4 Training Objective

다음 토큰을 예측하는 방식으로 single object를 쉽게 학습 가능 

-> multi-modal language generation을 목적으로 하기 때문에 multi-modal label들을 수집해 multiple objectives 데이터를 학습함



# 4 Experiments

## 4.1 Prismer Model Variants

논문에서는 PrismerZ모델로 정의하며 Prismer과 유사한 백본을 가지고 있다고함

![t_2](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\t_2.PNG)

실험에 사용된 모델은 2개이며 base 와 large모델을 사용하고 비교대상은 이전 모델인 Primer와 비교

## 4.2 Training and Evaluation Details

- Pre-training Datasets

coco, Visual genome, conceptual Captions, SBU caption, Conceptual 12M 을 사용 

11M의 web dataset 사용 



총 12.7 image-text쌍의 unique한 이미지를 수집해 학습에 활용

- Optimisation and Implementation 

AdamW optimiser를 사용 

weight decay =0.05



학습 시  

1. 효울적인 학습을 위해 ZeRO Stage 2 technique 사용
2. Automatic Mixed Precision(AMP)

1번 2번 둘 다 학습을 효율적으로 하기 위한 기술 1번은 분산학습 최적화 2번은 양자화

- Evaluation Setting 

VQAv2 dataset 을 사용 

평가 시 beam search size 3을 사용함



## Results on Vision-Language Benchmarks

![t_3](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\t_3.PNG)

primzer z 스코어가 평균적으로 낮음 (파라미터 수가 낮은걸 감안하면 어느정도 비교되는 수준인듯)

![t_4](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\t_4.PNG)

가장 위의 keyboard가 살짝만 보이거나 거의안보이는데 언급하거나 답변이 짧은걸 봐서 특정 객체에 많이 의존적인걸로 보임



.. 나머지 생략...



#6 Conclusions, Limitations and Discussion

- Multi-modal In-context Learning

최근 large model과 나오면서 많이 나오는 키워드

크지 않은 모델에서 접근하기 위해 본 연구에서 작은 모델을 제안 (기존 모델에 비해)

- Zero-shot Adaptation on New Experts

pre-training에서 학습하지 않은 segmentation을 inference 해봄 

-> 이때 좋지 않은 결과가 나옴 

- Free-form Inference on Partial Experts

당연하게도 exprts 수가 줄어들 수록 스코어가 줄어듬 

- Representation of Expert Knowledge

expert labels을 이미지와 같은 3 demention tensor로 전환시킴

-> 전환하는 방법에 더 효율적인 방법들이 있고 이걸 연구하면 더 안정적이고 강력함을 보여 더 연구가 필요함 







# 참고

- ALt Text

대체 텍스트는 alternative text의 축약

사진이나 동영상을 인공지능을 이용하여 분석한 뒤, caption을 생성한 데이터

- Mixture of Experts (MoE)

참고 : https://chickencat-jjanga.tistory.com/5![moe_2](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\moe_2.PNG)

![moe](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\moe.PNG)

복잡한 문제를 단순화해 합쳐서 산출하는 방식의 아이디어 

g(x)는 softmax  (i번째 export를 몇%나 믿을지)

f(x)는 export network의 output

- squared ReLU

![squared_relu](\img\2023\Prismer A Vision-Language Model with An Ensemble of Experts\squared_relu.PNG)

Primer: Searching for Efficient Transformers for Language Modeling에서 제시한 방법으로 (결국 자기내꺼) 

위 그림처럼 생김

- ZeRO Stage 2 

참고 : https://velog.io/@seoyeon96/%EB%A6%AC%EC%84%9C%EC%B9%98-%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8-%EB%B6%84%EC%82%B0-%ED%95%99%EC%8A%B5%EC%9D%84-%EC%9C%84%ED%95%9C-DeepSpeed-ZeRO

ZeRO는 분산 학습 과정에서의 불필요한 메모리의 중복을 제거하여 같은 환경 내에서 대용량의 모델을 학습을 가능하도록록 도와줌

- **Stage 1. Optimizer State Partitioning**(Pos) - 메모리 4배 감소
- **Stage 2. Add Gradient Partitioning**(Pos+g) - 메모리 8배 감소
- **Stage 3. Add Parameter Partitioning**(Pos+g+p) - GPU의 개수와 메모리 감소 정도는 비례.(예를 들어, 64개의 GPU를 사용한다면 메모리 64배 감소)

V100 1000개로 stage2학습시 2000억 개의 파라미터도 학습 가능하다고 함

(gpu 수와 파라미터 수 둘다 높다....)

- AMP(Automatic Mixed Precision)

참고 : https://cvml.tistory.com/8

처리 속도를 높이기 위한 FP16(16bit floating point)연산과 정확도 유지를 위한 FP32 연산을 섞어 학습하는 방법

Tensor Core를 활용한 FP16연산을 이용하면 FP32연산 대비 절반의 메모리 사용량과 8배의 연산 처리량 & 2배의 메모리 처리량 효과가 있다

배치크기 2배로 증가해도 속도가 2.5~3배정도 증가한다고함 
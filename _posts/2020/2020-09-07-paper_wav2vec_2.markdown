---
layout: post
title: "wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations"
date: 2020-09-06 19:20:23 +0900
category: paper
---



# wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations



paper : https://arxiv.org/pdf/2006.11477.pdf

code : https://github.com/pytorch/fairseq

## abstract

Transformer basd model



- wav2vec 2.0의 특징

> 1. 발화 representation vector를 생성 
>
> 2. fine-tuning 시에만 음성-텍스트 합쳐진 데이터 필요
>
> > pre-train 시에는 음성파일만 있으면 가능
>
> 3. 음성 데이터를 양자화 시킴으로써 latent representation을 생성
>
> > 100시 간 가량의 Librispeech 파일을 사용해 음성인식 sota를 기록
> >
> > - 기록 
> >
> > 53k hours 의 라벨이 안된 데이터로 pre-train을 한것으로5.7/10.1 WER 기록
> >
> > 100 시간의 라벨링 된 데이터로 fine-tuning 후 1.9/3.5 WER을 기록
> >
> > 



- WER(word error rate) 

```
음성 인식 또는 기계 번역 시스템의 성능에 대한 측정 방식
WER = (I + D + S) / N  * 100%
삽입(I) : 잘못 추가된 단어
삭제(D) : 감지되지 않은 단어
대체(S) : 대체 된 단어
```



## Introduction

이전 음성인식 혹은 음성에 대한 모델은 많은 라벨이 있는(음성-텍스트)데이터를 필요로 한지만 wav2vec 2.0에서는 라벨링 되지 않은 데이터를 이용하여 pre training을 진행하고, 적은 양의 데이터를 통해서 STT 가 가능하다.



![model](img\paper\wav2vec_2\model.JPG)

CNN모델을 통해 음성을 양자화 시키고 이를 잠재 음성 표현 백터로 생성.

gumbel softmax 를 통해 latent representations 을 생성하고

CTC loss를 이용하여 fine-tuned 된다.



- gumbel softmax

```
랜덤 구성 요소를 샘플링 하는것은 미분을 할수가 없기 때문에 gumbel softmax트릭을 이용하여 해결한다.

- 정리 하기
```

- ctc(Connectionist Temporal Classification)

```
학습데이터에 클래스 라벨만 순서대로 있고 각 클래스의 위치는 어디있는지 모르는 unsegmented 시퀀스 데이터의 학습을 위한 알고리즘

- 정리 하기 
```



## model

f : x -> z

audio를  넣으면 다중 cnn lyaer에 의해 Z의 latent speech represantation vecot를 생성

 g : Z -> C

Z를 트랜스 포머를 이용하여 representation c를 생성한다. 



- Feature encoder

CNN의 여러 블록으로 구성됨  그리고 그룹 정규화를 한 후 GELU 활성화 함수를 사용

첫 오디오 블럭은 원시 오디오의 representation하기 위해 사용

 견고성을 올리기 위해 사용.

- Contextualized representations with Transformers.

트랜스포머 모델의 position embedding을 사용하는 대신 커널이 있는 컨벌루션 계층을 사용한 위치 임베딩을 사용

cnn의 output에 GELU 를 추가하여 사용한다.

- Quantization module.

음성 데이터를 CNN레이어를 통해 양자화를 한다.

이때, Gumbel softmax를 통해 개별 부호화를 할 수 있음.

CNN레이어를 통해 나온 Z는 G*V 로 매칭된다(G : gumbel softmax operations 설정 값, v - 부호화)

![formula_1](\img\paper\wav2vec_2\formula_1.JPG)

 t는 음이아닌 값이고,  n = − log(− log(u)) 이다. u는  0~1사이로 정규화된 값(학습시 x 출력값 사용)

역방향 학습시에는 gumbel softmax output을 사용하고, 학습하지 않는 forword 인 경우 u를 사용



## training

mask 의 경우  BERT와 완벽히 같은 방식과 비율을 사용하여 학습.



1. Masking

> 학습 벡터로 변형되기 전에 인코더의 출력의 일부와 시간의 일부를 마스킹한다.
>
> -> cnn의 아웃풋 or 입력 음성의 특정시간만큼 전체 마스크
>
> 전체 음성에서 p = 0.065 의 시간만큼 making한다.  그 부분으로 부터 M= 10 의 연속된 타임만큼 마스킹한다.
>
> ->299ms가 마스킹 된다.

2. Objective

> 사전학습 시에는 representation을 위해 masked 모델을 사용한다. 
>
> ![formula_2](\img\paper\wav2vec_2\formula_2.JPG)
>
> Lm은 mask task
>
> Lf 는 L2 wjdrbghk
>
> Ld 는 codebook
>
> 알파와 베타는 하이퍼파라미터 이다.
>
> 1. Contractive Loss
>
> 마스킹된 오디오를 중심으로 ct가 주어지면 양자화된 표현 Qt를 식별해야 한다.
>
> ![formula_3](\img\paper\wav2vec_2\formula_3.JPG)
>
> sim(a,b) = a^t b  /  |a| |b|
>
> 2. Diversity Loss
>
> 다양한 codebook 표현의 사용을 증가시키기 위한 loss
>
> softmax의 분포



- codebook

```
부호화를 위해 미리 정해지는 코드 벡터(복원 벡터)를 모안호은 색인화된 집합체
충분히 큰 개수의 다양한 패턴들을 패턴화시켜, 이들을 색인화시킨 코드 벡터들의 집약체
```





# 참고

- WER

https://en.wikipedia.org/wiki/Word_error_rate

- gumbel softmax

https://data-newbie.tistory.com/263

https://www.youtube.com/watch?v=ty3SciyoIyk

- ctc

[https://hulk89.github.io/machine%20learning/2018/01/30/ctc/](https://hulk89.github.io/machine learning/2018/01/30/ctc/)
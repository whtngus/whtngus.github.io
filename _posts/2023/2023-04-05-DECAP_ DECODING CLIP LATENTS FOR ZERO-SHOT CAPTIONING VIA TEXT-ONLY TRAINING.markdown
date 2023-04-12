---
layout: post
title: "DECAP: DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING"
date: 2023-04-05 00:05:23 +0900
category: paper
---

# DECAP: DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING

2023년 3월 6일 ICLR 게재

ByteDance 회사

paper : https://arxiv.org/abs/2303.03032

code : https://github.com/dhg-wei/DeCap



# ABSTRACT

CLIP(Large-scale pre-trained multi-modal models)는 강력한 zero-shot 분류, 생성등의 능력을 보여줌

하지만 large languagemodel은 분번별력 있는 설명을 만들지 못함

이를 해결하기 위해 lightweight의 DeCap 프레임워크를 제안

DeCap 프레임워크 특징

> - text 캡셧 데이터 쌍으로만 학습 
> - text only데이터 학습시 end-to-end 학습이 필요하지 않음

image와text 멀티모달 테스크시 데이터의 형식이 다른 이슈를 해결하기 위해 contrastive model을 주로 사용함

(같은 임베딩 공간에 배치)

-> 연구에서 이런 형식이 다른 이슈(modality gap)을 줄일 수 있는 방법을 제안



# 1 INTRODUCTION

Image Captioning의 목표는 이미지를 자동으로 설명하는것!

일반적으로 사람이 이미지를보고 설명한 데이터 셋을 가지고 학습하지만, 해당 데이터는 많지 않다는 문제를 가지고 있다.

-> 해당 연구에서는 text 데이터만을 사용함으로 이런 의존성을 줄임

또한 대규모 모델인 GPT, CLIP등이 있지만 모델이 크기 때문에 Infernece가 느린 단점이 있음

연구에서는 이러한 문제점을 해결하기 위해 

DeCap 모델인  zero-shot captioning를 제안

논문의 메인 컨트리뷰션

> 1. Zero Shot base 모델인 DeCap 프레임 워크를 제안
>
> 이 모델인 CLIP를 포함하고 있음
>
> (임베딩 영역 스페이스와 decoder를 가져와서 사용)
>
> 2. training-free projection mechanism 제안
>
> 이 방법은 vision text 의 CLIP에서 modality gap을 줄일 수 있음
>
> 또한 많은 메모리를 사용하지 않음
>
> 3. 여러 실험 케이스 설명
>
>  MSCOCO and NoCaps. 를 이용해 밴치마크 하고 
>
> MSCOCO and Flickr30k 데이터셋 에서 학습(Caption data인 Text 만 사용함)
>
> MSR-VTT and ActivityNet-Captions 과 비교해 SOTA 스코어 달성



# 2. RELATED WORK

#### CLIP in Captioning.

![f_1](\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\f_1.PNG)

Vision-Language 모델로 contrastive loss를 사용 

-> 하지만 바로 generatino하기 때문에 프리 트레이닝 모델에 text decoder가 없음

해당 논문에서 제시하는 모델로 Text Incoder를 만들고 training free 메커티즘을 만듦

#### Zero-shot Captioning

Zero-shot Captioning은 사람의 도움 없이 이미지, 비디오의 캡션을 생성하는걸 목표로함

fine tuning 없이 프리트레이닝 모델로만 캡션을 생성

#### Text Reconstruction

pair 텍스트와 unpair 텍스트를구분하는 테스크



# 3. METHOD

위의 Fiugre 1이 해당 연구에서 제안하는 프레임워크

## 3.1 TEXT-ONLY DECODER PRE-TRAINING

기존에는 zero-shot 캡셔닝을 위한 PLM (Pretraining Language Model) 을 사용

-> 그러나 PLM은 웹공간의 다양한 이미지를 학습하여 caption된 좋은 데이터가 없어 이미지 캡셔닝 테스크에 적합하지 않음

![fm](\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\fm.PNG)

> t : 문장  t = {word1, word2 , .... , wordt}
>
> Pθ : lanuage model - prefix로 프리징 시킴
>
> Etext(·) : CLIP 인코더의 L2-normalized embedding space

그냥 이전 문장을보고 다음 단어의 representation의 평균값? 인듯

-> 텍스트 임베딩을 이미지  임베딩에 최적화 시킴

## 3.2 INFERENCE STRATEGIES

위의 3.1을 통해 TEXT embedding 을 이용한 캡셔닝 생성 decoder 를 만듦

여기에서는 question을 이용해 어떻게 캡션을 생성하는지가 관건

### 3.2.1 PROJECTION-BASED DECODING (PD)

![fm_2](\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\fm_2.PNG)

> M : {m1, m2, ..., mN}  임베딩 스페이스
>
> mi : E_{text}(ti)  -> 즉 단어 t에 대한 임베딩
>
> v :E_{image}(I)
>
> τ : 하이퍼 파라미터 
>
> wi : 텍스트에 대한 가중치
>
> v_{proj} : 이미지와 텍스트를 조합한 임베딩 
>
> 텍스트와 이미지 임베딩인 m과 v의 코사인 유사도 

이미지 임베딩과 가장 가까운 softmax 를 사용 

![fm_s_2](\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\fm_s_2.PNG)

v_proj = projected vector -> auto-regressive 

###  3.2.2 DISCUSSION

inference 비교를 통해 decoder 부분의 projection 영역에 대한 영향도를 조사함 

1. CLIPRe

간단한 retrieval-based로 decoder가 필요없는 방법을 고민

이미지 I 와 text set T = {t1, ... tn}이 주어지면 CLIP를 통해 이미지와 텍스트의 유사도를평가하는 방법으로 사용

-> arg max t∈Tsim(Eimage(I), Etext(t)),  코사인 유사도 

이걸 베이스라인으로 사용

2. Visaul Decoding (VD)

텍스트 임베딩과, 이미지 임베딩의 상관관계를 분석 -> Visual Decoding이라 명칭

-> Pθ(Eimage(I))

그러나 실험 결과가 좋지 못함 

이미지와 텍스트 임베딩 간의 gap 큼 

3. Nearest-neighbor Decoding (NDD)

 nearest text embedding 방법을 사용

1) 이미지 임베딩인 Eimage(I)과 텍스트 임베딩 M의 유사도를 검사

2) nearest text embedding을 통해 가장 가까운 임베딩을 적용 

이를 Nearest-neighbor Decoding으로 정의

-> Pθ(arg maxm∈M sim(Eimage(I), m))

위 결과는 1번인 CLIPRe와 비슷한 스코어가 나옴 



# 4. EXPERIMENTS

다양하게 수집덴 corpora에서 zero-shot image captino을 수행 

## 4.1 ZERO-SHOT IMAGE CAPTIONING

전통적인 image captioning 방법은 이미지와 사람이 레이블링한 캡션 세트로 학습 

이러한 방법은 다양한 크기와 여러 텍스트를 학습할 수 없다는 단점이 있음

이를 해결하기 위해 연구에서 3가지 방법을 제안

![t_1](\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\t_1.PNG)

1. CC3M 

300만개의 인터넷 이미지에 대한 설명셋을 가지고 있음  (CC3M-text)

랜덤 셈플을 통해 100만개만 학습

2. SS1M

MSCOCO caption

978.662 문장과 2,322,628개의 수집된 이미지

3. BookCorpus

무료 소설책을 수집한 코퍼스 6,217,799개의 문장

## 4.2 UNPAIRED IMAGE CAPTIONING

![T_2](\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\T_2.PNG)

연결되지 않은 이미지와 켑셧 셋에서의 평가 

-> 대신 트레이닝 테스트셋이 같음, 학습데이터는 unpaired로 

## 4.3 VIDEO CAPTIONING

![t_4](\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\t_4.PNG)

msr-vtt, Activity0captions, VATEX(테스트셋 5182 raw test videos out of 6000) 데이터셋 에서 평가

-> VATEX에서 일부 데이터만 사용한건 영상을 일부 사용할수 없어서 라고함

1. Generic corpus

book corpus 로 학습함

2. Image captions

MSCOCO 데이터와 CC3M 데이터로 학습

3. Video captions

비디오 학습 셋에서 text를 수집해 학습 



Table4를 보니 비디오 데이터보다 CC3M이나 COCO가 더 정확도가 높음 

![f_2](\img\2023\DECAP DECODING CLIP LATENTS FOR ZERO-SHOT CAPTIONING VIA TEXT-ONLY TRAINING\f_2.PNG)

데이터와 메모리 크기에 따른 CIDEr 스코어 비교

# 5. CONCLUSION

lightweight VISUAL-AWARE 모델을 제안

training-free 방법론 제안.











# 참고

- CLIP

Learning Transferable Visual Models From Natural Language Supervision논문으로

인터넷에서 얻은 대규모 데이터셋을 이용, 이미지와 연관된 caption으로 사전학습

자연어 지시문을 주면 zero-shot으로 모델에 적용 가능(pre train으로 여러 down-stream task 적용 가능)

- web scale

아마존, 구글, 페이스북 등 대형 클라우드 서비스 제공업체들의 클라우드 운영 방식을 일컫는다
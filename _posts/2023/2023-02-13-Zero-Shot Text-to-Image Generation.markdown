---
layout: post
title: "Zero-Shot Text-to-Image Generation"
date: 2023-02-10 01:20:23 +0900
category: datascience
---

# Zero-Shot Text-to-Image Generation

DALL-E

2021년 2월 24일 최초 arxiv

OpenAI 에서 연구됨

- paper  url

[Zero-Shot Text-to-Image Generation](https://arxiv.org/abs/2102.12092)

- 사용 사이트

[openai.com/blog/dall-e](http://openai.com/blog/dall-e)

- github

<https://github.com/openai/dall-e>

- 관련 대표 기사

<https://www.aitimes.com/news/articleView.html?idxno=146393>

![f1](\img\2023\Zero-Shot_Text-to-Image_Generation\f1.jpg)

![f1](\img\2023\Zero-Shot_Text-to-Image_Generation\f2.jpg)

# Abstract

Text-to-image 생성은 이미지와 텍스트 쌍의 고정된 학습 데이터를 이용해 학습하는 방식을 사용하고 이를 추론하기 위해 복잡한 구조의 auxiliary losses 등의 방식을 사용함

또한 정보량은 국한된 데이터셋에 있어 정보량이 부족 함

해당 연구에서는 AUTOREGRESSIVELY MODEL과 충분한 데이터량으로 학습할 수 있는 모델을 제안

그리고 zero-shot fashion으로 평가를 진행

# 1. Introduction

최근 machine learning을 이융한 text to image 방법론들이 연구되고 있다.

DRAW :2015년 이미지 생성 모델

goodfellow : 2014년 visualization GAN 모델

2016년 생성 뿐만아니라 zero-shot learning을 통한 인식도 되는 모델

multi-scale generation : 성능이 향상된 생성모델 2017년

2016~2021년 단지 text만으로 이미지를 생성할 수 있는 연구 수행

또한 대규모 학습 데이터를 제공하는 MS-COCO 데이터셋과 pretrained 트랜스포머 모델등 다양한 연구가 진행됨

- 관련 데이터셋

MS-COCO : 이미지당 5개의 캡션으로 구성된 대규모 데이터셋

CUB : 북미 새 200종에 대한 11,788개의 이미지당 5개의 캡션으로 설명을 추가

해당 연구에서는 MS-COCO데이터셋을 zero-shot 을 통해 label없이 정확도를 비교하여 보여줌 또한 image-to-image 도 같이 보여줌

# 2. Method

연구의 목표는 transformer를 이용해 text에서 이미지를 생성할 수 있도록 하는것

그러나 pixcel 단위로 바로 이미지를 생성하려고 하면 지나치게 많은 메모리가 필요하다.

→ 이미지 해상도가 좋아질수록 더 많은 메모리가 필요

이러한 방법들을 해결하기 위해 연구에서는 2개의 stage로 학습을 진행

1. Stage 1

> ![img](file:///D:/src/whtngus.github.io/img/2023/Zero-Shot_Text-to-Image_Generation/f3.jpg?lastModify=1676010143)
>
> 분리된 오토인코더인 dVAD(discrete variational autoencoder)를 학습한다.
>
> 이는 위에서 말한 pixcel 단위로 이미지를 생성시 지나치게 많은 메모리가 사용되는걸 방지하기 위한 압축을 위해서 사용
>
> → 256 * 256 RGB 이미지를 32*32 이미지 토큰으로 변경  이렇게 되면 8192의 정보만 예측하면 됨   -  8192 = 32*32*8 (rgb 2^3) → 8이 rgb값이 맞는지 확인하기
>
> 이렇게 압축된 저 용량의 데이터를 사용 (위의 그림1 - 위쪽이 원본 아래쪽이 dVAD를 통해 축소된 이미지

- Stage 2

> 256 BPE-encoding된 텍스트 토큰과 32*32=1024개의 이미지토큰을 conctenate  그리고 이 두 관계를 joint distribution 방식을 통해 학습 진행

![f6](\img\2023\Zero-Shot_Text-to-Image_Generation\f6.PNG)

> x : images
>
> y : captions
>
> z : 인코딩된 RGB image tokens
>
> ![f7](\img\2023\Zero-Shot_Text-to-Image_Generation\f7.PNG)
>
> factorization 분포를 기반으로 함 
>
>  q_θ : dVAE encoder로 만들어진 32*32 image token의 분포
>
> p_θ : dVAE decoder로 RGB image를 생성한 image token의 분포
>
> p_Ψ : transformer모델에 의한 이미지와 text의 join distribution 
>
> 위 수식에서  경계는 β = 1로 유지되지만 일반적으로 더 클경우 유의한 경우가 많음

### 2.1. Stage One: Learning the Visual Codebook

θ와 Ψ를 비슷하게 하기 위해 ELVO(Evidence of Lower BOund)를 최대화 하는 dVAE를 학습한다.

학습 데이터는 8192개의 카테고리를 가지고있는 codebook vectors를 사용

논문에서 p_Ψ를 만들기 어렵다고 마구 설명을 적어둠 .. 

gumbel-softmax와 Adam optimizer 등 여러가지 사용

안정적인 학습을 위한 방법

> - annealing t를 1/16를 사용 -> 이를  q_θ 에서  q_θ^t 로 정의
> - 1*1 convoution layer
>
> encoder 마지막과 decoder 시작에 1*1 convoution layer를 사용해
>
> 전반적인 이미지 generalize를 통해 ELB최적화
>
> - Multiplication loss
>
> encoder와 decodr에 작은 loss의 resblock을 사용해 안정적으로 weight를 관리
>
> KL weight to β = 6.6사용

### 2.2. Stage Two: Learning the Prior

사전 확률인 φ and θ를 고정해서 사용 

12-billion parameter를 통해 pφ 최적화 

텍스트는 256 token 이고 이미지는 32*32=1024 토큰이며

텍스트 사전의 수는 16,384 그리고 이미지 사전 수는 8,192개(gumbel noise) 이다.

![figure11](\img\2023\Zero-Shot_Text-to-Image_Generation\figure11.PNG)

> 64개의 self-attention layer 사용하고 3개의 다양한 attention masks를 사용한다.
>
> 앞의 6개는 text 영역 뒤의 16개는이미지 영역
>
> text-to-text attention : casual mask만 사용 가능
>
> image-to-image attention : row/column/convolutional attention mask 적용 
>
> ex) a는 이전 5개의 그림 토큰을 이용

모델에서 생성할 수 있는 caption의 최대 길이는 256 token으로 제안

-> pretraining 모델 크기때문으로 보임

1/8 text, 7/8 image cross-entropy로스를 별도로 사용 

606,000개의 validation image dataset 사용 

### 2.3. Data Collection

1.2 billion parameters 크기의 모델로 Conceptual Captions 데이터셋(3.3 milion text-image paire MS-COCO데이터)을 학습 

->논문에서 제시하는 모델 사이즈는 12 billion parameter크기의 모델로 JFT-300M 데이터셋과 비슷한 크기로 텍스트-이미지쌍 데이터 수집 (250Million 개의 데이터셋)

### 2.4. Mixed-Precision Training

![table1](\img\2023\Zero-Shot_Text-to-Image_Generation\table1.PNG)

GPU memory를 아끼기 위해서 아래와 같은 방법들을 사용

- 16-bit로 양자화 

대신 학습시 underflow발생으로 이슈가 있음 

그래서 per-resblock gradient scaling 방법을 사용



- activation checkpointing and recompute

(checkpointing and rematerilization 이라고도 함)

이후 재사용될 가능성이 있는 값을 메모리에 저장해두고 다시 사용하는 방법 대신 값을 일단 버리고 나중에 필요할 때 재계산 하는 방법. (gpu memory 에서 메인memory로 변환하는데 시간이 많이 들기때문에 이렇게 하는게 더 효울적일 수 있음)

-> 10억개에 달하는 모델을 초기화 하고 훈련시키는 방법이 어려웠다고 말함

![figure4](\img\2023\Zero-Shot_Text-to-Image_Generation\figure4.PNG)

연구에서는 underflow현상이 발생하고, 이를해결해 잘 학습되도록 하는걸 목표로 연구함

-> 이를 하결하기 위해 Standard loss saling을 함 

최종 모델은 그림4와같이 지정 

> 줄선 : forward propagation
>
> 점선 : backpropagation - underflow를 해결하기 위해  16, 32bit를 사용 



### 2.5 Distributed Optimization

![figure5](\img\2023\Zero-Shot_Text-to-Image_Generation\figure5.PNG)

120억개의 파라미터를 학습하기 위해 24GB메모리가 필요하고 16(V100)으로 학습하기 위해 

- parameter sharing 방법을 사용

이 과정에서 그래디언트를 취합하는 병목비용이 추가로 듦

- PowerSGD 사용해 그래디언트를 압축하여 비용 최소화

> 1. backprop과정에서 그라디언트를 error buffer로 축적해둠으로써 각기 다른 buffer를 할당하는 것 대비 메모리를 절약
> 2. error buffer를 0으로 만드는 인스턴스를 최소화 (mixed-precision backprop에서 생기는 nonfinite 값 혹은 체크포인트에서 모델을 재시작할 때 등)
> 3. Gram-Schmidt 대신 Householder orthogonalization을 사용함으로써 수치적인 안정성을 더한다.
> 4. 16FP를 사용함으로써 발생할 수 있는 underflow를 피할 수 있다.

그 외에도 다양한 방법 사용 ...

### 2.6. Sample Generation

![figure2](\img\2023\Zero-Shot_Text-to-Image_Generation\figure2.PNG)

![figure6](\img\2023\Zero-Shot_Text-to-Image_Generation\figure6.PNG)

transformer 기반의 contrastive model을 통해 샘플을 다시 랭킹화 시킴 

-> 이미지를 텍스트와 얼마나 잘 매칭했는지 판단하는 모델 

해당 방식을 통해 (그림 6) 데이터를 증가시킴

그리고 top k를 추출함으로 써, 양적인 + 직적인 데이터셋을 모두 구축했다고 이야기함 

# 3. Experiments

### 3.1. Quantitative Results

![figure3](\img\2023\Zero-Shot_Text-to-Image_Generation\figure3.PNG)

- 질적인 평가

zero-shot 접근방법으로 MS-COCO 데이터셋을 Inception Score, Frechet Inception Distance평가를 함

![figure7](\img\2023\Zero-Shot_Text-to-Image_Generation\figure7.PNG)

MS-COCO 데이터셋에 있는 캡션을 주고  top 5개의 이미지를 추출한 결과 논문에서 제시한 모델이 많이 뽑히는걸 확인 

![figure9](\img\2023\Zero-Shot_Text-to-Image_Generation\figure9.PNG)

- 양적인 평가

실선 - FID 스코어 결과

점선 - 생성된 데이터를 평가한 결과 

a와 b는 MS-COCO 와 CUB 데이터셋에 블러를 심하게 했을데 각 모델별 성능 차이 (is는높을수록, FID는 낮을수록 좋음)

c는 reranking 으로 sapling한 수에 따른 스코어 차이



- 데이터 전처리  

contrastive model 모델을 이용해 중복 혹은 비슷한 유사 학습 이미지 제거 진행

-> 마지막에는 손으로 직접 검사후 제거했다고 함 





# 참고지식

- auxiliary losses

**GoogLeNet (ILSVRC challenge 2014 winner)**에서 처음 도입된 개념 (**Training**을 잘하도록 도와주는 보조 역할 )

gradient 전달이 잘 되지 않는 하위 layer를 training 하기 위해서 classification의 문제를 해결하는 Neural Network는 softmax를 맨 마지막 layer에 딱 하나만 놓는데, Auxiliary classifier는 중간중간 에 softmax를 두어 중간에서도 Backpropagation을 하게 함

- joint distribution(결합확률분포)

확률 변수가 두 개 이상일 때 여러 사건이 동시에 일어날 확률을 말함.

규칙1. 합 규칙

![f4](\img\2023\Zero-Shot_Text-to-Image_Generation\f4.png)

어떤 특정한 확률을 구하려고 한다면, 그와 관련된 모든 변수들을 포함한 모든 경우에 대해서 결합 분포의 값을 더함 (이산 확률 분포)

규칙 2.  곱 규칙

![f5](\img\2023\Zero-Shot_Text-to-Image_Generation\f5.png)

각각의 랜덤 변수들이 독립인 경우. 조건부 확률을 이용해 모두

- Factorization of Bayesian network

![f8](\img\2023\Zero-Shot_Text-to-Image_Generation\f8.PNG)

베이지안 네트워크의** Factorization**은 Full joint distribution을 구할 때, 개별 노드의 Conditional probability의 Condition에 포함되는 노드를 각 노드의 부모 노드만을 고려함으로써 계산에 사용되는 파라미터를 줄여주는 역할을 한다.

p(a,b,c) = p(c|a,b)p(a,b) = p(c|a,b)p(b|a)p(a)

와 같은 원리 이용

- ELBO (Evidence of Lower BOund)

![f9](\img\2023\Zero-Shot_Text-to-Image_Generation\f9.PNG)

P(z|x)가 다루기 힘든 분포를 이루고 있을 때 조금 더 다루기 쉬운 분포인 Q(x)로 대신 표현하려 하는 과정에서 두 분포 (P(z|x)와 Q(x))의 차이 (KL Divergence)를 최소화 하기 위해 사용

-  gumbel-softmax

![f10](\img\2023\Zero-Shot_Text-to-Image_Generation\f10.PNG)

1) sampling을 하고 싶은데, neural network에서 backpropagation시에 불가능하다. 이를 해결하기 위해 Gumbel-Max Trick을 사용하여 backpropagation이 흐르도록 해주자

2) argmax를 사용하였더니 backpropagation이 흐르지 않는다. 이를 어떻게 해결할까? Softmax를 취하여 해결함과 동시에, continuous하게 relaxation을 하기 위해 temperature τ를 쓰자

- annealing

Cosine annealing은 학습율의 최대값과 최소값을 정해서 그 범위의 학습율을 코싸인 함수를 이용하여 스케쥴링하는 방법

`learning rate annealing`은 learning rate schedule과 혼용되어 사용되지만 특히, learning rate가 iteration에 따라 monotonically decreasing하는 경우를 의미

![f11](\img\2023\Zero-Shot_Text-to-Image_Generation\f11.PNG)

Learning rate annaeling을 사용하면 초기 learning rate를 상대적으로 크게 설정하여 Local minimum에 보다 더 빠르게 다가갈 수 있게 만들어주고 이후 learning rate를 줄여가며 local minimum에 보다 더 정확하게 수렴할 수 있게 만들어준다.

- Inception Score(IS)

GAN 모델을 평가하기 위해 사용되는 score

inception-V3모델을 이용해 특정 클래스에 속할 확률을 계산 

1) 이미지의 질 : 이미지는 어떤 특정 물체 같아 보이는지

2) 이미지 다양성 : 다양한 물체가 생성되는가? 

1~1000점을 가짐 

- Frechet inception distance(FID)

실제 이미지와 생성된 이미지 사이의 feature vector간의 거리를 계산한 점

IS와 마찬가지로 inception-v3모델을 사용하여 마지막 pooling layer에서 나온 벡터 간의 거리를 평가  

2020년 기준 GAN모델의 결과를 평가하는 표준 척도로 사용 

FID가 낮을수록 좋은 모델로 해석가능

![f12](\img\2023\Zero-Shot_Text-to-Image_Generation\f12.PNG)





# 참고 사이트

- dall-e

<https://littlefoxdiary.tistory.com/74>

- auxiliary losses

<https://technical-support.tistory.com/87>

- joint distribution

<https://m.blog.naver.com/PostView.naver?blogId=study_together_&logNo=220820354072>

- Factorization of Bayesian network

https://rooney-song.tistory.com/53

- ELBO (Evidence of Lower BOund)

https://yonghyuc.wordpress.com/2019/09/26/elbo-evidence-of-lower-bound/

-  gumbel-softmax

https://kaen2891.tistory.com/81

- annealing

https://hiddenbeginner.github.io/deeplearning/paperreview/2020/01/04/paper_review_AdamWR.html

- 딥러닝 메모리 효율화 방법

https://yunmorning.tistory.com/20
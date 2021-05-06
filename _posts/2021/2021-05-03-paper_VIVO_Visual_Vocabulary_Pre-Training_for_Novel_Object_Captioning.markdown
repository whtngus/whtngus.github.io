---
layout: post
title: "paper : VIVO: Visual Vocabulary Pre-Training for Novel Object Captioning"
date: 2021-05-08 19:20:23 +0900
category: paper
---

# VIVO: Visual Vocabulary Pre-Training for Novel Object Captioning

## 논문 정보 

- 2020년 9월 28일 게재 - (v2 2021년 3월)
- 학회 : AAAI (2021)
- 기관 Microsoft Corporation
- url : https://arxiv.org/abs/2009.13682

# 논문 요약 시작



## 도입

nocaps(novel object captioning challenge)를 목적으로 한 논문 ! 

테스크를 수행하는것 뿐만 아니라 Vision-Language Pre-training (VLP)를 위한 모델을 제공 



최근에 많은 데이터 셋이 공개됨 COCO(2015) 데이터 셋과 Flickr30k(2014) 데이터 셋외에  많은 데이터셋이 공개됨 

Image captioning은 오래된 첼린지이다. 

이러한 데이터셋 들과 오래된 연구에도 불고하고 그러나 아직 극적인 효과를 보진 못함

-> 테스크에서 제공되는 데이터셋의 개체와 ocr태그에 극한되어 있기 때문에 



광범위한 데이터셋을 사용하기 위해 nocaps를 이용했고 약 400개의 객체를 사용하여 학습(데이터셋은 500개이나 사람이 직접 판단하여 100개정도는 애매해서 제외했다고 함)



![vivo_prtraining](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\vivo_prtraining.PNG)

> VIVO 연구는 대량의 사진 데이터로부터 pre-training을(cpation 이 없는 데이터) 하고, 이미지의 위치와 태그 정보를 vectorize하는걸 목표로 함
>
> 위 사진에서 개체 쌍 이미지 태그 데이터를 사용해서 의미적으로 유사한 객체의 이미지 영역과 태그가 서로 가까운 백터에 매칭되도록 학습을 시킴
>
> 그 후 fine-tuning을 통해 제한된 수의 개체(파란색))만 포함되는 페어링된 이미지에 대해 미세조정을 하는 방식
>
> -> 이러한 방식으로 학습하면 추론시에 (사진의 Infernece) 노란색을 설명하기 위해 벡터를 통해 일반화 할 수 있음





해당 연구에서 제시하고자 하는 contribution

> - 많은 양의 캡션이 없는 사진데이터를 통해 VIVO pre-training 방법과 사진 representation learning 방법
> - Hungraian matching loss 함수 (image-tag pairs를 예측하기 위한 loss 함수)
> - CIDEr score state-of-the-art 스코어 달성 - nocaps benchmark



## 사전 연구

- Image Captioning

> 기존 연구에서 이미지 캡셔닝은 특정한 테스크에 집중되어 있다.
>
> - 캡션 데이터에 대한 Attentin 메커니즘에 집중한 논문들
>
>  Song et al. (2019); Wang, Chen, and Hu (2019); Gao et al. (2019); Huang et al. (2019); Pan et al. (2020); Guo et al. (2020); Cornia et al. (2020)
>
> - 강화학습에 집중한 논문들
>
>  (Rennie et al. 2017; Li, Chen, and Liu 2019; Yang et al. 2020) or adversarial learning (Chen et al. 2019; Dognin et al. 2019)
>
> - dense captioning
>
>  (Johnson, Karpathy, and Fei-Fei 2016; Yin et al. 2019; Li, Jiang, and Han 2019),
>
> - grounded cationing
>
> (Ma et al. 2020; Zhou et al. 2020b)

그러나 위의 연구들은 이미지를 vectorize해서 학습시 보지 못한 데이터를 예측하는데는 연구를 하진 않았음.



- Novel Object Captioning (NOC) 

> NOC는 새로운 혹은 만들어진 이미지에 대해서도 이미지 캡셔닝을 할 수 있어야함.(현실에서 적용하기 위해)
>
> 이미지와 텍스트의 관계를 알아하며 캡션을 생성할 수 있어야 함.
>
> 해당 논문에서 pre-training을 통해서 해결하고자 하는 목표



- Vision and Language Pre-training

> BERT의 pretraining 기법을 이용해서 VLP 를 하고자 함
>
> Vision-language representation 을 목표로 하며 이미 관련해서 해당 연구가 많이 진행되어 있음
>
>  (Lu et al. 2019; Tan and Bansal 2019; Su et al. 2019; Chen et al. 2020; Zhou et al. 2020a; Li et al. 2020) 
>
> -> 위와같은 연구를 통해 image-text retrieval 과 viaul question answering을 수행할 수 있음
>
> 그러나 위와같은 연구는 이미지와 캡션의 연결된 데이터를 통해서 학습을 시켜야 함(pre-training)
>
> 해당 연구에선s image-caption 데이터 없이 pre-trainining 하는 방법을 제공



## 학습 방법

![image-model](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\vivo_model.png)



- 학습 방법은 위 사진으로 모든게 설명됨! 

최신 연구 방법들은 정해진 테스크에서 높은 스코어를 달성했으나 역시 정해진 데이터에서만 작동을 잘하기때문에 범용적인 모델이 필요

다양한 객체와 다양한 ocr에 대해서 적용이 되야 함.

COCO 데이터셋의 같은 경우 object를 그대로 설명함 예를들어 사람, 개, 코 같은 그러나 이미지를 설명할때 개체를 완벽히 그대로 언급하는 경우가 많지 않기 때문에 오히려 자연스러운 설명 생성이 힘들다.

- 학습은 총 2가지 방법으로 진행

> 1. Pre-training
>
> 이미지의 라벨과 위치를 같이넣어 mask된 라벨(객체)를 맞추는 형식
>
> -> 같이 나오는 이미지 셋을 학습하면서 BERT처럼 이미지의 문맥을 학습할 수 있음
>
> 2. Fine-tuning
>
> 이미지와-설명이 있는 데이터를 통해서 fine-tuning 진행 여기에서도 객체를 비워두고 해당 객체를 응답하는 방식을 사용 
>
> 사진의 예시 B에서 "A" holding a  "B" 의 객체를 맞침으로써 객체관의 관계와 사진의 문맥에 대한 이해로들 향상 +(NLP도 향상)

위와 같은 학습방법을 통해 여러개의 Transformer 레이어를 통해 입력 데이터로부터 vectorization 후 사진에 대한 설명 text를 생성할 수 있음.



#### VIVO Pre-training

대용량 사진 데이터를 통해 pretraining 진행

약 6만 4천개의 image 태그 데이터 (상당히 많음..)

image-tag 페어를 통해 사전학습을 진행

학습 방법은 마스크를 씌운 태그를 bag of image-level tag 와 image regions을 통해 맞추는 방식

> ![formula_1](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\formula_1.PNG)
>
> N - 이미지 개수
>
> ![formula_2](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\formula_2.PNG)
>
> G의 경우 이미지 라벨셋인 Li 데이터 
>
> I(i)는 이미지 G(i)는 이미지내의 테그셋들(라벨링된 객체 데이터들)
>
> 해당 모델에서 Multi transformer model을 사용한다고 했는데 그럼 입력은??
>
> 
>
> ![formula_3](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\formula_3.PNG)
>
> V : image region features -> 이미지 I에서 추출된 객체 (Visual genome dataset - 2018)
>
> ![formula_4](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\formula_4.PNG)
>
> T : Tag tokens - tokenized tag으로 학습되는 동안 토큰은 랜덤하게 마스크를 씌어 예측하게 됨
>
> 이때 T,V는 정렬하지 않은 상태에서 예측을 시작



#### Hungarian matching loss (Stewart, Andrilucka, and Ng 2016, Carion - 2020)

> ![formula_5](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\formula_5.PNG)
>
> 마스크 씌어진 토큰 M에 대해서 T^hat 은  다음과 같다
>
> t(m)은 토큰 아이디(vocabulary 에서)그리고 예측 확률이 T^(hat) 이다. 
>
> 이때, 정렬디지 않은 토큰이다. 
>
> ![formula_6](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\formula_6.PNG)
>
> 그 후 토큰이 정렬되지 않았기 때문에 토큰과 객체 1 대 1 매칭이 필요하다.
>
> P는 i마스크에 대한 포지션 classification 확률 이다.
>
> ![formula_7](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\formula_7.PNG)
>
> 최종적으로 두가지 모두 수행해야 위와 같은 수식이 나온다.
>
> 위 식에서  α는  M(mask)지수의 순열 -> α(i)는 i번째 예측에 할당된 토큰의 인덱스
>
> ![image-20210502230654706](C:\Users\Suhyun\AppData\Roaming\Typora\typora-user-images\image-20210502230654706.png)
>
> 모델에서 어떤 값이 할당된건지 알 수 없음으로 α는  T와 P사이에서 가장 좋은 매칭을 학습하는걸 목표로 한다.
>
> -> 유효한 순열 중 위와 같은 총 비용을 최소화하 하는 가장 최선의 α를 정의
>
> ![formula_8](\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\formula_8.PNG)
>
> C는 위와 같은 cost function 
>
> 최종 로스는 L 로 구하지만  L의 α값은  C로 구해진다

위 사진에서 pre-training은 bi-directional attention mask 모델을 통해 학습 

-> VLP 가 가능하게 만듦

#### Fine-tuning and Inference

> pre-training 후 Transformer 모델은 fine-tuned 을 COCO 데이터 셋을 통해 진행 (80개의 오브젝트가 있음)
>
> 여기에서도 이미지의 위치와 태그는 랜덤하게 지정되어 학습된다. 또한 문장에서도 랜덤하게 마스크가 씌어지면서 학습된다

> fine tuning의 3가지 학습 feature는 다음과 같다.
>
> V : 영역  
>
> T : 테그 셋
>
> C : 캡션
>
> 세트로 구성된다
>
> V와 T는 pre-training과 동일하며, C는 연속된 토큰이다.
>
> fine-tuning 시에 랜덤하게 마스크를 문장에서 씌우며 이를 예측한다 
>
> -> 이때 cross-entropy loss를 사용
>
> 이렇게 학습해서 모델에서 left to right 방향으로 infernece 를 하며 문장을 생성할 수 있다. (Image captioning 가능)
>
> 인퍼런스 하는 동안에 image의 featur의 위치와 객체 테그는 계속 입력으로 주어진다.



## Experiments



- Experimental Settings

> - Datasets
>
> Open Images V5 challenge training set을 이용 (1.7개의 이미지) - VIVO pre-training
>
> 500개의 객체 분류가 있고  해당 데이터에서 bounding box는 6.4K개의 독립적인 클래스가 존재
>
> finetuning 시에는 COCO 데이터 셋을 통해 118K개의 이미지에서 각 이미지당 5개의 캡션을 사용
>
> validation은 4.5K test는 10.6K개의 이미지를 사용

- Implementation Details

> Object Detector 로 UpDown(Anderson - 2018)을 사용 -> image region feature
>
> 해당 데이터를 2054의 차원(2048D의 이미지와 6D의 bounding box 인코딩 )으로 concatenate를 시킴 
>
> object detector 또하니 Open Image 데이터를 이용해서 훈련  
>
> 미세 조정시에 훈련 세트의 태그 정보도 같이 학습 (ground-truth tag가 없는 데이터도 사용)
>
> VIVO pre-training시에 모델 초기값은 BERT-base를 사용했으며,
>
> 이미지에서 최대  50개의 이미지 영억과 15개의 태그토큰을 사용.
>
> 학습에서 160K iterations (약 100 epochs)을 하였고, batch size는 1024 dlrh 
>
> learning rate 는 5*10^-5 를 사용
>
> fine-tuning 시에는 최대 캡션 길이는 40, 태그는 최대 30이다.
>
>  256 배치 사이즈와 5*10^5 learing rate를 사용하며 30epochs를 수행한다.
>
> **여기에서 성능을 향상시키기 위해 한번더 학습**
>
> CSST optimization(Rennie - 2017)을 사용한다.
>
> 2 * 10 ^ 6 learning rate로 5 epoch을 추가로 학습한다. 
>
> inference 시에는 greedy decoding을 사용하여 최대 길이가 20인 이미지 캡션을 생성한다.

- Novel Object Captioning

 (Anderson et al. 2018; Agrawal et al. 2019) and OSCAR4 (Li et al. 2020) 논문들과 비교해서 nocaps benchmark 데이터 에서  state-of-the-art 를 달성  학습 데이터는 COCO 데이터셋을 사용 

> - setting
>
>  SCST (Rennie et al. 2017) 옵티마이제이션 사용
>
> 캡션 텍스트 생성시에는 Constrained Beam Search (CBS) (Anderson et al. 2017) 을 사용
>
> ![table_1](D:\code\whtngus.github.io\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\table_1.PNG)
>
> 위의 표에서 VIVO pre-training 데이터가 Human 보다 높은 점수르 달성한 것을 볼 수 있다.
>
> ![vivo_model_2](D:\code\whtngus.github.io\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\vivo_model_2.PNG)
>
> vivo 모델은 위와 같은 방식으로 학습하며 학습 방식은 이전에 설명한 바와 같다.

- Visual-Text Alignment, General Image Captioning

> ![table_4](D:\code\whtngus.github.io\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\table_4.PNG)
>
> ![table_2](D:\code\whtngus.github.io\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\table_2.PNG)
>
> ![table_3](D:\code\whtngus.github.io\img\vivo_visual_vocabulrary_pre_training_for_novel_object_captioning\table_3.PNG)
>
> 이미지 여역을 객체 태그에 맞춰 정렬하는 것은 어휘 학습에서 VIVO 사전 훈련이 데이터를 더 잘이해할 수 있도록 한다.
>
> 또한 VIVO 모델 pre-training시에 이미지 캡션 데이터가 없어도 가능하다는 점에서 집중 

-  Ablation Study

10% Open Images training set을 추출하여 ablation을 수행

fine-tuning을 cross-entropy로 진행하면서 COCO 데이터 셋을 학습하고 nocaps validation set을 이용

> - Using a Larger Set of Tags
>
> 500개 이상의 객체와, 6.4K 개의 테그셋으로 모델을 학습
>
> - Using Humgarian Matching Loss
>
> Hungarian matching loss를 사용해서 효과적인 학습을 진행  (위 점수 사진의 Table 6 참조 )

## Conclusions

논문에서는 임지 캡션 모델을 두 단계로 훈련하는 모델을 제시 

첫째, 트랜스포머 기반 모델은 얻기 어려운 이미지 캡션 쌍을 사용할 필요 없이 어휘 학습을 위해 대용량 데이터셋 사용

-> 이미 object detection 데이터라 ...  이것도 없이 nlp처럼 학습할 방법은 없을까?

둘째, 모델은 이미지 캡션 데이터를 통해 미세 조정하여 사전 훈련된 시각적 어휘 정보를 이용해 캡션 정보를 구성

-> nocpas 데이터를 통해 zero-shot 에서도 잘 작동함을 보임 

CIDEr 점수는 state-of-the-art 를 찍었다고 논문에서말함  

-> 논문 읽는 내내 CIDEr만 언급하는걸 보니 다른 평가 메트릭스는.. 글쎄?



결론으로 두 가지 스텝을 이용하니 첫 번째 데이터가 많은 object detction 데이터로 학습해서  모델이 사진에 대한 문맥 이해를 잘 하도로 만들었다는게 포인트





## 관련 지식

- nocaps(novel object captioning challenge)

링크 : https://nocaps.org/

이미지 캡션 모델은 제한된 시각적 사진에서 개념과 시각 데이터셋을 이용해 모델의 좋은 성능을 이끌었으나 실제 데이터에 사용은 힘들다.

이러한 점을 해결하기 위해 대규모 벤치 마크를 제시 -> 5,100 개 이미지를 설명하는 166,100 개의 사람이 생성 한 캡션으로 구성

COCO 이미지-캡션 쌍과 Open Images 이미지 수준 레이블 및 개체 경계 상자로 구성

400 개의 객체 클래스에는 관련 교육 캡션 존재

조지아, 맥쿼리 대학에서 만든걸로 보임(2019년도 ICCV 학회 데이터셋 관련 논문 게재)

-  Ground-truth

이 논문에서 말하는 ground-truth는 학습하고자 하는 데이터의 원본 혹은 실제 값을 표현할 때 사용  

즉,  segmentation에서 객체 간의 경계선
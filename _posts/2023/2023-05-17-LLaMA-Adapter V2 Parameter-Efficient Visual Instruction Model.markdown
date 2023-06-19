---
layout: post
title: "Exploring Diverse In-Context Configurations for Image Captioning"
date: 2023-06-17 00:05:23 +0900
category: paper
---

# Exploring Diverse In-Context Configurations for Image Captioning

2023년 3월 26일

url : https://arxiv.org/pdf/2305.14800v2.pdf

code : https://github.com/mlfoundations/open_flamingo



# Abstract

VL를 위해 4가지 방법으로 나눠 분석을함

Image selection,  이미지 캡션

# 1 Introduction

NLP 테스크에서 강력한 모델을 VL도 합쳐 해결할 수 있는 방법을 제안함 

![f_1](\img\2023\Exploring Diverse In-Context Configurations for Image Captioning\f_1.PNG)

위의 그림은 LM 과 VLM의 예시를 보여줌 

MSCOCO 데이터셋을 사용 해서 학습함

이미지 선택을 위해 4가지 방법 사용 

1. Random Sampling(RS)
2. Similarity-based Image-Image Retirival (SIIR)
3. Similarity-based Image-Caption Retrival (SICR)
4. Diversity-based Image-Image Retrival(DIIR)

4가지 타입의 이미지 캡션을 생성

1. Ground-Truth Captions (GTC)
2. Model-Generated Captions(MGC)
3. Interatively Prompting(IP)
4. Model-Generated Captions as Anchors(MGCA)

다양한 캡션 생성을 위해 MGC에서는 두 가지 모델을 사용 

# 2 Related Work

### Prompting Language Model (LM).

최근 몇년간 두 가지 방법론으로 NLP가 연구되고 있음

- GPT, BERT, BART 처럼 LM을 이용해 pre-training -> fine-tuning 방식
- prompt paradigm

GPT-3 가 나오면서 패러다임이 바뀜 

downstream task를 함에 있어서 fine-tuning을 하는것이 아닌 적절한 프롬프트를 만들어 채우는 방식으로 해결 

prompt-based techniques 기술이 필요해짐 

### Prompting Vision-Language Model (VLM).

Image Caption , VQA 등의 테스크가 있음 

### Exploring In-Context Configurations in NLP

- 생략

# 3 Configuring In-Context Sequences

![f_2](\img\2023\Exploring Diverse In-Context Configurations for Image Captioning\f_2.PNG)

 S = {(I1, C1); (I2, C2); ...; (In, Cn); ˆI} 

각 context sequence는 이미지와 캡션의데이터셋으로 구성됨 

![f1](\img\2023\Exploring Diverse In-Context Configurations for Image Captioning\f1.PNG)

역시 seq 방식으로 PreTraining된 VLM모델의 representation vector를 이용

## 3.1 Selecting Images

### Random Selection (RS)

주어진 데이터셋 D = {(I1, C1), ...,(IM, CM)} 과 M(이미지-캡션 셋)에서 랜덤으로 이미지를 n개를 샘플링함

### Similarity-based Image-Image Retrieval (SIIR)

데이터셋 D에서 가장 유사한 n개의 이미지를선택

유사한 이미지를 찾기 위해 Figure 2의 a 방식(encoder 벡터를 이용)과 b방식(탐지된 객체를 이용)을 사용

### Similarity-based Image-Caption Retrieval (SICR-CLIP)

위의 Figure 2의 c 방식으로 CLIP를 사용

이미지 캡션 문장 벡터와 주어진 이미지를 를 이용해 유사도를 계산 해 비슷한 이미지를 추출 

### Diversity-based Image-Image Retrieval (DIIR)

Figure 2의 d방식 사용  클러스터링을 해 이미지군집에서 추출하는 방식

1. DIIR-TR

각 이미지에서 VinVL 모델과 IETrans모델을 통해 태그를 추출하고 랜점 N개로 클러스터링

클러스터링 시에 SIIR-TAG를 통해 유사 이미지 클러스터링 

2. DIIR-TT

 SIIR-Tags인 object, attirubte, relation을 추출

그후 top-n개의 비슷한 카테고리를 군집화함 (이를 위해 4K-shot image로 S그룹을 생성)



논문 설명만 봐선 DIIR방식은 잘 안될 것 같은데 Result 스코어를 확인해보자

## 3.2 Assigning Captions

이미지 선택 후 선택된 이미지를 이용해 캡션을 생성 

캡션을 퀄리티를 올리기 위해 4가지 방법을 사용 

### Ground-Truth Captions (GTC)

MSCOCO 데이터 셋의 캡션을그대로 사용 

5개의 캡션중 첫 캡션을 사요했다고 함 

### Model-Generated Captions (MGC)

MGC는 GTC보다 성능이 안좋음 (GTC도 썩 좋을것 같진 않다...)

이유 1. 간단한 단어와 생성된 문장의 유연성이 떨어짐

이유 2. 생성된 문장은 말로 표현하기엔 이미지 패턴에서 부족하고 잘못된 정보를 가지고 있음

-> 기존 모델은 타겟 이미지에서 캡션을 생성함으로 MGC방식인데 정확도가높다 GTC MGC는 비교모델의 베이스라인 스코어를 낮추기 위한 방법이 아닐까?

 ### Iteratively Prompting (IP)

I ∈ D 각 이미지에서 캡션을 생성 

이를 합해 VLM에서 향상된 최종 캡션을 생성 

### Model-Generated Captions as Anchors (MGCA)

MGC 방식은 화려한 묘사를 하지 못함 

이를 해결하기 위해 anchor를 사용해 강조를 함

이렇게 하니 CIDEr score가 매우 올라감

-> 결국 최종적으로 이걸 제안하고 싶은 걸로 보임

# 4 Experiments

![f_4](\img\2023\Exploring Diverse In-Context Configurations for Image Captioning\f_4.PNG)

MSCOCO 데이터셋 모델 별 비교 

Figure 3은 image select 방법 별 

Figure 4는 캡션 생성 방법 별 비교 

MGC-TF@X 에서 X는 text 셋에서 CIDEr score

3090 RTX로 학습했다고 함 

여기서는 베이스 라인으로 삼은 RS와 비교해서 높아진걸 보여주고자 함 (RS와 비교하는게 맞나..)



아래 생략

























# 참고

- Chain-of-Thought 

추론 능력 사고 사슬

프롬프트를 이용해 사람이 사고하는 것과 비슷하게 추론 단계를 추가
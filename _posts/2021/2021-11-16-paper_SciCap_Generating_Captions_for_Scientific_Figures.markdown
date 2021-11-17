---
layout: post
title: "paper : SciCap: Generating Captions for Scientific Figures"
date: 2021-11-17 19:20:23 +0900
category: paper
---

# SciCap: Generating Captions for Scientific Figures

Computation and Language (cs.CL); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)

url : https://arxiv.org/abs/2110.11624

2021년 10월 게재 



# Abstract

Image Caption은 범용적인 사진에 대한 캡션을 잘 달고 있지만 

과학 논문지에서 등의 수치를 나타내기 위한 그림 (차트) 캡션은 복잡한 정보를 나타내기 위한 매우 중요한 정보이다.

해당 논문에서 이런 차트 기반의 이미지 캡션을 생성하기 위한 데이터 세트인 SCICAP을 제시

2010 ~ 2020년 arXiv 논문을 크롤링하여 차트 설명을 캡션으로 사용 



# 1. Introduction

![f1](\img\2021\SciCap_Generating_Captions_for_Scientific_Figures\f1.PNG)

논문에서는 복잡한 개념을 설명하거나 결과를 보여주기 위해 수치를 사용함

학술적 기사에서 그림 캡션은 메시지를 효과적으로 전달하기위해 x축과 y축에대한 설명을 해야하지만 기존 이미지 캡션은 

"실험의 결과", "X와 Y의 관계" 등과 같이 간단하게 생성함에 그쳤다.

해당 논문은 수치와 차트에 대한 고품질 캡션을 생성하는 자동 형상 캡션 모델을 개발하는 것을 목표로 한다

SCICAP는 290,000개 이상의 논문에서 추출한 2백만 개 이상의 수치를 포함하고 있다.



# 2. Related Work

생략.



# 3. Constructing SCICAP Dataset

실제 형상 캡처 데이터를 NLP 커뮤니티에 사용하기 쉬운 적절한 형식으로 처리하는 프로세스 

### Step 1: Data Acquisition and Pre-processing

역시나 데이터 수집이 어렵다 .

arXiv 데이터 세트를 기반으로 모든 학술 기사를 다운로드하고 2020년 12월 22일(총 1,921,287편의 논문) 날짜를 고정 ( 2010~ 2020 년)

+ 컴퓨터 과학(cs), 기계학습(stat) 분야만 추출 -> 295,028개로 줄어듦

### Step 2: Figure-Caption Pair Extraction.

PDFFigures 2.0(Clark and Divvala, 2016) -> 이걸 사용해 논문의 형식을 추출 

그림, 캡션, 표, 섹션, 제목, x-y레이블 등 정보들을 추출 

 295,028개의 논문과 2,170,719개의 수치를 추출함

### Step 3: Figure Type Classification.

 한 가지 특정 차트 유형에 특화된 캡션 모델을 만드는 것을 목표로함

그래서 차트 분류기를 만들어 사용 

그래프 그림, 순서도(노드 다이어그램이라고도 함), 방정식(알고리즘이라고도 함), 막대 그림, 산점도, 표 및 기타의 7가지 유형의 수치를 분류함 

분류 결과 정확도는 정확도는 60,000개 샘플에 대해 86%

분포도는   19.2%(416,804개)가 그래프 그림이고, 23.6%(511,984개)가 표이며, 3개의 5.9%(127,197개)가 방정식(알고리즘 및 유사 코드 포함), 8.5%(185,3988개)가 순서도 이다.



해당 논문에서는 그래프 플롯에 초점을 맞춤 (분류 성능이 가장 좋아 그래프 플롯만 온전히 가져올수 있어서 그런걸로 보임)

![t1](\img\2021\SciCap_Generating_Captions_for_Scientific_Figures\t1.PNG)

### Step 4: Removing Figures with Subfigures

하위 구조를 포함하고 있는 형식들을 제거 

 시범 연구(섹션 3.1)에서 전체 과학 수치의 35.72%가 하위 구조를 가지고 있었다. SCICAP는 단일 그림에 대한 캡션을 생성하는 데 중점을 두기 때문에 데이터 집합에서 하위 형상이 있는 그림을 제거

133,543개의 그림으로 더 좁혔다. (하위 구조가 없는 32%를 사용)

### Step 5: Text Normalization.

숫자는 [NUM]

수식은 [EQUATION]

{}. ()등  괄호는 [BRACKET]

토큰으로 변경 

-> 수치도 의미있는 값으로 사용되야하는거 아닐까?

### Step 6: Target Caption Text Selection.

여러 문장인 경우 설명 문장중 첫 번째 문장만을 사용(133,543 Figures)

- Single-Sentence Caption (94,110 Figures)

- Caption with No More than 100 Words (131,319 Figures) -> 길이제한



## 3.1 Data Analysis and Quality Measurement

![t2](\img\2021\SciCap_Generating_Captions_for_Scientific_Figures\t2.PNG)

 파이프라인의 품질을 평가하기 위해 원본 arXiv 데이터 세트에서 2,000개의 수치를 무작위로 샘플링 하고

샘플링한 데이터를 기준으로 하위 형상을 포함하는지 여부를 직접 라벨링 함 

그림의 20.35%가 그래프 그림, 4.1%가 막대 차트, 3.11%가 산점도였습니다.5 하위구조의 경우 전체 수치 1,926개 중 237개(35.72%)가 하위구조에 포함되었으며, 이 중 33.14%는 하위구조에 그래프 그림을 포함했고 5.81%는 막대형 차트를 포함했으며 6.83%는 산포도를 포함했다.

# 4. Experimental Results

![f2](\img\2021\SciCap_Generating_Captions_for_Scientific_Figures\f2.PNG)

![t3](\img\2021\SciCap_Generating_Captions_for_Scientific_Figures\t3.PNG)

고전적인 이미지 캡처 모델인 CNN+LSTM 아키텍처를 기준으로 사용 

-> 가공한 데이터 셋이 잘 분석이 되는지 확인하기 위해 

사전 훈련된 ResNet-101(He 등, 2016)은 2048차원 벡터로 수치를 나타내는 이미지 인코더로 사용

여러 학습을 통해 확인작업을 함 

# 5. Conclusion and Future Work

실제 과학적 수치와 캡션을 포함하는 대규모 이미지 캡션 데이터 세트인 SCICAP를 소개

arXiv가 수집하여 배포한 29만 개 이상의 논문으로부터 얻은 200만 개 이상의 이미지를 사용하여 구축




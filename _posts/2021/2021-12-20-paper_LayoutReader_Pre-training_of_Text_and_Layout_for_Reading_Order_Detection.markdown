---
layout: post
title: "paper :LayoutReader: Pre-training of Text and Layout for Reading Order Detection"
date: 2021-12-22 00:20:23 +0900
category: paper
---
# LayoutReader: Pre-training of Text and Layout for Reading Order Detection

소속 : Microsoft Research Asia

학회 :  EMNLP 2021

게재 날짜 : 2021 8월 27일

paper URL : https://arxiv.org/abs/2108.11591

code URL : https://github.com/microsoft/unilm/tree/master/layoutreader


# Abstract 

OCR 에서 글자를 읽는 순서를 감지하는 것은 영수증 및 양식 사진을 이해하는 초석이다.

그러나 정보량이 많아 충분히 큰 데이터에 대해 라벨링하는 것은 힘들다.

WORD문서의 일기 순서가 XML 메타데이터에 포함되어 있으며, PDF 문서로도 변형 가능하다.

따라서 직접 라벨링이 아니라 자동화된 방식으로 데이터를 구축 할 수 있다.

이를 ReadingBank 데이터셋으로 명명하고 모델에서 제안한다.

# 1. Introduction

![f_1](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\f_1.PNG)

사람이 자연스럽게 이해할 수 있는 단어 시퀀스를  포착하는 것을 목표로 하는 읽기 순서 탐지는 시각적으로 풍부한 문서 이해를 위한 기본 작업이다. 

잘못된 읽기 순서는 영수증/송신에서 정보 추출과 같은 문서 이해 작업에 대해 허용되지 않는 결과를 초래할 수 있다.

이를 위해 읽기 순서 탐지를 위한 50만 개의 실제 문서 이미지가 있는 벤치마크 데이터 세트인 ReadingBank를 제안

기존의 인간 레이블 데이터와 달리, 제안된 방법은 자동화된 메타데이터 추출을 통해 단순하지만 효과적인 방법으로 고품질 읽기 순서 주석을 얻는다.

WORD 문서는 이진 형식(Doc 파일)과 XML 형식(DocX 파일)의 두 가지 형식을 가진다. 

읽기 순서 정보가 XML 메타데이터에 포함됨에 따라 XML 형식의 WORD 문서를 독점적으로 사용

WORD 문서를 PDF 형식으로 변환하여 기성 PDF 파서를 사용하여 각 단어의 2D 경계 상자를 쉽게 추출

XML 메타데이터의 텍스트를 PDF의 경계 상자와 정렬하기 위해 신중하게 설계된 색상표를 적용

시퀀스를 생성하여 seq2seq 모델이 사용되는 새로운 읽기 순서 탐지 모델인 LayoutReader를 제안

- 논문의 contribution

1. 읽기 순서 탐지를 위한 500,000개의 문서 이미지가 있는 벤치마크 데이터 세트인 ReadingBank를 제시

2. 판독 순서 탐지 연구를 위한 최초의 대규모 벤치마크

3.  판독 순서 감지를 위한 LayoutReader를 제안하고 다른 매개 변수 설정으로 실험을 수행

4. ReadingBank 데이터 세트와 LayoutReader 모델은 읽기 순서 탐지에 대한 더 깊은 학습 모델을 지원하기 위해 공개적으로 사용

# 2. Problem Formulation

![f_2](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\f_2.PNG)

NLP 데이터 세트의 기본 요구 사항처럼 보이지만 테이블, 다중 열 및 대부분의 OCR 엔진이 적절한 판독 순서를 제공하지 못하는 등 다양한 형식으로 인해 문서 이미지에서 적절한 판독 순서를 얻는 것이 중요

문서 이미지에서 자연스러운 판독 시퀀스를 추출하는 것을 목표로 판독 순서 탐지 작업을 다룬다.

문서 이미지 D가 주어지면 이산 토큰 세트 {t1, t2, t3, ...을 획득한다.}

여기서 각 토큰 ti는 단어 wi와 그 경계 상자 좌표(x i 0 , yi 0 , xi 1 , yi 1 )로 구성된다(왼쪽 상단 모서리와 오른쪽 하단 모서리).

문서 이미지에서 토큰의 텍스트 및 레이아웃 정보를 갖추고 토큰을 읽기 순서로 정렬하려고 합니다.

# 3. ReadingBank

ReadingBank에는 단어 순서와 해당 경계 상자 좌표의 두 부분이 포함

단어 시퀀스를 DocX 파일에서 추출된 Reading Sequence로 나타냅니다. 

해당하는 경계 상자는 DocX 파일에서 생성된 PDF 파일에서 추출

각 단어와 그 경계 상자를 일치시킬 때 단어 중복을 해결하기 위한 색칠 방식을 제안

이 절에서는 문서 수집, 읽기 순서 추출, 색상 체계와의 레이아웃 정렬을 포함하여 데이터 파이프라인을 자세히 소개

ReadingBank에는 총 50만 장의 문서 페이지가 포함되어 있으며, 교육 세트에는 40만 장의 문서 페이지가 포함되어 있으며 검증 세트와 테스트 세트에는 각각 5만 장의 문서 페이지가 포함

## 3.1  Document Collection

1. 영어 문서에 대한 읽기 순서 탐지에 중점을 두기 때문에 신뢰 임계값이 높은 언어 탐지 API 2를 추가로 사용하여 비영어 또는 이중 언어 문서를 필터링

영어 자료만을 가져옴

2. 각 페이지의 충분한 정보를 보장하기 위해 50단어 이상의 페이지만 보관

21만 개의 WORD 문서들을 모았고 여여기에서 데이터 세트를 구축하기 위해 50만 페이지를 무작위 선택 

## 3.2 Reading Sequence Extraction

DocX 파일은 압축된 보관 파일이며, 여기서 워드 시퀀스를 내부 오피스 XML 코드로부터 구문 분석할 수 있습니다.

python-docx3 라이브러리를 이용해서 XML 메타 데이터에서 시퀀스를 추출 하고 레이아웃 정렬 단계의 단어 색상을 변경

문단을 한 줄로 이동하고 테이블 셀을 셀로 이동하고 DocX 파일에서 단어 시퀀스를 얻습니다. 우리는 수열을 [w1, w2, ..., wn]으로 나타내며, 여기서 n은 이 문서의 단어 수

획득된 시퀀스는 레이아웃 정보가 없는 판독 순서이며 판독 시퀀스로 표시

다음 단계에서 경계 상자를 이 시퀀스의 각 단어에 정렬

## 3.3 Layout Alignment with Coloring Scheme

광범위한 컬렉션에서는 동일한 단어가 동일한 문서에 여러 번 나타날 수 있으며, 각 단어에 좌표를 지정할 때 이러한 중복을 해결해야 합니다.

-> 뒤에서 나오는 제안 metric에서 중복 단어에 대한 처리가 없기 때문으로 보임 

각 단어마다 모양 지수를 나타내는 추가 레이블을 지정

예를 들어, 시퀀스 [the, car, hits, the, bus]가 주어졌을 때, 추가 라벨은 [0, 0, 0, 0, 1, 0]이어야 한다.

각 단어 쌍과 해당 단어 모양 인덱스는 고유하며 위치 좌표를 할당할 때 키로 사용될 수 있습니다

![f1](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\f1.PNG)

C : N 7 → RGB를 통해 모양 지수를 RGB 색상에 매핑하고 그에 따라 단어를 색칠

원래 단어 색상의 간섭을 제거하기 위해 먼저 모든 단어를 검은색으로 색칠

i = word index, & = bit wise operation, C = mapping function

DocX 파일의 각 단어의 위치는 고정되어 있지 않습니다.

따라서 컬러 DocX 파일에서 생성된 PDF 파일을 중간 파일로 사용하여 레이아웃 정보를 추출

PDF 변성법을 채택합니다.Net4는 DocX 파일을 PDF로 변환하고 오픈 소스 도구 MuPDF5를 PDF 파서로 사용

PDF 파일에서 단어, 경계 상자 좌표, 단어 색상을 추출

매핑 함수 C는 일대일 대응이기 때문에, 우리는 색칠 방식을 사용하여 모양 지수를 쉽게 얻을 수 있습니다. 

학습의 편의를 위해 페이지의 높이와 폭도 추출

이러한 방식으로 Reading Sequence와 PDF 레이아웃 정보 간에 일대일 일치를 구축

![f2](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\f2.PNG)

w와 w 0은 각각 DocX와 PDF에서 단어

i는 w의 모양 지수이고, c는 PDF 파서가 인식하는 단어 색상 

x0, y0, x1, y1은 왼쪽 위 및 오른쪽 아래 좌표이며

W, H는 단어가 위치한 페이지의 너비 및 높이입니다. 

후처리 단계에서는 페이지별로 데이터를 수집하고 데이터셋을 구축합니다.

## 3.4 Dataset Statistics

![t_1](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\t_1.PNG)

ReadingBank는 이미지 및 단어 및 좌표를 읽기 순서로 포함한 50만 장의 문서 페이지로 구성

교육, 검증 및 테스트를 위해 전체 데이터 세트를 비율 8:1:1로 나눈다. 

표 1은 평균 단어 번호, 평균 문장 수준 BLEU 점수 및 문장 수준 BLEU 점수 분포가 있다.

데이터 균형을 보장하기 위해 단어 번호와 BLEU 점수의 분포는 각 하위 집합에 페이지를 임의로 모을 때 일치

ReadingBank가 사전 교육 또는 미세 조정 중에 데이터 불균형을 겪지 않을 것으로 가정

# 4 LayoutReader

![f_3](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\f_3.PNG)

ReadingBank를 사용하여 판독 순서 감지 작업을 해결하기 위해 LayoutReader를 추가로 제안

LayoutReader는 텍스트 및 레이아웃 정보를 모두 사용하는 시퀀스 투 시퀀스 모델

레이아웃 인식 언어 모델을 활용합니다.LM(Xu 등, 2020)을 인코더로 사용하고 인코더-디코더 구조의 생성 단계를 수정하여 판독 순서 시퀀스를 생성한다.

- Encoder

인코딩 단계에서 LayoutReader는 소스 세그먼트와 대상 세그먼트의 쌍을 레이아웃의 연속 입력 시퀀스로 포장

LM은 토큰 간 가시성을 제어하기 위해 셀프 어텐션 마스크를 세심하게 디자인

그림 3에서와 같이, LayoutReader는 대상 세그먼트의 토큰이 오른쪽 컨텍스트로 이동하는 것을 방지하면서 소스 세그먼트에 있는 토큰이 서로 연결될 수 있도록 합니다

1이 허용을 의미하고 0이 예방을 의미한다면 M 마스크의 세부 사항은 다음과 같다.

![f3](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\f3.PNG)

i, j는 source or target segments 입력 순서

- Decoder

디코딩 단계에서는 소스와 대상이 재정렬 시퀀스이기 때문에 예측 후보가 소스 세그먼트로 제한

모델이 소스 시퀀스의 지수를 예측하도록 요청한다. 확률은 다음과 같이 계산

![f4](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\f4.PNG)

i는 segment index, e는 source segement embeddings, h는 hidden states, k-th는 time, b는 k time step의 bias

# 5. Experiments

...

![t_2](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\t_2.PNG)

## 5.3 Evaluation Metrics

- Average Relative Distance (ARD)

ARD 점수는 재정렬된 시퀀스 간의 차이를 평가하기 위해 제안

다른 시퀀스에서 공통 요소들 사이의 상대적인 거리를 측정

재배열된 시퀀스가 생성되기 때문에 ARD는 요소 누락은 허용하지만 그에 대한 처벌을 추가

시퀀스 A = [e1, e2, ..., en] 및 생성된 재정렬 시퀀스 B = [ei1, ei2, ..., eim]이 주어지면, 여기서 {i1, i2, ..., im} 1 {1, 2, ..., n} ARD 점수는 다음과 같이 계산

![f5](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\f5.PNG)

ek 는 A 문장의 k 번째 seq, I(ek, B)는 B의 인덱스, n은 A의 길이 

![t_3](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\t_3.PNG)

![t_4](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\t_4.PNG)

![f_4](\img\2021\LayoutReader_Pre-training_of_Text_and_Layout_for_Reading_Order_Detection\f_4.PNG)

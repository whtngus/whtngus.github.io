---
layout: post
title: "SPREADSHEETLLM: Encoding Spreadsheets for Large Language Models"
date: 2024-07-10 02:05:23 +0900
category: paper
---

# SPREADSHEETLLM: Encoding Spreadsheets for Large Language Models

Microsoft 

2024년 2월 12일 



# Abstract 

Spreadsheets는 특성이있는 2차원 형식의 격자의, 유연한 형식의다양한 포맷을 지원함 

LLM을 이용해 해당 데이터를 활용하는건 중요한 과제 중하나임

이를 해결하기 위해 SPREADSHEETLLM를 제안함 

SPREADSHEETLLM는Spreadsheets를 혁신적으로 인코딩할 수 있는 방법이라고함 

 

vanilla 방법으로 셀 주소 값 형식을 통합하는 방법이 있음 

  -> 그러니 이런경우 token을 너무 많이 사용하게되어 llm 적용이 힘들어 비현실적인 방법임



이 방법을 해결하기 위해 SHEETCOMPRESSOR  인코딩 프레임워크를 개발함 

SHEETCOMPRESSOR  은 3개의 모듈로 분리되어있음

1. structural-anchorbased compression
2. inverse index translation
3. data-format-aware aggregation

이 방법을 통하면 GPT4 기준 기본적인 접근법 대비 25.6% 성능 향상한다고함 

평균적으로 25x만큼 압축한경우에도 f1스코어 78.9%로 sota 스코어를 달성 



# 1 Introduction

![f_1](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f_1.PNG)

스프레드시트는 데이터를 관리하고 활용하기위해 많이 사용되고 있음 (ms excel, google sheets 등)



기존 LLM 기반 방식은 스프레드시트 기반 QA에 상당히 낮은 답변 퀄리티를 보인다고함 

ms는 이를 해결하기위한 선구적인 SPREADSHEETLLM를 제안함 

vanilla encoding 방법에서 연속적인 스프레드시트 직렬화 방법으로 markdown 인코딩 방식으로 변경함 

그리고 LLM의 토큰 제한을 해결

### 1) Structural Anchors for Efficient Layout Understanding:

![f_2](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f_2.PNG)

대용량의 스프레드시트는 동일한 속성의 row와  column들이 발견되어 이는 테이블 구조를 이해하는데 도움이됨 

불균형을 확인하기 위해 row와 column의 바운더리를 먼저 확인함 (그림2의 b)

그리고 거리가 멀리있는경우 삭제를하고 압축된 "skeleton" 버전의 스프레드시트를 생성함 (그림2의 b)

### 2) Inverted-Index Translation for Token Efficiency:

vanilla 인코딩 방법은 모든 셀을 다 인코등 함으로 토큰을 많이 사용하게됨 

이를 해결하기 위해 기존 전통적인 방식의 

row-by-row  colunn-by-column을 직렬화하는  방식과 json 포맷으로 모든 셀을 변환하는 방식 사용하지 않음 



dictionary 기반 인덱싱을 활용하여 비어있는셀과 중복된 셀에 대한 중복 토큰을 제거함

-> 이럼 구조가 복잡해져서 llm이 이해하는데 더 어려울 것 같아 보임

### 3) Data Format Aggregation for Numerical Cells:

인접한 수치형 셀은 같은 숫자 포멧을 사용하게됨 

이런 셀들의 정확한 수치를 파악하는건 spredsheet의 구조를 파악하는데 크게 영향이 없음 

-> 숫자 형식과 문자 형식 셀들을 추출해 동일한 형식의 셀들끼리 클러스터링을 함 

그림2에서 오른쪽 방식을 통해 데이터유형별로 파싱하여 구조를 쉽게 알 수 있는 방식으로 변경



이런 3가지 방식을 지원하는 SHEETCOMPRESSOR 프렘워크를 쓰면 기존 방식대비 96% 토큰을 절약할 수 있다고함 그리고 성능또한 기존 sota 대비 12.3% 상승함



기존 CoT 방식 대신 Chain of Spreadsheet(CoS) 방법을 제안함 

-> detection-match-reasoning pipeline

논문에서의 컨트리뷰션

- SPREADSHEETLLM방법을 제안하여 LLM이 spreadsheet data데이터를 이해할 수 있도록 함 
- sota 스코어를 달성함 
- SPREADSHEETLLM을 광범위한 downstream task에 적용하기 위해  CoS를 제안하고 검증함 

# 2 Related Work

### Spreadsheet Representation

Spreadsheet representation은 다양한 모델에 대해 스프레드시트를 구체적으로 어떻게 변경할지와 관련이 있다.

 그리고 기존에 다양한 연구 방법들이 있었음 

MaskRCNN 방법을 이용해서 visual encoding 방법이 있었으나 VLM을 확용하기엔 잘 작동하지 않았음 

의미적인 rows와 columns을 파싱해 LSTM 모델을 확용하는 방법 

그리고 효과적인 방법으로 Markdown과 HTML으로 변환하는 방식이 있음 

그러나 위 방법들은 스프레드 시트에 적합하지 않다고 함 

![f_5](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f_5.PNG)

Markdown, html과 xlm로 변경하는경우 그림5와 같이 많은 토큰을 사용하게됨 

![t_6](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\t_6.PNG)

 ICL 실험한 결과  테이블 6과 같은 결과가 나옴 

markdown 방식의 평가 방법이 가장 성능이 좋음 그리고 토큰더 더 적게 사용함 

### Spread

###  dsheet Understanding

대부분의 LLM은 하나의 테이블 셋팅으로 제한됨 

-> 여러 테이블을 인코딩하기엔 토큰이 너무 많이 사용되기 때문에 

여러 테이블의 레이아웃 구조는 상당히 혼란스럽고 어려운 문제가있음 

이런 모든 테이블을 이해하기 위한것을 목표로하는 연구가 있음

### Spreadsheet Downstream Tasks

일련의 Spreadsheet테스크에서 Spreadsheet를 이해하고 답변하는것은 가능함 

- table question answering analysis
- table extraction
- formula or code generation
-  error detection

등의 테스크가 있다고함

이 중 논문에서는  spreadsheet QA 테스크를 메인으로 잡음 

### LLMs’ Token Efficiency

long context에서 LLM의 성능이 상당히 내려가기 때문에  성능 향상을 위해 costs를 감소시키기 위한 노력이 계속 되고 있음 (plompt compression)

기존 연구로는 장황환 발화를 줄이는 방법이나 프롬프트 최적화를통한 압축방법이 있으나 기존연구들은 tabular데이터를 처리하고 압축하는 방법론들은 없음 

그리고 프롬프트 압축 과정에서 데이터 손실이 일어나게됨 

그 외에도 DBCopilot 모델의 text-to-SQL이 있으나 성능이 매우 떨어지는 문제가 있으며 복잡한 구조의 쿼리나 여러 테이블을 다루지 못함 

# 3 Method

spreadsheet데이터셋을 Markdown 과 비슷한 형식으로 변환하는 인코딩 방법을 제안함 

결합되지 않은 3개의 모듈을 제안함

1. structural-anchor-based extraction
2. inverteindex translation
3. data-format-aware aggregation

## 3.1 Vanilla Spreadsheet Encoding with Cell Value, Address, and Format

spreadsheet를 LLM에 인코딩하기 위한 일반적인 방법은아직 없음 

주로 HTML, XML, and Markdown 3가지로 인코딩하고, 위의 그림5와 table 6같이 평가한경우 일반적으로 markdown이 더 효율적인것을 알 수 잇음 

![f1](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f1.PNG)

S ∈ R^m,n : 스프레드시트

T ∈ R^1 : cell의 text representation

i, j : row, column index

S : row와 column의 범위



위와같은 인베딩 방식은 성능이 떨어지는 결과를 초래함 

## 3.2 Structural-anchor-based Extraction

큰 spreadsheet의 경우 수치형 동형의 row나 column이 있어서 이를 이용하면 레이아수 구조를 이해하는데 수월함 

이런 구조를 임베딩하기 위해  heuristic-based방법을 제안함 

![f3](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f3.PNG)

![f3_1](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f3_1.PNG)

r은 특정 row  에 대한 임베딩

c는 특정 column에 대한 임베딩



위 앵커포인트를 정하기 위해 row column 범위를 정하고 나머지를 자름 

이때 k파라미터를 설정해서 k이상 떨어진 경우 바운더리에서 떨어짐으로 제외하는 방식으로 처리함 

![t_7](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\t_7.PNG)

k파라미터에 따른 성능차이는 위와 같음 

k가 클수록 성능은 올라가나 당연히 사용하는 토큰은 많아질것으로 보임 

단 Huge 사이즈에서는 입력 토큰이 너무길어져서 8k 에서 스코어가 내려간듯 (F1 스코어)

![f4](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f4.PNG)

Se : k 단위로자른 압축된 스프레드시트

Te : Se를통해 매우 압축된 text representation



이방식을 사용하면 75%의 스프레드시트 내용을 걸러내지만 97%의 row columns를 유지한다고함

-> ??!?



## 3.3 Inverted-index Translation

Spreadsheets는 매우 많은 빈 row와 column 들을 보함하고 있음 

3.1에서 소개한 예전 방식들은 이런 빈값들을 전부 표시해야함 

-> 정보는 없으나 토큰 정보를 계속 소비시킴 

또한 반복된 셀들이 계속 발생하여 인코딩됨 



 two-stage Inverted-index-based Translation method을 통해 이를 해결하고자 함 

- first stage 

전통적인 방법으로 matrix-style encoding으로 실행 

이때 dictionary  format으로 데이터를 변환함 

- second stage

같은 value를 가진 sel들을 합치는 작업을 실행함 

![f6](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f6.PNG)

이러면 구조 정보를 잃어서 오히려 안좋을것 같은데 신기함..

이런 방식을 사용하면 데이터를 압축하면서도 손실이 없는 압축이됨 (lossless compression)

![t_1](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\t_1.PNG)

Table1에서 토큰 수가 상당히 압축됨을 알수 있음 

## 3.4 Data-format-aware Aggregation

위의 그림2의 (3)번처럼 cells들은 보통 같은 포맷을 사용하기 때문에 

컬럼정보들을 구체적으로 저장할 필요가 없음 

이떄 18,476 과 18,674 같은 세부적인 정보는 잃을 수 있으나 QA성능에는 큰 영향이 없음 

시간, 핸드폰번호 등의 타입정보만 가지고있어도 됌 

그래서 타입을 사전에 지정해두고 클러스터링함 

Number Format String (NFS)방식을 사용해서 ClosedXML or OpenPyXL을 사용해서 포맷을 정의 ''20242.14' -> 'yyyy-mm-dd' 와 같은 형식

![f7](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f7.PNG)

R : 미리 정의된 룰들 

## 3.5 Chain of Spreadsheet

3.2~ 3.4와같은 인코딩을 거치고 SPREADSHEETLLM을 이용해 downstream tasks를 하기위해 CoS를 제안함 

2가지 전략으로 이루어짐

#### Table Identification and Boundary Detection

압축된 spreadsheet와 테스크정보를 같이 llm에 입력으로 넣음 



모델은 질문과 관련된 테이블을 파악하고 경계를 결정함

이단계에서는 절절한 데이터를 골라내고 유지하는것을 목표로함 

#### Response Generation

선택된 테이블을 기반으로 답변을 생성하기 위해 다시 LLM에 입력으로 집어 넣음 

 -> 불필요한 정보가 없기때문에 정확한 답변을 추론 



# 4 Experiments

## 4.1 Spreadsheet Table Detection

### 4.1.1 Dataset

(Dong et al.,2019b 데이터셋으로 실제 데이터셋과 비슷하다고함 

이데이터셋은 데이터 크기에 따라 : Small, Medium, Large, and Huge 4가지로 구분되어있음 



## 4.1.2 Experiment Setup

LLM이 아직 스프레드시트에 체계적으로 적용되지 않았기 때문에 TAPEX and Binder 을 베이스라인으로 설정함 (2020년 2022년 )

두 데이터는 단일 테이블 기반의 데이터 



모델은 GPT4 모델을 사용



.. 데이터셋 스킵



# 5 Results

![t_2](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\t_2.PNG)

spreadsheet table  detection task에 대한 모델별 정확도 

![f_7](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\f_7.PNG)

![t_3](F:\code\whtngus.github.io\img\2024\SPREADSHEETLLM__Encoding_Spreadsheets_for_Large_Language_Models\t_3.PNG)

요약을 한경우 스코어가 더 잘나옴을 확인할 수 있음 

Table 4는 QA 성능 

- 결론

GPT4에서 CoS를 쓰는경우 베이스란대비 22% 성능 향상

 fine-tuning하는경우 6%정도 선성능향상









# 참고

1. ICL 실험

문맥 학습(In-Context Learning, ICL)은 모델이 주어진 몇 가지 예시만으로 새로운 작업을 학습하고 적응할 수 있는 기계 학습 패러다임입니다. 이는 모델이 명시적인 재훈련 없이, 제공된 예시들을 바탕으로 작업을 수행할 수 있게 합니다. 예를 들어, 스프레드시트 테이블 탐지 작업에서 ICL을 사용하는 경우, 모델에게 몇 가지 테이블 예시를 보여주면, 모델은 이전에 본 적 없는 새로운 스프레드시트 데이터에서 테이블을 식별하고 추출할 수 있게 됩니다.

2. Table Detection

테이블을 식별하고 추출하는task
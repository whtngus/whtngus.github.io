---
layout: post
title: "paper : Family Shopping Recommendation System Using User Profile and Behavior Data"
date: 2022-03-27 00:01:01 +0900
category: paper
---
Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data

# Family Shopping Recommendation System Using User Profile and Behavior Data

2017년 8월 24일

Information Retrieval (cs.IR)

https://arxiv.org/pdf/1708.07289.pdf

# Abstract 

빅데이터가 쌓임에 따라 매출 효율화를 위해 추천시스템이 점점 많이 사용됨

기존 추천시스템은 개인화 추천 시스템에 초점을 맞추고 있지만, 개인화가 아닌 그룹화를 시킨 추천 시스템이다.

-> 이를 해결하기 위해 그룹 단위가 아니라 가족 단위로 줄임 (2017년 논문이라 그런것 같음 최근에는 개인화)

쇼핑 기록 테이블, 고객 프로파일 테이블 및 가족 관계 테이블로 구성된 실제 쇼핑몰의 데이터 세트를 사용

사용자 동작의 유사성과 사용자 프로파일의 유사성을 통합하여 사용자 기반의 협업 필터링 모델을 구축합니다. 실제 쇼핑몰 데이터 세트에 대한 접근 방식을 평가



# 1. Introduction

추천시스템은 빠르게 개발되고 있으며, 많은 종류 기반의 추천시템이 생기고 있다.(모바일, 뉴스, 음악 등)

 그룹 추천 시스템 : 그룹 내 각 사용자의 선호도를 고려

그룹 구성원의 요구를 최대한 충족시키는 것이 그룹 추천제도의 핵심 과제이다.

해당 논문에서는 가족단위 추천 알고리즘을 제안 (논문에서 가족 그룹단위를 계속 강조)

> 가족단위로 하는 이유는 쇼핑할때 고객의 결제 내용이 잠재적으로 가족 정보에 영향을 가지고 있기 때문
>
> -> 그들은 우리에게 누가 그의 아내인지, 누가 그의 자녀인지 말해주지 않는다.
>
> -> 성인 남성이 기저귀를 구입 (가족 구성원 - 아이)

실제 쇼핑 기록 테이블을 기준으로 연구됨 

논문의 컨트리뷰션 

- 가족 단위의 개인화 추천 시스템을 제안 
- 가족단위 쇼핑 결제 정보 데이터를 결합
- 실제 결제 데이터셋에서 가족단위 분석이 유용하다는 것을 분석 및 증명

# 2. Related Work

## A. Memory-based Collaborative Filtering

Memory-based collaborative filtering (CF) 알고리즘은 자주 사용되는 유명한 알고리즘이다.

user-item 데이터를 이용해 사용자가 좋아하는 아이템을 추천

모든 유저 그룹중 비슷한 유저 그룹을 찾아 그룹의 사람들이 흥미있어하는 아이템을 추천

(ex -  neighborhood-based recommendation system 일반적으로 많이 사용)

- neighborhood-based recommendation system  작동 예시

> 1. 비슷한 Representation vector를 갖는 user or item  Wij 를 찾는다.
> 2. rating을 모르는 user-item에 대해 예측 유사한 n개의 weight를 가진 벡터를 추천
>
> - Similarity Computation
>
> 유사도 계싼은 CF에서 중요한 스텝 !
>
> 유사도 계산 공식에 따라 결과가 달라짐
>
> 일반적으로 코사인 유사도를 사용 

### Vector cosine-based similarity 

![f1](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f1.png)

두 항목간의 유사성을 비교 ( 항목 또는 사용자를 벡터로 취급하고 두 벡터 사이의 각도의 코사인을 계산)

벡터의 요소는 항목의 사용자 등급이 됌  

 · :  dot-product -> Item Vector i와 j의곱

U : User set 

R u,i : user u와 item i가 주어진 경우의 rating

아래의 fig. 1 참조 

![f_1](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f_1.png)

그러나 코사인 유사도는 한계상황이 있다 

사용자마다 다른 등급 기준을 사용하는 경우 두 항목의 유사성을 나타낼 수 없음 -> 사용자의 평점주는 경향에 따라 평균이 많이 달라지기 때문

이를 제거하기 위해 각 등급의 쌍에서 대응하는 사용자 평균을 빼준다.

### Correlation-based similarity

![f2](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f2.PNG)

pearson 상관 관계를 통해 유사도를 계산하는 방법 

Pearson 상관관계 : 두 변수가 서로 선형적으로 연관되어 있음을 나타냄

사용자 알고리즘의 경우 사용자 u와 아이템 v사이의 Pearson 상관 관계를 나타냄 

위 수식에서 사용자별 편향을 줄이기 위해 평균값을 빼준걸 알 수 있음

I : 전체 항목 세트

ru (hat) : 각 아이템 유저의 평가(rating)의 평균

r u i : 사용자가 부여한 등급 

 -> 위의 Fig. 1 참조

![f3](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f3.PNG)

U : 모든 user set 

r i (hat) : 유저가 평가한 모든 점수의 평균 

Pearson correlation-based CF algorithm은 매우 효율적이여서 추천시스템에서 많이 사옹됨

그러나 위의 두 가지 방법에는 사용자와 항목에 대한 평가 매트릭스가 필요

-> 실제로 등급 데이터는 쉽게 이용할 수 없고 매우 희박한 경우가 많아서

암묵적인 데이터로부터 유용한 정보를 얻을 수 있다. 예를 들어, 만약 두 명의 사용자가 같은 상품을 산다면, 그들은 쇼핑몰에서 몇 가지 공통적인 선호도를 가지고 있다. 다음 방법은 정확한 유사성을 계산하여 이러한 문제를 해결할 수 있다.

### Jaccard similarity

![f4](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f4.PNG)

자카드 유사도는 매우 간단한 알고리즘  두 사용자가 동일한 상품을 많이 구매하고 구매하는 상품의 양이 적을수록 유사성이 높아짐

등급정보가 없는경우 쇼핑 기록을 처리하는데 유용함 

Nu : 사용자 u 가 구매한 아이템 세트

Nv :  사용자 v가 구매한 아이템 세트

|Nu n Nv| :  사용자 u 와 v가 구입한 교집합

|Nu u Nv| :  사용자 u 와 v가 구입한 합집합

u, v가 동일한 아이템을 구매하지 않으면 유사도가 0

u, v가 다른 아이템을 구입하지 않은 경우 유사도는 1

-> 즉 사용자간 유사성을 효과적으로 반영 가능

### Euclidean distance similarity

사용자와 항목 간의 관계는 필요하지 않음

유사성 문제는 2개의 벡터 거리 문제로 변환 (각 벡터의 실제 거리값으로 계산)

해당 논문에서는 Euclidean distance similarity를 사용하기로 결정함

![f5](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f5.PNG)

특정 항목 i에 대한 사용자 k의 등급을 정확하게 예측하기 위해 해당 항목 i에 대한 모든 등급의 가중 평균을 구할 수 있다

wk,u : 사용자 k와 사용자 u사이의 가중치 

rk(hat) :  모든 사용자가 평가한 평균 등급 

U : item i 와 관련된 모든 유저의 집합

특정 항목 i에 대한 사용자 k의 등급을 정확하게 예측하기 위해 해당 항목 i에 대한 모든 등급의 가중 평균을 구해서 빼줌 (유저의 평균이 아님 모든 등급의 평균)

![f6](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f6.PNG)

위 식을 이용해 predict를 함 

- Top-N 추천시스템

특정 사용자를 끌어들이는N개의 최상위 아이템 세트를 추천

주로 사용자 기반, 항목 기반 Top-N 두 가지 클래스로 나눌 수 있다

Pearson Correlation Similarity or Vector Cosine-based Similarity를 사용해 특정 사용자와 가장 유사한 k명의 사용자를 선택

항목 기반인경우 피어슨 상관 유사성 또는 벡터 코사인 기반 유사성에 의해 예측된 유사성에 따라 각 항목에 대해 가장 유사한 k개의 항목을 선택

가장 유사한 k개의 아이템을 조합하여 특정 사용자가 이미 구입한 세트 U의 각 아이템을 제거함으로써 세트 A를 식별

## B. Group-based Collaborative Filtering

그룹 베이스의 콜라보레이티브 필터링은 이 논문에서 제안하는 기법

경우에 따라서는 콜드 스타트 문제를 해결할 수 있다고 제안 -> 그룹 검출과 그룹 프리퍼런스 집약은 그룹 베이스의 콜라보레이티브필터링의 2개의 중요한 부분

1. Group Detection

Group-based Collaborative Filtering은 이 논문의 핵심 포인트 

단일 사용자 추천 시스템 유사도 계산 방법과 다른 방식으로 접근하게 됨

> 1. Group Detection
>
> 그룹 추천 시스템에서는 그룹핑을 제공해 주지 않는다. 그래서 특정 그룹에 사용자를 직접 추가해야 사용이 가능 
>
> 이를 직접 수행할 수 없어서 일반적으로 클러스터링을 통해서 그룹핑을 함 
>
> ex) k-means 를 사용한 클러스터링
>
> 2. Group Preference Aggregation Strategy
>
> 그룹 추천 시스템에서 선호 집계는 그룹 구성원의 선호도에 따라 그룹 선호도를 추출하는 것을 의미
>
> 이러한 전략중 5가지 전략을 제안(해당 논문의 참조 논문에서)
>
> > - Average Strategy
> >
> > 그룹핑된 멤버의 레이팅의 평균값을 사용 
> >
> > - Most Pleasure Strategy
> >
> > 그룹 구성원이 준 등급 중 가장 좋게 준 등급으로 사용 
> >
> > - Least Misery Strategy
> >
> > 그룹 구성원이 준 등급 중 가장 낮은 등급을 사용 
> >
> > - Average Without Misery Strategy
> >
> > 특정 임계값보다 높은 그룹 구성원 등급의 평균이 이 그룹의 평균으로 간주 
> >
> > - Most Respected Person Strategy
> >
> > 그룹의 등급은 이 그룹에서 가장 존경받는 사람의 등급에 따라 결정됩니다.
> >
> > -> 대표자를 선정
>
> 3. Group Preference Aggregation Method
>
> 그룹 선호도 집계 방법을 권장 결과 집계, 등급 집계 및 그룹 선호도 모델링의 세 가지 범주로 요약
>
> 집계 및 등급 집계를 위해 먼저 그룹 사용자별 추천을 생성하거나 예측 등급을 계산한 후 그룹 추천 집계 또는 그룹 예측 등급을 생성
>
> 그룹 구성원 기본 설정 모델을 집계하여 그룹 기본 설정 모델을 생성합니다. 그러면 그룹 선호 모델별로 추천

# 3. PROPOSED APPROACH

## A. Datasets

데이터 세트는 실제 쇼핑몰의 클라이언트 프로파일, 트랜잭션 데이터 세트, 방문 데이터 세트, 패밀리 데이터 세트 및 참여 데이터 세트로 구성

- Client profile dataset 

가입일, 성별, 연령, 전화, e-메일, 이웃, 등록원 및 수입의 7가지 속성이 있는 4505개의 클라이언트 프로파일

사용자 유사도 계산시 사용되는 클라이언트 데이터 셋

- Transaction dataset

제품 브랜드, 제품 유형 및 메인 카테고리의 쇼핑 기록이 25550개 포함

 60427개의 레코드가 있음 -> 사용자의 결제 데이터 

- Visit dataset 

60427 records 의 체크인 체크아웃 데이터 셋 

- Participation dataset

 사용자가 참여하는 활동을 기록

- Family dataset

 6378개의 패밀리 그룹 데이터 셋이있고 구성정보 데이터를 포함함

## B. Data Preprocessing

 해당 논문의 데이터 전처리는 두 부분으로 나뉨

1. Data Cleaning

![t_1](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\t_1.PNG)

결측값이 있는 항목의 일부 정보는 삭제되거나 0, 평균값 등의 특정 값으로 대체

2. Data Normalization

클라이언트 프로파일데이터셋의 경우 클라이언트의 속성을 수치변수와 카테고리변수로 구분

sex, neighborhood, register source 등의 카테고리 변수는 원샷 부호화로 부호화

Atribute telephone 및 e-mail의 경우 사용자가 정보를 남겼는지 여부에 따라 0 또는 1로 인코딩

## C. User Behavior-based Similarity Matrix

4개의 카테고리(제품 브랜드, 제품 타입, 메인 카테고리, 액티비티)로 이루어진 사용자 행동 기능에 따라 섹션 트리플을 사용

## D. User Profile-based Similarity Matrix

c에서 제시한 방법을 통해 사용자 프로파일 벡터가 생성된 값을 통해 사용자 속성을 공식화할 수 있다.

그 후 유클리드 거리로 사용자 거리 행렬을 계산

![f7](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f7.PNG)

W와 B 행렬 치수는 같고 

Wuv : 유저 U와 유저 v의 유사도 

U : 모든 사용자 집합

 Wprof ile : 유사성 매트릭스를 구별하기 위해 사용되는 유사성 매트릭스

## E. Hybrid Similarity Matrix Algorithm

5개의 유사도 매트릭스를 사용 

profile, brand,, type,, category,, activity 

## F. Family Recommendation Algorithm

그룹 유사도 매트릭스의 경우 패밀리 데이터 세트에 따라 패밀리 구성원을 알고 있기 때문에 그룹 발견 단계를 밟을 수 있다.

![f_2](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f_2.PNG)

패밀리(f)의 모든 벡터를 합한 후 사용자와 유사성기반 알고리즘을 통해 그룹핑을 하는 방식 

그리고 위에서 언급한 5가지 유사도를 이용해 추천을 제공 

# 4. EXPERIMENTS

## A. Models

세 가지 다른 모델을 제안하고 그것들을 평가 지표로 비교

해당 논문에서는 마지막에 제안할 모델 스코어가 가장 높다고 강조

- User Model

User Behavior-based + User Profile-based Recommendation

- Hybrid User Model

User Behavior-based+User Profile-base + Hybrid Similarity Matrix Algorithm Recommendation 

- Hybrid Family Model

User Behavior-based+User Profile-based + Hybrid Similarity Matrix Algorithm + Family Recommendation 



 권장되는 항목은 세 가지 범주(제품 브랜드, 제품 유형, 메인 카테고리 범주) 하이브리드 패밀리 모델의 경우 브랜드, 유형, 카테고리, 액티비티, 프로파일을 집계해 품목을 추천

## B. Dataset Splitting

![f__3](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f__3.PNG)

트랜잭션 데이터 세트를 테스트 세트로 한 부분과 두 부분으로 나누고 다른 부분은 트레이닝 세트

타임스탬프를 사용하여 데이터 세트를 시간별로 분할하기로 결정

## C. Evaluation Metric

![f8](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f8.PNG)

RMSE (Root Mean Square Error), MAE (Mean Absolute Error), recall rate, precision rate등을 많이 사용함 

R(u) : 용자 u에게 권장되는 아이템 세트

T(u) : 용자가 이미 구입한 아이템 세트

## D. Experimental Procedure

![f_4](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f_4.PNG)

![f_5](\img\2022\Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data\f_5.PNG)
















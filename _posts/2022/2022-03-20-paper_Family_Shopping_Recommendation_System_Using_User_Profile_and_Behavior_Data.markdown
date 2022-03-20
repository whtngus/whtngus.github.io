---
layout: post
title: "paper : Family Shopping Recommendation System Using User Profile and Behavior Data"
date: 2022-03-20 00:01:01 +0900
category: paper
---
Family_Shopping_Recommendation_System_Using_User_Profile_and_Behavior_Data

# Family Shopping Recommendation System Using User Profile and Behavior Data

2017년 8월 24일



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














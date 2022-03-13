---
layout: post
title: "paper : CImage Recommendation Algorithm Combined with Deep Neural Network Designed for Social Networks"
date: 2022-02-24 00:20:23 +0900
category: paper
---

# Image Recommendation Algorithm Combined with Deep Neural Network Designed for Social Networks

짧은 요약 

https://downloads.hindawi.com/journals/complexity/2021/5196190.pdf

Accepted 23 Jun 2021

코드 없음 ㅠ

# Abstract 

기존 이미지 추천 알고리즘은 텍스트 기반 추천 방법을 사용

소셜네트워크의 심층신경망을 기반으로 한 영상추천 알고리즘을 주로 연구

첫째, 데이터 세트의 타임스탬프 정보에 따라 각 사용자의 인터랙션 레코드가 가장 가까운 시간별로 정렬

이미지 추천을 위해 두 개의 LSTM 신경망이 설정되며, 이 두 네트워크는 각각 이러한 형상 벡터를 입력으로 사용

실험은 CNN 특징 벡터와 함께 제안된 LSTM 모델이 다른 알고리즘을 능가할 수 있음을 보여준다.



# Introduction

소셜 네트워크는 네트워크에서 노드 관계의 수학적 모델링에 초점을 맞춘다. 

-> 그래프와 행렬과 같은 수학적 방식을 사용

소셜 네트워크의 사회적 관계 추천에 대한 연구를 수행하여 소셜 관계의 잠재적 가치를 더 탐구할 필요가 있다



# 5. Conclusions

기존의 텍스트 기반 이미지 추천 방법의 단점을 보완하기 위해 딥러닝을 기반으로 이미지 추천 알고리즘을 주로 연구

다중 속성 이미지 분류, 표적 감지 알고리즘 최적화, 컨볼루션 신경망에 기반한 차원 감소 알고리즘

로컬 정보와 글로벌 정보의 가중치는 포괄적인 측정의 정확도를 향상시키고 마지막으로 네트워크의 실제 계층 구조를 마이닝하도록 최적화


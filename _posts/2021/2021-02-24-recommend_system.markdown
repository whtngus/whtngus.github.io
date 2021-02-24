---
layout: post
title: "recommend system : 토크ON세미나_SKplanet Tacademy 정리_4~6강"
date: 2021-02-23 19:20:23 +0900
category: recommend system
---
# recommend system : 토크ON세미나 _ SKplanet Tacademy 정리
url : https://www.youtube.com/watch?v=43gb7WK56Sk&ab_channel=SKplanetTacademy
## 4강 -협업 필터링 (KNN, SGD, ALS)

3강 생략 

아는내용 생략

- 정의

사용자의 구매 패턴이나 평점을 가지고 다른 사람들의 구매 패턴, 평점을 통해서 추천을 하는 방법.

추가적인 사요앚의 개인정보나 아이템의 정보가 없이도 추천할 수 있는게 큰 장점이며 2006년부터 2009년동안 열린 Netflix Prize Competition에서 우숭한 알고리즘



- 종류

최근접 이웃기반

잠재요인 기반



### Neighborhood based method

- 정의

메모리 기반 알고리즘으로 협업 필터링을 위해 개발된 초기 알고리즘.

- 알고리즘

> 1. User-based collaborative filtering
>
> 사용자의 구매 패턴(평점)과 유사한 사용자를 찾아서 추천 리스트 생성
>
> 2. Item-based collaborative filtering
>
> 특정 사용자가 준 점수간의 유사한 상품을 찾아서 추천 리스트 생성 



- 장점

간단하고 직관적인 접근 방식 때문에 구현 및 디버그가 쉬움

특정 Item을 추천하는 이유를 정당화하기 쉽고 Item 기반 방법의 해석 가능성이 두드러짐

추천 리스트에 새로운 item과  user가 추가되어도 상대적으로 안정적

- 단점

User 기반 방법의 시간, 속도, 메모리가 많이 필요

희소성 때문에 제한된 번위가 있음

-> John의 Top-K 에만 관심이 있음 (많이 보는 상품은 다 많이보게 되는 문제)

-> John과 비슷한 이웃중에서 아무도 평가를 하지 않으면, 해당 상품은 등급 예측을 제공할 수 없음



### Latent Factor Collborative Filtering

- 정의

잠재 요인 협업 필터링은 Rating Matrix에서 빈 공간을 채우기 위해서 사용자와 상ㅁ풍르 잘 표현하는 차원(Latent Factor)을 찾는 방법

잘 알려진 행렬 분해는 추천 시스템에서 사용되는 협업 필터링 알고리즘

- 원리

사용자의 잠재요인과 아이템의 잠재요인을 내적해서 평점 매트릭스를 계싼

SVD, SGD, ALS 등등이 있음 



- SGD

```
	- 정의
고유값 분해(eigen value Decomposition)와 같은  행렬을 대각화 하는 방법
	- 실행 순서
1. User Latent 와 Item Latent의 임의로 초기화
2. User Latent 와 Item Latent를 매트릭스 곱한 내요을 Gradient Descent 진행
	- 장점
매우 유연한 모델로 다른 Loss function을 사용할 수 있음
parallelized가 가능함
	- 단점
수렴까지 속도가 매우 느림
```

- ALS

```
	- 정의
기존의 SGD가 두개의 행렬(User Latent, Item Latent)을 동시에 최적화 -> ALS는 두 행렬 중 하나를 고정하키고 다른 하나의 행렬을 순차적으로 반복하면서 최적화를 진행 
	- 실행 순서
1. 초기 아이템, 사용자 행렬을 초기화
2. 아이템 행렬을 고정하고 사용자 행렬을 최적화 
3. 사용자 행렬을 고정하고 아이템 행렬을 최적화
4. 위의 2~3 과정을 반복
위 방식을 사용하면 수식을 이용하면 답이 정해져 있어서 빠르게 최적호 ㅏ가능
```

- 협업 필터링

```
	- 장점
도메인 지식이 필요하지 않음
사용자의 새로운 흥미를 발견하기 좋음
시작단계의 모델로 선택하기 좋음
	- 단점
새로운 아이템에 대해서 다루기가 힘듬
side features(고객 정보, 추가 정보, 메타 정보)를 포함시키기 어려움
```



## 평가함수

- 평가함수를 알아야 하는 이유

모델에 대한 평가를 위해 

도메인이나 목적에 맞는 평가함수가 필요

- MAP

```
AP : Precision @k's를 평균낸 값 (추천한 K개의 영화의 Precision을 평균)
MAP : N명의 사용자의 AP를 평균낸 값
```

- NDCG(Normalized Discounted Cumulative Gain)

```
검색알고리즘에서 주로 사용됨
	- CG(Cumulative Gain)
추천 해준경우 얼마나 맞은건지를 계산 
	- DCG
정규화 과정을 취해서 앞에서 맞을수록 분모값이 더 작아지게 해서 CG에서 맞춘 순서에 중요성을 더한 알고리즘
	- NDCG
DCG는 추천결과의 위치를 고혀할 때 다양한 요인에 따라 권장 사항 수가 상요자수마다 다를 수 있음.
DCG는 권장 사항의 수에 따라 결과가 달라지는 문제 발생(사람마다 추천해줘야 하는 갯수가 다를 수 있음) -> 정규화 필요성이 있음
NDCG = DCG / iDCG
iDCG는 이상적인 순서에서 얼마만큼의 값을 가지는지
```




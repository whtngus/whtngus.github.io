---
layout: post
title: "recommend system : 토크ON세미나_SKplanet Tacademy 정리_2강"
date: 2021-02-23 19:20:23 +0900
category: datascience
---
# recommend system : 토크ON세미나 _ SKplanet Tacademy 정리
url : https://www.youtube.com/watch?v=43gb7WK56Sk&ab_channel=SKplanetTacademy
## 2강 - 컨텐츠 기반 추천 시스템  (유사도 함수, TF-IDF)

- 정의

컨텐츠 기반 추천시스템은 사용자가 이전에 구매한 상품중에서 좋아하는 상품들과 유사한 상품들을 추천하는 방법.

주로 items을 벡터 형태로 표현하여 유사한 베터를 추천함 (Represented Items)



### 유사도 함수

- 유클리디안 유사도

```
	- 문서간의 유사도를 계산
유클리디안 유사도 = 1 / (유킬리당ㄴ 거리 + 1e-05)
	- 장점
계산하기가 쉬움
	- 단점
p와 q의 분포가 다르거나 범위가 다른 경우에 상관성을 놓침 

```

- 코사인 유사도

```
	- 문서간의 유사도를 계산
similarity = cos(seta) = (A B)  /  ||A|| ||B||
	- 장점
벡터의 크기가 중요하지 않은 경우에 거리를 측정하기 위한 메트릭스로 사용
	- 단점
벡터의 크기가 중요한 경우에 대해서 잘 작동하지 않음
```

- 피어슨 유사도

```
문서간의 유사도를 계산
-> 수식 쓰기 귀찮...
```

- 자카드 유사도

```
문서간의 유사도를 계산
집합에서 얼마만큼의 결합된 부분이 있는지로 계산
J(A, B) = | A n B |  /  | A U B|
```

그 외에도 많은 유사도 함수가 존재

Divergence, Dice, Sorensen ....

상황에 맞게 여러가지 모델을 사용하기



### TF-IDF 

알고있어서 생략



코드 : https://www.kaggle.com/embed/chocozzz/00-tf-idf-1









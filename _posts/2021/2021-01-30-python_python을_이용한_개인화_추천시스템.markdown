---
layout: post
title: "python을 이용한 개인화 추천시스템"
date: 2021-01-30 19:20:23 +0900
use_math: true
category: python_deeplearning_chatbot
comments: true
---

# 책 - python을 이용한 개인화 추천시스템 <br>

책 관련 코드 링크 : http://www.crbooks.co.kr/main/ -> 책 및 데이터 홈페이지에서 다운로드 가능 



## 1장 추천 시스템(recommender system) 소개



추천 시스템 : 사용자의 과거 행동 데이터나 다른 데이터를 바탕으로 사용자에게 필요한 정보나 제품을 골라서 제시해주는 시스템



### 주요 추천 알고리즘

- 협업 필터링(Collaborative Filtering: CF)

아이탬에 대한 소비자의 평가를 받아 평가 패턴이 비슷한 소비자를 한 집단으로 클러스터링

-> 집단의 취향을 활용하는 기술

- 내용 기반 필터링(Content-Based filtering: CB)

제품의 내용을 분석해서 추천하는 기술, 제품 중 텍스트 정보가 많은 제품을 분석하여 추천할 때 많이 사용

- 지식 기반 필터링(Knowledge-Based filtering: KB)

협업, 내용기반 필터링은 왜 그제품을 조아하는지 이유를 알 수 없는 문제가 있음

지식 기반 필터링은 특정 분야 전문가의 도움을 받아서 그 분야에 대한 전체적인 지식구조를 만들어서 이를 활용하는 방법

- 딥러닝(Deep Learning: DL) 추천 기술

다양한 사용자 아이템의 특징값(feature)을 사용하여 선호도를 구하는것



-> 실제로는 추천 시스템을 구축할 때는 한 가지만 사용하지 않고 여러가지를 사용함.



### 2장  기본적인 추천 시스템

$$
RMSE = \sqrt{\frac{1}{N}\sum\limits_{i=1}^{N}(y_i- \widehat{y_i})^2}
$$

```
추천 시스템의 성능은 "정확성"으로 표시
가장 많이 사용하는 지표로 위의 RMSE가 있음 

```


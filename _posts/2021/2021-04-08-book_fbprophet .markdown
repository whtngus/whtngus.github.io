---
layout: post
title: "prophet 설명"
date: 2021-04-03 19:20:23 +0900
category: python

---

# prophet 



## Prophet 이란

페이스북 연구팀의 션 테일러와 벤 레담은 블로그 포스트를 통해 "프로핏은 전무가는 물론 비전문가도 높은 품질의 예측 작업을 좀 더쉽게 할수 있는 툴"로 소개

Prophet은 Facebook의 [Core Data Science 팀](https://research.fb.com/category/data-science/) 에서 출시 한 [오픈 소스 소프트웨어](https://code.facebook.com/projects/) 입니다.

-> 시계열 알고리즘 

prophet 클래스 인스턴스 생성 후 fit과 predict 메소드를 불러와서 사용.

시계열 데이터 분석에 사용 

- 특징

정확하고 빠름

완전 자동

조정 가능한 예측

R or Python 에서 제공



- 사용방법

```
import pandas as pd
from fbprophet import Prophet 

m = Prophet()
m.fit(df) # df 데이터에 맞게 학습 

future = m.make_future_dataframe(periods=100) # ㅎperiods는 향후 몇개의 데이터를 예측할 것인지
future.tail() # 예측 마지막 결과 출력
forecast = m.predict(future) # 예측 

fig1 = m.plot(forecast) #결과 시각화
fig2 = m.plot_components(forecast) #  예측 및 구성 요소의 그림

```



- 사용 알고리즘

정확한 내용이 적혀있는곳은 찾기 힘듦

- 베이지안 구조 시계열 모델

> 1. Introduction
>
> > - 시계열에서 높은 품질의 예측은 매우 어렵다.
> >
> > 완전한 자동화 예측 기술은 튜닝하기 매우 어렵고 유연하지 않음
> >
> > 도메인 지식 전문가는 시계열 예측에 대한 전문지식을 갖고 있지 않는 경우 많음
>
> 2. Features of Business Time Series
>
> > 비즈니스 예측 문제는 어렵지만 다음과같은 공통점이 있다.
> >
> > Prophet은 다음 구성 요소의 합으로 표현할 수 있는 최상의 부드러운 곡선을 찾는 모델
> >
> > ```
> > Y(t) = g(t) + s(t) + h(t) +  ϵₜ
> > 
> > g(t) : 시계열의 비 주기적 변화를 모델링하기위한 부분적 선형 또는 로지스틱 곡선
> > s(t) : 주기적 변화 (계절성, 주간 등)
> > h(t) : 일정한 불규칙 효과(휴일, 이벤트 등 )
> > ϵₜ : 모델에서 해결하지 못하는 잔차
> > ```
>
> 3. The Prophet Forcastring Model
>
> > 2에서 소개한 수식을 기본으로 GAM 모델(Generalized Additive Model)과 비슷 
> >
> > curve-fitting 문제를 잘 반영하도록 커브를 그리는것이 초점
> >
> > ARIMA처럼 inferential한 이점을 가지고 있지는 않음
> >
> > - 이점
> >
> > 유연성 : 계절성과 여러 기간들에 대한 예측을 쉽게 모델에 적용
> >
> > ARIMA모델과 다르게, 모델을 차분해서 정규화 X, 결측치 채워넣기 필요 X
> >
> > 학습이 빠르고 분석가는 상세한 모델 스펙을 평가 가능
> >
> > 회귀분석과 매우 유사하여 생소한 시계열 분석보다 빠르게 적응 가능
>
> 
>
> 
















# 참고 사이트

- fbprophet 설명

https://steemit.com/kr/@yoon/python-prophet-and

https://hyperconnect.github.io/2020/03/09/prophet-package.html

https://ichi.pro/ko/python-eulo-sigyeyeol-yecheug-eul-wihan-facebook-prophet-1-bu-239090574793501

- 도큐먼트

https://facebook.github.io/prophet/

- github

https://github.com/facebook/prophet

- paper

https://peerj.com/preprints/3190/

https://dodonam.tistory.com/275?category=899198  -> 논문 설명
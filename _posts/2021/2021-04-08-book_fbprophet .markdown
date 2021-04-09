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
> > - 3.1 The Trend Model
> >
> > > trend model로 saturating growth model, piecewise liner model을 사용
> > >
> > > - Nonlinear, Saturating Growth
> > >
> > > growth예측을 위해서 핵심요소는 얼마나 population이 성장, 지속될것지
> > >
> > > 자연 생태계서의 인구성장 모델과 유사
> > >
> > > nonlinear성장이 있는데 이는 수용가능한 용량에 영향을 받음
> > >
> > > g(t) = C /  ( 1 + exp(-k(t-m)))
> > >
> > > C : carrying capacity -> 시간에 따라 변화하기 때문에 time-varyin capacity C(t)로 사용 
> > >
> > > k : growth rate -> 역사적인 데이터를 맞추기 위해 다양한 rate를 통합해야함 
> > >
> > > m : an offset parmater
> > >
> > > 최종 모델 수식
> > >
> > > g(t) = C(t) / (1 + exp(-...))  복잡 논문 참조 
> > >
> > > - Linear Trend with Changepoints
> > >
> > > 성장 모델에 포화상태가 일어나지 않는 경우(용량이 제한되지 않은 경우 linear로 해결 가능)
> > >
> > > - automatic Changepoint selection
> > >
> > > 분석가에 의해 정의
> > >
> > > - Trend Forecast Uncertainty
> > >
> > > 모델의 불확실성을 추정 
> > >
> > > 라플라스를 이용 해서 평균 changepoints빈도, (즉 미래의 chagnepoints를 설정)
> > >
> > > 즉, 미래에도 과거와 같은 평균의 빈도의 변화가 있을 것이라는 가정 
> >
> > - Seasonality
> >
> > > p라는 파라미터를 통해서 주기를 설정 가능
> > >
> > > ex) p=365.25 는 1년 p=7이면 1주일
> >
> > - Holidays and Events
> >
> > > 과거 데이터에서 특정 이벤트가 있는 것들의 리스트를 넣을 수 있고, 이를 반영하게 만듦
>
> 4. Model Fitting
>
> > Stan's L-BFGS을 사용
>
> 5. Analyst-in-the-Loop Modeling
>
> > 분석 전문가가 모델을 적용할때 도메인 지식을 이용해서 파라미터를 조정가능하게 함
> >
> > - Capacities : 시장 규모와 어떤 것에 대한 용량 수준
> > - ChangePoints : 상품이 바뀌거나 신제품이 출시되는 changepoints
> > - Holiday and Seasonality : 영향을 미치는 특별한 휴일이나 이벤트 기간
> > - Smoothing Parameter : 주기마다 변동을 줄 수준

4. Automating Evaluation of Forecasts

> 1. Use of Beseline Forecasts
>
> 어떤 모델을 비교할 때 baseline과 비교하는 것이 중요 
>
> last value, sample mean으로 단순한 모델 비교
>
> 2. Modeling Forecst Accuracy
>
> 예측은 특정 horizon H에 대해 이루어짐
>
> 시간별 추정된 값과 실제값 사이의 MAE, MAPE(요걸 더 많이씀)
>
> 3. Simulated Historical Forecasts
>
> cross validation과 같은 방법을 사용하기 어려움 -> 시계열 데이터 여서 셔플 힘듦
>
> SHFs(simulated historical forcasts)를 사용 -> 다양한 cutoff point에서 예측치 k를 ㅔㅈ공
>
> 4. Identifying Large Forecasts Errors
>
> 분석가는 잘못된 예측 결과에 대해서도 확인하고, 이를 수정할 필요가 있음 -> 서포트 필요
>
> > 처리방법
> >
> > 1. baseline 모델과 비교하여 큰 에러가 있으면 trend, seasnoality등 수정
> > 2. 특정 일자에 예측률이 떨어진다면, 아웃라이어 제거
> > 3. 특정 cutoff에 예측률이 떨어지면 chagepoint를 추가





 
















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
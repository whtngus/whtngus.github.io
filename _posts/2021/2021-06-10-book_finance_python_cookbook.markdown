---
layout: post
title: "book : 금융 파이썬 쿡북"
date: 2021-06-16 19:20:23 +0900
category: book
---

# 책 제목 :  금융 파이썬 쿡북

예제 코드 다운로드 : http://www.acornpub.co.kr/book/python-finance

-> https://github.com/AcornPublishing/python-finance

많은 내용 생략!

#  1장 금융 데이터와 전처리

1. 주식 데이터 다운로드

- 데이터 다운로드 가능한 api

> - yfinance
>
> 라이브러리로 1일단위 주식 데이터 다운 가능
>
> - quandl 
>
> api key 필요+ 더 많은 컬럼 지원 
>
> 라이브러리로 1일단위 주식 데이터 다운 가능
>
> - intrinio_sdk
>
> api key 필요+ 더 많은 컬럼 지원 
>
> 라이브러리로 1일단위 주식 데이터 다운 가능

2.  수익률

- 단순 수익률

자산에 대해 집계

Rt = (Pt - Pt-1)/Pt-1 

- 로그 수익률

시간에 대해 집계

Rt = log(Pt/Pt-1)

# 2장 파이썬에서의 기술적 분석

- 백테스팅(backtesting)

일부 휴리스틱이나 기술 지표를 사용해 구축된 거래 전략의 성능을 과거 데이터에 적용해 평가해 보는것

-> backtrader 를 사용해 테스트 가능

- 볼린저 밴드(Bollinger Band)

시간에 따른 특정 자산 가격과 변동성의 정보를 도출하는 데 사용되는 통계쩍인 방법

- RSI(Relative Strength Index)

자산의 종가를 사용해 매도/매수 조건을 실벽하는 지표



# 3장 시계열 모델링

### 시계열 분해

시계열을 여러 구성 요소로 나눠 데이터에 대한 이해를 높이는것

- 체계적 구성 요소 

일반적이고 묘사와 모델링 가능

> - level : 계열의 평균값
> - trend : 추세의 추정치, 즉 특정 시점에서 연속 지점 사이의 값 변화
> - seasonality : 단기 사이클로 반복되는 평균으로부터의 편차

- 비체계적 구성 요소

직접적으로 모델링 할 수 없음

> - noise : 시계열상 랜덤 변화

- 가산적(additive) 유형

> - 모델의 식
>
> y(t) = level + trend + seasonality + noise
>
> - 설형 모델
>
> 시간에 따른 크기 변화가 일정
>
> - 추세는 선형
> - 시간 주기에 대해 동일한 빈도와 폭을 가진 성형 계절성

- 승산적(multiplicative)  유형

> - 모델의 식
>
> y(t) = level * trend * seasonality * noise
>
> - non-linear model 
>
> 시간에 따른 변화가 일정하지 않다.
>
> - 곡선이며 비선형 추세
> - 시간 주기에 대해 증가/감소하는 빈도와 폭을 가지는 비선형 계절성

##### 코드

- 코드 예시

```
	- 이동 평균 
df['rolling_mean'] = df.price.rolling(window=WINDOW_SIZE)
	- 계절성 분해
from statsmodels.tsa.seasonal import seasonal_decompose
를 사용해서 볼 수 있음
```

- 페이스북의 Prophet 라이브러리도 잘되있음

##### 시계열의 정상성 테스트

- 정상성(stationary) 시계열

평균, 분산, 공분산 등의 통계적인 속성이 시간에 대해 일정한 시계열 

- stationary 테스트 방법

> - ADF(Augmented Dickey-Fuller) 검정
>
> 시계열이 정상성이 아니다라는 귀무가설로 p-값이 1또는 임계치보다 큰 경우 귀무가설을 긱할 이유가 없음으로 정상성이 아니라는 결론을 내림
>
> - KPSS(Kwiatkowski-Pjillips_Schmidt-Shine) 검정
>
> 귀무가설은 시계열이 정상성이다를 기보능로 해서 p값이 0.01이거나 큰 경우 대립가설이 선호되며 귀무가설을 기각
>
> - 자기 상관 함수(PACF/ACF) 도면

### 시계열의 전상성 교정

- 디플레이션

CPI(소비자 물가 지수, Consumer Price Index)를 사용해 인플레이션을 반영

- 자연 로그

지수 추세를 선형에 가깝게 만듬

- differencing (차분)

현 관측값과 지연 값 사이의 차이를 취함 

ex) 월별 데이터에 연간 계쩔성이 있는 경우에는 높은 차수를 사용(12)

- Box-Cos transformation(반스-콕스 변환)

시계열 데이터에 사용할 수 있는 조정 

다른 지수 변환 함수를 결합해 분포를 정규 분포와 유사하게 만듦

단, 시계열 모든값이 양수여야함

### 지수 평활법(exponential smoothing)을 사용한 시계열 모델링

비정상 데이터에 적합하며 지수 이동 평균과 유사하게 작동

- SES(단순 지수 평활, Simple Exponential Smoothing)

가장 기본적인 모델을 단순 지수 평활이라고 한다.

0~1 사이의 a(알파)를 매개 변수화하여 값이 클수록 최근 관측값에 더 많은 가중치가 적용

0이면 과거데이터의 평균 1이면 마지막 관측값과 동일 

추세나 계절성이 없는경우 적당함

- Holt(홀트)의 선형 추세 방법

SES의 확자응로서 추세 구성 요소를 모델 사양에 추가해 시게열의 추세롤 고려 

감쇠 매개 변수를 추가해 추세를 완화

0.8 ~ 0.98 사이가 적절   1은 감쇠가 없는값과 동일

### ARIMA(Autoregressive Moving Average)

- AR(Autoregressive) 모델

관측값과 지연된 값 아이의 관계를 사용

금융의 맥락에서 AR모델은 모멘텀과 평균 회귀 효과를 반영하려고 한다.

- I(Integration)

I는 원래 시계열을 차분해 정상성으로 만드는 것

통합을 담당하는 매개 변수는 d이며 차분을 적용하는 횟수를 말함

- MA(Moving Average)

관측값과 백색 노이즈 항간의 관계를 이용

이동 평균 모델은 관측된 시계열에 영향을 미치는 예측할 수 없는 충경르 설명

###  4. 다팩터 모델

- CAPM(자본 자산 가격 모델, Capital Asset Pricing Model)

![CAPM](D:\code\whtngus.github.io\img\2021\finance_pytohn_cookbook\CAPM.PNG)

> E(ri) : 자산 i의 기대 수익률
>
> rf : 무위험 금리 (국고채 등)
>
> E(rm) : 시장의 기대 수익률, 즉 배타 계수
>
> - beta
>
> -1 < beta : 자산이 벤치 마크와 반대 방향이며, 벤치 마크의 음수보다 더 큰 정도로 이동
>
> -1  < beta < 0 :자산이 벤치 마크와 반대 방향으로 이동
>
> beta = 0 : 자산의 가격 변동과 시장 벤치 마크 사이에는 상관관계가 없다
>
> 0 < beta < 1 : 자산이 시장과 같은 방향으로 움직이잠ㄴ 크기는 더 작다.
>
> beta =1 : 자산과 시장이 같은 방향과 같은 크기로 이동
>
> beta > 1 : 자산이 시장과 같은 방향으로 더 크게 이동 

위 식에서  rf를 좌항으로 이동시켜 

E(ri) - rf = B *(E(rm) - rf) 로 나타낼 수있다

좌변은 위험 프리미엄 우변은 시장 프리미엄을 나타낸다 

 

- 파마-프렌치 3-팩터

파마와 프렌치는 자신들의 유명한 논문에서 자산이나 포트폴리오의 초과 수익을 설명하는 두 가지 팩터를 추가해 CAPM 모델을 확장

> - MKT(Markget Factor)
>
> CAPM과 유사한 ㅅ장의 초과 수익률을 측정
>
> - SMB(Small Minus Big)
>
> 시가 총액이 큰 주식 대비 시가 총액이 작은 주식의 초과 수익률
>
> - HML(High Minus Low)
>
> 성장 주식 대비 초과 가치 주식의 초과 수익률을 츨정
>
> 가치 주식은 높은 시장가 대비 장부가(book-to-market) 비율을 갖고 성장 주식은 그 비율이 낮다.



# 5장 GARCH 클래스 모델을  사용한 변동성 모델링

ARIMA같은 모델은 시간에 대해 일정하지 않은 변동성은 설명할 수 없는 문제가 있음

-  ARCH 모델을 사용한 주식 수익률의 변동성 설명

ARCH(Autoregressive Conditional Heteroskedasticity) 모델을 사용해 주식 수익률의 조건부 변동성을 설명

- 특징

> - 시계열의 무조건과 조건부 차이를 명시적으로 인식
> - 평균 프로세스에서 조건부 분산을 과거 잔차의 함수로 모델링
> - 무조건 분산은 시간에 대해 일정하다고 가정
> - 모델의 사전 잔차 수를 자기회긔 모델과 유사하게 지정해야 함
> - 주어진 시계열에 다른 모델을 적합화한 후 얻은 자차에만 적용가능
> - 잔차는 불연속 백색 잡음의 관측값과 유사해야함









# 참고

- CAPM 수식 스림

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=carrot_1027&logNo=220780295571
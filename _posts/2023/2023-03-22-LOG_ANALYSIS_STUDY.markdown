---
layout: post
title: "LOG ANALYSIS STUDY"
date: 2023-03-22 00:01:23 +0900
category: datascience
---

# LOG ANALYSIS STUDY



### 어트리뷰션 적재시 관점

1. CPA/ROI/ROAS등 어디에 기준을 두냐에 다라 적재 어트리뷰션 요소가 달라짐 
2. 세그먼트별 성과 확인 

그룹군(나이, 성별, 사는지역 그리고 신규 유저 등)에 따라 성과를 달리할 수 있어야함

3. 보이지 않는 지표 

눈에 보이진 않지만(페이지) 클릭, 마우스 트랙킹등도 매우 중요한 지표 중 하나



### 앱로그 데이터 분석을 위한 DB화시 고려 사항 

앱로그 데이터 구성 요소

한 사용자가 여러 번 접속해서 했던 행동

하나의 행에 들어가야할 내용 



테이블을 2개로 나눠서 구성

- 서비스 로그

가입완료, 예약완료, 결제완료, 결제취소, 개인정보 변경 등 

- 행동 로그

가입하기 클릭, 배너 스와프, 검색 실행 등 

- 행동로그 설계 방법

```
행동로그를 설계하는 방법에 따라 얻을 수 있는 정보의 수준이 달라진다.
가장 간단한 방식은 이벤트의 숫자를 count 하는것 (이벤트의 특성과 사용자의 특성 집계)
```





# 관련 지식

- attribution(어트리뷰션)

 마케팅 캠페인이라는 '원인'과 앱 설치나 인앱 전환과 같은 성과의 '결과'를 매칭하여 '기여도', 즉 '인과 관계'를 분석하는 것을 의미

- LTV(LiveTime Value) : 고객상애가치

고객 1명이 기업에게(평생) 줄 수 있는 매출

- CAC(Customer Acqusition Cost)

고객 1명을 획득하기 위해서 써야 하는 금액

- CPI(Cost Per Install)

설치 건당 광고비

- CPA(Cost Per Action)

유입, 클릭을 넘어 특정 행동(Action)을 할 때 지불하는 비용

- ROI(Return On Investment)

투자대비 이익률

- ROAS(Return On Ad Spend)

광고비용 대비 수익률





# 참고

- 오늘의집 - 마케팅 데이터 만들기(APP/WRB)

https://www.bucketplace.com/post/2021-07-06-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%A7%88%EC%BC%80%ED%8C%85-%EA%B8%B0%EB%B0%98-%EB%A7%8C%EB%93%A4%EA%B8%B0/

- 행동로그 설계 방법

https://medium.com/myrealtrip-product/%EB%AA%A8%EB%B0%94%EC%9D%BC-%EC%95%B1-%EB%A1%9C%EA%B7%B8%EB%B6%84%EC%84%9D-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%8B%9C%EC%9E%91%ED%95%B4%EC%95%BC-%ED%95%A0%EA%B9%8C-13b8109df196
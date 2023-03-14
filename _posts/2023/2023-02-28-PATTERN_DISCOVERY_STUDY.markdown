---
layout: post
title: "PATTERN DISCOVERY STUDY"
date: 2023-02-29 00:05:23 +0900
category: datascience
---

# PATTERN DISCOVERY STUDY

## 기본 개념

#### Support(S)

```
Beer, Nut, Diaper
Beer, Coffee, Diaper
Beer, Diaper, Eggs
Nuts, Eggs, Milk
Nuts, Coffee, Diaper, Eggs, Milk
```

전체 중에서 해당 이벤트가 발생했을 확률 

위의 예시에서

freq 1 - Beer(60%), Nuts(60%), Diaper(80%), Eggs(60%)

freq 2 -  Beer, Disaper (60%)

#### confidence(C)

X가 포함되어 있을때 Y까지 구매되었을 조건부 확률

C = sup(X U Y) / S(X)

#### association rule

min support와 min confidence를 정해놓고 그 이상이 되는 Rule X->Y를 찾는것

beer -> Diaper (s:60%, c : 100%)  

Diaper -> beer (sL60%, c : 75%)

둘다 동시발생은 60%  beer를 구매할때 Diaper를 구매한 경우는 100% 반대는 75%

#### max pattern  closed pattern

![closed_pattern](D:\src\whtngus.github.io\img\2023\PATTERN_DISCOVERY_STUDY\closed_pattern.PNG)

max pattern이 min-support보다 크면 그 부분집합은 당연히 min-support보다 클것이다.  라는 개념을 이용 

위 그림중 파란색이 closed 패턴 =>  자신을 포함하는 상위 집합 중에 자신보다 크거나 같은 support가 없는 경우에만 파란색인 것

### Downard Closure Property(Apriori property)

{beer, diaper, nuts} 가 frequent 하면 subitem 인 {beer diaper} 는 적어도 그 만큼은 frequent 해야한다

-> 반대로 보면 s의 어떤 subset도 infrequent하면 S가 frequent할 수 없음

![Apriori property](F:\code\whtngus.github.io\img\2023\PATTERN_DISCOVERY_STUDY\Apriori property.PNG)

minsup 보다 큰 조합들을 계속해서 합쳐 가장 큰 조합을 참조 

### Partitioning

![partitioning](F:\code\whtngus.github.io\img\2023\PATTERN_DISCOVERY_STUDY\partitioning.PNG)

local TDB에서 frequent하지 않으면 global TDB 에서도 frequent하지 않다고 가정 -> 글로벌에서 frequent 하려면 적어도 partitioning된 lcal TDB중 하나에서는 fequent 해야한다.

### Direct Hashing and Pruning

DHP는 candidates의 수를 줄이기 위해 사용 

item이 frequent한다면, hasing bucket에 들어갔을때 그 count 값이 threshold보다 높아야 한다.

### Vertical Data Format

- *ECLAT* (Equivalence Class Transformation) 

![ECLAT](F:\code\whtngus.github.io\img\2023\PATTERN_DISCOVERY_STUDY\ECLAT.PNG)

패턴분석의 연산 속도 향상을 위한 방법으로 item 기준으로 접근하는 방법 

> - t(x) = t(Y) 이면 x와 y가 언제나 같이 일어남 
> - t(x) ⊂ t(Y) 이면 X가 있을땐 언제나 Y가 있음 
>
> diffset 연산을 통해 공간을 많이 아낄 수 있는 장점이 있음

데이터를 접근하는 방법을 바꿔 저장해서 빠른 연산속도를 보장하도록 함 

### FP Growth


















# 참고

- main

https://1ambda.github.io/data-analysis/pattern-discovery-1/

- max, clsed pattern

https://sijoo.tistory.com/16

- *ECLAT* 

https://nyamin9.github.io/data_mining/Data-Mining-Pattern-3/

- FP Growth02
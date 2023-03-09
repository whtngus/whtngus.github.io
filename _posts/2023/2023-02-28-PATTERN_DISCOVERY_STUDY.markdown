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


 



# 참고

- main

https://1ambda.github.io/data-analysis/pattern-discovery-1/


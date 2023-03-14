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

![closed_pattern](\img\2023\PATTERN_DISCOVERY_STUDY\closed_pattern.PNG)

max pattern이 min-support보다 크면 그 부분집합은 당연히 min-support보다 클것이다.  라는 개념을 이용 

위 그림중 파란색이 closed 패턴 =>  자신을 포함하는 상위 집합 중에 자신보다 크거나 같은 support가 없는 경우에만 파란색인 것

### Downard Closure Property(Apriori property)

{beer, diaper, nuts} 가 frequent 하면 subitem 인 {beer diaper} 는 적어도 그 만큼은 frequent 해야한다

-> 반대로 보면 s의 어떤 subset도 infrequent하면 S가 frequent할 수 없음

![Apriori property](\img\2023\PATTERN_DISCOVERY_STUDY\Apriori property.PNG)

minsup 보다 큰 조합들을 계속해서 합쳐 가장 큰 조합을 참조 

### Partitioning

![partitioning](\img\2023\PATTERN_DISCOVERY_STUDY\partitioning.PNG)

local TDB에서 frequent하지 않으면 global TDB 에서도 frequent하지 않다고 가정 -> 글로벌에서 frequent 하려면 적어도 partitioning된 lcal TDB중 하나에서는 fequent 해야한다.

### Direct Hashing and Pruning

DHP는 candidates의 수를 줄이기 위해 사용 

item이 frequent한다면, hasing bucket에 들어갔을때 그 count 값이 threshold보다 높아야 한다.

### Vertical Data Format

- *ECLAT* (Equivalence Class Transformation) 

![ECLAT](\img\2023\PATTERN_DISCOVERY_STUDY\ECLAT.PNG)

패턴분석의 연산 속도 향상을 위한 방법으로 item 기준으로 접근하는 방법 

> - t(x) = t(Y) 이면 x와 y가 언제나 같이 일어남 
> - t(x) ⊂ t(Y) 이면 X가 있을땐 언제나 Y가 있음 
>
> diffset 연산을 통해 공간을 많이 아낄 수 있는 장점이 있음

데이터를 접근하는 방법을 바꿔 저장해서 빠른 연산속도를 보장하도록 함 

### FP Growth

데이터셋이 큰 경우 연관 규칙을 만들기 위해 후보 itemset을 하나하나 검사하는것은 굉장히 비효율 적임 이러한 문제를 해결하기 위헤해 FP-growth 알고리즘을 제안

- FP Growth 과정

> 1. Build FP-Tree
>
> 검색시간을 단축시키기 위해 FP-Tree를 생성 
>
> 각각 item의 카운트를 기반으르 높게 다운 집합 순으로 tree 연결
>
> ![fp_1](\img\2023\PATTERN_DISCOVERY_STUDY\fp_1.PNG)
>
> ![pf_2](\img\2023\PATTERN_DISCOVERY_STUDY\pf_2.PNG)
>
> 2. Main FP-Tree
>
> 각 frequent item들을 각각 postfix로 놓고 item별로 recursive하게 support를 구함 
>
> ![fp_3](\img\2023\PATTERN_DISCOVERY_STUDY\fp_3.PNG)
>
> 트리가 위로부터 join count로 구성됨으로 minimum suport 와 itemset조합 등 다양한 분석에서 빠르게 접근 가능



# 패턴 마이닝의 결과 평가

### Lift, χ²(Chi-squared)

confidence는 두 변수가 관련있는지 말해주지만 positive, negative관계는 알 수 없음 이를 판단하기 위해 lift를 이용

![lift_1](\img\2023\PATTERN_DISCOVERY_STUDY\lift_1.PNG)

Lift는 위의 수삭처럼 B와 C가 얼마나 관련 있는지를 말함 

-> lift 가 1이면 독립, 1보다 크면 positive correlated, 1보다 작으면 negative correlated 

### 1. Multi-Level Associations

![mla](\img\2023\PATTERN_DISCOVERY_STUDY\mla.PNG)

Item들 간에 hierarchy가 존재하는 것

Uniform support를 적용하면 레벨에 관계 없이 동일한 min_sup을 적용하게 된다.그런데 lower level의 item들은 더 작은 support를 가질 확률이 높기 때문에 lower level에 대한 association rule은 나오기 힘들기 때문에 support를 변경해 줘야함 

### 2. Multi-Dimensional Associations

2개 이상의 dimension(predicate, attribute)를 가지고 있는 rule

- inter-dimension association rule
  - predicate를 반복하지 않는다.
  - 중복되는 predicate가 없다.
  - 예시
    - age(X, "19-25") ∩ ocupation(X, "student") → buys(X, "coke")
    - 위 예시의 dimension은 3이다.
- hybrid-dimension association rule
  - 중복되는 predicate가 존재한다.
  - 예시
    - age(X, "19-25") ∩ buys(X, "popcorn") → buys(X, "coke")
    - 위 예시의 dimension도 3이다.

-> 이해안감

### 3. Quantitative Associations

*numerical attribute* (e.g *age, salary*) 를 마이닝 하기 위해 다양한 *method* 를 사용

1. static discretization based on prefefined concept hierarchies. data cube-based aggregation

데이터를 비닝 하는듯등 사전 정의 형식으로 분할

2. dynamic discretization based on data distribution

데이터 분포에 기반해 이산화 

2. clustering: distance-based association. first one-dimensional clustering, then association

클러스터링 

4. deviation analysis

편차 분석 -> 공부해보기

#### 4. Negative Correlations

주의 점 

rere patterns : 아주 낮은 support지만, 중요할 수 있음

negative patterns : 자동차를 동시에 2개 사는섯처럼, 같이 일어나는 경우가 드뭄



여러가지 방법이 있지만 lift를 이용하기도 함 (데이터가 커지면 적용되지 않음)

### 5. Compressed Patterns

너무 많아 의미가 없는 *scattered pattern* 때문에 *compressed pattern* 을 마이닝 할 필요가 있다.

compressed pattern

> closed pattern : 패턴이 자주 발생, 동일한 support를 가지는 슈퍼패턴 존재 X 
>
> max pattern : 빈번하게 발생하고 슈퍼패턴이 존재하지 않는 경우



# Sequential Pattern Mining

- Sequential pattern의 종류 

1. gapped

패턴 사이의 gap을 허용

-> 웹사이트에서 클릭 사이 gap은 중요할 수 있음 

2. non-gapped

패턴 사이의 gap을 비 허용(모든 시퀀스가 중요함)

##### algorithm

1. GSP (Generalized Sequential Patterns)

apriori-based sequential pattern mining 기법

지지도 기반 너비 우선 탐색으로 길이가 k인 후보 패턴 중에서 가장 빈번한 패턴을 찾아가는 방식

![gsp](\img\2023\PATTERN_DISCOVERY_STUDY\gsp.PNG)

DB를 지속적으로 스캔해 가면서 minimum support를 통과하지 못하는것들을 제거하고 위 패턴을 반복하는것

2. SPADE (Sequential Pattern Mining in Vertical Data)

![spade](\img\2023\PATTERN_DISCOVERY_STUDY\spade.PNG)

> 1. SID 뿐만 아니라 element ID(각 seq에서의 순서로 보임) 를 이용해서 테이블을 좌측처럼 하나 생성
> 2.  우측 위처럼 아이템 별 SID, EID를 나열
> 3. 패턴의 길이를 늘려가며 계속 조인해 support를 계산

3. PrefixSpan

Pattern-Growth 기반의 알고리즘

![prefixspan_1](\img\2023\PATTERN_DISCOVERY_STUDY\prefixspan_1.PNG)

length-1 패턴을 찾고 이를 기반으러 projected DB를 만들어가며 마이닝 진행

![prefixspan_2](\img\2023\PATTERN_DISCOVERY_STUDY\prefixspan_2.PNG)

단계가 지나면 지날수록 candidate 가 생겨나는 비율이 줄고, projected DB 자체도 줄어든다는 장점발생

-> projected DB 에서 많은 중복이 발생하기 때문에 이를 해결하기 위해 pseudo projection 을 이용할 수 있다.

4. CloSpan

closed sequential pattern 을 마이닝하는 알고리즘

![clospan](\img\2023\PATTERN_DISCOVERY_STUDY\clospan.PNG)

Closed pattern을 사용하는 이유는 중복된 패턴을 피하기위함 

위 그림처럼 redundant search space(중복 검색) 를 prunin

5. Constraint-Based

> - anti-monotonic
>
> S 가 제약조건 c 를 위반했을때, 나머지 부분인 s 를 더해도 여전히 위반이라면 s 를 제거
>
> ex) Sum(S.price) < 150
>
> - *monotonic* 
>
> S가 제약조건 c를 만족할때, 슈퍼셋(S를 포함한 셋) 또한 이를 만족한다.
>
> - Sunccint
>
> 약조건 c 를 기준으로 데이터를 직접 조작
>
> ex) S 가 {i-phone, MacAir} 를 반드시 포함해야 한다고 할때, 그렇지 못하면 S 를 제거
>
> - Convertible
>
> 아이템을 정렬해서 제약조건을 anti-monotonic 이나 monotonic 등으로 바꿈



# Graph Pattern Mining

- 다양한 방법들이 있음 

> 1.  Generation of candidate subgraphs
>
> Apriori (FSG) vs Pattern Growth(gSpan)
>
> 2.  Search Order
>
> Breadth vs Depth
>
> 3. Elimination of duplicate subgraph
>
> Passive vs Active (e.g gSpan)
>
> 4. Support calculation
>
> Store embeddings (e.g GASTON, FFSM, MoFA)
>
> 5. Order of Pattern Discovery
>
> Path -> Tree -> Graph (GASTON)



### CloseGraph 여기 이어서 보기 **






# 참고

- main

https://1ambda.github.io/data-analysis/pattern-discovery-1/

- max, clsed pattern

https://sijoo.tistory.com/16

- *ECLAT* 

https://nyamin9.github.io/data_mining/Data-Mining-Pattern-3/

- FP Growth

https://process-mining.tistory.com/92

- Multi-Level Associations, Multi-Dimensional Associations

https://gofo-coding.tistory.com/entry/Multi-level-Association-Multi-dimensional-Association?category=1056379
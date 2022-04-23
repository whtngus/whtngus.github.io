---
layout: post
title: "paper : LightGBM: A Highly Efficient Gradient Boosting Decision Tree"
date: 2022-04-23 01:01:01 +0900
category: paper
---

# LightGBM: A Highly Efficient Gradient Boosting Decision Tree

url : https://proceedings.neurips.cc/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf
2017  microsoft

유명하니 이하 생략 ..



# Abstract

Gradient Boosting Decision Tree (GBDT)는 널리 사용되고 있으며 XGBoost와 pGBRT 같이 효율적으로 구현된 모델들이 있다. 

but 차원 변수에 데이터 크기가 큰 경우 효율성과 확장성은 불만족 스러움

-> 각 변수마다 가능한 모든 분할점에 대해 정보 획득을 평가하려면 데이터 개체 모두 훑어야 하는데 이에 많은 시간이 소요

이를 해결하기 위해 2가지 방법을 제안

> 1. Gradient-based One-Side Sampling (GOSS)
>
> GOSS를 통해 데이터 개체 중 기울기가 작은 상당 부분을 제외시키고 나머지만 사용하여 정보를 얻을 수 있다. 기울기가 큰 데이터 개체가 정보 획득 계산에 더 중요한 역할을 하기 때문에 GOSS는 훨씬 작은 크기의 데이터로 정보 획득을 매우 정확하게 추정해낼 수 있다. 
>
> 2. Exclusive Feature Bundling (EFB)
>
> 변수 개수를 줄이기 위해 상호 배타적 변수들(예컨대, 0이 아닌 값을 동시에 갖는 일이 거의 없는 변수들)을 묶는다. 
>
> 배타적 변수의 최적 묶음을 찾는 일은 NP-hard지만 탐욕 알고리즘을 통해 매우 괜찮은 근사 비율을 얻을 수 있다. 따라서 분할점 결정 정확도를 크게 훼손시키지 않으면서 변수 개수를 효과적으로 줄일 수 있다.

위 두가지 방법을 통해 LGBM이 기존 GBDT 보다 최대 20배 이상 빠르면서 동일한 성능을 달성했다고 한다.

# 1. Introduction

GBDT 기존 구현은 각 변수마다 가능한 모든 분할점에 대해 정보 획득을 평가하기 위해 데이터 개체 모두 훑어야 한다.

계산 복잡도는 변수 개수와 개체 수에 비례 -> 큰 데이터에 대해 시간을 많이 소모하게 됨

- GOSS(Gradient-based One-Side Sampling)

GBDT의 경우 데이터 개체에 대한 기본 가중치는 없지만 서로 다른 기울기를 가진 데이터 개체가 정보 획득 계산 시 서로 다른 역할을 한다는 점은 알고 있다

정보 획득의 정의로 보자면 기울기가 보다 큰[1](https://aldente0630.github.io/data-science/2018/06/29/highly-efficient-gbdt.html#fn:1)(즉, 과소 훈련시킨 개체) 개체가 정보 획득에 더 기여할 것이다.

 데이터 개체를 다운 샘플링할 때 정보 획득 추정의 정확도를 유지하려면 기울기가 큰 개체를 많이 유지하며 기울기가 작은 개체는 무작위로 떨굼 

-> 즉, 이미 잘 맞춘 데이터는 드랍시키고 잘 맞추지 못한 데이터는 그대로 사용

- EFB

일반적으로 많은 수의 변수를 갖지만 변수 공간은 매우 희소하여 변수 개수를 효과적으로 줄이기 위한 거의 손실 없는 방식을 만들어낼 수 있다. 

특히 히소한 변수 공간에서 많은 변수들이 거의 상호 배타적이다.

-> 변수들이 0이 아닌 값을 동시에 갖는 일이 없는경우 (ont hot encoding)

결국 graph coloring problem과 같은 방식을 설계

(변수를 각 꼭짓점에 두고 두 변수가 상호 배타적이지 않으면 두 변수를 잇는 변을 추가)

# 2 Preliminaries

## 2.1 GBDT and Its Complexity Analysis

GBDT는 결정 트리를 순차적으로 훈련시키는 앙상블 모형

각 iteration 마다 negative gradients를 학습

GBDT 주요 비용은 의사 결정 트리 학습에서 발생하며 의사 결정 트리를 학습시키는 데 시간 소요가 가장 큰 부분이 데이터를 분리하는 포인트를 찾는 것

1. 모든 포인트를 검색

사전 정렬한 변수 값에 대해 가능한 모든 분할점을 나열

최적 분할점을 찾아낼 수 있지만 훈련 속도와 메모리 소비 모든 면에서 비효율적

2. histogram-based algorithm



연속적인 변수 값을 개별 구간으로 나누고 이 구간을 사용하여 훈련 시 변수 히스토그램을 만든다. 

 메모리 소비와 훈련 속도에서 보다 효율적이므로 이를 바탕으로 작업을 진행

히스토그램 만드는 일에 O(#data×#feature), 분할점 찾는 일에 O(#bin×#feature)가 필요

## Related Work

![algorithm_1](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\algorithm_1.png)

- Algorithm1 Histogram-based Algorithm

rowset <-  트리 노드에서의 색인 

(**히스토그램**(**histogram**)은 표로 되어 있는 도수 분포를 정보 그림으로 나타낸 것이다.)



# 3 Gradient-based One-Side Sampling

데이터 개체 수를 줄이는 것과 학습한 의사 결정 트리 정확도를 유지하는 것 사이에서 균형을 잘 잡을 수 있는 GBDT의 새로운 표본 추출 방법을 제안

## 3.1 Algorithm Description

GBDT에서 각 데이터 개체에 대한 기울기는 데이터 표본 추출에 유용한 정보를 제공

체의 기울기가 작다면 해당 개체에 대한 훈련 오차가 작고 이미 잘 훈련된 것

-> 기울기가 작은 데이터는 잘 맞춤으로 데이터를 제거해나감 but 그냥 제거한다면 데이터의 분포가 바껴 정상적인 학습이 불가능함

이 문제를 피하기 위해 기울기 기반 단측 표본 추출(GOSS)이라는 새로운 방법을 제안



GOSS는 기울기가 큰 개체는 모두 유지하되 기울기가 작은 개체에 대해 무작위 표본 추출을 수행

분포에 미치는 영향을 보정하기 위해서 정보 획득 계산 시 기울기가 작은 데이터 개체에 승수 상수를 적용

기울기 절댓값에 따라 데이터 개체를 정렬(높은 GD부터 정렬)하고 상위 a×100% 개체를 선택한다. 그런 다음 나머지 데이터에서 b×100%개체를 무작위 표본 추출

그 후 GOSS는 정보 획득을 계산할 때 기울기가 작은 표본 데이터를 상수 (1−a)/b만큼 증폭시킨다. 

-> 이렇게 함으로써 원래 데이터 분포를 많이 변경하지 않고 훈련이 덜 된 개체에 초점을 잘 맞추도록 유도함

## 3.2 Theoretical Analysis

![f_1](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\f_1.png)

GBDT는 결정 트리를 사용하여 입력 공간 Xs에서 기울기 공간 G까지의 함수를 학습

xi - 공간 Xs내 차원이 s인 벡터

{g1,…,gn} - 손실 함수의 음의 기울기

노드에 대해 점 d에서 분할하는 변수 j의 분산 획득은 위와 같이 정의

j  - feature 

O - trainining dataset



변수 j에 대해 결정 트리 알고리즘은 dj=argmax dVj(d)를 선택하고 최대 획득 Vj(d∗j)를 계산한다.  그런 다음 데이터를 변수 j∗의 점 dj∗에 따라 왼쪽과 오른쪽 하위 노드로 분할한다.

- GOSS 에서는 데이터셋을 변경했음으로 다음과 같이 변경

![f_2](img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\f_2.PNG)

제안된 GOSS 방법론은 우선 기울기 절댓값에 따라 훈련 개체 순위를 내림차순으로 매긴다.

기울기가 큰 상위 α×100%개체를 가지고 개체 부분 집합 A를 만든다. (1−α)×100의 기울기가 작은 개체가 속하는 여집합 Ac에 대해 b×|Ac| 크기의 부분 집합 B를 무작위 표본 추출하여 만든다. 





![f_3](img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\f_3.PNG)

이건 모르겠다.. 

GOSS가 정학도를 저하시키지 않음을 증명하는 수식

1. GOSS의 점근적 근사 비율은 O(1/ nl(d) + 1/nr(d) + 1/root(n)) 이다. 

한쪽으로 치우쳐 분할되지 않았다면 n(d) >= O(root(n)) 이고 데이터가 많다면 근사값은 상당이 유사 

![algorithm_2](img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\algorithm_2.png)

- Algorithm 2 Gradient-based One -Side Samping

d 최대 깊이,  I 훈련 데이터, m 변수 차원

nodeset  현재 깊이에서의 트리 노드들

rowSet  트리 노드에서 데이터 색인들 

w[randSet] X= fact  <- 기울기 작은 데이터에 가중치 Fact를 부여함 



# 4 Exclusive Feature Bundling

이 장에서는 변수 개수를 효과적으로 줄이는 새로운 방법을 제안



고차원 데이터는 일반적으로 매우 희소하다. -> 이런 변수들은 변수 다수가 상호 배타적 이다. (즉, 0이 아닌값을 동시에 갖지 않는다.)

베타적 변수를 단일 변수(exclusive feature bundle)로 안전하게 묶을 수 있다.

이 경우 히스토그램 생성 복잡도는 O(#data×#feature)에서 O(#data×#bundle)로 바뀐다.

- 여기에서 가장 적은 수의 배타적 묶음으로 변수를 나누는 문제는 NP-hard  이다.

>  문제를 그래프 색칠 문제로 한정 지을 수 있다. 그래프 색칠 문제는 NP-hard이기 때문에 결론은 추론 가능

즉, 최적의 문제를 찾는게 NP-hard 임으로 보고 탐욕 알고리즘을 사용해 검색

아래의 알고리즘 3은 변수들을 묶기 위한 알고리즘

![algorithm_3](img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\algorithm_3.png)

> 변마다 가중치가 있는 그래프를 구성한다. 이 가중치는 변수 간 총 충돌 횟수에 해당한다. 그다음 그래프 내 꼭짓점 차수에 따라 내림차순으로 변수를 정렬한다. 마지막으로 정렬시킨 목록의 각 변수를 확인하면서 작은 충돌(γγ로 제어함)이 있는 기존 묶음에 할당하거나 새로운 묶음을 만든다. 알고리즘 3의 시간 복잡도는 O(#feature2))이며 훈련 전 딱 한 번만 처리

변마다 가중치 있는 그래프를 그래프를 구성(가중치는 변수 간충돌 횟수)

그래프 내 꼭시점 차수에 따라 내림차순으로 변수를 정렬

정렬시킨 목록의 각 변수를 확인하면서 작은 충돌(r 변수로 조정)

 작은 비율의 충돌을 허용한다면 더 적게 변수를 묶을 수 있고 계산 효율성을 더욱 증대시킬 수 있다.

변수 값을 작은 비율로 무작위 오염시킬때 영향도는

![f_4](img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\f_4.PNG)

정도로 r 묶음에서의 최대 충돌 비율이다 즉, 상대적으로 작은 r을 선택하면 정확도와 효율성 사이의 균형을 잡ㅇ르 수 있다.



알고리즘 3의 경우 변수가 적은 경우 적용해 볼 수 있지만 수백만 개라면 여전히 수행하기 어려울 수 있다. 효율성을 높이기 위해 그래프를 만들지 않는 효율적인 방법을 제안 

![algorithm_4](img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\algorithm_4.png)



묶음의 훈련 복잡도를 줄이기 위해 같이 묶인 변수를 병합하는 적당한 방법이 필요하다.



- 히스토그램 기반 알고리즘은 변수의 연속적인 값 대신 개별 구간을 저장하기 때문에 배타적 변수를 각기 다른 구간에 두어 변수 묶음을 구성할 수 있다

> 원래의 변수 A는 [0, 10] 값을 취하고 변수 B는 [0, 20] 값을 취한다. 그렇다면 변수 B 값에 오프셋 10을 더하여 가공한 변수가 [10, 30]에서 값을 취하게 한다.
>
>  변수 A와 B를 병합하고 [0, 30] 범위의 변수 묶음을 사용하여 원래의 변수 A와 B를 대체하는 것이 안전

해당 테이블의 데이터를 훑는 경우 변수 히스토그램 생성 비용은 O(#data)에서 O(#non_zero_data)로 바뀐다.



# 5 Experiments

## 5.1 Overall Comparision

baseline = XGBoost

![dataset](img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\dataset.PNG)

- 실험 데이터셋

![table_2](img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\table_2.PNG)

- 결과 비교 

> table2는 훈련시간 비교 
>
> table3은 NDCG@10 스코어 비교 

![auc](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\auc.PNG)

## 5.2 Analysis on GOSS

1.  GOSS가 얼마나 속도가 향상하는지 연구

표 2에서 ightGBM과 EFB_only를 비교하면 10~20% 데이터를 사용해 속도가 거의 2배 향상함을 알 수 있음.

2. SGB 정확도 비교 

동일한 표본 추출 비율을 사용하는 경우 GOSS 정확도가 SGB보다 항상 우수함을 알 수 있다. 이 결과는 3.2절 논의와 일치한다. 모든 실험이 확률적 표본 추출보다 GOSS가 더 효과적인 표본 추출 방법임을 입증

![table_4](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\table_4.PNG)

 GOSS는 서로 다른 aa와 bb를 선택하여 표본 추출 비율을 조정했고 SGB는 동일한 전체 표본 추출 비율을 사용

(동일한 표본 추출을 사용하는 경우 GOSS가 더 효과적은 표본 추출 방법입을 증명)

## 5.3 Analysis on EFB

표2에서 EFB_only를 비교하여 속도 향상에 기여함을 확인

EFB가 많은 희소 변수(원-핫 코딩 변수와 암시적으로 배타적인 변수 모두)를 훨씬 적은 변수로 병합하기 때문에 속도를 향상시킬수 있음.

또한 메모리적 측면에서 EFB의 경우 트리 학습 절차 중 변수 별 0이 아닌 데이터 테이블을 유지, 관리하는 데 추가 비용이 들지 않는다. -> 전반적인 효율성은 극적으로 향상

EFB는 희소행렬에 대해 매우 효과적임

# 6 Conclusion

이 알고리즘은 데이터 개체 다수와 변수 다수를 처리하는 두 가지 새로운 기술, 즉 *기울기 기반 단측 표본추출*과 *배타적 변수 묶음*을 포함한다. 이 두 가지 기법에 대한 이론적 분석과 실험적 연구 모두 수행했다. 실험 결과는 이론과 일치하며 GOSS와 EFB 도움으로 LightGBM이 계산 속도와 메모리 소비면에서 XGBoost 및 SGB보다 훨씬 뛰어난 성능을 보여준다. 향후 진행할 작업은 기울기 기반 단측 표본 추출에서 a와 b의 최적 선택을 연구하고 희소 혹은 그렇지 않은 변수 다수를 처리하기 위해 배타적 변수 묶음 성능이 지속적으로 향상하는 일이다.













# 참고지식

## NP-hard

[NP](https://ko.wikipedia.org/wiki/NP_(%EB%B3%B5%EC%9E%A1%EB%8F%84))에 속하는 모든 [판정 문제](https://ko.wikipedia.org/wiki/%ED%8C%90%EC%A0%95_%EB%AC%B8%EC%A0%9C)를 [다항 시간에 다대일 환산](https://ko.wikipedia.org/wiki/%EB%8B%A4%ED%95%AD_%EC%8B%9C%EA%B0%84_%ED%99%98%EC%82%B0)할 수 있는 문제들의 집합

P-NP Problem는 [클레이 수학연구소](http://ko.wikipedia.org/wiki/%ED%81%B4%EB%A0%88%EC%9D%B4_%EC%88%98%ED%95%99%EC%97%B0%EA%B5%AC%EC%86%8C)에서 발표한 7개의 '밀레니엄 문제' 중 하나로 컴퓨터 과학에서 중요한 위치를 차지하고 있는 문제다

- polynomial (P)

P는 **결정론적 (deterministic) 튜링 기계**를 사용해서 다항 시간내에 답을 구할 수 있는 문제의 집합이다. P는 yes/no 로 답할 수 있는 문제

-> 즉, **알고리즘의 복잡도가 O(n^x)로 표현**되는 모든 문제들을 말한다.



결정성(deterministic) 알고리즘 : 각 단계에세ㅓ 그 다음 단계가 유일하게 결정되는 알고리즘 

비결정성 알고리즘 : 그 다음 단계가 유일하게 결정되지 않는 알고리즘

튜링 기계 : Alan Turing에 의해서 고안된 것으로 무한한 메모리와 저장장치를 말함

- Nondeterministic polynomial (NP)

NP는 비결정론적 튜링 기계를 사용해서 polynomial time내에 답을 구할 수 있는 문제의 집합

->  yes라고 답을 주었을 때, 그 답이 정말 yes가 맞는지를 polynomial time안에 확인할 수 있으면 그 문제를 NP문제라고 한다.

즉, polynomial time내에 해결할 수 있는 방법이 있지는 않지만 만약에 solution을 찾게 되면 polynomial time내에 해결이 가능하다라고 이해하면 된다.



NP문제 중에서도 답을 polynomial time 안에 찾을 수 있으면 그 문제를 P문제 라고 한다. 

(P는 NP의 부분집합)

### NP(non-deterministic polynomial time)의 종류 

![np](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\np.png)



- NP-hard

![NP-hard](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\NP-hard.png)

x들과 y의 관계는 다대일이 될 수 있어서 다대일 환산이라고도 한다. 그리고 만약 이 변형이 다항시간내에 이루어 질 수 있다면 polynomial-time many-one reducible이라고 한다.

> **NP-hard**는 다항시간내에 풀 수 없는 문제를 말한다. 다항 방정식 대신에 지수 방정식으로 풀 수 있는 문제를 말한다. 즉 결정석 다항식으로 구성할 수 없다는 것이다. NP-hard라고 해서 다항식이 아니라는 것은 아니다. 다만 다항식으로 표현될 수 있을 지의 여부가 아직 알려지지 않았다라는 것

- NP-complete

NP-hard이며 NP 부류에 속하는 문제

이 문제를 해결하는 다차 함수 시간 결정성 알고리즘이 존재한다면 NP에 속한 각 문제를 해결하는 다차 함수 시간 결정성 알고리즘이 존재한다. 

-> 완전한 진짜 정답을 찾기 보다는 훨씬 적은 양의 계산을 통해서 정답에 가까운 값을 찾는데 만족

"**현재"의 알고리즘으로 그것을 다항시간 내에 해결 가능한지 불가능한지 알 수 없지만 적어도 다항시간 이상은 걸릴 수 밖에 없는 알고리즘일 것이기 때문**이다.

명백하지 않은 문제 크기의 NP-complete를 해결하기 위한 방법론들이 있음 

> 1. Approximatin(근사)
>
>  어떤 알려져 있는 적절한 범위내에 있는 차선의 (suboptimal) 해결책을 빠르게 찾는 알고리즘. 모든 NP-complete 문제가 good approximation algorithms 을 가진 것은 아니며, good approximation algorithm 을 발견한 문제도 문제 그 자체를 해결하기에 충분하지는 않다.
>
> 2. Probabilistic (확률)
>
> 문제의 instance 에 대한 확률 분포 (이상적으로는 "hard" 입력에 대해 낮은 확률을 할당하는) 에 대해 훌륭한 평균 runtime behavior 를 낳는다고 입증된 알고리즘
>
> 3. Special cases
>
> 문제의 instance 가 어떤 특별한 경우에 속한다면 빠르다는 것이 입증된 알고리즘
>
> 4. Heuristic
>
> 많은 경우에 "reasonably well" 작동하지만, 항상 빠르다는 증명은 없는 알고리즘



# error(오차) 와 residual(잔차) 차이

만약 모집단에서 회귀식을 얻었다면, 그 회귀식을 통해 얻은 예측값과 실제 관측값의 차이가 **오차**

반면 표본집단에서 회귀식을 얻었다면, 그 회귀식을 통해 얻은 예측값과 실제 관측값의 차이가 **잔차**

즉, 

**오차 = 모집단의 회귀식에서 예측된 값 - 실제 관측값**

-> 추정한 회귀식과 모집단에서의 관측값의 차이 ε로 표기 

**잔차 = 표본집단의 회귀식에서 예측된 값 - 실제 관측값 **

-> 모수를 추정하는 방법

잔차들의 제곱들을 더한 것(잔차제곱합)을 최소로 만들어주는 파라미터를 찾는 것이 최소제곱법 

- 오차

> 1. **고정 오차(fixed error)**
>
> 회귀식이 변수들 사이의 참의 관계식을 반영하지 못할때 발생
>
> 2. 확률적 요소(random component)
>
> > - **측정오차란(measurement error) **
> >
> > 측정하고자 하는 관찰값과, 측정도구를 적용하여 얻은 측정값의 차이
> >
> > - **설명변수의 부재로부터 일어나는 오차**
> > - **Pure error**
> >
> > 자연 발생적으로 생겨나 통제불능한 오차

- 잔차

잔차를 바탕으로 회귀식을 추정하고, 오차에 대한 진단을 할 수 있기 때문에, 잔차는 사실상 매우 중요한 값

## GBDT(Gradient Boosting Decision Tree)

Gradient Boosting Algorithm (GBM)은 회귀분석 또는 분류 분석을 수행할 수 있는 **예측모형**이며 예측모형의 **앙상블 방법론** 중 **부스팅** 계열에 속하는 알고리즘

- Boosting

Boosting이란 약한 분류기를 결합하여 강한 분류기를 만드는 과정

![boostring](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\boostring.png)

![adaboost](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\adaboost.png)

- Gradient

**residual에 fitting해서 다음 모델을 순차적으로 만들어 나가는 것**은** negative gradient를 이용해 다음 모델을 순차적으로 만들어 나가는 것**

![gradient](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\gradient.png)

## Graph Coloring Problem

특정 제한 및 제약 조건에 따라 그래프의 특정 요소에 색상을 할당하는 것

-> 인접한 두 꼭지점이 같은 색을 가지지 않도록 색을 할당하는 과정

![graph_coloring](\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\graph_coloring.png)

접근방식

1. Brute Force
2. Backtracking

 정점에 색상을 지정하고 인접한 정점에 색상을 지정하는 동안 다른 색상을 선택

채색 후 시작했던 동일한 꼭짓점으로 돌아가 모든 색상이 사용되면 더 많은 색상이 필요



- 응용

> 1. 일정 또는 시간표
> 2. 기지국 주파수 할당
> 3. 스도쿠
> 4. 레지스터 할당(CPU에 프로세스 할당)
> 5. 지도 채색
> 6. ... 





# 참고

- np-hard

https://ko.wikipedia.org/wiki/NP-%EB%82%9C%ED%95%B4

https://m.blog.naver.com/jinp7/222068113705

https://inverse90.tistory.com/entry/PNP-NP-Hard-NP-Complete

- error(오차) 와 residual(잔차) 차이

https://bskyvision.com/642

https://bpapa.tistory.com/8

https://jangpiano-science.tistory.com/116

- LGBM

https://aldente0630.github.io/data-science/2018/06/29/highly-efficient-gbdt.html

- GBDT(Gradient Boosting Decision Tree)

https://3months.tistory.com/368

https://www.slideshare.net/freepsw/boosting-bagging-vs-boosting

- Graph Coloring Problem

https://www.interviewbit.com/blog/graph-coloring-problem/

https://www.geeksforgeeks.org/graph-coloring-applications/
---
layout: post
title: "paper : LightGBM: A Highly Efficient Gradient Boosting Decision Tree"
date: 2022-04-22 16:20:23 +0900
category: paper
---

# LightGBM: A Highly Efficient Gradient Boosting Decision Tree

url : https://proceedings.neurips.cc/paper/2017/file/6449f44a102fde848669bdd9eb6b76fa-Paper.pdf
2017  microsoft









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

![np](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\np.png)



- NP-hard

![NP-hard](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\LightGBM_A_Highly_Efficient_Gradient_Boosting_Decision_Tree\NP-hard.png)

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





# 참고

- np-hard

https://ko.wikipedia.org/wiki/NP-%EB%82%9C%ED%95%B4

https://m.blog.naver.com/jinp7/222068113705

https://inverse90.tistory.com/entry/PNP-NP-Hard-NP-Complete

- error(오차) 와 residual(잔차) 차이

https://bskyvision.com/642

https://bpapa.tistory.com/8

https://jangpiano-science.tistory.com/116
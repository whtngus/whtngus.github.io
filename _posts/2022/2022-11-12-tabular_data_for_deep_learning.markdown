---
layout: post
title: "tabular data for deep learning"
date: 2022-11-12 01:20:23 +0900
category: datascience
---

# 왜 deep learning을 사용하려고 하는가?

tabular 데이터에서 효과적으로 학습하는 deep learning 의 장점은?

1. 자동화된 엔지니어링

deep learning을 이용해 전처리를 대신 할 수 있다.

1. transfer learning

transfer learning을 통해 pre training된 모델을 원하는 테스크에 fine-tuning하여 적용 할 수 있음

1. 단일 모델에서 비정형 데이터 및 다양한 데이터와 결합 가능

트리 계열 모델은 화장이 불가능 하나  딥러닝 기반의 접근 방법에서는 멀티모달과 다른 입력 데이터를 비교적 자유롭게 조합 가능

1. 활용의 유용성

1~3번과 더불이 representation vector 를 생성하여 다양한 방법으로 응용 가능

ex) few shot learning, cross domain recommendation, etc ….

# Tabular data에서 deep learning의 성능이 좋지 않은 이유

이렇게 좋은점이 있는데 왜 tabular 데이터에서 XGboost, CatBoostm LightGBM 들과 같은 트리계열 모델 모델을 사용할까?

1. 데이터에 종종 상관 관계가 있으므로 특성이 작은 하위 집합이 대부분 예측을 담당 
2. NULL 데이터베이스의 값 형태로 누락된 데이터
3. imbalance 
4. 이질적인 데이터가 비정형 데이터에 비해 비교적 많음(목표와 관련 없는 feature)
5. 각 feature 별 의미 단위가 달라 scaling 적용이 어려움 
6. 데이터에 비해 실질적인 정보량이 적음
7. feature의 value의 차이값이 거의 없는 데이터가 발생할 가능성이 높음 
8. etc …

이러한 많은 이유로 tabular data 에서 deep learning을 적용하고자 할 때 딥러닝에 최적화된 방식의 전처리 혹은 임베딩 방식이 필요하다!

# deep learning을 사용한 예시

## TabNet

TabNet의 핵심은**입력 기능의 학습 가능한 마스크**.
또한 학습 가능한 마스크는**부족한**,*즉,*예측 작업을 해결하는 작은 기능 세트를 선택하는 것

![f1](\img\2022\tabular_data_for_deep_learning\f1.png)

의사 결정 트리에서는 특성 값에 엄격한 임계값이 지정되므로 값이 임계값*T*  를 초과하면 트리의 오른쪽 분기로 내려가고 그렇지 않으면 왼쪽으로 이동 하지만, trainable mask를 사용해  결정을 내림

![f2](\img\2022\tabular_data_for_deep_learning\f2.png)

이 모델의 두 번째 장점은 비지도 학습으로도 가능 하다는것

## Neural Oblivious Decision Ensembles (NODE)

이 방식은 CatBoot를 개발한 Yandex 출신자가 게재한 논문으로 CatBoost와 방식이 유사함

![f3](\img\2022\tabular_data_for_deep_learning\f3.png)

각각 동일한 깊이  *d 를 갖는 ODT(Oblivious Decision Trees)의 미리 지정된 수  m*  으로 구성

여기에서의 기능은 각 ODT가 미분 가능해 역전파가 가능하다는 것! 

(트리 구조를 미리 지정을 한후 해당 트리 노드를 weight로 사용)

![f4](\img\2022\tabular_data_for_deep_learning\f4.png)

각 수준에서 분할을 위해 정확히 하나의 feature가 선택됨

이 방식은 약 학습기의 neural network 들을 합쳐 강 학습기로 만드는 것 

## nomolization 정리

sclearn.preprocessing 라이브러리를 중심으로 정리 

- StandardScaler

```jsx
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
df_std = scaler.fit_transform(df)
```

**각 열의 feature 값의 평균을 0으로 잡고, 표준편차를 1로 간주하여 정규화**시키는 방법

특징 각 데이터가 평균에서 몇 표준편차만큼 떨어져 있는지를 기준으로 삼기 때문에 

데이터의 특징을 모르는 경우 무난하게 사용 가능

- MinMaxScaler

```
X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
X_scaled = X_std * (max - min) + min

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df_mm = scaler(df)
```

각 feature의 최소값 0, 최대값 1로 균등하게 값을 배정

**이상치에 민감하다는 단점**이 있긴 하지만,

**각 feature의 범위가 모두 0~1로 동등하게 분포를 바꿀 수 있다는 장점**

- RobustScaler

```jsx
from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
df_robust = scaler.fit_transform(df)
```

**각 feature의 median(Q2)에 해당하는 데이터를 0으로 잡고, Q1, Q3 사분위수와의 IQR 차이 만큼을 기준**으로 정규화

(x - q2) / (q3 - q1)

- MaxAbsScaler

```jsx
from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()
df_mas = scaler.fit_transform(df)
```

절대값이 0~1 사이에 매칭하게 해서 -1 ~ 1 사이로 재조정

- [QuantileTransformer](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.QuantileTransformer.html)

```jsx
>>> import numpy as np
>>> from sklearn.preprocessing import QuantileTransformer
>>> rng = np.random.RandomState(0)
>>> X = np.sort(rng.normal(loc=0.5, scale=0.25, size=(25, 1)), axis=0)
>>> qt = QuantileTransformer(n_quantiles=10, random_state=0)
>>> qt.fit_transform(X)
array([...])
```

지정된 분위수에 맞게 균등분포로 데이터를 변환(default 1,000)

RobustScaler와 비슷하게 이상치에 민감하지 않게됨

하지만 균등 분포라서 무조건 0 ~ 1 사이로 클리핑함

output_distribution=’normal’ 로 지정하면  [scipy.stats.norm.ppf()](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) 함수를 사용하여 정규 분포로 변환

### 최종 정리

- 나머지는 알겠는데 Quantile Transformer는 …

많은 머신러닝 알고리즘들은 변수의 분포가 가우시안분포일때, 더 좋은 성능을냄

quantile transformation은 변수의 확률분포를 퀀타일 함수(PPF)로 맵핑시키는 작업

→ 퀀타일 함수는 누적분포함수(CDF)의 역함수

CDF는 현재 값과 현재 값 이전의 값들을 반환하는 반면
PPF는 반대로 현재 값과 이전의 값들에게 주어진 확률을 반환

### 2022 년도에 tabular를 deep learning으로 접근하기 위한 논문들이 많이 나오고있다.;

이중 몇개를 찾아보자~ 

# 참고

- deep learning 적용

[https://towardsdatascience.com/the-unreasonable-ineffectiveness-of-deep-learning-on-tabular-data-fd784ea29c33](https://towardsdatascience.com/the-unreasonable-ineffectiveness-of-deep-learning-on-tabular-data-fd784ea29c33) (* 거의 모든내용 다 참고)

- base

[https://neptune.ai/blog/tabular-data-binary-classification-tips-and-tricks-from-5-kaggle-competitions](https://neptune.ai/blog/tabular-data-binary-classification-tips-and-tricks-from-5-kaggle-competitions)

- nomalization

[https://jimmy-ai.tistory.com/139](https://jimmy-ai.tistory.com/139)

[https://tensorflow.blog/2018/01/14/quantiletransformer/](https://tensorflow.blog/2018/01/14/quantiletransformer/)

- Quantile Transforme

[https://mkitlez630.blogspot.com/2021/12/quantile-transformation-1.html](https://mkitlez630.blogspot.com/2021/12/quantile-transformation-1.html)
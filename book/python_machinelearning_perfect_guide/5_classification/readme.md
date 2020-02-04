# 4장 분류

## 2. 결정 트리

> 결정트리 (Decision Tree) <br>
>> ML 알고리즘 중 지관적으로 이해하기 쉬운 알고리즘.
>> 데이터에 있는 규칙을 학습을 통해 자동으로 찾아내 Tree 기반으로 분류 규칙을 만드는 것.
>> ex) if, else 를 자동으로 찾아내 예측을 위한 규칙을 만드는 알고리즘 

<img src="./pic/decision_tree_01.PNG" width="400px" height="300px"></img> <br>
>> 출처 wiki <br>
```
    - 위 예의 사진을 통한 결정트리 개념 설명
규칙 노드 (Decision Node) : 규칙 조건   ex) 남자인가?
리프 노드 (Leaf Node) : 규칙 노드를 통해 결정된 클래스 값
서브 트리(Sub tree) : 새로운 규칙 조건마다 서브 트리가 생성됨

이러한 노드들을 추가하여 불균형하게 나눠주는 결정들을 찾아야 한다.  
-> 균일도가 높아야한다 (각 분류된 결과에 하나의 결과로만 이루어 질수록 좋다)
==> 즉, 정보 이득 지수와 지니 계수를 통해 구할 수 있음.(지니 계수가 1(높은)수가 되도록 한다)

    - 결정 트리의 장단점
- 장점
정보의 "균일도"라는 룰을 기반으로 하고있어 알고리즘이 쉽고 직관적이다.
시각화가 가능하다.
피처의 스케일링과 정규화 작업이 필요가 없다
- 단점
과적합으로 정확도가 떨어진다.
피처가 많고 균일도가 다양하게 존재할수록 트리의 깊이가 커지고 복잡해진다.

    - 결정 트리 파라미터
* 사이킷런 기준
- min_smaples_split
노드를 분할하기 위한 최소한의 샘플 데이터 수 (과적합 제어에 좋음)
default : 2  
- min_smaples_leaf
말단 노드(Leaf)가 되기 위한 최소한을 샘플 데이터 수 (과적합 제어에 좋음)
비대칭적 데이터의 경우 특정 클래스의 데이터가 극도로 작을 수 있음으로 작게 설정해야한다.
- max_features
최적의 분할을 위해 고려할 최대 피처 개수  
defalut : None  -> 고려 안함
sqrt, auto : 루트(전체 피처 개수)
log : log2(전체 피처 개수) 
- max_depth
트리의 최대 깊이를 규정
- max_lef_nodes
말단 노드의 최대 개수
```

> 결정 트리 모델의 시각화

```
Graphviz 패키지를 이용하는 방법이 있음
=> 굳이 보고싶지 않음으로 이부분은 패스
아래 링크 참조 
https://github.com/wikibook/ml-definitive-guide/blob/master/4%EC%9E%A5/4.2%20%EA%B2%B0%EC%A0%95%20%ED%8A%B8%EB%A6%AC.ipynb
```

> 결정 트리 시습 - 사용자 행동 인식 데이터 세트
```
UCI 머신러닝 리포지토리(Machine Learning Repository)에서 제공하는 사용자 행동 인식 데이터 세트(Human Activity Reconition) 데이터 세트 사용
url : http://archive.ics.uci.edu/ml/datasets/Human+Activity+Recognition+Using+Smartphones
코드 ./decision_tree.py  참조
코드 돌린결과 출력 아래 (중요 피처 출력)
```
<img src="./pic/decision_tree_code_result_01.PNG" width="400px" height="300px"></img> <br>

## 앙상블 학습
> 앙상블 (Ensemble)
```
    - 앙상블 학습 (Ensemble Learning)
여러 개의분류기(Classifier)를 생성하고 그 예측을 결합함으로써 보다 정확한 최종 예측을 도출하는 기법
* 부스팅 계열의 앙상블 알고리즘의 개발 가속화 (인기 가 많음)

    - 앙상블의 학습 유형
- 보팅(Voting), 배깅(Bagging)
여러개의 분류기기가 투표를 통해 최종 예측 결과를 결정하는 방식.
보팅은 서로 다른 알고리즘을 가진 분류기를 결합
배깅은 각각의 분류기가 모두 같은 유형의 알고리즘 기반 (데이터 샘플링을 다르게 둠)
부트스트래핑(Bootstrapping) 분할 방식 : classifier에게 데이터를 셈플링해서 추출하는 방식
- 부스팅(Boostring)
여러 개의 분류기가 순차적으로 학습을 수행, 앞에서 학습한 분류기가 예측이 틀린 데이터에 대해서는 올바르게 예측할 수 있도록
다음 분류기에는 가중치(weight)를 부여하면서 학습과 예측을 진행.
대표 부스팅 : 그래언트 부스트, XGBoost(eXtra Gradient Boost), LightGBM(Light Gradient Boost)
```
> 보팅 유형 
```
    - 하드 보팅(Hard Voting)과 소프트 보팅(Soft Voting)
- 하드 보팅
다수결의 원칙과 비슷함.
예측한 결괏값들 중 다수의 분류기가 결정한 예측값을 최종 보팅 결괏값으로 선정 

- 소프트 보팅 
분류기들의 레이블 값 결정 확률을 모두 더하고 이를 평균해서 이드 중 확률이 가장 높은 레이블 값을 최종 보팅 결괏값으로 선정
* 일반적으로 소프트 보팅을 많이 사용 

    - 보팅 분류기 (Voting Classifier)
사이킷 런에서 VotingClassifier 클래스를 제공 


```



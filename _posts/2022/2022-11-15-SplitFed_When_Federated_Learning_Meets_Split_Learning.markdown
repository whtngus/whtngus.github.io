---
layout: post
title: "SplitFed: When Federated Learning Meets Split Learning Recommendation"
date: 2022-11-19 01:20:23 +0900
category: paper
---
# split learning

****SplitFed: When Federated Learning Meets Split Learning****

2020 4월 25일 최초 arxiv

Accepted at AAAI 2022 

위 논문을 베이스로 설명 

# Federated Learning

최초로 federated learning이라는 용어가 생긴 이유는 google에서 막대한 연산량에 부담을 느끼고, Android OS를 사용하는 수많은 device들을 이용해보면 어떨까 라는 것에서 시작 

각 클라이언트에서 학습 후 모델을 서버에서 전송해 그 결과를 어그리게이션 해 클라이언트로 다시 전송하는 행위

![f1](\img\2022\SplitFed_When_Federated_Learning_Meets_Split_Learning\f1.png)

- 단점
- local device에서 모든 학습이 이루어진 후 학습 결과를 server에 반환하는 구조 이기 때문에

    1. 부족한 연산 능력  local device가 충분한 computing power를 가지고 있어야 하지만 부족하기 때문에 고도화된 모델 적용이 불가능함  

    2. Server 관리자가 악의적인 마음을 가지고 있다면 얼마든지 model에 접근할 수 있다는 보안상의 약점을 가지고 있음 
    3. Byzantine Fault Tolerance : 악이적 접근을 가진 device가 학습에 참여하는 경우 모델에 문제가 생길 수 있음
    4. 각기 다른 device 사양 : 적용되는 device가 다 다르기때문에 연산 능력의 차이로 생기는 문제점  

# federated learning 의 유형

| 연합학습의 유형                        | 설명                                       |
| ------------------------------- | ---------------------------------------- |
| Cross-device federated learning | 몇 대 부터 수천, 수백만대 기기까지 설정 범위가 넓음, 사용자 경험을 점진적으로 향상하는 등의 사용사례에 이상적인 방식 |
| Cross-silo federated learning   | 개별 기기가 아닌 조직 사이에서 이루어지는 학습, 대량의 데이터셋을 보유한 기관이 서로 협력하여 ML 모델을 발전시키는 데 있음 |

# what is Split Learning

![f2](\img\2022\SplitFed_When_Federated_Learning_Meets_Split_Learning\f2.png)

![f3](\img\2022\SplitFed_When_Federated_Learning_Meets_Split_Learning\f3.png)

위 그림에서 초록색은 client와 server 간의 통신이 이루어지는 레이어 

해당 지점을 Cut Layer라고 부르며,  Client가 Cut Layer 이전까지 local에서 학습을 진행하면 Server에서 그때까지의 학습 결과를 받는데 이 데이터를 Smashed Data라고 지칭

장점

- Split Learning의 경우
    1. shallow한 부분만 local에서 학습을 진행(computing power 여유) deep한 부분은 server에서 학습하며, 
    2. 과정을 두 부분으로 분리하기 때문에 보안상의 이점을 가지고 있음 

![f4](\img\2022\SplitFed_When_Federated_Learning_Meets_Split_Learning\f4.png)

- 처리 빙법
    1. 각 Client가 Cut Layer까지 forward propagation을 진행하고 그 결과인 Smashed Data를 Main Server로 전송
    2. Main Server는 Smashed Data를 이용해 forward propagation을 수행하고, 다시 Cut Layer까지 backpropagation을 수행 후, 그 결과를 Client 에게 반환
    3. Client는 마저 backpropagation을 한 후 그 결과를 Fed Server로 반호나 
    4. Fed Server는 FedAVG 등의 aggregation method를 통해 global update를 수행 후 Client 에게 전송 
- 학습에 요구되는 Total Cost

    ![f5](\img\2022\SplitFed_When_Federated_Learning_Meets_Split_Learning\f5.png)


K: 학습에 참여한 client의 수

W: global model

β: W의 client-side fraction (따라서, |WC|=β|W|)

p: dataset 전체의 크기

q: smashed layer의 크기 (따라서, pq/K는 smashed data의 크기)

T: 크기 p 만큼의 dataset을 가지고 1회 forward / backword propogation하는 데에 걸리는 시간

fedavg: 1회(Client + Server)의 model aggregation에 걸리는 시간

R: communication rate

# 실 적용 사례

1. 구글 Gboard

    ![f6](\img\2022\SplitFed_When_Federated_Learning_Meets_Split_Learning\f6.png)


각 사용자가 입력할 단어를 예측해주는 기능

각 사용자의 단어 사용 패턴을 익힐 때에 사용자의 채팅 이력을 device에 둔 채로 학습할 수 있으므로 privacy preserving에 용이

1. 의료  분야 

****Federated Learning powered by NVIDIA Clara****

[https://www.nature.com/articles/s41746-021-00431-6](https://www.nature.com/articles/s41746-021-00431-6)

새로운 감염병이 유행하기 시작한다면, 초기에는 임상 자료가 충분하지 않아 원활한 model 학습이 진행되지 않을 것입니다. 이때에 각 병의원마다, 혹은 각 국가마다 몇 건 씩 흩어져 있는 데이터를 모두 사용할 수 있다면 더욱 원활한 model 학습이 진행될 것입니다. 물론, 이러한 의료 데이터는 민감한 개인정보이므로 함부로 주고 받을 수 없지만, 연합학습을 사용한다면 이 부분은 해결될 것입니다. 실제로 COVID-19 관련 데이터 분석에 연합학습을 적용한 사례

# 참고 지식

- calibrated noise

해당 논문에서 Client Backpropagation과정에서 noise Layer가 등장하는데 PixcelDP라는 concept를 학습 과정에 적용한 것

- dp(differential privacy)

    ![f7](\img\2022\SplitFed_When_Federated_Learning_Meets_Split_Learning\f7.png)


유저가 받은 모델을 통해 계산된 가중치(∇W)에 근사한 가중치(∇W′)가 생기도록 **GAN** 모델을 학습하여 원본 데이터를 복원하는 방법

참고 

1. ****splitFed****

[https://federated-learning.tistory.com/entry/AAAI-2022-SplitFed-1?category=978322](https://federated-learning.tistory.com/entry/AAAI-2022-SplitFed-1?category=978322)

1. dp

[https://tootouch.github.io/research/federated_learning/](https://tootouch.github.io/research/federated_learning/)

1. federated learning

[https://proandroiddev.com/federated-learning-e79e054c33ef](https://proandroiddev.com/federated-learning-e79e054c33ef)

[https://m.post.naver.com/viewer/postView.naver?volumeNo=31853352&memberNo=20717909](https://m.post.naver.com/viewer/postView.naver?volumeNo=31853352&memberNo=20717909)

1. split Learning

[https://github.com/mlpotter/SplitLearning](https://github.com/mlpotter/SplitLearning)

1. 적용 사례

[https://tootouch.github.io/research/federated_learning/](https://tootouch.github.io/research/federated_learning/)

[https://federated-learning.tistory.com/entry/2-Cross-Silo-FL과-Cross-Device-FL](https://federated-learning.tistory.com/entry/2-Cross-Silo-FL%EA%B3%BC-Cross-Device-FL)
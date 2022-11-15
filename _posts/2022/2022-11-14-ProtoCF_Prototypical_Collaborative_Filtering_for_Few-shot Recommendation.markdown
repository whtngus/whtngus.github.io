---
layout: post
title: "ProtoCF: Prototypical Collaborative Filtering for Few-shot  Recommendation"
date: 2022-11-15 01:20:23 +0900
category: paper
---


# ProtoCF: Prototypical Collaborative Filtering for Few-shot
Recommendation

ProtoCF: Prototypical Collaborative Filtering for Few-shot
Recommendation

# 지식

### pointwise, Pairwise

CDAE 논문에 따르면, 추천 시스템에서 Loss function은 보통 러프하게 2가지로 분류

1. point-wise approaches

Point-wise는 Loss function에서 한번에 하나의 아이템만 고려

하나의 User에 대응하는 하나의 Item을 가져와 Score를 계산하고 Label score와 비교하는 방식

score를 나열해 rank 개념으로 사용 가능 

- Item과 Item 사이의 순서 관계를 무시하고, 그냥 독립적인 개체로써 학습시키고, 결과만 정렬하기 때문에 단점이 명확함

그러나 직관적이고 일반적인 Loss와 분류 회귀 모델을 적용 가능 

(ex LSE Loss)

1. **Pair-wise approache**

**Pair-wise approache**

1개의 positive 1개의 negative item을 고려 

Pos, Neg item pair 가 들어오면, Pos item > Neg item 이라는 Rank가 자연스럽게 형성

- Rank를 미리 고려해서 학습을 하고, Rank로 평가를 하기 때문에 point-wise 보다 일반적으로 성능이 좋음

(ex - BPR, WARP, CLiMF)

### loss functino

- LSE loss(Least square error)

= mse loss

- BPR Loss(****Bayesian Personalized Ranking)****

베이지안 추론(maximum a posteriori, MAP)에 기반한 optimization 기법

- WARP Loss(Weighted Approximate-Rank Pairwise)

순위학습 방법 , triplet loss 와 유사함 

추천 등급이 낮은 아이템과 높은 아이템을 가져와 *잘못된*  예측을 한 경우, 즉 부정적 품목이 긍정적 품목보다 높은 점수를 가질 경우에만 SGD를 업데이트

- CLiMF Loss

### episodic learning

따라서 적은 수의 데이터를 학습하는 Few Shot Learning에 기계가 스스로 학습규칙을 도출하도록 하는 meta learning을 적용해서 성능을 높이자는 것이 아이디어

즉, 적은 데이터를 보고 학습한 후 좋은 성능을 내는 사람을 모방해서, 모델 스스로가 학습규칙을 도출할 수 있도록 도와줌으로써 일반화 성능을 높일 수 있도록 하게 한다.

training set 전부를 쓰지 않고 test set과 동일한 환경에서 training을 진행하는 것이 episodic training

episode 마다 training set에서 uniform하게 클래스를 선택후 support set과 batch set을 구성

![f1](\img\2022\ProtoCF_Prototypical_Collaborative_Filtering_for_Few-shot\f1.png)

![f2](\img\2022\ProtoCF_Prototypical_Collaborative_Filtering_for_Few-shot\f2.png)



전체 training set으로 학습을 진행하는게 아니라 episode 단위로 몇개의 클래스만 선정하여 학습하기 때문에, overfitting이 방지되는 효과가 있다

# 참고

- pointwise pariwise

[https://junklee.tistory.com/126](https://junklee.tistory.com/126)

- episodic learning

[https://mambo-coding-note.tistory.com/477](https://mambo-coding-note.tistory.com/477)

[https://deep-learning-study.tistory.com/941](https://deep-learning-study.tistory.com/941)


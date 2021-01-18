---
layout: post
title: "paper : CogLTX: Applying BERT to Long Texts"
date: 2021-01-19 19:20:23 +0900
category: paper
---



# CogLTX: Applying BERT to Long Texts



## 정보

- 논문 URL  

https://proceedings.neurips.cc/paper/2020/file/96671501524948bc3937b4b30d0e57b9-Paper.pdf

- git URL 

https://github.com/Sleepychord/CogLTX

- 게재일 

34th Conference on Neural Information Processing Systems (NeurIPS 2020), Vancouver, Canada



## 리뷰

### 1. 도입

BERT 베이스 모델을 이용하여 긴 텍스트에 대한 임베딩을 하기 위한 논문

BERT는 좋지만 긴 텍스트에 대해서 모델의 입력으로 쓸기 힘든 문제가 있다.

트랜스 포머의 인력 시퀀스 길이(n)이 커짐에 따라 메모리 크기가 n^2 으로 상승 

너무 커지는 메모리를 해결하고 긴 텍스트를 문장단위로 임베딩 하기 위한 방법을 제시 

<img src="/img/paper/CogLTX_Applying_BERT_to_Long_Texts/model_input.PNG" width="600px" height="250px"/>

```
각 테스크에 따라 입력 테스트를 MemRecall 모델을 통해 z를 추출 
z는 아래에서 설명(입력 문장에서 필요한 텍스트만을 추출한 압력 텍스트)
```



### 2. 관련 설명

- long texts

기존 BERT의 최대 임베딩 토큰 수는 512개 이다.

 BERT-large모델 모델에서 1500 token의 text라면 1 batch size기준으로 14.6GB memory가 필요하다.

-> 벌써 RTX 2080ti(11GB)를 넘어선다.

토큰이 늘어날 수록 O(L^2)만큼 메모리를 차지하게 됨으로 그냥 입력 사이즈를 늘린다면 감당하기 힘들다

- Related works









# 참고 사이트

- 


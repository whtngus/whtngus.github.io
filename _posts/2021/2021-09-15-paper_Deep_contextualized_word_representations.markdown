---
layout: post
title: "paper : Deep contextualized word representations"
date: 2021-09-16 19:20:23 +0900
category: paper
---

# Deep contextualized word representations 

paper : https://arxiv.org/abs/1802.05365

NAACL 2018

Allen Institute for Artificial Intelligence
allenai.org



# 0. abstract

새로운 타입의 문맥을 고려한 임베딩 모델을 제안함 

1. 문맥에 따라 단어의 복잡도가 올라감(단어의 복합성)
2. 여러 언어들을 어떻게 처리할 것인지 (맥락에 따른 언어 사용)

대구모 텍스트 말뭉치에서 사전 훈련돤 bi-LM 모델을 사용해 학습 

-> bi-LSTM 사용 

이를 이용하여 6가지 down stream nlp task에서 높은 점수를 찍음



#  1. Introduction

사전 훈련된 단어 표현학습들이 많이 존재하나 abstract에서 설명한 문맥을 고려한 표현을 하는것은 어렵다 

이를 해결하기 위해 해당 연구에서 많은 말뭉치를 이용한 언어모델을 제안 

-> LSTM을 이용 (지금은 언어 학습모델은 트랜스포머로 사용하지만 이때는 아직 LSTM위주로 사용하는듯 ELMO와 비슷 )  

기존 LSTM기반 언어모델의 예시로는 ELMO 와 CoVo가 있다. 

(Covo모델은 모르겠어서 차후 하단에 정리 하자)



# 2. Related work

라벨이없는 대규모 텍스트에서 단어의 구문 및 의미 정보를 캡처하는 학습 들은 

```
pretrained word vectors (Turian et al., 2010; Mikolov et al., 2013; Pennington et al., 2014) are a standard component of most state-ofthe-art NLP architectures, including for question answering (Liu et al., 2017), textual entailment (Chen et al., 2017) and semantic role labeling (He et al., 2017).
```

위와 같이 많이 있다. 하지만 의미적 영역을 해결하기 어려운 단점이 있다.

해당 연구에서는 Conv layer를 이용해서 하위 단어의 이점을 얻으며 클래스를 예측하여 다중 정보를 다운스트림 작업에 완벽하게 적용시키고자 한다.



# 3. ELMo: Embeddings from Language Models

보통 사용되는 Word2Vec 과 달리 ELMo의 단어 표현은 문장 전체를 입력으로 하고 내부 네트워크에서 Convolution Layer를 가진 biLM 모델에서 계산된다 .

## 3.1 Bidirectional language models

주어진 문장에서 각 토큰 t1  ~ tn 에서 일반적인 시퀀스 모델링의 k번째 토큰 tk는 다음과 같다.

![f_1](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\f_1.PNG)

- 단순하게 이전의 입력 토큰을 보고 다음 토큰을 예측 혹은 representation 하겠다는 의미

CNN 기반의 캐릭터 임베딩을 통해 위의 레이어를 쌓는다 

각각의 위치 k에 따라 각 레이어의 마지막 LSTM Layer의 output을 사용하고 다음 토큰 이용시에넌 Softmax를 통해 사용한다.

 ![f_2](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\f_2.PNG)

- 위 수식은 간단하게 이전 토큰들만 보는게 아니라 문장 전체를 보고 representation을 하기 위해서 이후토큰도 보고 embedding한다는 의미 

![f_3](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\f_3.PNG)

위처럼 bi LM 을 만들기 위해서 각 토큰의 forward와 backward LM 정보를 정보 보고 output을 생성한다. 

위 수식에서 세타x는 각 forward와 backward의 softmax layer 이다.



## 3.2 ELMo

ELMo는 biLM 의 준간 계층 표현의 조합이다.

각 토큰 Tk에 대해 L층 biLM은 2L + 1 표현집합을 계산한디 (forward back word)

![f4](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\f4.PNG)

각 Representation 은  h-> h<- (각 방향의 LSTM <- biLSTM) 레어의 결과와 해당 토큰의 output으로 결정된다. 각 R은 single vetor



다운스트림 테스크 시에는 ELMo는 top  layer를 선택한다 

![f5](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\f5.PNG)

s-task는 softmax-normalized weights 

r-task 는 scalar parameter 이다 .(모델의 task scalar을 결정)

## 3.3 Using biLMs for supervised NLP tasks

위의 과정을 거쳐 사전 훈련된 biLM과 대상 NLP task에 대해 지도학습을 고려할때 biLM을 사용해 작업 모델을 fine-tuning 한다.

사전 훈련된 단어 임베딩 및 선택적으로 문자 기반 표현을 사용하여 각 토큰 위치에 대해 컨텍스트에 독립적인 토큰 표현 xk를 형성하는 것이 표준

RNN, CNN 또는 피드 포워드 네트워크를 사용하여 상황에 맞는 표현 hk를 형성

 biLM 계층의 평균에 가깝게 유지하기 위해 ELMo 가중치에 유도 편향을 부과한다. -> L2 Normalization

## 3.4 Pre-trained bidirectional language model architecture

해당 논문의 biLM은 양방향 훈련을 한다는 점에서 차이점을 두고 있음 

그리고 LSTM의 차수를 줄여 모델을 적당선에서 경량화

최종 모델은 406개의 유닛과 512찿수의 representation 벡터를 가진 L =2 개의 biLSTM 레이어를 사용 



# 4. Evaluation

![t_1](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\t_1.PNG)

![t_2](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\t_2.PNG)

여러 테스크에서 sota를 찍었으며 각 스코어를 공유 

# 5. Analysis

![c_1](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\c_1.PNG)

위의 Figure 1 은 base line 대비 ELMo의 성능 비교이다 .

Figure 2는 softmax 후 각 layer weight에 대한 값을 시각화한것  (주로 최종 레이어가 가장 높을것으로 예상했으나 LSTM 1이 높다 신기 )

# 6. Conclusion

기존 연구들과 달리 biLM을 통해 여러 다운스트림 테스크에 대해 sota 를 달성하고 문맥적인 정보를 효율적으로 임베딩 한다는 것을 확인 



# 참고

## COVE(Contextualized Word Vectors)

참고 url : https://towardsdatascience.com/replacing-your-word-embeddings-by-contextualized-word-vectors-9508877ad65d



![cove_!](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\cove_!.PNG)

![cove_2](D:\code\whtngus.github.io\img\2021\Deep_contextualized_word_representations\cove_2.PNG)

문맥 임베등을 위해 GLOVE 임베딩 방법을 LSTM 모델 구조로 한번더 학습시킨 모델


---
layout: post
title: "Dimensional Emotion Detection from Categorical Emotion"
date: 2022-12-17 01:20:23 +0900
category: datascience
---

# Dimensional Emotion Detection from Categorical Emotion

•2021년 11월 게재

•학회:EMNLP

•소속– 서울대, 카이스트, upstage


# 1. Introduction

•미묘한감정의 변화도 잘 잡아야함.

VAD의 3-dimensional의 연속적인 공간으로 표현 

그러나 이건 3가지 감정만을 포함하기 때문에 다양한 감정을 포착해야 할 필요가있음

부족한 데이터에도 불구하고 여러가지 감정을 디텍션하는 방법을 고안해냄

•데이터셋

문장 단위의 VAD 학습파일이 필요하지만 데이터셋이 많이 부족함

논문에서는 이걸 해결하기 위해  NRC-VAD어휘에서얻은 점수를 활용하여 VAD점수에 사용하는 방법을 제안

![Untitled](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f3.png)

- 그림 설명
- 그림설명
    1. 입력 문장에 대한 3가지 카테고리컬 감정 분포를 학습 후 예측

    각 단어단위로 예측 감정 카테고리 예측  

    b. 카테고리 레이블링 데이터를 받아 VAD점수를 정렬

    각 감정의 분포와 예측한 감정의 분포가 일치하도록 학습 

    c. 레이블링된 VAD점수를 기반으로 가장 감정이 심한 것들을 추출 

    추출된 각 단어 단위의 감정 카테고리 중 max 값을 추출

    → 왜 max만 추출하지?  

    argmax를 통해 확률값으로 값을 치환 

    d. 감정 분포 결과를 이용해 VAD score 추출


해당 논문에서의 접근 방법은 단어 단위의 VAD score를 예측하는 NCR-VAD lexicon을 활용

- 예시

    ‘joy’인 경우 (0.9, 0.3, 0.1)   ‘sad’인 경우 (0.2, 0.3 ,0.1)로 각 vad 예측 

    ![Untitled](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f4.png)


### 모델 학습

RoBERTa 모델을 이용해 문장 임베딩을 함 

- 메인 아이디어

VAD 카테고리 레이블을 학습한 모델 

이게 가능한 이유는 word-label로 VAD가 가능한 NRC-VAD lexicon을 찾았기 때문 

- 모델 구조

X : input text., e : categorical emotion

일반적인 VAD 예측은 P(e|X)로 sequence별로 V,A,D 예측 

![f5](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f5.png)

함수는 EMD로 아래와 같은 누적함수 분포의 차이값으로 학습

![f6](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f6.png)

p는 label p hat은 예측값

![f7](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f7.png)

vc는 클래스간 거리가 서로 동일하지 않은 경우가 많아서 멀리 떨어져 있으면 더 큰 가중치를 주기 위한 장치 (V ,A ,D 중 하나)

![f8](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f8.png)

 이전 수식은 각 V, A, D 별로 구했음으로 EMD를 다 더한것을 기준으로 함 

# 3. Dataset

4개의 텍스트 감정 데이터셋을 사용

3개는 가정 카테고리컬, 하나는 VAD 스코어 

- SemEval 2018 E-c(SemEval)

multi-labeld 감정 카테고리 데이터셋 

10,983 개의 트위터와 응답 데이터 

11개의 감정 분류 

- ISEAR

single-labeled categorical emotion

7,666 문장과 7개의 감정 

- GoEmotions

multi-labeld 감정 카테코리 데이터셋

58,009개의 redit 대화와 28개의 감정 카테고리가 있음 

→ 희소성이 심함 이를 해결하면 7개의 감정 카테고리가 남음 

- EmoBank

연속적인 문장의 VAD score 

6가지 도메인의  10,062 문장   1~5점으로 점수화됨 

train set 7  valid set 1.5 test set 1.5 비율로 구성 

## Zero-shot VAD Prediction

EmoBank 데이터셋을 사요하지 않고 다른 데이터셋을 Zero-Shot Learning으로 학습 후 EmoBank 데이터셋을 테스트 

![f9](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f9.png)

- 그림 설명
    - Ours

    3개의 데이터셋을 zero-shot learning을 통해 학습

    - AAN(Adversarial Attention Network)

    감정 regression 모델

    VAD스코어와  Pearson correlation으로 벼교 

    - Emsemble

    Multi-task ensemble neural networks 

    - SRV-SLSTM

    VAD Prediction sota 모델, 

    - RoBERTa-Large

    linear layer과 Relu 레이어를 추가해 EmoBank Training Set을 학습 

    → 당연히 데이터셋이 부족하니 스코어가 낮겠지. .. .

    MSE loss 사용 


# 4. Results and 5. Ablation Study

![f10](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f10.png)

대체적으로 높은 성능을 보임 

→ 아마 해당 데이터셋에서 RoBERTa-Large가 아닌 Base를 사용했다면 더 높지않을까..



# 기타 지식

### EMD (Earth Mover’s Distance) loss 

![f1](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f1.png)

### VAD (valence, arousal, and dominance)

![f2](\img\2022\Dimensional_Emotion_Detection_from_Categorical_Emotion\f2.png)



# 참조

1. NCR-VAD lexicon

[https://saifmohammad.com/WebPages/nrc-vad.html](https://saifmohammad.com/WebPages/nrc-vad.html)

- EMD

 https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=swkim4610&logNo=220970999014

- VAD

https://brunch.co.kr/@learning/18


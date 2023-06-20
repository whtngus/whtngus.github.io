---
layout: post
title: "VAST: A Vision-Audio-Subtitle-Text Omni-Modality Foundation Model and Dataset"
date: 2023-06-25 02:05:23 +0900
category: paper
---

# VAST: A Vision-Audio-Subtitle-Text Omni-Modality Foundation Model and Dataset



2023년 3월 29일

url : https://arxiv.org/pdf/2305.18500.pdf
code url : https://github.com/TXH-mercury/VALOR



# Abstract

video 와 text는 최근 많이 연구되고 있지만 비디오에서 오디오와 자막등은 충분한 연구가 되고 있지 않음

해당 연구에서 멀티모달 트랙을 새롭게 정의

Vision, Audio, and Subtitle, and Text -> VAST-27M dataset으로 정의함

27M 개의 공개된 비디오 클립과 영상과 음성캡션 데이터셋

LLM을 이용해 캡션을 생성 

여기에서 제안하는 VAST모델을 통해 22개의 sota 스코어를 달성

# 1 Introduction

![f_1](F:\code\whtngus.github.io\img\2023\VAST_A_Vision-Audio-Subtitle-Text_Omni-Modality_Foundation_Model_and_Dataset\f_1.PNG)

많은 양의 영상들이 플랫폼에 매일 업로드 되고있고 AI가 영상을 이해하는게 중요한 역할을 차지하게 됨

video captioninig - 비디오를 이해하는 테스크

text-to-video retrieval - 비디오 검색

video QA -  video 질의응답

이를 해결하기 위해위 위와 같은 테스크가 있음



그러나 현재 연구되고 있는 모델들은 멀티모달을 온전히 반영하지 못함 

-> 오디오와 자막등을 고려하지 않았기 때문에 

Figure 1 에서 omni-modality 모델은 vision audio subtitle을 모두 처리하는것을 볼 수 있음 

![t_2](F:\code\whtngus.github.io\img\2023\VAST_A_Vision-Audio-Subtitle-Text_Omni-Modality_Foundation_Model_and_Dataset\t_2.PNG)

위의 Table 2에서 처럼 모든 데이터가 같이 있는 겨우가 없음 그렇다고 새로 데이터를 가공하기에는 많은 비용이 드는 문제가 있음

![f_2](F:\code\whtngus.github.io\img\2023\VAST_A_Vision-Audio-Subtitle-Text_Omni-Modality_Foundation_Model_and_Dataset\f_2.PNG)

데이터셋 이슈를 해결하기 위해 Figure 2에서처럼 두 가지 파이프 라인으로 amni-modality 데이터셋을 생성

Vision, audio 캡션 모델을 각각 학습시킴 -> 높은 성능의 싱글 modality 모델을 사용

Vicuna-13b (LLM) sota 모델 사용



# 2 Related Work

## 2.1 Cross-Modality Pretraining Corpus

### Video-Text Pretraining Corpus

해당 테스크의 경우 large cale인 HowTo100M 데이터셋 사용

136M 비디오 클립과 1.22M 개의 유튜브 비디오 데이터셋 



YT-Temporal-180M 데이터셋은 180m비디오 클립과, 6m 유튜브 비디오셋이 있음 

HD_VILA_100M 은 100M 비디오 클립, 3.3M 유튜브 비디오

### Audio-Text Pretraining Corpus.

Clotho, AudioCaps, MCAS, AudioCaption 데이터셋이 있으며 50,000  오디오 클립이 있음 

## 2.2 Multi-Modality Learning

MMT - video-test understanding

SMPFF - text-to-video retirieval  (비디오 입력을 받아 영상과 오디오로 텍스트를 생성)

그 외에도 UniVL, CoMVT, VALUE 등이 있음 

# 3 Dataset

## 3.1 Data Collection of VAST-27M

### Vision Captioner Training




















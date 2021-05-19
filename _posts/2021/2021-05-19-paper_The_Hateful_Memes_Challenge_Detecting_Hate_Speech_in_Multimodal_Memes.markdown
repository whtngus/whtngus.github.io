---
layout: post
title: "paper : The Hateful Memes Challenge: Detecting Hate Speech in Multimodal Memes"
date: 2021-05-20 19:20:23 +0900
category: book
---

# 논문 정보 

논문 명 : The Hateful Memes Challenge: Detecting Hate Speech in Multimodal Memes

2020년 5월 10일 게재 (최종 업데이트 2021년 4월 7일)

Facebook AI

url : https://arxiv.org/abs/2005.04790

기술 논문이 아닌 데이터 논문으로 간단하게만 정리



# 1. Introduction

이미지 캡션에서 시각적 질문에 대한 답변(VQA) 및 그 이후까지 멀티 테스크러닝에 대한 관심이 금증하고 있다.

이 멀티모달을 이용해서 현실에서 발생하는 데이터를 처리하고싶어 한다. 

기존 연구들에서는 멀티모달 테스크를 진행함에 있어 이미지는 상대적으로 중요하지 않은것으로 밝혀졌다. 



해당 논문에서는 혐오성 있는 발언을 탐지하는것을 목표로 한다.

![example_image](\img\2021\The_Hateful_Memes_Challenge_Detecting_Hate_Speech_in_Multimodal_Memes\example_image.PNG)

위의 사진 예시와 같이 같은 사진에서도 우측 사진은 좋은 글이지만 좌측 사진은 혐오성 있는 발언임을 알 수 있다.

이 데이터를 가공하는 목적은 혐오성 있는 데이터를 혐오스럽지 않은 텍스트로 변환하는것을 목표로 한다 (위 예시에서 좌측 사진의 입력을 우측 사진으로 바꾸는것을 목표로 함)

-> 혐오스럽다는 느낌의 기준점과 데이터셋을 구축하는 방법들이 이 논문에 메인 주제

# 혐오스러운 데이터 정의

혐오스럽다는 기준을 명확하게 하기 위해서 클라우드 소싱 알바생? 들에게 태깅을 하기전 충분한 교육을 시키고 정확한 판단을 하기 위해 하나의 밈당 27분정도를 사용 (데이터를 구축하는데 많은 돈이 소모되었을걸로 예상)

혐오스러운 데이터를 정의하기 위해 다양한 정의와 용어를 사용(인종, 국적, 종교, 성, 장애, 질병 등등 매우 많음)

혐오스러움의 기준을 정하기가 어렵기 때문에 몇가지 예외를 둔다  유명인이나 개인에대한 공격을 허용(왜?) 또한  증오를 가하는 공격도 포함하지 않음 -> 애매한 경계에 있는 내용들을 제거하기 위해

![annotation](\img\2021\The_Hateful_Memes_Challenge_Detecting_Hate_Speech_in_Multimodal_Memes\annotation.PNG)



위의 사진과 같은 데이터 가공 방법을 통해 해결 - 언어는 OCR 엔진을 통해 영어가 아닌 내용은 먼저 걸러냄 

... 그 이후 필터링, OCR을 위한 텍스트를 사진에 추가, 혐오스러움 정도 측정, 테스트셋등을 구성 

# 데이터 분석

![performance](\img\2021\The_Hateful_Memes_Challenge_Detecting_Hate_Speech_in_Multimodal_Memes\performance.PNG)

스코어를 보여줌으로써 데이터를 예측및 검증 



진짜 간단하게 끝(기술 논문인줄알고 열었는데 데이터셋 논문이여서 읽은김에 쭉 읽고 정리는 대충)
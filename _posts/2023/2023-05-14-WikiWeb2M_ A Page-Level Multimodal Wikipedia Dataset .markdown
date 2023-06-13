---
layout: post
title: "WikiWeb2M: A Page-Level Multimodal Wikipedia Dataset"
date: 2023-06-13 00:05:23 +0900
category: paper
---

# WikiWeb2M: A Page-Level Multimodal Wikipedia Dataset

2023년 3월 9일

google

url : https://arxiv.org/pdf/2305.05432v1.pdf

code : https://github.com/google-research-datasets/wit/blob/main/wikiweb2m.md

학습 데이터셋 

(짧은 논문)

# Abstract

Web Page들은 NLP 혹은 VLP task를 처리하기에 풍부한 데이터셋을 가지고있음

아직은 웹페이지 전부를데이터셋으로 구성하지 못하고 일부 이미지-캡션, 긴 텍스트 설명, 원문 html 등 부분적으로만 사용되고 있음 

이를 해결하기 위해 Wikipedia Webpage 2M 데이터 셋을 소개함 -> 앞으로 WikiWeb2M이라고 부름

우선,  웹페이지의 텍스트와 이미지 그리고 그 구조를 유지함 -> 원문 html을 가공한다는 건가?



WikiWeb2M는 페이지 설명 생성, 요약, image captioning 테스크에 사용될 수 있다고 함 



# Indroduction

웹페이지 데이터는 pre-training과 fine-tuning에 주로 쓰였음

-> wiki 데이터등 을 이야기 하는듯

그러나 웹페이지 데이터는 노이즈를 많이 포함해 다운스트림 테스크에 잘 작동하지 않는 케이스들이 발생 

그리고 대부분의 데이터는 공개되 않음 

![t_1](\img\2023\WikiWeb2M A Page-Level Multimodal Wikipedia Dataset\t_1.PNG)

예시로 Wikipedia Image Text(WIT) 데이터셋은 html 구조를 포함하지 못하며 텍스트를 잃어버림 

 Table 1에서 Image의 개수 차이를 볼 수 있음 

-> 여기에서 WIT도 Text는 있는데 - 로 표시한건 section단위 인덱스로 비교하지 못해서 그런듯 

WikiWeb2M은 모든 텍스트와 이미지를 포함함 

하나의 페이지에서 다운 스트림 테스크인 section 요약 contextual captionig을 어떤식으로 만들 수 있을지 알지?

라고 함 

![t_2](\img\2023\WikiWeb2M A Page-Level Multimodal Wikipedia Dataset\t_2.PNG)

Table 2의 왼쪽 표는 down stream task 적용 시 페이지 단위 예시 데이터셋 크기

# The WikiWeb2M Dataset

영어 데이터셋인 WIT 데이터셋을 기반으로 데이터셋을 구축함

Table 2의 왼쪽은 WIT 웹페이지를 랜덤하게 섞어서 만든 데이터 

제목 세션의 경우 비어있거나 테이블 정보로 다른 세션의 아티클에 연결됨 (참조)

# The WikiWeb2M Tasks

Table 2의 분할된 학습 데이터를 토대로 T5 와 ViT base 모델 사용해 평가

- Page Description Generation


웹페이지 이미지가 들어온 경우 설명을 생성하는것 

여기에서 설명은 단순 텍스트가 아닌 구조를 포함한 텍스트 

- Section Summarization

웹페이지의 이미지와 텍스트에서 highlights 텍스트를 생성하는것 

사람들은 보통 세션의 처음 부분을 중요하다고 요약함 

-> 그래서 바이어스를 제거하기위해 마지막 5 세션만 제공함 (상위 root 섹션은 제공 X)

- Contextual Image Captioning

웹페이지의 하나의 섹션이 아닌 전체 문맥을 사용할 수 있음 

WIT 이미지만 사용함  3단어 이상이 포함된 경우 사용

중복이 많이 있는 경우 제외함 


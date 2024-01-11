---
layout: post
title: "LLM-Adapters: An Adapter Family for Parameter-Efficient Fine-Tuning of Large Language Models"
date: 2024-01-11 02:05:23 +0900
category: paper
---

# LLM-Adapters: An Adapter Family for Parameter-Efficient Fine-Tuning of Large Language Models

2023년 10월 9일 

url : https://arxiv.org/abs/2304.01933

EMNLP 2023

학생 



# Abstract

GPT-4와 ChatGPT가 나오면서 fine-tunig 대신 open-access LLM 방식이나  instruction data 방식을 사용하게 됨 

PEFT 방식은 일부 파라미터만 학습하는 좋은 방식이고 계속해서 연구되고 있다.



LLM은  LLaMA, BLOOM, and GPT-J등 

-> 최근 게재된 논문이지만 참조되는 논문은 오래된 논문이 많음을 감안해야할듯

2가지 테스크의 14개의 테스크 데이터셋을 이용해 PEFT와 smaller-scale LLM(7B)를 학습하고 평가함 

# 1 Introduction

Chat-GPT와 GPT-4가 NLP에서 엄청난 퍼포먼스를 보임

-> 이렇게 되면서 대규모 모델과 비공개 코드가 다시 많이지게됨 (공개해줘 ㅠ)



이를 해결하기 위해 비용효율이 높은 학습 방법이 연구되었고 예시로 LLaMA모델이 나오게됨

(LLaMA는 ChatDoctor, instructional data 를 통해 학습)

그래도 FFT(Full-model Fine-Tuning)을 하기엔 모델이 매우 큼... (BERT때도 프리트레이닝 하기엔 충분히 컸는데)

이렇게 되면서 현실적인 최적화 연구가 시작됨











# 참고지식

- BLOOM

약 1,000명 정도의 학술 자원봉사자로 구성된 공개 협업 프로젝트인 빅사이언스(BigScience)에서 개발 

-> 2022년도 개발됨 

- GPT-J

마찬가지로 2022년도 모델

GPT-3의 오픈소스 버전

 60억 개 파라미터 (6B)



# 참고
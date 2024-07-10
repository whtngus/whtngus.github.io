---
layout: post
title: "ChatQA: Surpassing GPT-4 on Conversational QA and RAG"
date: 2024-07-10 02:05:23 +0900
category: paper
---

# ChatQA: Surpassing GPT-4 on Conversational QA and RAG



NVIDIA

2024년 5월 22일

url : https://arxiv.org/abs/2401.10225

https://chatqa-project.github.io/



# Abstract

GPT-4 보다 뛰어난 ChatQA 를 제안함 



생성 성능을 높이기 위해  two-stage instruction tuning 방법을 제안함 

-> 이방법을 통해 RAG 성능을 상당히 높힐 수 있다고 함 



1. QA 대화를 위한 dense retriever optimized 방법

기존 sota 방식인( query rewriting models)에 비해 비용감소도 가능하다고함 

CHATRAG BENCH 데이터셋 을통해 10가지 데이터셋으로 RAG를 종합적으로 평가함

- table-related QA
- 산술 계산
- 대답할 수 없는 질문들이 포함된 시나리오

등이 있음



해당 모델은 Llama2를 베이스로 함 ChatQA-1.0-70B (score: 54.14),



GPT-4-0613 (score: 53.90) and GPT-4-Turbo2024-04-09 (score: 54.03) 두 모델보다 높은 성능을 달성



# 1 Introduction


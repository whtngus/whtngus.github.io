---
layout: post
title: "G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment"
date: 2024-06-20 02:05:23 +0900
category: paper
---

# G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment

url : https://arxiv.org/abs/2303.16634



# 1 Introduction

LLM 모델 평가 방법은 

사람의 개입 없이 평가하는 방법과 사람이 평가하는 Human Evaluation 평가 방법이 있음 



태스크에 대한 정답이 있는 경우 사용할 수 있는 reference-based 평가에서 gold label에 대한 기계적인 평가 매트릭인 BLEU, ROUGE와 같은 지표는 창의성이나 다양성이 필요한 태스크에서 인간의 판단 혹은 선호도와 낮은 상관관계를 보여 사용하기 힘듦

 모든 태스크에 대해 Gold label이 존재하는 것이 아니므로 최근에는 정답 없이도(reference-free) 생성 결과물의 품질을 평가하는 LLM 기반의 평가 방법들이 제안되고 있음 



G-Eval인 자연어 생성(NLG) 시스템이 생성한 텍스트의 품질을 자동으로 평가하는 방법으로  Chain-of-Thought(CoT)과 form-filling을 제안함 

논문의 컨트리뷰션

1. 개방형 및 창의적 자연 언어 생성 작업에서 인간 품질 판단과의 상관관계 측면에서 참조 기반 및 참조 없는 기본 메트릭보다 성능이 뛰남
2. 사고의 연쇄(chain-of-thought)는 더 많은 맥락과 지침을 제공함으로써 LLM 기반 평가자의 성능을 향상시킬 수 있음
3. 토큰 확률에 따라 이산 점수를 재가중하여 더 세분화된 연속 점수를 제공할 수 있음
4. LLM 기반 평가를 하는 경우 

# 2. Method

![f_1](F:\code\whtngus.github.io\img\2024\G-Eval__NLG_Evaluation_using_GPT-4_with_Better_Human_Alignment\f_1.PNG)





















# 참고 

- G-Eval

https://littlefoxdiary.tistory.com/123

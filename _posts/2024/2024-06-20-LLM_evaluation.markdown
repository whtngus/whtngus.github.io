---
layout: post
title: "LLM Evaluation"
date: 2024-06-20 02:05:23 +0900
category: datascience
---

# LLM 모델 평가 방법

LLM 모델 평가 방법은 

사람의 개입 없이 평가하는 방법과 사람이 평가하는 Human Evaluation 평가 방법이 있음 



태스크에 대한 정답이 있는 경우 사용할 수 있는 reference-based 평가에서 gold label에 대한 기계적인 평가 매트릭인 BLEU, ROUGE와 같은 지표는 창의성이나 다양성이 필요한 태스크에서 인간의 판단 혹은 선호도와 낮은 상관관계를 보여 사용하기 힘듦

 모든 태스크에 대해 Gold label이 존재하는 것이 아니므로 최근에는 정답 없이도(reference-free) 생성 결과물의 품질을 평가하는 LLM 기반의 평가 방법들이 제안되고 있음 





# G-Eval 평가 방법

paper url : G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment

 

자연어 생성(NLG) 시스템이 생성한 텍스트의 품질을 자동으로 평가하는 방법

해당 연구에서는 

 Chain-of-Thought(CoT)과 form-filling을 제안함 





















# 참고 

- 전체 내용 

https://gagadi.tistory.com/58
---
layout: post
title: "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval"
date: 2024-06-27 02:05:23 +0900
category: paper
---

# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

2024년 1월 31일 

스탠포드

url : https://arxiv.org/html/2401.18059v1



# ABSTRACT

RAG 모델은 long tail 지식의 문제점에 도움을 줌 

그러나 작은사이즈의 청크의 문제의 한계로 전체적인 문맥의 이해는 하지 못하는 ㅁ누제가 있다.

bottom up방식의 recursively embedding, clustering, and summarizing chunks 3가지 방법을 제안함 

RAPTOR model은 tree 구조로  QA , multi-step reasoning 등 다양한 테스크에서 sota를 찍음 

-> 이때 llm 은 GPT-4를 사용함 



# 1 INTRODUCTION

LMMs는 크기가 커짐에 따라 많은 테스크에서 매우 좋은 성능을 보임 

그리고  fine-tuning을 통해 구체적인 테스크에 접근가능함 



그럼에도 모델에도 특정 작업에 대한 도메인별 지식이 충분하지 않아 LLM이 무효화되며 fine-tuning하는것은 점점 더 어려워지고 있음.

retrieval-augmented 접근 방법으로도 결함이 있음 

대부분이 few shot 기반의 접근 방식으로 chunk 된 데이터 기바으로 데이터 길이에 제한이 있음

ex) NarrativeQA dataset



![f_1](F:\code\whtngus.github.io\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\f_1.PNG)

RAPTOR 방식은 텍스트 요약을 통해 청크 클러스터 방식을 사용함 

해당 내용은 반복 생성을 통한  bottom up 방식의 트리형 생성 방법을 사용 

이렇게 함으로써 어려운 테스크도 효과적으로 질문에 답변할 수 있음 



논문에 메인 컨트리뷰션은 서로다른 크기의 텍스트를 요약하고 retrieval argumentation으로 활용하는 아이디어 



# 2 RELATED WORK

#### Why Retrieval? 

최근 고급화된 hardware나 알고리즘은 문맥의 길이에 따라 확장 및 처리 가 필요하다.

-> 이걸 retrieval로 해결



그러나 모델은 긴 문맥의 정보를 충분히 이용하지 못하고 있어 성능이 저하되고 있다.

추가로 긴 문맥은 비용이 비싸며 답변도 느리게 만든다 

#### Retrieval Methods

Retrieval-augmented language models (RALMs) 은 다양한 구성요소로부터 발전되어옴 

..생략..

#### Recursive summarization as Context

요약 테스크는 문서의 압축된 정보를 제공함으로써 문맥에 집중할 수 있게 해줌 



반복적이고 추상적인 요약 방법론들은 텍스트 청크요약으로 많이 사용되어옴 

그러나 세부정보를 놓칠 수 있는 단점이 있음 

# 3 METHODS

#### Overview of RAPTOR

긴 텍스트를 부분적인 토픽의 계층적인 구조료 요약함

이때 의미적인 단계 그리고 트리로 관계에 의한 균형있는 구조를만들어서 사용함 

RAPTOR 트리 구성은 검색 코퍼스를 짧고 연속적으로 분한하는것으로 시작됨 

전통적으로 사사용하는 길이는 100 토큰 정도라고함 

청크와 SBERT 임베딩은 트리 구조의 리프 노드를 형성함 



또 유사한 텍스트 청크 군집화를 제공 



트리 내에서 쿼리하는 방법은 트리 순회 및 축소 2가지 전략을사용함

순회 트리 : 트리를 한 층씩 순회하면서 관련성 높은 노드를 선택

축소 트리 : 가장 관렷어 높은 노드를 찾기 위해 모든 계층에 걸쳐 노드를 일괄적으로 평가

#### Clustering Algorithm

RAPTOR의 클러스터링의 핵심 방법은 텍스트의 응집력있는 segement그룹을 선택하는것

 소프트 클러스터링을 사용하여 노드가 여러 클러스터에 속할 수 있으며, 고정된 클러스터 수를 요구하지 않는 특징이 있음 

-> 개별 텍스트 세그먼트가 종종 다양한 주제와 관련된 정보를 포함하고 있어 여러 요약에 포함될 필요가 있기 때문에 중요함

 Gaussian Mixture Models (GMMs) 알고리즘을 기반으로 클러스터링함 

GMM은 데이터 포인트를 mixture Gaussian distribution의여러 혼합 분포에서 데이터가 생성된다고 가정

![f1](F:\code\whtngus.github.io\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\f1.PNG)

N : 텍스트 세그먼트들

X : d-dimention embedding vector











# 참고

- multi-step reasoning 

일반적으로 query가 주어지고 그에 대한 answer를 주는 QA와 달리 multi-step reasoning은 LM에게 해당 정답이 나올 때까지의 추론 과정을 요구

ult-step 자체를 평가하기는 어렵기에 대부분의 benchmark에서 accuracy와 함께 perplexity를 보는 task이다



https://velog.io/@xuio/%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0NLPSpecializing-Smaller-Language-Models-towards-Multi-step-Reasoning



-  Gaussian Mixture Models (GMMs),

![g-1](F:\code\whtngus.github.io\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\g-1.PNG)

Gaussian Mixture Model (GMM)은 이름 그대로 [가우시안 분포 (정규분포)](https://en.wikipedia.org/wiki/Normal_distribution)를 여러 개 혼합하여 데이터의 복잡한 분포를 근사하기 위한 머신러닝 알고리즘

아래와 같은 확률밀도함수의 혼합으로 정의됨

![gf-1](F:\code\whtngus.github.io\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\gf-1.PNG)

자세한 수식 생략



https://untitledtblog.tistory.com/133
---
layout: post
title: "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval"
date: 2024-07-02 02:05:23 +0900
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



![f_1](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\f_1.PNG)

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

![f1](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\f1.PNG)

N : 텍스트 세그먼트들

X : d-dimention embedding vector

πk : k개의 mixture weight 



전통적인 GMM 방식은 high-dimension공간에 취약함 

이런 문제를 오나화시키기 위해 y Uniform Manifold Approximation and Projection(UMAP) 방법을 사용함 

-> manifold learning 방법으로 차원을 축소시키는 방법론중 하나로 보임 (차원축소 알고리즘 중 하나)



UMAP 에서 사용하는 n_neigbors(nearest neigbors parameter) 로 로컬과 글로벌 구조를 보존함 

-> 이걸 활용해 계층적 클러스터 구조를생성함 



지역내 클러스터의 결합된 컨텍스트가 요약 모델의 토큰 한도를 초과하는 경우, 클러스터 내에서 재귀적으로 클러스터링을 적용하며 컨텍스트가 토큰한도 내에 유지되도록함 



최적화된 클러스터 수를 유지하기 위해 Bayesian Information Criterion (BIC) 모델 selection 방법을 사용함 

... 내용 생략 ...

#### Model-Based Summarization

Gaussian Mixture Models을 통해 클러스터 노드를 설정 후 각가의 노드들은 텍스트 요약을 진행함 

이렇게 만들어진 일관성 있는 데이터는 GPT-3.5 를 이용하여 요약함 

![t_10](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\t_10.PNG)

table 10은 데이터 형상  -> 데이터 길이가 짧음 

table 11은 그때 사용한 템플릿 -> 생각이상으로 간단함 



요약을 진행할대 4% 이하의 요약 할루시내이션이 발생하도록 함 

-> 질문 답변 테스크 진행시 식별 가능할정도의 임팩트를 제거함 

## 트리 생성방법 다시 정리 

1. 재귀적 임베딩, 클러스터링 요약

문서의 작은 부분을 재귀적으로 임베딩하고, 클러스터링 및 요약을 함 

이렇게하면 문서의 요약 수진이 다른 여러 단계로 구성된 트리를 생성 가능



#### Querying

![a_1](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\a_1.PNG)

다층구조의 PARTOR의 tree traversal과 collaped tree 2개를 정교하게 설정하여 검색하는 고유한 방법을 제공함

각각의 고유 방법들은 장점과잔점이 있고 모든노드는 SBERT를 사용하여 임베딩함 

- #### tree traversal 방법

query embedding을 통해 root node와 관련있는 top-k를 cosin similarity로 최초로 선택 

선택된 children 노도들은 다음 레이어의 top-k를 또 선택하는것을 반복함 

그리고 모든 노드들이 선택되면 종료

![f_2](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\f_2.PNG)

다시 정리 - 그림2의 위쪽과 같음 

1. PARTOR tree의 root layer를 설정 (query로 부터) 그후 cosin similarity 기준 가장 가까운 inital layer를 생성
2. 가장 가까운 top-k 노드의 스코어를 S_1 로 정의
3. S_1의 집합 요소들의 자식 노드로 이동해 쿼리 백터와 자식 노드들의 벡터 임베딩과의 거리를 체크
4. 쿼리 코사인 유사도가 가장 높은 상위 k개의 자식노드를선택하여 s_2 집합을생성 
5. 쿼리에 대한관련 컨텍스트를조립하기 위해 s1에서 sd 까지 연결함

이 과정을 반복하여 depth d로 내려가면서 각 레이어 별로 k개의 노드를 선택함 

- 특징

*트리 탐색 방법은 검색된 저옵의구체성과 폭을 제어할 수 있음*

상위 계층을 고려하여 넓은 시각으로 시작하고 하위 계층으로 내려가면서 점진적으로 세부 사항에 집중할 수 있음 

- #### collapsed tree

간단한 방법의로 트리의모든 노드에서 유사도를 검색함 

1. 전체 PARTOR 트리를 단일계층으로 축소 
2. 쿼리 임베딩과축소된 집합 C에있는 모든 노드간의 유사도를 계산
3. 유사도가 높은 k개 노드를 선정  이때 모델의 입력 제한을 초과하지 않도록 미리 정해진 토큰수에 맞게 계속 노드를 하나씩 추가

-> 일반적인 RAG 방식으로 보임 

![f_3](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\f_3.PNG)

QASPER 데이터셋에서 총 20개의 스토리를 선정하여 비교함

그림 3은 결과이고 vector db는 FAISS를 사용

tree traversal 방법이 성능이 더 낮음 

-> 그럼 그냥 일반적인 rag로 하는게 더 좋은거 아닌가.. 싶기도 함

이때 하나의 청크들은 최대 2000토큰까지로 제한했다고함 (UnifiedQA  에서는 400토큰 사용)



#### Qualitative Study

![f_4](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\f_4.PNG)

RAPTOR의 검색과정에 Dense Passage Retrieval(DRP) 방법에 비해 가지는 이점을 이해하기 위해 질적분석 방법을 수행함 

1500단어로 구성된 신데렐라 동화를 사용하여 주제적이고 다단계적인 질문에 초점을 맞춥

 RAPTOR의 트리 기반 검색은 질문의 세부 수준에 맞춰 다양한 트리 계층에서 노드를 선택할 수 있게함



# 4 EXPERIMENTS

#### Datasets

NarrativeQA, QASPER, and QuALITY 데이터셋을 사용

- NarrativeQA 

책과 영화 대본에서 질문 답변을 하는 테스크 





- QASPER  Dataset

과학 연구 논문에 대한 질문 답변을 위한 데이터 세트

1,585개의 자연어 처리 논문에 걸쳐 5,049개의 질문으로 구성 1,572개의 문서가 있음 

Answerable/Unanswerable, Yes/No 방식의 답변 형식

- QuALITY Dataset

multiple-choice 질문이 있는 데이터셋 

데이터의 길이가 평균 5000토큰인 긴 데이터셋

![t_1](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\t_1.PNG)

SBERT, BM25, DPR 다양한 방식에 따른 결과 비교 







나머지는 논문참조 생략...







# 참고

- multi-step reasoning 

일반적으로 query가 주어지고 그에 대한 answer를 주는 QA와 달리 multi-step reasoning은 LM에게 해당 정답이 나올 때까지의 추론 과정을 요구

ult-step 자체를 평가하기는 어렵기에 대부분의 benchmark에서 accuracy와 함께 perplexity를 보는 task이다



https://velog.io/@xuio/%EB%85%BC%EB%AC%B8%EB%A6%AC%EB%B7%B0NLPSpecializing-Smaller-Language-Models-towards-Multi-step-Reasoning



-  Gaussian Mixture Models (GMMs),

![g-1](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\g-1.PNG)

Gaussian Mixture Model (GMM)은 이름 그대로 [가우시안 분포 (정규분포)](https://en.wikipedia.org/wiki/Normal_distribution)를 여러 개 혼합하여 데이터의 복잡한 분포를 근사하기 위한 머신러닝 알고리즘

아래와 같은 확률밀도함수의 혼합으로 정의됨

![gf-1](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\gf-1.PNG)

자세한 수식 생략



https://untitledtblog.tistory.com/133

- manifold learning

고차원 데이터를 데이터 공간에 뿌리면 셈플들알 잘 아우르는 subspace가 있을 것이라는 가정에서 학습을 진행하는 방법

ex) auto encoder로 차원을 축소

주로 4가지로 활용됨

1. 데이터 요약
2. 데이터 시각화
3. 차원의 저주 -> 요약을 통해 차원축소를 함으로써 감소시킴
4. 중요feature 발견

https://deepinsight.tistory.com/124

- sbert

![sbert](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\sbert.PNG)

버트를 이용한 메트릭러닝 방법

https://wikidocs.net/156176

- bm25

![bm25](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\bm25.PNG)

 Bag-of-words 개념을 사용해서 쿼리에 있는 용어가 각각의 문서에 얼마나 자주 등장하는지를 평가함 

https://littlefoxdiary.tistory.com/12

- dpr

![dpr](\img\2024\RAPTOR__Recursive_Abstractive_Processing_for_Tree-Organized_Retrieval\dpr.PNG)

dense Encoder EP를 사용하여 d차원의 실수 벡터로 매핑하고 retrival함 

다른 인코더 EQ에 적용되며 이는 입력으로 받은 질문을 d 차원의 벡터로 매핑하고 질문 벡터와 가장 유사한 k개의 벡터를 검색

여기서도 버트 신경망을 사용함 

Positive and negative passages 방식사용

1. 무작위추출
2. BM25를 사용하여 상위지문 추출 (내용이 비슷한 걸 추출해서 사용가능)
3. 동일한 배치에서 positive 를 다른데이터의 nagative passage로 사용하는건 학습에 도움이 된돠고함 



https://velog.io/@sangmandu/Dense-Passage-Retrieval
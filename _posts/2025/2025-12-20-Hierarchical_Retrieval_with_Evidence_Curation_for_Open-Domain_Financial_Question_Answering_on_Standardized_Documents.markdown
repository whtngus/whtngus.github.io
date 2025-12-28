---
layout: post
title: "Hierarchical Retrieval with Evidence Curation for Open-Domain Financial Question Answering on Standardized Documents"
date: 2025-12-21 02:05:23 +0900
category: paper
---

# Hierarchical Retrieval with Evidence Curation for Open-Domain Financial Question Answering on Standardized Documents

아카이빙



[[2505.20368v1] Hierarchical Retrieval with Evidence Curation for Open-Domain Financial Question Answering on Standardized Documents](https://arxiv.org/abs/2505.20368v1)

한양대학교

2025년 3월 26일 아카이빙



# Abstract

금융 분야의 RAG는 10-K 보고서(연차 보고서)와 같은 정형화된 문서를 다룰 때 어려움을 겪습니다. 이러한 문서는 기업이나 기간이 달라도 반복적인 상용구(boilerplate text)나 유사한 표 구조를 공유함

저자들은 **HiREC(Hierarchical Retrieval with Evidence Curation)** 프레임워크를 제안

1. **계층적 검색(Hierarchical Retrieval):** 관련 문서를 먼저 찾고 그 안에서 구절(passage)을 찾는 방식으로 혼동을 줄입니다.

2. **증거 큐레이션(Evidence Curation):** 불필요한 구절을 필터링하고, 정보가 부족할 경우 '보완 질문(complementary query)'을 생성하여 추가 검색을 수행합니다

![f_1.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\f_1.jpg)

형화된 금융 문서에서 기존 방식과 제안 방식의 차이를 보여줌

- **상단 (Standardized documents):** 아마존(Amazon), 메타(Meta), 월마트(Walmart)의 2023년 10-K 보고서는 "Operating income(영업 이익)" 항목과 같이 매우 유사한 구조와 텍스트를 가지고 있음

- **좌측 (Naive RAG):** "2023년 아마존과 월마트의 영업 이익 비율 차이는?"이라는 질문에 대해, 단순 RAG는 아마존과 월마트 문서를 구별하지 못하고 섞어서 검색하거나 잘못된 정보를 가져와 오답(2.09)

- **우측 (HiREC RAG):** HiREC는 먼저 아마존 관련 정보를 찾고, 부족한 정보(월마트의 영업 이익)를 찾기 위해 **보완 질문(Complementary question)**("What is the operating income ratio Walmart in 2023?")을 생성합니다. 이를 통해 정확한 문서들만 선별하여 정답(3.07)을 도출





![f_2.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\f_2.jpg)

### HiREC 프레임워크 (Methodology)

HiREC은 크게 두 단계로 나뉨

1. **계층적 검색 (Hierarchical Retrieval):**

    ◦ 질문이 들어오면 먼저 **Document Retriever**가 관련 문서(예: 특정 회사의 특정 연도 보고서)를 검색하여 후보군을 좁힙니다.

    ◦ 그 후 **Passage Retriever**가 선별된 문서 내에서 가장 관련성 높은 구절(Top-k)을 찾습니다. 이 과정은 유사한 텍스트로 인한 혼란을 줄여줍니다

2. **증거 큐레이션 (Evidence Curation):**

    ◦ **Passage Filter:** 검색된 구절 중 질문과 무관한 내용을 제거합니다.

    ◦ **Answerability Checker:** 현재 정보로 답변이 가능한지 판단합니다.

    ◦ **Complementary Question Generator:** 답변하기에 정보가 부족하다면(Unanswerable), 필요한 정보를 찾기 위한 새로운 질문(보완 질문)을 생성하여 다시 검색 단계로 보냅니다(빨간 화살표 흐름).



## LOFin 벤치마크

기존 금융 QA 데이터셋은 규모가 작거나 비공개인 경우가 많아 현실적인 평가가 어려웠습니다. 저자들은 S&P 500 기업의 2001~2025년 SEC 파일링(약 145,000건)을 수집하여 **LOFin** 벤치마크를 만들었습니다. 

총 1,595개의 질문-답변 쌍을 포함하며, 여러 문서를 참조해야 하는 복합적인 질문들도 포함

러 문서를 동시에 봐야 풀 수 있는 문제(Multi-document QA)를 포함하기 위해 SEC-QA의 템플릿을 활용함

예를 들어 "A사와 B사의 매출 차이는?"과 같은 질문을 수동으로 작성하고, 이에 대한 정답과 근거 페이지를 사람이 직접 주석(Annotation) 달아 데이터의 품질을 높임

### 데이터 구축 방법

1. FinQA (약 70% 비중): AI 변환 + 사람 검수 (Hybrid)

가장 많은 비중을 차지하는 이 데이터는 **AI가 변환하고 사람이 검증**하는 방식을 썼습니다.

• **질문 변환:** 기존에 있던 FinQA 질문들은 특정 문단을 보고 푸는 방식이라 "영업 이익은?"처럼 주어가 빠져 있었습니다. 이를 **GPT-4o**를 시켜서 "2016년 록히드 마틴의 영업 이익은?"처럼 회사와 연도를 포함하도록 **자동 변환**했습니다.

• **정답 검증:** 질문의 답이 있는 페이지를 찾을 때는 알고리즘(BM25, NLI 모델)을 먼저 돌렸습니다. 하지만 두 알고리즘의 결과가 다를 경우, **사람이 직접 개입하여 정답 페이지를 지정(Annotation)**했습니다.

2. SEC-QA 및 확장 데이터 (약 21% 비중): 100% 사람이 작성 (Manual)

이 논문의 핵심인 **'여러 문서를 참고해야 하는 복잡한 문제(Multi-document)'**들은 AI가 아닌 **사람이 직접** 만들었습니다.

• **직접 제작:** 여러 해의 보고서를 비교하거나 복잡한 추론이 필요한 질문들은 연구진이 템플릿을 바탕으로 **수동으로 작성(Manually craft)**하고 정답을 달았습니다.

• **데이터 유출 방지:** 특히 나중에 추가된 200여 개의 확장 데이터(LOFin-1.6k)는 최신(2025년 4월까지) 문서를 바탕으로 **전적으로 사람이 직접 작성**하여, AI가 훈련 과정에서 미리 데이터를 봤을 가능성(Data leakage)을 원천 차단했습니다.

3. FinanceBench (약 9% 비중): 기존 데이터 활용

• 이미 오픈 도메인 형식으로 잘 만들어진 기존 데이터셋이므로 수정 없이 그대로 가져와 사용했습니다.



## 실험결과

![f_3.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\f_3.jpg)

각 모델이 범하는 오류의 유형(회사 오류, 문서 오류, 페이지 오류)을 보여줌 

**Company error(진한 파랑):** 검색된 정보가 아예 다른 회사의 것인 경우

제안한 HiREC건이 계층적 검색을 통해 회사식별오류를 해결함을 보임 

![f_4.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\f_4.jpg)

증거 큐레이션 과정에서 반복(iteration) 횟수가 늘어날수록 성능이 어떻게 변하는지 보여줌

**파란 선 (Page Recall):** 반복할수록 관련 페이지를 찾는 재현율이 상승

• **회색 점선 (Passages per query):** 반복하면서 불필요한 구절은 필터링되므로, 반복하면서 불필요한 구절은 필터링되므로, 최종적으로 LLM에 입력되는 구절의 수는 줄어들어 비용 효율성이 높아짐을 보여줍니다.

![t_4.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\t_4.jpg)

AG 시스템을 운영할 때 발생하는 **토큰 사용량(Tokens)**과 **비용(Cost, 달러 기준)**을 비교

**배경:** LLM을 이용한 RAG 시스템에서 비용은 주로 LLM이 읽어야 하는 입력 토큰(Input Tokens)의 양에 비례

• **비교 대상:**

    ◦ **Dense:** 일반적인 검색 방식.

    ◦ **IRCoT:** 반복적으로 검색하고 추론하는 방식(성능은 좋지만 비용이 비쌈).

    ◦ **HiREC (제안 모델):** 계층적 검색 및 증거 큐레이션을 적용한 방식.

**토큰 사용량 감소:** HiREC는 검색 단계(Retrieval)에서 불필요한 문서를 걸러내기 때문에, 최종 답변 생성(Generation) 단계에서 LLM에 입력되는 토큰 수가 **1,052개**로 가장 적습니다. 반면 Dense는 2,666개, IRCoT는 3,475개로 훨씬 많음

![t_5.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\t_5.jpg)

이 표는 "답변을 생성하는 LLM(Generator)"을 바꿨을 때 성능이 어떻게 변하는지를 보여줍니다. HiREC 프레임워크가 특정 LLM에만 의존적인지, 아니면 범용적으로 작동하는지 검증합니다.

• **비교 설정:** 검색 방식(Dense vs. HiREC) × 생성 모델(Qwen-2.5-7B, Deepseek-14B, GPT-4o).

• **핵심 결과:**

    ◦ **일관된 우위:** 어떤 LLM을 사용하든 **HiREC가 Dense(기존 방식)보다 항상 높은 성능**을 보입니다,.

    ◦ **작은 모델의 반란 (중요):** **HiREC + Deepseek-14B (오픈소스 소형 모델)**의 성능(평균 38.76점)이 **Dense + GPT-4o (상용 대형 모델)**의 성능(29.22점)보다 훨씬 높게 나왔습니다.

    ◦ **의미:** 검색된 정보(Context)의 품질이 좋으면(HiREC), 굳이 값비싼 최신 LLM(GPT-4o)을 쓰지 않고 **저렴한 오픈소스 모델을 써도 더 나은 결과를 낼 수 있음**을 시사합니다. 이는 기업 입장에서 비용 최적화에 매우 중요한 포인트

![t_6.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\t_6.jpg)

이 표는 LOFin 벤치마크를 구성하는 3가지 원천 데이터셋(FinanceBench, FinQA, SEC-QA) 각각에 대해 모델들의 성능을 세부적으로 쪼개서 보여줍니다.

• **데이터셋 특징:**

    ◦ **FinQA / FinanceBench:** 주로 단일 문서나 페이지에서 답을 찾는 경우가 많습니다.

    ◦ **SEC-QA:** 여러 문서(Multi-document)를 동시에 참고해야 답을 낼 수 있는 가장 어려운 난이도의 문제입니다.

• **핵심 결과:**

    ◦ **모든 영역에서 최고 성능:** HiREC는 세 가지 데이터셋 모두에서 다른 베이스라인 모델(Self-RAG, RQ-RAG 등)을 압도하는 성능을 보였습니다.

    ◦ **SEC-QA (난이도 최상) 결과:** 모든 모델이 SEC-QA에서 점수가 급락합니다(어렵기 때문). 하지만 HiREC는 여기서도 Page Recall(관련 페이지 찾기) 약 20%, 정답률 14%대를 기록하며 2위 모델(HybridSearch, Dense 등)보다 약 2배 가까이 높은 성능을 보였습니다.

    ◦ **의미:** HiREC의 **'보완 질문 생성(Complementary Question Generator)'** 기능이 정보가 부족할 때 추가 검색을 수행하므로, 여러 문서를 뒤져야 하는 복잡한(Multi-hop) 질문에서도 강점을 발휘한다는 것을 보여줍니다.



![t_2.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\t_2.jpg)

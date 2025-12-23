---
layout: post
title: "Hierarchical Retrieval with Evidence Curation for Open-Domain Financial Question Answering on Standardized Documents"
date: 2025-12-23 02:05:23 +0900
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





## 실험결과

![f_3.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\f_3.jpg)

각 모델이 범하는 오류의 유형(회사 오류, 문서 오류, 페이지 오류)을 보여줌 

**Company error(진한 파랑):** 검색된 정보가 아예 다른 회사의 것인 경우

제안한 HiREC건이 계층적 검색을 통해 회사식별오류를 해결함을 보임 

![f_4.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\f_4.jpg)



증거 큐레이션 과정에서 반복(iteration) 횟수가 늘어날수록 성능이 어떻게 변하는지 보여줌

**파란 선 (Page Recall):** 반복할수록 관련 페이지를 찾는 재현율이 상승

• **회색 점선 (Passages per query):** 반복하면서 불필요한 구절은 필터링되므로, 반복하면서 불필요한 구절은 필터링되므로, 최종적으로 LLM에 입력되는 구절의 수는 줄어들어 비용 효율성이 높아짐을 보여줍니다.







![t_2.jpg](G:\code\whtngus.github.io\img\2025\Hierarchical_Retrieval_with_Evidence_Curation_for_Open-Domain_Financial_Question_Answering_on_Standardized_Documents\t_2.jpg)

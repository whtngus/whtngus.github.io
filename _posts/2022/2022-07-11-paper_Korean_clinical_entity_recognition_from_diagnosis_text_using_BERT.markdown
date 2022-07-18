---
layout: post
title: "paper : Korean clinical entity recognition from diagnosis text using BERT"
date: 2022-07-11 01:01:01 +0900
category: paper
---

# Korean clinical entity recognition from diagnosis text using BERT

BMC Medical Informatics and Decision Making 2020

한양대 학생

https://bmcmedinformdecismak.biomedcentral.com/track/pdf/10.1186/s12911-020-01241-8.pdf



# Abstract

- 배경

electronic health records (EHRs)를 목표로 하는 연구들은 다른 유형의 텍스트를 처리해야 한다.

네이버 QA를 통해 EHR과 다른 의료 entity 추출 방법을 제안 

- 결과

새로운 NER 데이터셋을 만들어서 제시 및 NER을 사용하고 

BERT를 사용해 높은 f1 score를 달성

- 결론

위 데이터셋에 BERT 를 이용한 NER 테스크를 수행하고

EHR이 아닌 데이터에 임상 엔티티 추출을 다루는 첫번째 연구를 수행한다.

# Background

- 사용자 생성 QA(관련 연구)

대화 프로세스를 통해 작동하는 자동 의료 진단 시스템을 구축하는 것이 목표

데이터에서 표현된 임상 실체는 시스템을 구성하는 데 필수적이나 

저자들은 강화 학습을 통한 시스템 구축에 중점 둠

- 의료데이터 세트 추출 (non-EHR)

의료 NER을 통해 객체를 추출하는 것을 목표로 함 

![f_1](C:\Users\whtng\OneDrive\문서\src\whtngus.github.io\img\2022\Korean_clinical_entity_recognition_from_diagnosis_text_using_BERT\f_1.png)

위의 Fig. 1은 대상 시스템의 전체 프로세스

챗봇의 기본적인 방법인 entitie와 intent를 인식해 답변을 반환 

-> entity를 의료기반으로 가져감








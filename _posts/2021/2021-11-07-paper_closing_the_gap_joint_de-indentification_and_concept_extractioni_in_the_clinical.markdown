---
layout: post
title: "paper : closing the gap: joint de-indentification and concept extractioni in the clinical"
date: 2021-11-08 19:20:23 +0900
category: paper
---

# closing the gap: joint de-indentification and concept extractioni in the clinical

 ACL 2020

url : https://arxiv.org/pdf/2005.09397.pdf

학생 



# Abstract 

임상 영역에서 nlp를 이용한 개인정보 비식별화가 필요 

현재 연구는 비식별화된 정보를 다른 테스크에 이용하지 않는다.

해당 연구에서는 여러 제한된 스택형 모델과 멀티태킹 모델을 제안함

# 1. Introduction

![f1](\img\2021\closing_the_gap_joint_de-indentification_and_concept_extractioni_in_the_clinical\f1.PNG)

단순히 개인정보만 마스킹하는게 아니라 구조화된 정보를 추출해 용도에 맞게 마스킹을 씌워 사용가능 

현재 환자 데이터를 가지고 이용하는 downsteam task에는 비식별화가 포함되어 있지 않다. 그래서 비식별화를 한 경우 모델에 어떤 영향을 주는지 알수 없는 문제가 있음 

해당 논문에서는 비식별화 후에 모델의 정확도를 측정해야한다고 주장 

 Gumbel softmax trick과 CE로스를 사용하며 영어와 스페인어를 테스트함



# 2. Related Work

최근 많은 연구들이 멀티태스크 학습을 제안한다. 

### De-Identification

일반적으로 RNN  Transformer모델을 이용 

### Medical Information Extraction

의료 개체 인식을 위한 연구들이 많이 있으며 해당 연구에서 비식별화 및 개념 추출을 공동으로 제안한다.



# 3. Model

![f2](\img\2021\closing_the_gap_joint_de-indentification_and_concept_extractioni_in_the_clinical\f2.PNG)

논문에서는 Figure 2에서 보여주는대로 모델을 제안 

### General Architecture

anonymization (ANON) and clinical concept extraction (CE)를 시퀀스 레이블링 문제로 모델링하고 CRF 출력 레이어를 추가 

모델은 스페인어의 경우 BERT와  fastText를 포함 

### Pipeline Model

 pipeline model은 비식별 모델을 적용하여 CE 데이터 세트를 익명화한 다음 익명화된 데이터에 대한 CE 모델을 평가

-> 그냥 비식별화 후에 모델을 평가한다는 의미 

각 phi를 변환해 여러 개인정보 데이터를 익명의 데이터로 변환해 일관적인 입력 데이터로 변환시킴 

### Joint Models

멀티내스킹과 스택형 모델 두가지를 제안 

- Multitask Model

(Figure 2의 b)BiLSTM layer 공통 레이어와 테스크별 레이어를 위에서 나눈 방식 

- Stacked Model

(Figure 2의 c)비식별화 모델을 먼저 통과 후에 gumbel softmax 결과를 이용해  masked embedding 후 테스크를 수행하는 방식

![f_1](\img\2021\closing_the_gap_joint_de-indentification_and_concept_extractioni_in_the_clinical\f_1.PNG)

위 수식은 그냥 gumbel softmax 수식

![f3](\img\2021\closing_the_gap_joint_de-indentification_and_concept_extractioni_in_the_clinical\f3.PNG)

위 그림은 masked embedding의 설명 

gumbel softmax의 결과를 이용해 원래 입력 데이터에서 특수한 토큰으로 분류된 토큰들을 마스킹 씌우는 방식 



# 4. Experiments

![t4](\img\2021\closing_the_gap_joint_de-indentification_and_concept_extractioni_in_the_clinical\t4.PNG)

![t1](\img\2021\closing_the_gap_joint_de-indentification_and_concept_extractioni_in_the_clinical\t1.PNG)

![t2](\img\2021\closing_the_gap_joint_de-indentification_and_concept_extractioni_in_the_clinical\t2.PNG)

![t3](\img\2021\closing_the_gap_joint_de-indentification_and_concept_extractioni_in_the_clinical\t3.PNG)

결과들은 위 표와 같음 ... 

# 5. Conclusion

논문에서는 비식별화 후 테스크를 수행해 스코어를 측정하는것을 제안하고 그 실험을 실제로 수행해 비교해 보여주며 두 가지 모델을 제안 (영어 스페인어)




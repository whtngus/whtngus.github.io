---
layout: post
title: "paper : De-identification of Unstructured Clinical Texts from Sequence to Sequence Perspective"
date: 2021-11-06 19:20:23 +0900
category: paper
---

# De-identification of Unstructured Clinical Texts from Sequence to Sequence Perspective



학생 논문 University of Manitoba Winnipeg, MB, Canada

 ACM CCS 2021



# ABSTRACT

비정형 임상 텍스트의 데이터에서 개인정보 비식별화를 위한 연구 주제 



개체 인식을 위한 시퀀스 학습 모델을 이용해 i2b2 데이터 세트에서 98.91% recall을 달성 

비정형 데이터인 임상 텍스트 식별을 목표로 함 



# 1. INTRODUCTION 

F Toscano, E O’Donnell, MA Unruh, D Golinelli, G Carullo, G Messina, and LP Casalino. 2018. Electronic health records implementation: can the European Union learn from the United States? European Journal of Public Health 28 (2018), 213–401

위 연구에 따르면 병원의 약 95%와 모든 병원 의사으 62%가 EHR(전자 건강 기록)시스템을 사용하는 것으로 나타났다.

하지만 EHR은 구조화되지 않은 텍스트 노트 정보를 포함하고 있다 (-> 병원가면 의사선생님들이 상담하면서 마구 적는 텍스트 내용을 말하는 걸로 보임)

=> EHR의 통계적 분석은 오류 발생 가능성이 적은 의료 진단, 의료 비용 절감 및 단기 예방 치료 개선으로 이어질 수 있다

 

그러나 EHR은 비정형 데이터로써 통계 분석이 간단하지 않고, 환자에 대한 민감한 개인정보를 포함하고 있다.

HIPAA(미국 의료보험 휴대성 및 책입법)은 배포 전에 18개 범주의 정보를 HER에서 다시 식별하도록 요구한다

이 정보는 PHI(개인 건강 정보)인 이름, 직업, 사회보장번호, 운전면허 번호 등 이다. -> 이를 해결하지 못하면 법적으로 분석을 수행하지 못한다.

이를 해결하기 위해 시간당 50달러(시급이 높다)의 비용이 드는 노동자를 사용하며 1억 개의 단어를 포함하는 데이터 세트에 주석을 다는 데 25만 달러가 들 것으로 추론한다. 

또한 사람이 직접 작업하면서 데이터를 주석을 잘못 달거나 안다는등의 실수를 저지르는 경우도 많이 발생한다.

그러나 규칙기반의 비식별화 접근은 많은 문제점을 포함하고 있음으로 BERT와 RNN 등의 레이어를 이용해 이를 해결하려고 함.

 i2b2, MIMIC-II 및 MIMIC-III 와 같은 데이터셋이 있음



# 2. PROBLEM DEFINITION

![model](\De-identification_of_Unstructured_Clinical_Texts_from_Sequence_to_Sequence_Perspective\model.PNG)

구조화되지 않은 임상 텍스트를 식별해 비식별화 하는걸 목표로 한다. 

HIPAA는 공개 전 EHR에서 제거해야하는 18가지 유형의 PHI를 식별한다. 

각 토큰 T는 phi등급 중 하나에 속하거나 속하지 않는걸 분류로 보고 토큰별 classification을 수행한다.

![f1](\De-identification_of_Unstructured_Clinical_Texts_from_Sequence_to_Sequence_Perspective\f1.PNG)

위 수식은 간단하게 PHI정보를 포함하고 있으면 마스킹을 포함하고 있지 않으면 원본 텍스트를 그대로 둔다 .



# 3. PROPOSED SOLUTION

인코더와 디코더 모두 Multi head Attention으로 구성된 모델을 사용 

입력은 고정 시퀀스 길이 그리고 간단하게 PHI 토큰인지 아닌지를 분류하는 모델을 학습 

-> Figure 1을 보면 확인 가능 

 PHI 토큰 {Doctor, Did, Not, Proposition, Insulin, For, Mins}은 0으로 매핑되고 PHI 토큰 {Matthew, Edelson}은 1로 매핑



생각보다 내용은 간단하다 .



# 4. PRELIMINARY RESULT

### Implementation

연구에서 Precision 모다는 Recall에 중점을 둠 (모든 개인정보를 마스킹하기 위해서 인듯)

학습 파라미터는 생략...

### Experimental Result.

Precision은 기존 sota보다 낮고 Recall은 기존 sota보다 높다고 한다. ...

=> 그럼 그냥 기존 모델 loss만 변경해도 될거같은데.. 무슨 의미가 있을까?

![t1](\De-identification_of_Unstructured_Clinical_Texts_from_Sequence_to_Sequence_Perspective\t1.PNG)

심지어 3가지 데이터셋 중 한가지 데이터 셋에서만 sota를 찍고 다른 2가지 데이터셋에서는 정화도가 밀린듯 하다 



# 5. FUTURE WORK

### Experiment on MIMIC-II and III

아직 해당데이터에 대해서는 실험을 안했다고함 ??? ? ??? 

### Transfer Learning

비식별화를 이용한 응용 방법을 탐구 하겠다~

### SemiSupervised Learning and Domain Adaptation

설명 생략

# 6. CONCLUSION

 PHI 토큰이 있는 비정형 임상 텍스트를 PHI 토큰이 없는 살균 임상 텍스트로 변환하도록 인코더-디코더 아키텍처를 설계




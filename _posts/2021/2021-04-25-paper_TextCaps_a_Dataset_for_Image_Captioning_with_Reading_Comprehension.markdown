---
layout: post
title: "paper : TextCaps: a Dataset for Image Captioning with Reading Comprehension"
date: 2021-04-29 19:20:23 +0900
category: paper
---

# TextCaps: a Dataset for Image Captioning with Reading Comprehension



- 논문 정보 

게재 일 : 2020년 8원 4일

URL : https://arxiv.org/pdf/2003.12462.pdf

기관 : FaceBook AI Research 



## 1. Introduction

이미지 캡셔닝은 물체를 인식(Object Detection)하는 것뿐만 아니라 관련 택스트를 읽고(OCR) 시각적 장면을 맥락에서 이해하는 것이 중요하다.

![example_image_1](\img\textcaps_a_dataset_for_image_cpationing_with_reading_comprehension\example_image_1.PNG)

위 그림의 예시의 a에서 object detection의 경우 빨간 볼안에 검은 박스가 있는것을 알고 있으나 ocr인 MORNING CRESCENT가 적혀있는것을 알아야 하고 C그림에서도 의미적인 해석을 위해 악세사리의 길이를 알아야한다 

그리고 그림 b의 예시에서 OCR을 전부 사용하는것이라 어떤것을 사용해야할지를 알아야 하며 OCR의 오류요소에 대해서도 판별하여 사용할 수 있어야 한다.

-> 시각 장애인들의 이미지에 대한 질문의 21%가 이미지에 포함된 텍스트와 관련이 있기 때문에 OCR이 중요한 요소를 차지 



- 이미지 기계 번역은 다음 기술들을 포함함

> 1. 서로 다른 OCR 토큰과 OCR 토큰 관의 관계를 결정해야 하며 문장에서 OCR 토큰을 언급해야 하는지, 그리고 OCR 토큰을 함께 결합해야 하는지를 결정
> 2. Switching multiple times
>
> 모델의 vocab와 OCR토큰의 단어 사이에서 캡션 생선 중에 여러 번 변환
>
> -> 위 그림의 b1 처럼 OCR 토큰과 모델의 vocab사이의 변환 작업 
>
> 3. Paraphrasing and inference
>
> 이해를 돕기 위한 의역과 출력 텍스트 의 의미를 잘 generate 하는 것
>
> 4. zero-shot
>
> 학번도 학습하지 않은 OCR토큰들을 예측 하는것

위와 같은 기술들을 포함하여 이미지 기계 번역을 하기 위에서는 데이터셋이 중요하다.

- 데이터 셋 과 task 설명 

> - COCO Captioning dataset 참조 
>
> 2.7% 의 OCR token을 언급한 이미지 데이터 -> 최소 350개의 OCR 토큰(vocab)
>
> 해당 데이터에서 일반적으로 자주 쓰이는 토큰(정지, 남자 등)은 이미 존재
>
> - TextCaps
>
> image captioning with reading comprehension 테스크를 수행하기 위해 해당 논문에서 수집한 데이터
>
> 28,408데이터에 대해 142,040개의 caption을 포함하고 있다.
>
> - sota 모델을 통한 데이터 검증 및 베이스라인
>
> TextVQA, M4C, TextCaps 의 모델로 테스트를 해보고 좋은 점수가 나왔다고함 
>
> - human evaluataion
>
> 해당 task에서 sota 모델과 사람의 정확도의 차를 극대화 시킬 수 있음을 보여줌??



## 2. Related work

- Image Captioning

> Flickr30k 와 COCO Captions 데이터셋을 사용 (상당히 데이터 셋이 많음)
>
> Flickr30k 데이터 셋은 164,062개의 이미지에서 995,684 캡션 데이터가 있음 
>
> 논문에서 제공하는 데이터 셋은 image와 sentence 쌍으로 연결되어 있음.

- Visual Character Recognition (OCR)

> OCR 은 일반적으로 두 가지 스텝으 진행된다 
>
> 1. detection
>
> 이미지에서 텍스트의 위치를 찾아냄
>
> 2. extraction
>
> 찾아낸 텍스트 위치 박스에서 문자열을 추출
>
> OCR은  image captioning with reading comprehension의 하위 테스크중 하나로 볼 수 있다.
>
> -> OCR 모델을 통해 추출된 토큰들의 의미를 인해하는것이 중요하다.

- Visual Question Answering with Text Reading Ability

> Visual Question Answering에서 3가지 데이터 셋이 있음 
>
> - TextVQA
>
> 28,408개의 이미지로 구성되어 있으며 Open Image v3 dataset 카테고리 
>
> 45,336의 질문과 각 질문에 대해 10개의 답변으로 구성되어 있다.
>
> - Scene Text VQA (ST-VQA)
>
> 23,083개의 이미지에 31,791 개의 질문과 각 질문당 1개 씩의 답변셋이 존재 
>
> crowd-sourcing으로 구축된 데이터
>
> - OCR-VQA
>
> 207,572 이미지 (책과 이미지 데이터) 



## 3. TextCaps Dataset

해당 논문에서는 image captioning with reading comprehension를 위한 데이터를 가공

데이터셋은 무료 공개

1. Dataset collection

> Open Images v3 dataset을 기반으로 가공
>
> 사람이 직접 가공했으며??  가공한 과정은 두 가지 스텝으로 진행됨
>
> 1. Annotators
>
> 이미지를 받고 문장단위로 텍스트를 읽도록 요구
>
> 2. Evaluators
>
> 1번 스텝에서 읽은 문장이 사진을 잘 표현하고 있는지 yes/no를 투표를 진행
>
> 해당 투표를 통해 이미지당 5개의 텍스트를 추출



2. Dataset analysis

> 가공한 데이터셋의 퀄리티를 확인하기 위한 방법
>
> - Qualitative observations
>
> annotator에게 텍스트를 읽고 테깅을 요청했지만 텍스트를 사용하게 강제하지는 않음.
>
> 실제 텍스트에서 20%정도는 사진에 있는 텍스트를 복사하는게 아니라 추론을 통해서 사용되고 있음을 보임 
>
> - Dataset statistics
>
> COCO, SBU, Conceptual Cations  데이터 셋과 VQA 데이터 셋인 TextVQA, ST-VQA, OCR-VQA 데이터 셋을 비교
>
> > ![data_set](\img\textcaps_a_dataset_for_image_cpationing_with_reading_comprehension\data_set.PNG)
> >
> > - 평균 답변 길이
> >
> > 1.53 - TextVQA
> >
> > 1.51 - ST-VQA
> >
> > 3.31 - OCR-VQA
> >
> > 답변이 대체로 응답식이라 yes, two, coca coal 등 단답형이 있어 대체로 짧은 편
> >
> > ![data_set_2](\img\textcaps_a_dataset_for_image_cpationing_with_reading_comprehension\data_set_2.PNG)
> >
> > 그러나 coco dataset 같은경우 ocr 토큰에 대한 정보가 없는경우가 많음



## 4. Benchmark Evaluation



1. Baselines

![base_line_model](\img\textcaps_a_dataset_for_image_cpationing_with_reading_comprehension\base_line_model.PNG)

> 위 모델은 image object detection한 정보와 ocr 토큰의 위치값을 Transformer 의 입력으로 받아 text를 출력하는 방식 -> 해당 논문 정리할 필요 있어보임 논문 명 - **M4C-Captioner architecture**

2. Experimental setup

AoANet 을 베이스 라인 모델로 시작 -  TextVQA task 

caption generation 을 할때 <unk> 토큰을 제거함 

BLUE, MEMetrixs, ROUGE_L, SPICE, CIDEr  metrics 를 사욯하는데 해당 내용은 따로 정리 필요 

-> 검색해도 잘 안나오는 메트릭스도 있음 ㅠ

- 각 테스크 별 base-line

![base_line](\img\textcaps_a_dataset_for_image_cpationing_with_reading_comprehension\base_line.PNG)

> TextCaps (논문에서 제공한 데이터셋) 을 평가한 base-line - M4C-Captioner
>
> OCR입력에 대해 CIDEr이 높은 점수를 보이고 있음 



![base_line_2](./\img\textcaps_a_dataset_for_image_cpationing_with_reading_comprehension\base_line_2.PNG)

> 200개의 사진을 랜덤 샘플링 한 경우 정확도를 평가 (퀄리티 평균)
>
> 아직은 사람이 더 좋은 걸 알 수 있음 

## 4~5 Results and Conclusion

COCO dataset은 CIDEr 스코어가 더 낮게나오는것을 확인할 수 있음

-> 도메인이 바껴서 그렇다고판단 (학습은 TextCaps로 하기 때문)

TextCaps에서 제공하는 데이터는 Test set의 데이터도 많음으로 평가하기 좋음 (내용들이 쭉 자랑)



Image captioning with reading comprehension 첼린지는 사진에서 텍스트를 읽고 사진의 문맥을 같이 이해하는것이 매우 중요하다. 

그래서 ocr 모델과 사진 인식모델의 결합이 중요한 역할을 한다.

이를 효율적으로 하기위해 ocr 토큰의 라벨과 Image captioning with reading comprehension라벨을 독립적을 제공 

현제 Image captioning with reading comprehension sota 모델들은 COCO데이터 위주로 되어 있으로 이미지에서 텍스트를 읽고 설명해야하는 OCR문제를 잘 해결하지 못한다. 이를 해당 논문에서 제공한 데이터를 통해 해결해라!! 




















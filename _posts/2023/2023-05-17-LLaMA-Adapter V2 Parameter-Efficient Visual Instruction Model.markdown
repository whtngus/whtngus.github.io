---
layout: post
title: "LLaMA-Adapter V2: Parameter-Efficient Visual Instruction Model"
date: 2023-06-13 00:05:23 +0900
category: paper
---

# LLaMA-Adapter V2: Parameter-Efficient Visual Instruction Model

2023년 4월 28일

url : https://arxiv.org/abs/2304.15010

code url : https://github.com/ZrrSkywalker/LLaMA-Adapter

상하이 대학교



# Abstract

 효율적인 파라미터 크기의 모델인 LLaMA-Adapter V2를 제안함 

llama 모델의 능력을 분산함 ?

추가로 구조화된 이미지 텍스트 페어 데이터에 최적화 함 

추가적으로 captioning ocr기능을 제공

모델 크기가 14M여서 매우 작은편 

#  1. Introduction

대규모 생성 모델이 많이 나오고 있고,  예시로 Stanford Alpaca는 Instruct GPT 모델에서 생성된 예제를 이용해 파인튜닝함

frozen 된 LLaMA 모델을 효과적으로 fine-tuning해 가벼운 멀티모달 모델을 만듦

최근 gpt4를 경량화 하기위해 LLaMA-Adapter와 같은 MiniGPT-4나 LLaVA등의 연구가 계속 나오고 있음 

-> 나중에 찾아보자

light weight 모델을 학습시키기 위해서는 학습 데이터가 필요함 LLaMA-Adapter는 COCO Caption 데이터를 이용해 학습함 

해당 연구에서는 최근 사용하는 대규모의 multi-modal 데이터셋을 사용하지 않음

그러면서 좋은 성능을 유지한다고 함 



그리고 시각적인 feature들이 prompte를 지배하는 경향이 있음 (텍스트를 무시하는듯)

LLaMAAdapter V2 모델은 처음 k 레이어를 사용해 다양한 visual prompt를 제공 

-> 이 방법을 통해 joint training with disjoint parameters  방법을 제안

그리고 기존 모델의 0.04% 파라미터만 사용하고 성능을 보장함

![f_1](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\f_1.PNG)

논문의 컨트리뷰션

- Stronger Language Instruction Model

효과적인 파라미터 튜닝과 좋은 퀄리티의 데이터로 학습 

긜고 multi-turn dialog 등 강력한 모델을 제공

- Balanced Visual Instruction Tuning

이미지와 텍스트에 대한 inference모델을 제안 

- •Integration of Expert Systems.

end-to-end 모델로 여러 expert 모델 이 작동하는걸 하나의 모델에서 해줌 



#  2. Related Work

- Instruction-following Language Models

Transformer기반의 모델로 대규모 데이터를 학습한 Large Language Model들이 좋은 성능을 보여주고 있음 

최근 InstructGPT와 FLAN 등 구조화된 fine-tuning 방법을 제안함

Alpaca나 gpt4 등 좋은 모델들이 많이 나왔지만 언제나 memory 이슈가 발생 (너무 많은 메모리를 차지)

- Visual Instruction Models 


전통적인 image caption 과 vqa 모델은 gpt-4가 나온 이후 성능이나 효울성 면에서 비교적 

그리고 기존 내용들은 명시적인 설명들 뿐임

- Parameter-efficient Fine-tuning 

pre-training 후에 fine-tuning 을 하는 방식은 매우 효과적이여서 기존에 자주 사용됨

그러나, 최근들어 모델이 너무 켜저셔 fine-tuning하기에도 부담스러운 수준이 되어가고 있음 

이를 해결하기 위해 parameterefficient fine-tuning (PEFT) 연구도 진행중이고 많은 효과를 보임

LLaMA-Adapter V2도 이런 방식을 사용 그리고 기존 모델의 0.04%의 파라미터만 사용

- Integration of Expert Systems 

여러 exprot model들이 있지만 하나의 모델에서 전부다 하는 경우가 거의 없음

최근 gpt 모델이 나오면서 여러 전문가 모델을 한번에 해결하는 모델들이 많이 나오고 있음

HuggingGPT, Visual ChatGPT, Chameleon, MMReACT, ViperGPT 등 ..

#  3. A Revisit of LLaMA-Adapter

- Zero-initialized Attention

LLaMA-Adapter에선 효율적인 fine-tuning 방법을 제안함 

LLaMA model을 프리징 시킨 후  1.2M parameters크기의 가벼운 모델을 생성함 

그후에 다시 llama 모델과 결합

- Simple Multi-modal Variant

visaul encoder를 pretraining된 CLIP모델을 사용해 projection layer만 학습

- Open-ended Multi-modal Reasoning

Vision-Language를 위해 COCO Caption 데이터도 있지만

adaptation prompts 방식을 상용

# LLaMA-Adapter V2

4가지 기법이 사용됨

## 4.1. Bias Tuning of Linear Layers

zero-initialized attention mechanism을 사용 

LLaMA model을 frozen 시킨 후 knowledge distllation 

LLM 내부의 파라미터 변경 없이 프롬프트 및 계수가 제한됨 

  -> 내부 파라미터의 변경 없는 fine-tunig이여서 performence가 제약사항이 있음

![f1](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\f1.PNG)

LLaMA 모델에서 normalization layer만 unfreeze 시킴 그리고 바이어스 와 레이어 추가 

-> 바이어스와 레이어 추가 위의 식 1 참고 (zero initialized)  1과 0으로 초기화 시켜야 안정적이라고 함 

기존에 영향을 안주는 상태에서 시작해야 하는듯 (대규모 모델에서 fine-tuning이라서)



-> 전체 모델 크기가 0.04%인줄 알았는데 그래서 추가된 레이어의 크기가 전체모델의 0.04(~5M) 라고 함

- Discussion

bias tuning strategy은 BitFit 방식과 유사함 

(BitFit and SSF 은 80M 파라미터로 크기 규모) 하지만  gpt-4가 아닌 지금 사용 모델은 모델의 크기가 더 커짐 

반면  bias tuning은 65B 에서  7B 로 압축

## 4.2. Joint Training with Disjoint Parameters

![f_2](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\f_2.PNG)

LLaMA-AdapterV2의 목표는 긴 질문에 대한 답변과 멀티모달 이해이다.

이를 위해 joint training paradgm을 제안

위의 Figure 2 cjfja LLaMA-AdapterV2는 자연어만 혹은 자연어-텍스트 테스크를 포함하여 처리함

500K image-text pairs and 50K instruction data를 사용 

두 테스클 학습하기 위해 투 테스크를 분리해 optimization 함 -> 인퍼런스 이슈를 자동으로 해결해줌

visual projection layer랑 zeo-initialized된 atteion 레이어를 캡션 데이터로 학습함

- Discussion

![t_1](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\t_1.PNG)

join training paradigm을 이용함으로 써 대규모의 학습 모델은 필요가 없어지고 image-text pairs and instruction-following data 만을 필요로함 -> Table 1 참조

![t_2](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\t_2.PNG)

Table 2는 langauge only  만 이용한 경우 

더 디에틸한 설명과 구조화된 설명을 생성

## 4.3. Early Fusion of Visual Knowledge

![f_3](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\f_3.PNG)

텍스트와 이미지의 학습을 잘되게 하기 위해서 direct interaction을 input visual prompt, adaptation prompts결합함

projection은 마지막 Layer

## 4.4. Integration with Experts

![f_4](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\f_4.PNG)

최근 visual instruction models인 miniGPT4 와 LLaVA 등은 거대한 사이즈의 이미지-텍스트 데이터로 학습해야 함 -> LLaMA-Adapter V2는 작은 규모의 데이터로 fine-tuning가능하다고 함 

이미지에 대한 이해도가 부족하기 때문에(가끔 정확하지 않은 답변을 함) 이를 향상시킬 방법이 필요

image-text data를 더 수집하기 보다는 integrating expert systems 방법을 사용

질문 답변 방식으로 Captioning, detection, OCR 능력을향상시킴 (각각을 dexport 라고 부름)

COCO Caption 데이터셋을 사용 

#  5. Experiments

## 5.1 Experimental Setups

- Training Data.

Table 1에서 학습한 GPT4-LLM  657K caption data 데이터는 COCO Caption

학습 시 visual instruction data는 사용하지 않음

MiniGPT-4 and LLaVA는 80K의 ShareGPT에서 수집된 chatbot 데이터 사용  

- Implementation Details.

LLaMA-7B model with 32 Transformer layers 모델을 사용 

마지막 31 layer를 사용하고 레이어 하나를 붙임 

prompt 길이는 20으로 설정

normalization layer, linear layer bias, scale 레이어는 학습 대상 나머지는 프리징 시킴

## 5.2. Stronger Language Instruction Model

![f_5](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\f_5.PNG)

 7B 모델로 학습해도 QA에서 문맥을 잘 이해하지 못하는 상황이 발생 

-> large 모델인 65B 모델로 확장하며 더 잘 답변하게 됨 

Figure 5를 보면 GPT4보다 LLaMA-Adapter V2가 더 잘하는걸 볼 수 있음

## 5.3. Visual Instruction Model

- Image Captioning

![t_3](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\t_3.PNG)

coco caption 으로 fine tuning 후 스코어 결과 

스코어가 좋지 않지만 논문에서는 많은 데이터로 학습하지 않았는데도 이정도로 결과가 나왔다고 함 

![f_6](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\f_6.PNG)

- Visual Understanding

![f_7](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\f_7.PNG)

Figure 6, 7 의 예시를 통해 Image Caption, VQA 성능이 좋다는걸 보여줌 














# 참고 지식

- InstructGPT

참고 : https://littlefoxdiary.tistory.com/101

대규모 언어모델이 나오면서  prompt engineering의중요성이 대두되고 있음

즉, 언어 AI는 이제 fine-tuning이 아니라 모델에게 질문을 통해 사용하는 방식으로 바뀌고 있음 

프롬프트 엔지니어링을 잘해야 더 좋은 결과를 얻을 수 있고 이는 많은 작업이 필요하기에 이를 극복하고자 InstructGPT가 발표됨 (지금은 성능이 좋아서 기본값 모델로 사용 175B InstructGPT -> text-davinci-001 모델)



GPT-3 모델을 InstructGPT 모델로 만들기 위해 OpenAI는 다음의 세 가지 단계를 도입 (딥마인드에서 개발한  **RLHF** (reinforcement learning with human feedback)을 적용)

![instructGPT](\img\2023\LLaMA-Adapter V2 Parameter-Efficient Visual Instruction Model\instructGPT.PNG)



1. 지도학습을 통해 SFT 확보 

이를 위해 지시 프롬프트와 그에 대한 결과물로 이루어진 데이터셋 (demonstration dataset)을 정의해야함

-> 이 결과로 SFT (supervised fine-tuning) 모델을 얻음

2. Reward Model 확보

33k로 이루어진 Comparision dataset을 통해 Reward Model을 학습 

사람의 feedback을 모사하는 policy 모델을 생성

( comparison dataset은 프롬프트와 그에 따른 결과물들 (4-9개), 그리고 그 결과에 대한 선호도 순위로 구성됨)

3. 강화학습을 사용해 policy를 최적화 해 InstructGPT 모델을 얻음

> 1. InstructGPT는 프롬프트를 보고, 그에 대한 결과 (completion)를 추론
> 2. 이 결과물을 Reward Model이 평가하여 reward(보상)를 계산
> 3. 보상 값이 InstructGPT에게 주어지고, 모델은 정책을 업데이트하여 사람이 원하는 아웃풋에 더 가까운 결과를 내게 됨

- MiniGPT-4

BLIP-2와 Vicuna를 연결해서 사용해 GPT4와 유사한 성능을 제공 

4개의 A100으로 10시간 동안  Vincuna가 이미지를 이해하는 학습

chatgpt를활용해 같이 학습함 

fine-tuning 단계에서는 대화형 템플릿으로 학습함 A100 한대로 7분

- parameterefficient fine-tuning (PEFT) 

LLM의 대부분의 파라미터를 freezing 시키고 일부 파라미터만 fine-tuning 하는기법
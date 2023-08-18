---
layout: post
title: "MiniGPT-4:Enhancing Vision-Language Understanding with Advanced Large Language Models"
date: 2023-08-20 02:05:23 +0900
category: paper
---

# GMiniGPT-4:Enhancing Vision-Language Understanding with Advanced Large Language Models

2023년  4월 20일 게재



url : https://arxiv.org/abs/2304.10592

code url : https://github.com/Vision-CAIR/MiniGPT-4



# Abstract

최근 GPT-4로 인해 multi-modal 능력이 비상적으로 상승함 

논문에서 제시하는 frozen 된 visual encoder LLM인 Vicuna 모델을 사용한 MiniGPT-4 모델을 통해 멀티모달 테스크의 높은 성능 향상을 기대람 

MiniGPT-4 는 GPT-4와  이미지에 대한 설명 등 상당히 유사함 

해당 연구에서 pretraining 과정에서 사용하는 image-text 셋의텍 텍스트 문장이 일관적이지 않다는것을 발견함 

이를 해결하기 위해 두 번째 스텝에서 잘 정렬된 image-text셋을 추출하여 다시 학습함 ( 5M 데이터)

제시하는 모델은 매우 효율적이라고 함 



# 1 Introduction

최근 LLM이 연구되고 있고, 복잡한 zero-shot 방법들의 성능을 올리고 있음 

특히 GPT-4의 large-scale 멀티모델 모델은 최근 매우 큰 성능 향상을 보이고 있음 (왜 좋은 성능을 보이지는지는 미스터리라고함)

-> 이유는 모르지만  GPT-3 few-shot prompting setup을 통해 LLM 모델이 여러 응용테스크에 좋은 능력을 보이는것을 증명함 

MiniGPT-4 도 다른 GPT모델과 비슷하게 Vision embedding model 은 frozen 시키고 사용

모델의 구성은 사전학습된 BLIP-2(ViT-G/14), Q-Former로 구성됨 

- Pretraining

256 batch size로 20K step 만큼 학습함

A100GPU 4개를 사용 

학습 데이터셋으로 LAION, Conceptual Caption, SBU을 사용 

-> COCO 데이터셋은 안썻네?

- fine-tuning

pretraining에서 사용한 데이터셋에서 3,500 개의 퀄리티가 높은 image-text 데이터셋을 추출해 fine-tuning 함



# 2 Related Works

![f_1](F:\code\whtngus.github.io\img\2023\MiniGPT-4 Enhancing_Vision-Language_Understanding_with_Advanced_Large_Language_Models\f_1.PNG)

### Large language models

BERT, GPT-2, T5등의 모델에서 최근 GPT-3 모델이 나오며 LLM 모델이 개발되기 시작함 

Megatron-Turing NLG, Chinchilla, PaLM, OPT, BLOOM, LLaMA 등의 모델들이 연구됨 

### Leveraging Pre-trained LLMs in Vision-Language Tasks

VLM 에서 autoregressive langage model decoder 를 사용하는건 cross-modal transfer에 이점으로 작용함 

VisualGPT, Pioneering, Frozen모델은 사전학습된 Language model의 decoder를 사용함

Flamingo는 사전학습된 Vision encoder와 언어모델의 gated cross-attention을 통해 image-text pair 데이터셋을 학습 

 Q-Former 를 통해 효과적으로 이미지를 임베딩함 

# 3 Method

위의 그림1 참조 

## 3.1 First pretraining stage

첫 사전 학습시에는 label 되어있는 데이터들을 이용해 학습함

Conceptual Caption, SBU, LAION 데이터셋을 이용해 256batch 사이즈로 20,000 스텝 학습 (5M의 데이터)

A100 (80GB) 4대로 학습시 10시간 걸렸다고함 

-> 3090TI로 학습 시 학습 시간이 10배정도 더 들걸로 보임 

#### Issues of the first pretraining stage

대용량의 데이터로 학습 해 괜찮은 답변을 하는것을 보임 

그러나 반복적인 단어와 문장, 파편화된 문장, 엉뚱한 문장을 생성하기도 함 

-> 이를 해결하기 위해 다시 학습

### 3.2 Curating a high-quality alignment dataset for vision-language domain.

괜찮은 데이터를 추출해 fine-tuning 

#### Initial aligned image-text generation

```
###Human: <Img><ImageFeature></Img> Describe this image in detail. Give as many details as
possible. Say everything you see. ###Assistant:
```

위와 같이 프롬프트를 구성 

ImageFeature는 이미지 임베딩 벡터를 linear projection 함 

생성한 답변이 80토큰을 초과하지 않는경우 Human: Continue ###Assistant: 를 통해 추가 답변을 요구하도록 학습 

5000개의 이미지를 Conceptual Caption 데이터셋에서 랜덤으로 추출해 각이미지를 설명하도록 함

### Data post-processing

이미지에 대한 설명을 생성할때 단어 또는 문장을 반복하는 문제가 발생함 

이를 해결하기 위해 ChatGPT의 정교한 설명셋을 활용

```
Fix the error in the given paragraph. Remove any repeating sentences, meaningless characters, not English sentences, and so on. Remove unnecessary repetition. Rewrite any incomplete sentences.
Return directly the results without explanation. Return directly the input paragraph if it is already correct without explanation.
```

위의 문장을 통해 한번더 체크하도록 확인

### 3.3 Second-stage finetunin

마지막으러 first stage에서 학습한 모델을 빠르게 다시 학습함 

```
###Human: <Img><ImageFeature></Img> <Instruction> ###Assistant:
```

Instruction은 Describe this image in detail 혹은 Could you describe the contents of this image for me 중 랜덤으로 선택

A100 GPU로 7분 학습

# 4 Demonstrations

figure로 결과를 보여줌 

잘하는걸로 보임 .. 실행해보고 확인해보자

![f_2](F:\code\whtngus.github.io\img\2023\MiniGPT-4 Enhancing_Vision-Language_Understanding_with_Advanced_Large_Language_Models\f_2.PNG)

# 5 Limitations

아직 몇가지 문제를 포함하고있음 

#### Language hallucination

LLM 을 가져와 쓰기 때문에 일반적인 LLM의 문제를 그대로 가지고 있음

#### Inadequate perception capacities

이미지에 있는 세부적인 텍스트나 특별한 장소에 대해서 이해하지 못함 



예상 이유

1. 학습데이터의 부족으로 보임
2. Q-former를 frozen 시켰는데  image Embedding 모델도 학습 시켜야함 (이미지에서 특별한 feature를 추출하지 못하기 때문에) 
3. 마지막 Image embedding projection layer를 보강할 필요가 보임 





# 참고 지식

1. Vicuna

>  Meta의 LLaMA와 Stanford의 Alpaca에서 영감을 받아 개발한 오픈소스 챗봇 
>
> ShardGPT로 수집된 사용자들 대화로 LLaMA를 fine-tuning한 모델 
>
> - 특징
>
> 메모리 최적화 (긴 텍스트를 이용하도록 max seq 를 alpca의 512에서 2048로 확장)
>
> -> 이 과정에서 gradient checkpoint와 flash attention을 화용해 메모리 부족을 해결 
>
> Multi-round 대화 (Multi-round대화를 위해 loss 를 조정하고 챗봇의 출력에만 fine-tuning loss를 계산함)
>
> Spot 인스턴스를 통한 비용절감 (7B는 140\$   13B는 300\$ 로 절감함)
>
> - 특이한 평가 방법
>
> GPT-4를 이용해 평가함 

-  gradient checkpoint

GPU 사용 시 사용 가능한 메모리를 늘리기 위한 방법 중 하나

메모리 사용량을 줄이는 대신 연산시간을 늘림 

gradient 역전파시 일반적으로는 모델의 모든 레이어값이 메모리에 올라와 있어야함 

이 단계에서 연산속도를 고려하지 않으면 모든 레이어가중치를 저장할 필요가 없음 

-> 메모리 사용양은 확실히 줄어들지만 순전파를 2번씩 해야함으로 N^2 의 복잡도가 발생하게됨 

(각 레이어마다 순전파를 한번씩해 계산)

모든 gradient를 순전파로 계산하면 시간이 너무 오래들기 때문에 절충안으로 gradient checkpointing을 사용함 

checkpoint layer지점을 지정하고  그 노드의 gradient를 저장 후 사용  루트n 간격으로 checkpoint를 설정하면 O(sqrt(n)) 의 시간복잡도를 기록했다고 함 ???

- FLASHATTENTION v2

>  어텐션 메커니즘은 높은 정확도를 보이나 계산량이 매우 큼 이에 google research brain team에서 해결하기 위해 제안 (입력 토큰수를 늘릴수록 모델 크기가 제곱으로 증가해야 해서 )
>
> Flash_Attention v1은 배치 크기와 헤드 수를 병렬화함 -> 즉 seq길이를 차원에 추가 
>
> Flash_Attention v2에서는 K와 V를 엑세스 할 수 있게 유도하면서 Q를 4개로 분할해 더 효율적으로 만듦 
>
> 이를통해 일반적인 Attention 모다 5~9배 빠른 챗봇 모델을 만들었다고 함









# 참고

1. Vincuna

https://moon-walker.medium.com/%EB%A6%AC%EB%B7%B0-llama%EA%B8%B0%EB%B0%98-vicuna%EC%99%80-vicuna%EA%B8%B0%EB%B0%98-multi-modal-%EB%AA%A8%EB%8D%B8-minigpt-4-31838c4193c5

2. gradient checkpoint

https://only-wanna.tistory.com/entry/Gradient-checkpointing%EC%9D%B4%EB%9E%80

3. FLASHATTENTION v2

https://dajeblog.co.kr/flashattention-v2-%EB%85%BC%EB%AC%B8-%EB%A6%AC%EB%B7%B0-%EA%B8%B0%EC%A1%B4-attention%EB%B3%B4%EB%8B%A4-59%EB%B0%B0-%EB%B9%A0%EB%A5%B8-%EB%8C%80%ED%99%94%EC%B1%97%EB%B4%87-%EB%AA%A8%EB%8D%B8/
























---
layout: post
title: "paper : Towards Accurate Scene Text Recognition with Semantic Reasoning Networks"
date: 2021-05-25 19:20:23 +0900
category: paper
---

# 논문 정보 

논문 명 : Towards Accurate Scene Text Recognition with Semantic Reasoning Networks

2020년 3월 27일 게재

Baidu Inc

url : https://arxiv.org/abs/2003.12294

git url : https://github.com/chenjun2hao/SRN.pytorch



# 1. Abstract and Introduction

OCR의 장면 텍스트인식은 몇년간 많은 향상을 이루었지만, 텍스트 인식을 지원하기 위한 의미적인 해석을 하는 연구는 RNN과 유사한 구조의 탐색만 사용되어 왔다. 

-> 즉, 트랜스포머 시대에? RNN말고 트랜스포머를 써보자 라고 해석 가능

위의 한계를 안화하기 위해  

1. 장변 텍스트 인식인 semantic reasoning network (SRN)
2. 사진의 문맥 이해를 위한 global semantic reasoning module (GSRM) 

위 두 가지 학습 모델로  semantic reasoning network (SRN) 프레임워크를  제안하고, 7가지 벤치마크 테스크에서 state-of-the-art를 달성함 

![example_image](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\example_image.PNG)

OCR에서도 텍스트는 많은 의미를 가지고 있으며 장면 텍스트 인식은 비전 기반 응용프로그램에서 중요한 단계이다. 위의 예시 사진에서 그냥 단어만을 인식한다면 "HOUSE"의 "S"는 글자를 알아볼 수 없어 예측이 불가능하다. 하지만 의미적인 컨텍스트를 이해한다면 "S"를 유추할 수 있다.

또한 이러한 문맥 정보를 기존 RNN 방식으로 해결한다면 런타임 시간, 롱 텍스트 디펜던시, 그리고 RNN구조상 한번의 잘못된 디코딩으로 연속된 잘못된 정보를 축혀갛는 문제들이 발생하게 된다.

![rnn_transformer](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\rnn_transformer.PNG)

위 그림은 트랜스포머는 연속으로 잘못된 정보를 전달하지 않는다.  정도로 이해하고 넘어가자

-> 해당 논문에서는 GSRM, PVAM등 트랜스포머를 사용 하는 방식을 적용하여 sota를 찍음

# 2. Related Work

해당 논문에서는 OCR의 semantic context-free 와 semantic context-aware로 나누어서 정리를 함.

-  semantic context-free

> 의미론적인 정보를 명시적으로 사용하지 않고 장면 텍스트 인식을 순수하게 분류로만 사용
>
> 예시로 CRNN(CNN + RNN 과 CTC decoder, ACE 사용), FCN을 사용해 각 위치의 문자범주를 필셀단위로 분류
>
> 해당 연구는 불규칙한 텍스트에 대해 효과적인 특징을 추출하는 방법에 초점을 맞춰서 연구가 되고 있음
>
> -> 노이즈 처리(원근, 왜곡,  분포 곡면성 등)

- Context modeling structures

> 특정 시간범위 공간범위의 정보를 캡처하도록 설계됨
>
> 기존에는 ByteNet, ConvS2S등 CNN을 인코더로 사용  -> 글로벌 관계를 유추하기에는 어려움이 있음 (입력 필드의 한계점)
>
> -> 트랜스포머가 이러한 문제에 대해 효과적임을 많은 연구논문에서 검증함  *(SRN 논문에서 트랜스포머를 채용하는 이유)*



# 3. Approach

![SRN](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\SRN.PNG)

4가지 부분으로 구성된 모델

백본 네트워크에서 2D V를 추출하고, PVAM은 각 기능에 해당하는 G를 생성 해서 텍스트의 오류와 정렬된 시각적 정보를 캡처

N개의 병렬 1-D 를 GSRM에공급하여 의미정보인 S를 얻고 VSFD에 의해 융합되어 N자를 예측 

N의 남은 부분 패딩은 'EOS' 토큰을 사용



#### 3.1 Backbone Network

역시 이미지 처리이기떄문에 backbone 네트워크를 사용(바로 transformer로 넘겨주는줄 알았는데 backbone은 필수 요소인듯)

ResNet50의 사이즈의 1/8의 입력 이미지 크기이며 채널수는 512이다. 

backbone의 output 인 2-d feature 는 다음 모델의 입력으로 전달된다 

multil-head attention 은 8개 이고 feed-foraward output dimmention은 512 차원이다.

#### 3.2 Parallel Visual Attention Module

 그 다음으로 문자인식(문맥을 고려하지 않은)을 위해 입력정보를 정렬한 (3.1의 output) 결과값을 받아 처리한다.

parallel visual attention (PVA) 모듈을 이용해 처리

![formula_!](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\formula_!.PNG)

처리 방식의 수식은 위와 같다.

transformer의 key-valuer값은  3.1의 output 이다.

Wo, Wv 등 W는 학습 weights이고 Ot는 각각의 문자 들의 순서

f0(backbone network)는 임베딩 함수이다.

 ![formula_2](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\formula_2.PNG)

논문에서 제시하는  parallel visual attention module (PVAM)는 모든 시간적인 단계의 시각적 특징을 정렬해 사용한다

t번째 시간 단계의 정렬된 시각적 특징은 gt를 통해 병럴로 출력한다 

-> 이렇게 출력한 gt의 결과는 위 그림의 Features G처럼 병럴화 되어 다음 단계의 입력값으로 넘어간다.

#### 3.3. Global Semantic Reasoning Module

3.2 에도 트랜스포머 모델을 사용하기 때문에 문맥정보를 충분히 고려하고 있을걸로 생각하지만, 해당 논문에서는 global 한 의미정보를 포함하기 위해 transformer 모델인 global semantic reasoning module (GSRM)을 한번더 사용한다.

특이한 점은 RNN 구조를 사용하지 않고  실제 단어임베딩 e를 사용하지 않고, 근사 인베딩인 e0를 사용한다 

![formula_3](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\formula_3.PNG)

위 식과 같이 순차적으로 y값(ocr)을 추론하게 되며 이렇게 추론하는 이유는 문맥정보를 이해하기 위해서 라고 한다.

근사 임베딩인 e0를 사용함으로서 얻는 이점은 다음과 같다.

1. Ht-1의 숨겨진 상태값을 위의 수식에서 제거할수 있다.

트랜스 포머를 사용하기 때문에 앞뒤를 다 고려할 수 있어서 로 보임

위 수식에서 Ht-1을 제거함으로 써 시간 의존이 사라지고 병렬로 추론이 가능해진다(transformer 특징)

2. 글로벌 의미정보를 포함한다.

역시 transformer 의 특징으로써 어텐션이 이전 시퀀스와 앞의 시퀀스를 모두 입력으로 받기 때문에

![formula_4](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\formula_4.PNG)

e0는 t번째 시간에서 et의 대략적인 임베딩 정보이다. (역시 트랜스 포머이기 때문에 앞뒤의 이전 스텝의 임베딩 정보를 전부 입력으로 받음)

 St = fr(e1 .et-1, et+1.. eN) 의 각 t타임의 의미임베딩을 나타내고  이 식들을 단순화 하면 아래와 같다.

![formula_5](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\formula_5.PNG)

위의 수식구조가 논문에서 제안하는 GSRM 구조이다. 

st 정보와 gt 정보를 동시에 입력받아 결론을 추론하는 구조 

GSRM의 구조를 그림으로 하면 아래와 같다.

![GSRM](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\GSRM.PNG)

모델 3.2의 임베딩 정보를 학습하기 위한 CE Loss와 3.2 모델의 입력을 위한 임베딩을 위해 Argmax 와 embed 를 통해 3.3의 입력값은 e로 전달된다.

- Visual-to-semantic embedding block

![formula_6](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\formula_6.PNG)

위 그림에서 좌측(a)는 e0를 생성하기 위한 블록

PVAM 모델에서 모든 시간(seq)에 따른 임베딩이 되어 있음으로 정렬된 결과에서 argmax와 embedding layer를 통해 가능성 높은 출력 문자를 기반으로 계산하게 된다.

- Semantic reasoning block

![formula_7](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\formula_7.PNG)

마스킹된 0과 함께 여러 transformer 유닛을 통해 전역 컨텍스 정보를 512차원으로 추론한다.

손실 함수는 같은 CE Loss를 사용g해 학습 수렴시간을 다축시킨다.

GSRM의 병력 추론은 텍스트가 긴 경우 기존의 모델보다 더 빨리 실행할 수 있다(긴 텍스트에서 RNN보다 transformer가 빠르다는 이야기) 

위 두개의 Lr, Le 로스를 학습 loss에 활용한다. (아래 loss 더 있음)

#### 3.4 Visual-Semantic Function Decoder

장면 텍스트 인식을 위해 시각적 정렬인 G와 의미 정모 S를 모두 고려하는것이 중요하다.

G와 S는 서로 다른 영역에 속하기 때문에 두 정보를 합치는 작업 또한 중요(가중치가 필요)

VSFD에서 서로 다른 도메인의 기능 균형을 맞추기 위한 가중치를 추가로 도입

![formula_8](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\formula_8.PNG)

zt는 단순하게 gt 와 st의 가중치 곱을 sigmoid 함수로 씌운것 -> sigmoid를 통해 gt를 얼마나 사용할지에대한 0~1값을 뽑아냄

ft는 재귀적인 방법을 사용하지  않으며 zt를 이용해 gt와 st를 얼마나 사용할지를 고려해서 최종 문자를 예측 

![formula_9](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\formula_9.PNG)

최종적인 loss 함수는 위의 수식으로 3.2 3.3에서 나온 ce loss와 3.4의 Lf 로스이고 여기에서 a(e, r, f)는 각각 1.0, 0.15, 2.0의 가중치이다 

-> 또 weights 를 사용하는 줄 알았는데 고정값을 사용하고 생각보다 문맥가중치를 많이 두지는 않는듯 하다.



# 4. Experiment

#### 4.1 Dataset

6가지 데이터셋을 사용 

- ICDAR 2013 (IC13) contains 1095 testing images. 

- ICDAR 2015 (IC15) is taken with Google Glasses without careful position and focusing. 
-  IIIT 5K-Words (IIIT5k) is collected from the website and comprises of 3000 testing images. 
- Street View Text (SVT) has 647 testing images cropped form Google Street View. 
- Street View Text-Perspective (SVTP)  is also cropped form Google Street View. There are 639 test images in this set and many of them are perspectively distorted. 
- CUTE80 (CUTE) is proposed in for curved text recognition. 288 testing images are cropped from full images by using annotated words.

#### 4.2 Implemenation Details

파라미터 등 내용은 생략

8개의 p40 그래픽 카드로 3 epoch(1e-4, adam optimization, 256 batch size)을 통해 학습

-> 얼마나 걸린지는 안나와있음 . (모델의 크기가 큰 만큼 오래 걸렸을걸로 예상)

#### 4.3 Ablation Study

![result_1](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\result_1.PNG)

base 는 backbone, TU는 fransformer unit, CRO는 character reading order information 

![result_2](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\result_2.PNG)

트랜스포머 유닛을 몇개 사용하냐에 따른 결과 (많으면 일단 좋을줄 알았는데 아닌듯 - 파라미터 조절을 잘 못했나?)

![result_3](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\result_3.PNG)

데이터셋을 확인해 봐야겠지만 IIIT5K 데이터셋에서는 오히려 낮은 성능을 보임 

![result_4](\img\2021\Towards_Accurate_Scene_Text_Recognition_with_Semantic_Reasoning_Networks\result_4.PNG)

위 2개의 그림중 위는 GSRM을 사용한 경우 글로벌한 텍스트를 인식하기 때문에 그림에서 알 수 없는 단어를 유추할 수 있음을 보임(각 이미지에서 위가 SRN 아래가 SRN + GSRM을 사용한 경우) 아래 사진은 맨아래가 라벨 값이고 둘다 틀리는 경우 

-> 문맥 인식은 이해했으나 장면인식이아닌 문서인식의 케이스에서 잘 사용이 될지 의문이 생김 -> 이름 주소등 문맥으로 유츄할수 없는 고유명사가 나온경우 오히려 정확도를 낮출 가능성이 있음



그이후 논문에서 sota 정보와 중국어등 더있지만 생략







# 참고

- FPN(Feature Pyramid Network)

> 1. Featurized Image Pyramid
>
> 각 라벨에서 독립적으로 특징을 추출하여객체를 탐지하는 방법 
>
> 연산량과 시간 관점에서 비효율적, 적용하기 어려운 담점 있음
>
> 2. Single Featur Map
>
> Conv layer를 이용해서 특징을 압축하는 방식
>
> 멀티 스케일을 사용하지 않기 때문에 성능이 떨어지는 단점 발생
>
> 3. Pyramidal Feature Hierarchy
>
> 서로 다른 특징 맵을 이용해 멀티 스케일 특징을 추출하는 방식
>
> 각 레벨에서 독립적으로 특징을 추출하여 객체를 탐지
>
> 4. Feature Pyramid network
>
> Top-down 바잇ㄱ으로 특징울 추출
>
> 각 추출된 결과들인 low-resolution 및 high-resolution 들을 묶는 방식
>
> 

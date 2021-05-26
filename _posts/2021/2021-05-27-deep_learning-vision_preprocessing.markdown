au---
layout: post
title: "vision preprocessing(data augmentation)"
date: 2021-04-26 19:20:23 +0900
category: deep_learning
---



# RandAugment (Cubuk et al. 2020)

간단하게 설명하면 augmnet transform 기술들을 랜덤으로 선택하서 랜덤한 값으로 augmnet transform 을 하나 선택해서 augment를 n회 반복

*거의다 PIL 라이브러리에서 지원함*

### RandAugmnet안에 들어갈 augment 기술들 정리

- shearing

강제로 사진을 찌그러트린다.  

일반적으로 -20 ~ 20도 사이로 랜덤하게 줌

X축 Y축 또한 랜덤으로 선택지중 하나로 추가

- transloate

상하좌우로 몇 픽셀씩 미는것

X축 Y축 또한 랜덤으로 선택지중 하나로 추가

- rotate

0~360도 사이로 랜덤함게 회전

- color

색감을 바꾸는 작업으로 색 이탈(color jittering)방법 이 있음.

RGB에 랜덤 노이즈를 무작위로 더해 주기만 해도 이상한 색감이 됨.

혹은 pca를 통해 찾은 중요 성분들 만큼을 랜덤하게 더해주기도 함(AlexNet)

-> 흑백화 시키기도 함

- posterize

각 색상 채널의 비트 수를 줄임

각 채널에서 유지할 비트수 1~8개를 선택

- solarize

임계 값 이상의 모든 픽셀 값을 반전

default = 128

- contract

이미지 대비를 조정( 이미지의 밝은 부분과 어두운 부분 사이의 차이를 조절, 대비를 늘리면

밝은 부분이 더 밝아지고 어두운 부분은 더 어두워짐)

- sharpness

이미지 선명도를 조정(이미지의 중점을 더 뚜렷하게 또는 부드럽게(흐림))

- brightness

이미지 밝기를 조정(이미지의 흰색 양을 변경)

- autocontrast

색 대조를 높이는 방법(정규화 입력 이미지의 히스토스램을 계싼하고 가장 밝은 픽셀과 어두운 픽셀의 배분율을 제거, 가장 어두은 픽셀이 검은색 0이되고 밝은 픽셀이 0이 되도록 매핑)

- equalize

이미지 히스토그램을 균등화함 이미지에 비선형 매핑을 적용

- invert

좌우 이미지 반전



### 기타 추가 정리

- stretching

사진을 늘린다 1~1.3배

- flipping

상하/좌우 반전

- rescaling

사진 크기를 키우거나 줄이는데 사용 보통 1~1.6배로 사진을 키움

- shifting

랜덤하게 10px씩 상/ 하/ 좌/ 우f 로 움직임 

-> 각 외각쪽이 잘린 사진이 들어감

- RGB 평균을 0으로 만들기







### 정리 및 시도해볼 전처리 리스트 

- BDA(Base Data Augmentation)

> - rotation
> - perspective distortion
> - motion blur
> - Gaussian noise

- AutoAugment (Cubuk et al. 2019)
- RandAugment (Cubuk et al. 2020)  -> best for OCR
- CutOut (DeVries and Taylor 2017)
- RandErasing (Zhong et al. 2020)   -> good for OCR
- HideAndSeek (Singh and Lee 2017)
- GridMask (Chen 2020)
- Mixup (Zhang et al. 2017)
- Cutmix (Yun et al. 2019)
- TIA (Luo et al. 2020)  -> effective auggmentation for OCR 사용시 0.91 스코어 상승

### vision argumentation benchmark 

- PP-OCR 논문 중에서

![benchmark_1](D:\code\whtngus.github.io\img\2021\vision_data_augmentation\benchmark_1.PNG)

-

# 참고 사이트

https://nittaku.tistory.com/272

https://arxiv.org/pdf/2009.09941.pdf
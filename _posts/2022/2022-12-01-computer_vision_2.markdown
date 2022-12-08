---
layout: post
title: "computer_vision_2"
date: 2022-12-08 01:20:23 +0900
category: datascience
---



# Streo Vision

## Epipolar Geometry

동일한 사물 또는 장면에 대한 영상을 서로 다른 두 지점에서 획득했을 때, 영상 A와 영상 B의 매칭쌍들 사이의 기하학적 관계를 다루는 것

![f1](\img\2022\computer_vision\f1.png)

- 용어

> base line :  카메라 중앙에 연결되는 선
>
> Epipole : bsae line과 이미지의 교차점 
>
> Epipolar plane :  base line과 world point가 포함된 평면 - 영상 평면
>
> Epipolar line :  Epipolar planer과 image plane의 교차점 

한 이미지의 한 점이 주어지면, 필수 행렬에 곱하면 두 번째 이미지의 착생선을 알 수 있다.

## Stereo Vision

- Triangulation(삼각 측량)

왼쪽 이미지의 점과 오른쪽 이미지의 점을 일치 시키는것 

진행 순서

> 1. 한 이미지에서 포인트 선택
> 2. 두 번째 영상에서 해당 지점에 대한 에폴라 선을 형성
> 3. 라인을 따라 일치하는 지점 찾기
> 4. 삼각 측량 수행

- stereo rectification(입체 교정)

수평인 경우

> • 카메라의 영상 평면이 서로 평행하고 기준선에 평행합니다.
> • 카메라 중심이 동일한 높이에 있음
> • 초점 거리가 같습니다.
> • 그런 다음 영상의 수평 스캔 라인을 따라 에피폴라 라인이 떨어집니다.

순서

> 1. 오른쪽 카메라를 R로 돌립니다. (카메라 좌표계 방향 지정만 해당)
> 2. 왼쪽 카메라를 회전시켜 에피폴이 무한대가 되도록 합니다.
> 3. 에피폴이 무한대가 되도록 오른쪽 카메라를 회전(수정)합니다.
> 4. scale 조정

- Stereo matching

stereo rectification 이후 응용하는 과정 

수평 이동의 양은 카메라로부터의 거리에 반비례한다.

컨셉

> - 두 눈이 기록한 그림을 융합하고 그들 사이의 차이(또는 불균형)를 활용하면 강한 깊이감을 얻을 수 있다
> - Disparity(불균형) : 눈이 한 물체에 고정되고 다른 물체가 다른 시각으로 나타날 때 발생

순서

> 1.  Rectify images (make epipolar lines horizontal)
> 2.  각각의 픽셀에 대해 수행
>
> 2-1 Find epipolar line
>
> 2-2 Scan line for best match
>
> 2-3 Compute depth from disparity



# Segmentation & Clustering

## Segmentation

이미지를 의미 있는 영역으로 나누는 것으로 물리적 entities에서 객체와 경계를 찾는데 사용

idea 

> 1. 사람이 직접 분할한 것과 비교
> 2. Superpixels : **지각적으로(perceptually) 의미있는 픽셀들을 모아서 그룹화해준 것**
> 3. Multiple segmentations : 동일한 이미지의 여러 분할 생성후 결합
> 4. ​

평가 방법

> 1.  Boundary agreement - 경계선과의 가장 먼 거리
> 2.  영역이 얼마나 정답값과 겹치는지



## Morphological operations

![f2](\img\2022\computer_vision\f2.png)

![f3](\img\2022\computer_vision\f3.png)

## Clustering

- K-means clustering

> 1. k를 입력
> 2. 임의로 중심 k를 선택
> 3. 각 객체를 가장 가까운 중심이 있는 클러스터에 할당
> 4. 각 중심을 할당된 객체의 평균으로 계싼
> 5. 변경되지 않을 때까지 이전 2단계를 반복

특징

> - 장점
>
> 분산의 최소화 하는 군집을 찾음
>
> 간편하고 빠름 
>
> 구현이 용이함
>
> - 단점
>
> k를 직접 선택해야함 
>
> 길쭉한 클러스터에 대해 실패
>
> outlier에 민감함
>
> 느릴 수 있음 (차원가 데이터 수에 따라)

- Mean-Shift method

Mean Shift는 어떤 데이터 분포의 peak 또는 무게중심을 찾는 한 방법으로서, 현재 자신의 주변에서 가장 데이터가 밀집된 방향으로 이동한다. 그러다 보면 언젠가는 분포 중심을 찾을 수 있을 거라는 방법

순서

> 1. 현재 위치에서 반경 r 이내에 들어오는 데이터들을 구한다: (x1,y1), (x2,y2), ..., (xn,yn)
> 2. 이들의 무게중심의 좌표 (∑xi/n, ∑yi/n)로 현재 위치를 이동시킨다.
> 3. 1~2 과정을 위치변화가 거의 없을 때까지, 즉 수렴할 때까지 반복한다.

- Graph theoretic clustering

Regular graph: 그래프의 모든 노드의 정도가 동일합니다.
Eulerian graph: 모든 노드는 균등도를 갖습니다.
Complete graph: 모든 정점 쌍에 모서리가 있음

todo : ? 생략 ...

## Fitting

![f4](\img\2022\computer_vision\f4.png)

픽셀 값 배열(또는 필터 출력)에서 영역, 개체 및 모양의 집합으로 이동

todo : 생략, active contour modeling도 같이 생략

# classification

### BOW (Bag of Word)

1. 사전 학습:
  ‐ 클러스터링을 사용하여 시각적 단어 학습

  extract features (e.g., SIFT) from images

  Learn visual dictionary (e.g., K-means clustering)

2. 인코딩:
  ‐ 각 이미지에 대한 단어 모음(BOW) 벡터 구축

  Regular grid

  Interest point detector

  기타 방법: 랜덤 샘플링 및 분할 기반 패치

3. 분류:
  ‐ BOW를 사용하여 데이터 교육 및 테스트

### K-Nearest

• 테스트 시간에 성능이 좋지 않음
• 전체 이미지 수준에 대한 거리 메트릭은 매우 직관적이지 않을 수 있습니다.

# Motion Tracking

### Optical Flow

 두 개의 연속된 이미지 프레임이 주어지면 각 픽셀의 움직임을 추정

 색의 항상성
‐ 명암 영상의 밝기 항상성
‐ 암시: 픽셀 대 픽셀 비교 가능(이미지 기능 아님)
• 작은 움직임
‐ 픽셀은 조금만 움직인다.
‐ 시사점: 밝기 항상성 제약조건의 선형화

### Visual Tracking



문제점 

• 기하학적 변화(자세, 관절, 척도)로 인한 변화
• 측광학적 요인(조명, 외관)에 의한 변동
• 폐색
• 비선형 운동
• 매우 제한된 해상도, 흐릿함(표준 인식이 실패할 수 있음)
• 씬(scene)에서 유사한 개체





KLT(Kanade-Lucas-Tomasi)  알고리즘 단계

1. 만족스러운 코너 찾기
2. 루카스-카나데( Lucas-Kanade) 방법을 사용하여 각 코너에 대해 다음 프레임으로의 변위를 계산합니다.
3. 각 모서리의 변위 저장, 모서리 위치 업데이트
4. (선택사항) 1을 사용하여 M프레임마다 모서리점 추가
5. 2~3(4)을 반복합니다.
6. 각 코너 포인트에 대해 긴 궤적을 반환합니다



### Mean Shift Tracking

접근 방법 두가지

• 원하는 색상과 유사성에 따라 가중치가 부여된 픽셀을 사용하여 색상 "우도" 이미지를 만듭니다(단색 개체에 가장 적합).
• 히스토그램으로 색 분포를 나타냅니다. 평균 이동을 사용하여 색상 분포가 가장 유사한 영역을 찾습니다.

->

- 픽셀이 추적하려는 개체에 픽셀이 있을 가능성에 비례하는 가중치(픽셀 값)를 가진 데이터 포인트의 균일한 그리드를 형성하도록 합니다.
- 이 가중 점 집합을 사용하여 표준 평균 이동 알고리즘 수행



알고리즘 순서

Algorithm

1. Initialize location  𝑦
2. Compute H model
3. 연속 프레임(이미지)의 히스토그램 투영을 만듭니다.
4. Calculate mean-shift localization



# Convnet for Image

Alexnet
• Implemented a convolutional neural network
• Further theoretical improvements
‐ Rectified Linear Units (ReLU) instead of sigmoid or tanh
‐ Dropout
‐ Data augmentation



# Robot Vision

카메라 구성
• 직접적인 문제: 보정할 좌표 프레임이 많습니다.
카메라
– 투영 중심
– 다양한 모델
로봇
– 베이스 프레임
– 엔드 이펙터 프레임
– 객체





 비주얼 서보 제어 법칙
•  Image-based visual servoing(IBVS):
‐ 카메라에서 볼 수 있는 원하는 이미지 기능
‐ 이미지 기능에 전적으로 기반한 제어법
‐ 영상 좌표의 정렬
‐ 대상 이미지가 알려진 경우 보정 오류에 강합니다.
‐ 대상 깊이를 추정해야 합니다.
‐ 자세 오류가 크면 예측할 수 없는 궤적이 발생할 수 있습니다.
• Position-based visual servoing (PBVS):
‐ 견고하고 실시간 포즈 추정 로봇의 세계 공간(데카르트) 컨트롤러
‐ 대상 좌표계에서의 정렬
‐ 3D 궤적 계획 가능
‐ 보정 오류에 민감함
‐ 엔드 이펙터가 시야에서 벗어날 수 있음





### Visual SLAM

SLAM (Simultaneous Localization And Mapping)

동시 현지화 및 매핑
: 지도 제작과 현지화를 동시에 진행
• 확률론적 SLAM 문제의 기원은 1986년 IEEE 로보틱스 및 자동화 컨퍼런스에서 발생했다.
• 이 모델을 기준으로 로봇을 현지화하는 동시에 모바일 로봇 환경의 공간 맵 획득

![f5](\img\2022\computer_vision\f5.png)



# 중간고사 정리



- Image Transformations 

• Rigid Transformation
• Similarity Transformation
• Affine Transformation
• Perspective Transformation

- Filters

• Linear Filter
• Gaussian Filter / Derivative of Gaussian Filter

- Edge detection

‐ Prewitt, Sobel, Robert’s cross operator
• Line detection
‐ Canny edge detector
‐ Hough transform
• Corner detection
‐ Harris corner detection
• Blob detection
‐ Laplacian of Gaussian

- Feature Descriptors

• SIFT, SURF, HOG
• BRIEF, ORB

- Feature Matching

• Fitting, RANSAC

- Image Alignment

• Homography
• Rectification
• Stitching

- Two-view Geometry

• Epipolar Geometry
• Essential matrix
• Fundamental matrix

- Stereo Vision

• Stereo Rectification
• Stereo Matching
• Disparity & Depth






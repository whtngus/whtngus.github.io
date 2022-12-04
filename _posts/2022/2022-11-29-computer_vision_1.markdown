---
layout: post
title: "computer_vision_1"
date: 2022-12-04 01:20:23 +0900
category: datascience
---

                - 2주차
Geometry : 기하학적 왜곡현상(Geometric Distortion, G/D) 문제를 이야기 할 때 짧게 Geometry라고 표현
Radiometry : 적외선, 가시광선, 및 자외선 영역의 방사량 측정에 대한 것으로 모든 빛에 대해서 동일한 스펙트럼 반응 특성을 갖는 센서를 사용하여 측정 -> 전자기파의 복사량을 측정하는 과학
Photometry :  빛(가시광선)에 관계된 광량(조도,휘도,광도,광선속 등)을 측정하는 과학
Digitization : 연속 신호를 디지털 근사치로 변환하는 방법

Image Transformations
    image filtering(이미지 범위 변경),  image warping(이미지 도메인 변경 길이 변경 등 )
    linear transformation(회전 크기 변경 등)
    Euclidean, similarity, Affine(Linear Trnasformations), Perspective(관점)

Geometric Camera Model
        - Pinhole camera model : 핀홀 카메라는 렌즈를 사용하지 않고 작은 구멍을 통해 빛을 받아 들여 촬영하는 사진기
        - 빛의 회절 현상으로 흐리게 보일 수 있음 
        - 조리개 커지면 가까이 넓이 좁아지면 집중해서 하나를
        - focal length vs viewpoint -> 멀면 시야각이 좁아짐 

Pinhole Camera Mode
        - 상에 담겨서 180도 변경

Application
        - 아래서 건물을 찍으면 Perspective 이걸 펴줄 수 있음 
        - Redial distortion 동그랗게 가운대가 들어간거 같은 사진을 펴줄 수 있음         


                - 3주차

Image Filtering
필터링은 새로운 이미지 -> 기존이미지에서 새로운 픽셀을 만드는것(형태학적 X)
        - 구조적인 변화 없음
        - 변화를 주는 함수는 좌표에 의미 없고 픽셀 자체에서만 작용
        - output size full same valid
        - Lineartiy : 필터를 더함 , Shift invariance : 이동을한 후 필터 = 필터를 한후 이동 
        - non-linear filtering : 가우시안 .솔트, impulse 노이즈 
        - non-linear filtering : 튀는 현상없음, 연산 많이필요 

Edge detecting
        - Noise cleaning and Edge Detection :차이값을 구하기때문에 노이즈를 제거하는 역할을 하기도 함


                - 4주차
Aliasing
        - 아날로그에서 discret 한 내용을 가져오기 위한 샘플링 작업 
        - 주어진 값으로 샘플링을 하다보니 부족한 정보엥 의해서 외곡현상이 발생됨
        - Wagon-wheel effect : 비디오 프레임과 이미지의 이동이 같아서 일어나는 현상
        - 해결 방법 over sampling (최대 주파수의 2배샘플링을 더많이), 노이즈를 제거 후 가우시안 샘플링

Gaussian Image pyramid (다운 샘플링)
        - 필터링 처리를 해서 다운샘플링 시 다운사이증 가우시안 필터를 반복해 사용
        - 영상의 특징을 찾는데 도움이 됨 (상이즈를 작게 만들면서 원본 특징을 가져옴)
        - 블러링 전후를 제거해 차이값을 구함 그 차이값을 이용해 복원할 수 있음 -> 이렇게 나온게 아래

Laplacian Image pyramid (업셈플링)
        - Gaussian Image pyramid의 역순 작은연상을 큰 영상으로 복원 
        - 영상을 다운샘플링 시 차이값만을 가지고 있다면 복원할 수 있음 


                - 5주차
Locality(지역적인 특징), Quantity(이미지 안에서의 특징)
detection : 영상에서 특징을 가진점, Desription : detection된 포인트 들을 표현하는것  
feature
        edge line (point detection) coner blob (region detection)

edge detection 
        - 포인트의 차이가 커지는 경우, 미분값의 편차
        - canny edge detector : 가우시안 핉터를 이용하고 미분을 이용해 엣지를 구함(변화량의 절대값)
                                MS 최대가 아닌것중 하나를 선택
         ->엣지를 인식할때 엣지가 얇아지는 구간이 있음 -> 인접한 비슷한 구간을 연결해 나가는 방식을 사용


Hough Transform(허프변환)
        - 직선이나 곡선을 이용해 특징을 찾음, 라인 성분 및 곡선 원등을 찾음
        - 점좌표 극좌표를 이용하는 방법이 있음 
                점좌표 : edge들을 이용해서 라인을 그음 


Corner detection
        small window w - 지역의 윈도우를 구하기 위한 크기 값 (필터 크기)
        harris corner detection - w가 이동했을때 이도하는 전체적인 좌표값을 비교해서 사용  
        Invariance properties - 영상 전체의 픽셀의 같은값을 증가 변환 시켰을때 
                        affine intensity : ai+b 에서   a를 변화시킨 경우 
                        translation, rotaion : 부분적으로 변경가능 -> 이미지 로테이션은 코베리언트 하다 
                        scaling : 변회된 결과값을 가져올 수 잇음 


Blob detection
        엣지 디텍터들을 이용해서 블록을 구할 수 없을까?
        Laplacian of gaussian : 이미지 -> 가우시안 스무딩 -> 변화는 값 부분을 엣지로 판단
                                사이즈 크기에 따라 다름 -> 시그마를 올리는 경우 블록을 탐지 가능(그러나 방은값이 줄어들어 탐지가 안됨)
                                변형을 가한경우 달라짐 -> 영상이 같아졌는지를 확인 특징을 확인
                                변형을 가한건 주변을 통해서 nomalization을 함  


                - 6주차
SIFT, SURF, HOG
BRIEF, ORB -> binary
Characteristics of good features
        Repeatability(반복성), Saliency(독특해야함), Compactness and efficiency(적은 수여야함), Locality(지역적 표현이 있어야함)

SIFT
        관심점을 찾은후 affine 변화된 내용을 찾는 방법

SURF
        속도를 개선 - 검출을 잘 하고 있으나 너무 느리다고 함
        영상을 적분으로 미리 만들어 둬서 연산 속도를 줄임(그전은 매번 가우시안을 사용) 
        미분값 방향을 추출했을때 가장 큰 뱡향을 중심으로 특징점에 대한 기술을 함  

HOG
        각 영상에서 그레디언트를 추출해서 히스토그램으로 만드는 작업
        윤각적인 형태가 뚜렷한 사진을 디텍션할때 사용
        양상내의 블록을 만들어 구역을 나눠서 그래디언트를 구해서 히스토그램을 만듦

BRIEF 바이너리
        특징점을 찾은후 기술하는 방법에 대한 내용 
        특징점을 중심의로한 임의의 두 쌍을 정해 더큰 쌍은 1 작은쌍은 0을 부여
        이미지 외곡이나 변형이 된경우 찾을 수 없음(로테이션도 못잡음)


ORB(SIFT SURF 의 장점을 모아옴)
        FAST(특징추출) BRIEF(기술) 사용
        fast(코너를 잘 찾으나 방향성 못찾음 ), brief(rocatino 등 변형에 약함) -> 이를 해결


                - 7 주차
Features Matching 어떻게 적용할 것인지 
        Fitting :  노이즈 이상치 탐지 미싱데이터등 전처리 수행 (optimial - 최소제곱법 least squares, outliers - robust fitting ransac, many line - Ransac Hough rransform, -> Model selection)
        RANSAC : 적은 아웃라이어에 강하다, least squres 처럼 라인을 만들고 어느라인 내에서는 인정 나머지는 버림
                distance threshold t, number of samples n, consensus set size d (몇번이나 돌릴지) 

Correspondence(일관성)
        두 그림이 같은 부분을 찾을때 어떻게 연관성을 가져갈 수 있지?
        모든점들을 다 이어서 이미지 변환시킴 이미지 얼라인먼트 
        ex) 옜날 모습과 오늘날 사진을 합성

IMAGE Alignment
        Homography : 평면을 바라보는 관점에 따라 이미지를 저장 상들을 표현  어파인 변환의 한계가 있음
                        두개의 찍은 사진을 변환시켜 하나의 사진으로 만들어주는 작업 
                        -> affine translation만 하면 어색함  perspective 등 해줘야햄 image mapping 
                        다 찾은 특징점을 트랜스폼 관계를 찾아 붙여 나가기 시작 
                        => 화소값이 다른경우 REMOVING SEAMS(밝기 다름), 필터링  
        rectificatino
        stitching


        





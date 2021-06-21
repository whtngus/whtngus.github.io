---

layout: post
title: "paper : Predicting Camera Viewpoint Improves Cross-dataset Generalization for 3D Human Pose Estimation"
date: 2021-06-21 19:20:23 +0900
category: paper
---

# 논문 정보 

논문 명 : Predicting_Camera Viewpoint Improves Cross-dataset Generalization for 3D Human Pose Estimation

2020년 4월 7일 European Conference on Computer Vision. Springer, Cham, 2020. 게재

http://wangzheallen.github.io/cross-dataset-generalization

University of California + (NVIDA지원 받음)

url : https://arxiv.org/abs/2004.03143

git url : - 코드 없음



# Abstract

이미지 에서 사람의 3D 포즈에 대한 추정은 대용량 데이터셋이 제공됨에 따라 많은 관심을 끌고 있는 테스크 이다.

그러나 제공되는 데이터 셋은 특정 상황에 제약이 있음으로 범용적으로 사용하기 힘든 문제가 있음

이를 해결하기 위해 5개의 포즈 데이터 세트를 보안하고  결합하여 데이터를 가공

카메라 뷰 포인트 분포에 따른 차이에 초점을 맞춤

# 1. Introduction



![pic_1](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\pic_1.PNG)

많은 vision연구가 들은 특정 작업에 사용할 수 있는 데이터의 양과 품질을 향상시키기 위해 노력하고 있다.

위 그림은 3d 포즈 추정을 위한 훈련 모델에 사용되는 5가지 데이터세트 중 Human3이다.

**5가지 데이터 셋 : Human36M, GPA, SERPRIC, 3DPW, 3DHP **

논문에서는 위 그림에서 와 같은 데이터의 6M개의 데이터 세트를 어떻게 향상시킬건지를 제시하고 있다.

-> 서로다른 mocap 시스템(VICON, The Caputer, IMU)과 서로 다른 카메라를 사용하여 수집되었고,  관점과 포즈 또한 다르다. 

논문에서는 이런 3D포즈 모델의 일반화를 연구하고 보조예측 과제인 카메라 보기 방향과 몸통 방향에 의해 정의된 신체 중심 좌표계 사이의 상대적 회전축을 제안해서 데이터세트의 일반화를 시킴

5개의 3D포즈 데이터 세트에서SOTA 모델인 PoseNet의 성능을 능가함을 보임 



해당 연구에서 제시하고자 하는 컨트리뷰션

- 공개된 3D 인간 포즈 데이터셋에 대한 EDA -> 다양성을 특징화
- 데이터셋의 과적합을 제한해 모델 일반화 방법을 제한하고 카메라 관점 예측또한 제안
- sota모델과 비교해 3D 포즈 추정을 개선 sota스코어를 달성



# 2. Related Work

3D 포즈 추정은 모션 리타겟팅,  게임, 스포츠 분석, 의료와 같은 분야에서 적용이 가능하다.



카메라 프레임에 비례하여 중심 좌표를 계산하고 중심 좌표를 설정 

CNN 베이스의 모델을 이용해 많은 연구가 있었고 동공 감지, 분류 분할 등 많은 연구가 이루어 지고 있음 

예를 들어 3D 포즈 추정을 통해 얼굴 시점을 예측하면 얼굴 인식이 개선되는 결과가 있음 



# 3. Variation in 3D Human Pose Dataset

![table_1](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\table_1.PNG)

![pic_2](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\pic_2.PNG)

![pic_3](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\pic_3.PNG)

분석을 위해 잘 구성된 3개의 데이터 세트 

 Human3.6m(H36M), MPIinf-3dhp(3DHP), SERRIPT 와 최근에 추가된 2개의 데이터세트 3DPW 및 GPA를 이용

사진 캡처 기술, 외관, 신체 크기, 포즈, 뷰포인트, 의류, 인체 장면 상호 작용등 다양한 측면의 특징을 가진 데이터 세트로 구성되어 있음

Fig2 그림에서 

H36M은 네 개의 뚜렷한 피크(-30도, 30도, -160도, 160도)를 가진 방위보다 시야 방향이 넓다는 것을 관찰합니다.  0보다 높은 각도의 편향이 있고, 대부분 -60~90도 사이

SEPRRISTOR은 방위 위에 균일한 분포로 카메라 위치를 합성해서 샘플링되있고 고도에 대해서도 균일한 샘플링 

3DPW는 휴대용 또는 삼각대 장착 카메라에 피사체와 거의 동일한 높이로 촬영한 각도

3DPW는 방위성이 가장 균일하게 퍼져 있으며 천장을 포함한 여러 눈높이에 장착된 카메라를 사용한 결과로 광범위한 고도를 가지고 있음 

 3DHP는 14개의 카메라 위치에서 찍어 표준 방향의 특징을 나타냄

위는 고차원 임베딩을 시각화 하기 위해 UMAP시각화를 이용해 2D로 비선형 임베딩을 수행 

=> 결과적으로 데이터 들이 상당이 유사한 분포를 가지고 있음

논문에서는 이런 데이터 세트를 정량화할 수 있는 기하학적 수의 변화를 특성화하는데 초점을 맞춤  -> 위 사진의 테이블은 해당 데이터에 대한 정리 (*꽤 유용함*)

*위의 표1의 내용을 사용하여 카메라 고유 매개 변수와 카메라 거리의 데이터 세트 차이를 정규화를 하는데 이용함* 

-> 카메라 방향은 정규화 하지 않음 (위에서 카메라 방향을 예측한다고 해서 그런걸로 보임)

신체 중심 좌표 프레임 계산 관점에 독립적인 자세를 정의하려면 표준 신체 중심 좌표 프레임을 지정해야 한다.  위의 Fig2와 같이 원점을 root joint형(일반적으로 골반)을 카메라의 중심 좌표로 보고 pp = (xp, yp, zp)으로 설정 - 방향은 왼쪽 어깨와 오른쪽 어깨에 의해 고정됨!

![formula_0](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\formula_0.PNG)

위의 내용을 기본으로 전면 f, 위쪽 u 그리고 오른쪽 r로 구성된 직교 프레임을 위의 수식과 같이 정의한다.

또한 신체 중심 위치를 일반적인 골격 크기로 확장 (아래 수식)

ex) u 는 골반에서 두 어깨의 가운대 위치한 방향 ! (f r은 음...)

![formula_1](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\formula_1.PNG)

그럼 위의 수식처럼 중심 프레임과 카메라 프레임사이의 회전은 R = - [r, u, f]에 의해서 정해진다.



# 4.  Learning Pose and Viewpoint Prediction

*데이터 세트에 걸친 편향을 극복하기 위해 카메라 중심 포즈 추정을 위해 관점 예측을 사용할것을 제안*  -> 결국 핵심 제안 포인트

### 1.  Baseline architecture

![pic_4](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\pic_4.PNG)

![formula_2](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\formula_2.PNG)

base line은 2 step으로 구성됨

step 1. Resnet backbone 을 통해서 사람을 detection하고 그 위치를 가져감

step 2. Batch Normalization과 ReLu를 사용해 세 개의 연속 deConvlution 레이어를 사용해 셈플을 추출 (1*1 Conv 레이어를 이용해 업 셈플링)

위의 연산은 2D영상 좌표 (xi,yj)를 이용해 루트에 대한 상대 길이를 추출하는데 사용

loss함수는 예측 포인트와 실제 포인트와의 거리를 사용함

### 2. Predicting the camera viewpoint

![pic_5](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\pic_5.PNG)

해당 논문에서는 3가지 접근 방법을 고려함 

> 1. q의 직접 회귀 분석
> 2. 공간 또는 회전을 정량화하고 k-way classification을 수행
> 3. 정량화된 회전을 예측한 후 클러스터 중심에서 잔차를 회귀하는 결합된 접근방법

결국 좌표 분류기반 손실이기 때문에 정확한 프레임을 예측을 산출하지 않으면 포스 예측에서 개선을 하지 않는것을 발견해 이를 정량화하기 위해 k-means를 사용해 사분원을 k-100인 군집으로 나눠서 군집화를 수행 해 각 데이터세트에 대한 분수를 무작위로 셈플링함.

![formula_3](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\formula_3.PNG)

100개에서 어떤 좌표인지를 예측하는것을 목표로 함 

위 식의 k는 각 클러스터링된(100개)의 센터에 해당하는 값



![formula_4](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\formula_4.PNG)

negative log-likelihood를 통해 로스를 전달 

최종 로스는

 ![formula_5](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\formula_5.PNG)

이다

# 5. Experiments

이미 중복을 줄이기 위해 30fs을 5fps로 다운셈플링 해서 사용 

-> 25K의 학습 데이터셋과 2957개의 검증 데이터셋 

 PCK3D[19]로, 조인트 예측의 정확도(150mm MPJPE의 임계값

### 1. Cross-dataset evaluation

![table_2](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\table_2.PNG)

위의 표2 그림을 참조 

굵은 숫자는 검정 세트에서 가장 성능이 좋은 모형

최상의 성능은 동일한 세트에서 모델을 교육하고 평가할 때 발생

파란색으로 표시된 숫자는 제안된 쿼터니언 손실을 사용하여 오류 감소가 가장 큰 테스트 세트

->  총 교차 데이터 세트 오류가 10.6mm(MPJPE) 감소하는 반면, 동일한 데이터 세트 오류 감소는 1.2mm(MPJPE)

### 2. Effect of Model Architecture and Loss Functions

평가를 정량화 하기위해 베이스라인에도 고유 매개변수를 사용했지만 오류가 더 커짐을 보임

### 3.  Comparison with state-of-the-art performance

![pic_6](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\pic_6.PNG)

표5는 제안 접근방식을 모든 5개의 데이터세트를 사용한 경우를 비교 

모두 sota 스코어를 달성함

아래는 결과 예시

![pic_7](\img\2021\Predicting_Camera_Viewpoint_Improves_Cross-dataset_Generalization_for_3D_Human_Pose_Estimation\pic_7.PNG)

# 6. Conclusions

카메라의 분포에따라 존재하는 데이터 세트 평향을 관찰하고 신체 중심 좌표 프레임을 제안함

신체 중심과 마케라 중심 좌표 사이의 상대적 회전을 이용해 3d 예측 오류를 크게 줄이고 평가를 일반화 시킴 으로써 sota 스코어를 달성 
---
layout: post
title: "Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking"
date: 2025-01-18 02:05:23 +0900
category: paper
---

# Mimicking-Bench: A Benchmark for Generalizable Humanoid-Scene Interaction Learning via Human Mimicking



2024년 12월 23일

git : https://mimicking-bench.github.io/ 코드x

상하이대 



# Abstract

3d 에서 사람의 데이터를 범용적으로 인간과 비슷하게 사호작용할 수 있도록 하는 것은 로봇공학에서 실상활에 적용하기 위한 중요한 연구 과제이다 

그러나 아직까지 진행된 연구에서는 부자연스러운 작은 범위에서만 연구되고 있음

손으로 만든 부족한 설명과 데이터셋과 벤치마크는 일반적인 염구를 탐구하는데 부족함

이러한 문제를 해결하기 위해 Mimicking-Bench를 제안함

-> 종합적으로 설계된 장면기반의 상호작용 데이터

6개의 가정용 전신 휴머노이드 장면 상호작용이 테스크로 구성되어있음 

11K의 객체 형태와 20K개의 합성데이터, 3K의 상호작용데이터로 구성됨

그리고 이대이터를 모션추적, 모션리타겟팅, 모방 학습의 조합으로 완벽하게 구축함 

# 1. Introduction

지난 10년간 휴머노이드 로봇공학의 주목할만한 발전이 이루어짐 

실세상을 시뮬레이션할 수 있도록 개발되었으며, 여러 장애물 걷기 등 의 스킬들의 다양한 데이터가 나옴 

위사상학적 유사성을 가진 유머노이드와 인간골격등은 다양한 인간 기술 데이터를 사용한다 

그러나 이런 방식은 사람과 모델과의 차이점, 애니메이션으로의 변환, 일반화된 정책 도출 등  몇가지 기술적 난관에 부딪친다. 

그러나 실제에서 구현하기에는 비싼 로봇 가격이 들어 문제가 있음 

나머지 생략



Mimicking-Bench를 제안함

6개의 가정용 전신 휴머노이드 장면 상호작용이 테스크로 구성되어있음 (전신 접촉을 포함함)

이데이터는 두가지 과제를 다룸

1. 다양한 사람의 기술들을 참조하는 방법 
2. 기패러다임 내에서 추가적인 연구와 개발이 필요한 기술적 측면을 식별하는 것.

23K의 사람의 상호작용 모션 연속 데이터ㅏㄱ 있고 

11개의 다양한 객체가 있다고함 



그리고 다양한 핵심 기술을 식별함

1. 스켈레톤에서 retargeting human motions
2. 에니메이션에서 모션추적
3. 사람을 모방하는것을 설명함



그리고 2가지 타입을 연구를 함 

1. 기존에 잘 확립된 휴머노이드 기술 학습 파이프라인을 비교
2. humanoid-scene interaction learning과 관련된 다양한 우수 알고리즘을 비교함 



논문의 컨트리뷰션

1. 일반화된 humanoid-scene interaction learning을 위한 Mimicking-Bench를 제안함 
2. 다양한하고 많은 데이터셋을 통합함 
3. 일반적인 기술 학습 패러다임을 개발하고, 파이프라인 단위 및 모듈 단위 평가를 모두 지원
4. 사람을 따라하는 효과적인 실험을 함 

# 2. Related Work

## 2.1. Benchmarks for Humanoid Skill Learning

.. 나머지 생략 진짜 시뮬레이션 으로 가는듯 함..


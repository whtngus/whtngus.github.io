---
layout: post
title: "Generate model score matrix"
date: 2021-04-28 19:20:23 +0900
category: deep_learning
---
# Generate model matrix 정리 

 정리 score matrix 리스트 

BLEU, METEOR, ROUGE_L, SPICE, CIDEr1



## BLEU(**bilingual evaluation understudy**)

기계 번역 결과와 사람이 직접 번역한 결과가 얼마나 유사한지 비교하여 번역에 대힌 성능을 측정하는 방법

측정 기준은 n-gram에 기반

점수가 높을수록 더 좋은 성능 

- 장점

> - 언어에 구애받지 않고 사용할 수 있음
> - 계산 속도가 빠름

- BLEU algorithm

![bleu_matrix](\img\generate_score_matrix\bleu_matrix.PNG)

> n-gram을 통한 순서쌍들이 정답 순서쌍들과 얼마나 겹치는 지를 측정(Precision) -> 1~4 gram 
>
> 문장길이에 대한 과접합 보정(Brevity Penalty) -> precision을 측정하기 때문에 
>
> 같은 단어가 연속적으로 낭로때 과적합 되는 것을 보정(Clipping)



## METEOR(**Metric for Evaluation of Translation with Explicit ORdering**)

BLEU는 Precision만을 측정하기 때문에 Recall을 측정할 필요가 있음 

Uni-gram의 Precision과 Recall의 조화 평균을 기반으로 재현율을 더 높게 사용 

정확한 단어 일치 정도와 동의어 일치등의 BLEU의 일부 문제를 해결하기 위한 메트릭스 

- 평가 방법

> BLEU와 마찬가지로 문장 단위의 평가
>
> ![meteor_sort](\img\generate_score_matrix\meteor_sort.PNG)
>
> 정답 문장가 후보 문자열 사이에 정렬을 만듦 (위 그림 참조)
>
> - 정렬 생성 재약
>
> > 후보 전역의 모든 Uni-gram은 다른 문자열의 유니 그램 사이의 선으로 생각
> >
> > 후보 문자열의 모든 Uni-gram은 정답 문자열에서 0개 또는 1개의 유니 그램에 매핑되어야 함
> >
> > Uni-Gram의 정밀도는 아래와 같음
> >
> > ![meteor_formula_1](\img\generate_score_matrix\meteor_formula_1.PNG)
> >
> > m은 정답 문자열과 후보 문자열 모두 발견되는 유니 그램의 수 
> >
> > wt는 후보 번역의 유니 그램 수 
> >
> > Uni-Gram의 재현율은 다음과 같음
> >
> > 
> >
> > ![meteor_formula_1](\img\generate_score_matrix\meteor_formula_2.PNG)
> >
> > wr은 접답 문자열의 유니 그램 수
> >
> > METEOR 스코어 에서는 재현율을 높게 평가함 
> >
> > ![meteor_formula_1](\img\generate_score_matrix\meteor_formula_3.PNG)
> >
> > 위의 방법을 사용해 더 긴 n-gram 일치를 사용하여 정렬에 대한 패널티 p를 계산 
> >
> > ![meteor_formula_1](\img\generate_score_matrix\meteor_formula_4.PNG)
> >
> > c : 청크의 수  => 정답과 후보 번역의 인접한 유니 그램 집합(인접한 매핑이 길수록 더 적은 청크가 있음)
> >
> > Um : 매핑 된 유니 그램의 수 
> >
> > - 최종 스코어 계산
> >
> > 
> >
> > ![meteor_formula_1](\img\generate_score_matrix\meteor_formula_5.PNG)



## ROUGE(**Recall-Oriented Understudy for Gisting Evaluation**)

BLEU는 precision 기준으로 평가를 하기 때문에 Recall도 같이 보기 위해 사용 

ROUGE-N은 일반적으로 n-gram recall으로 평가한 metric 

- 평가 방법

> - ROUGE-n
>
> 재현율 기반 측정이며 n-gram 비교를 기반
>
> n-gram(대부분 2~3 가끔 4개)을 참조 요약 및 후보 요약에서 추출 
>
> p는 후보 요약과 참조 요약 사이의 공통 n-gram수
>
> q는 참조 요약에서만 추출한 n-gram수
>
> ROUGE-n = p/q
>
> - ROUGE-L
>
> 두 텍스트 시퀀스 사이에서 가장 긴 공통 하위 시퀀스(LCS) 개념을 사용 
>
> 두 요약 문장 사이의 LCS가 길수록 더 유사하다는 가정으로 해당 메트릭스는 ROUGE-n보다 유연하지만 n-gram이 연속적이여야 한다는 단점이 있음.
>
> > - LCS(Longest Common Subsequence)
> >
> > 최장 공통 부분 문자열 -> substring은 연속된 부분 문자열, subsequecne는 연속적이지 않은 부분 문자열
> >
> > 가장 긴 부분 문자열을 찾는것 
> >
> > ex)  Substring
> >
> > 고객건강지킴이
> >
> > 고가객잔지킴이
> >
> > 
> >
> > 가장 긴 SubString 은 문자열 뒤의 지킴이
> >
> > 가장 긴 Subsequence는 고객지킴이 
> >
> >  -> "고객" 건강 "지킴이"
> >
> > -> "고" 가 "객" 잔 "지킴이"
>
> - ROUGE-SU
>
> skip-bi-gram 및 uni-gram ROUGE라고도 하며 uni-gram과 bi-gram을 고려 
>
> bi-gram의 첫 번째 단어와 마지막 단어 사이에 단어를 삽입 할 수 있으므로 연속적인 단어 시퀀스일 필요가 없음



## SPICE(Semantic Propositional Image Caption Evaluation)

이미지 캡션 생성에 대한 평가를 위한 matrix

REOUGE, METEOR는 n-gam에 민감한데 n-gram중복은 두 문장이 동일한 의미를 전달하는지 파악하는데 충분하지 않음 

SPICE는 *의미 론적 명제 콘텐츠가 인간 캡션 평가의 중요한 구성 요소* 라고 가정합니다

- 이미지 캡션 에서 기존 방식의 잘못된 예시

> - n-gram의 유사도가 높게 나오나 설명이 잘못된 문장
>
> 테니스 코트 위에 서있는 어린 소녀
>
> 그린 코트 위에 서있는 기린.
>
> - n-gram의 유사도가 낮게 나오나 설명이 맞는 문장
>
> 잘게 썬 채소로 채워진 반짝이는 금속 냄비.
>
> 스토브의 팬에 다진 야채가 들어 있습니다.

-> 어렵 ㅠㅠ 추가정리 필요



## CIDEr1

-> 어렵 나중에 추가정리하기 !!! 

https://www.youtube.com/watch?v=YHVox8yjMUI








# 참고 

- BLEU 참조

https://donghwa-kim.github.io/BLEU.html

- METEOR 참고

https://en.wikipedia.org/wiki/METEOR

- ROUGE 참고

https://ichi.pro/ko/jadong-tegseuteu-yoyag-pyeong-ga-50788783524155

- SPICE 참고

https://link.springer.com/chapter/10.1007%2F978-3-319-46454-1_24

- CIDEr1 참고

https://arxiv.org/pdf/1411.5726.pdf
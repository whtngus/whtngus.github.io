---
layout: post
title: "voice - base"
date: 2020-08-05 19:20:23 +0900
category: deep_learning
---

# 기본 지식

# 기초지식 정리

### MOS(Mean opinion score)
```
전화통화 성능평가에 주로 사용되는 통계에 의한 의한 주관적 평가 기법
-> 음성은 평가할 수 있는 방법이 없기 때문에 사람이 직접 평가를 해야함 
평가 방법 개요
 - 주관적인 방법을 통하여 음성의 품질을 평가하는 방법으로, 
    . 선별된 여러명(남자,여자)의 음성을 녹음 후,
    . 이를 음성 플레이어를 이용하여 재생시킨 후 이에 대한 품질 평가를 하게 됨
        
단점 : 정확성/공정성이 떨어지며, 평가에 시간이 거릴고, 복잡함으로 인해 고비용이 요구됨
- 등급 구분 
5 (Excellent), 4 (Good), 3 (Fair), 2 (Poor), 1 (Bad)


- 개략적 MOS 수준
ㅇ MOS 4~5   : 고품질, ISDN 호 품질 이상. Toll 품질이라고도 함
ㅇ MOS 3.5~4 : 중간품질, 32Kbps ADPCM 품질 정도. 자연스러운 통화 수준
ㅇ MOS 3~3.5 : 대화는 잘 이루어지지만 품질저하 느낄 수 있음
ㅇ MOS 2.5~3 : 군사품질, 대화 가능하지만 집중할 필요
```

### mel spectrogram

```
멜 스펙트럼은 음성의 주파수 특성을 분석한 데이터
-> 음향 신호를 주파수, 진폭(강도), 시간으로 분석하여 얻어진 그림
음성 데이터의 주요한 정보들이 아주 효율적으로 정리되어 담겨 있습니다. 하지만 멜 스펙트럼을 곧바로 음성으로 변환할 수 없기 때문에, 멜 스펙트럼을 우리가 익히 아는 음성 데이터로 변환하기 위한 추가적인 작업이 필요

주파수와 진폭의 시간에 따른 변화를 보여주는 삼차원적인 그림이다 
x축 : 시간, y축 : 주파수, z축 :  진폭

Mel spectrogram의 y축은 filterbank의 개수와 동일한 dim을 갖는다. 즉 40개의 각 filterbank들이 커버하는 영역의 Hz를 triangle filter로 검출하여 요약한 정보이다.
Log Mel Spectrogram
- log 취하는 것이 deeplearning에서는 큰 의미를 갖는다.
```

### griffin-lim algorithm

```
griffin-lim : 스팩트로그램을 음성으로 만들어주는 알고리즘
위에서 보다시피(mel specrogram 설명) 스펙트럼은 곧바로 음성으로 변환할 수 없다.
프로세스 전체과정에서 강도 값을 일정하게 유지한 채로 STFT 및 역 STFT 연산이 수렴될 때까지 무작위로 위상 값을 추측하는 과정을 반복합니다.
-> 즉 스팩트럼을 STFT로 변환하는 알고리즘
```

### STFT(Short-Time Fourier Transform)

```
소음진동 분석에 기본이자 필수인 신호처리 기법
주파수 특성이 시간이 따라 달라지는 사운드를 분석하기 위한 방법이다.
즉,  STFT는 데이터에서 시간에 대해 구간을 짧게 나누어 나누어진 여러 구간의 데이터를 각각 푸리에 변환하는 방법
시계열을 일정한 시간 구간으로 나누고 각 구간에 대해 스펙트럼을 구한 데이터이다. 
시간-주파수의 2차원 데이터로 나타난다.
-> 직관적인 설명
프리퀀시가 시간에따라서 변화가 되는 것을 알기위해 사용
```

###  필터 뱅크 (Filter Bank)

```
Filter Bank는 모두 Overlapping 되어 있기 때문에 Filter Bank 에너지들 사이에 상관관계가 존재하기 때문이다. 
DCT는 에너지들 사이에 이러한 상관관계를 분리 해주는 역활을 해줍니다

ㅇ 여러 필터가 대역별(임계대역)로 병렬로 연결된 구조
```

### Discrete cosine transform (DCT)

```
DCT는 n개의 데이터를 n개의 코사인 함수의 합으로 표현하여 데이터의 양을 줄이는 방식입니다.
- 저 주파수에 에너지가 집중되고 고 주파수 영역에 에너지가 감소합니다.
```

### 양자화 (Quantization)

```
진폭(amplitude) 에 관련된 정보를 얼마나 자세히 담을 것인가를 결정하는 과정이며, 
단위는 2진법을 기초로 하는 비트(bit)라는 단 위를 사용한다
```

### 푸리에 변환 (Fourier transform)

```
임의의 입력 신호를 다양한 주파수를 갖는 주기 함수(복수 지수함수)들의 합으로 분해하여 표현하는것
ex) 입력 신호의 주기와  신호(음성)의 주기에 따른 진폭
-> 오일러 공식을 이용해서 사용 
결과 : 주기적으로 나오느 시퀀스를 얻어 내는것 
```

### 음성인식 세대 분류 

```
    - 1 세대
큰 서버를 이용하여 음소 음절을 인식하는 단계
    - 2 세대
DTW(Dynamic Time Warping)
같은 단어를 패턴 매칭을 이용해서 단어를 매칭하는 방법
-> 서로 같은 말을해도 말을 하는 길이가다름 이 길이를 정규화 하는 방법
(일부 사용화 되기 시작)
    - 3 세대
HMM, Viterbi decoding 이 나오기 시작
각 자모의 통계모델을 가지고 분석을 싲가
    - 4 세대
딥러닝 모델 분석의 시작
```

### WER(word error rate)

```
    - WER 
음성인식 모델 정확도를 측정 하는 산업 표준 
잘못된 단어 수를 계산 하 고, 사람이 레이블 지정 된 총 단어 수로 나눈다.
    - 식
wer = ( (I + D + S) / N ) * 100%
삽입(I) : 가설 성적 증명서에 잘못 추가 된 단어 
삭제(D) : 가설 성적 증명에서 감지 되지 않은 단어
대체(S) : 참조와 가설 사이에서 대체 된 단어

```

# 참고
- tactron 관련 <br>
http://www.ktword.co.kr/abbr_view.php?m_temp1=2056 <br>
https://newsight.tistory.com/294 <br>
http://contents.kocw.net/KOCW/document/2015/pusan/kwonsoonbok/9.pdf <br>
https://m.blog.naver.com/PostView.nhn?blogId=vmv-tech&logNo=220936084562&targetKeyword=&targetRecommendationCode=1 -> stfp <br>
- 양자화 Quantization <br>
http://www.kjorl.org/upload/pdf/0012004174.pdf <br>
- 음성신호 유튜브 <br>
https://www.youtube.com/watch?v=FjYNM3YGFB4 <br>
- 음성인식 딥러닝
https://www.youtube.com/watch?v=nzZkwMCH6V4&t=1s <br>
---
layout: post
title: "mfcc"
date: 2020-08-05 19:20:23 +0900
category: voice
---

# MFCC(Mel Frequency Cepstral Coefficient)

### MFCC 개념

> 음색(timbre)

```
MFCC는 오디오 신호에서 추출할 수 있는 feature로, 소리의 고유한 특징을 나타내는 수치입니다.

음색은 악기, 사람 목소리를 구별할 수 있게 해주는 차이 
공학적으로 보면 음색을 좌우하는 아주 중요한 요소는 "배읍 구조"이다.
ex) 피아노와 기타의 음색이 달라 같은 "도"를 쳐도 에너지 비율과 이루어 져있는 Hz(주파수)가 다르다
-> MFCC는 이 "배읍 구조"의 차이를 표현하는 숫자
```

> MFCC 특징

```
음정(음고 pitch)이 변해도 MFCC가 일정하게 유지된다.
ex) 높은 음의 안녕 과 낮은 음의 안녕 같게 인식되어야 함
-> 악기별 음표를 그려주는 경우에는 MFCC를 사용하면 안됨 (음정 차이를 무시하기 때문에)
```

### MFCC 이해

```
MFCC(Mel-Frequency Cepstral Coefficient)는 Mel Spectrum(멜 스펙트럼)에서 Cepstral(켑스트럴) 분석을 통해 추출된 값


MFCC를 기술적으로 이해하려면 선행으로 다음 개념들을 알아야 한다.
-  Spectrum(스펙트럼)
-  Cepstrum(켑스트럼)
-  Mel Spectrum(멜 스펙트럼)
```

### MFCC의 단계

<img src="/img/speech/mfcc/MFCC_추출_과정.PNG" width="600px" height="300px"></img> <br>

1. 입력 시간 도메인의 소리 신호를 작은 크기 프레임으로 자른다. <br>

```
시간 영역에서 입력된 소리 신호는 지속적으로 변화하게 된다. 
따라서 간단히 하기 위해 짧은 시간내에서는 소리 신호가 많이 변하지 않는다고 가정(짧은 구간에서 통계적으로 변화가 거의 없다고 가정) 
일반적인 MFCC의 프레임의 길이는 20~40ms 정도로 정한고 있다.
-> 샘플의 수가 너무 적으면 주파수 분석에 신뢰도가 떨어지고, 값이 너무 크면 신호의 변화가 한 프레임 내에서 너무 크게 되기 때문에 분석이 어려움
```

2. 각 프레임에 대하여 Power Spectrum의 Periodogram estimate(Periodogram Spectral Estimate)를 계산한다. <br>

```
해부학적으로 사람의 귀는 입력된 소리의 주파수에 따라 달팽이관의 진동하는 부위가 다르다 
-> 어느 지점이 진동하냐에 따라, 각 달팽이관 신경들이 뇌에 어떤 주파수가 입력되는지 알려줌.
MFCC의 Periodogram Estimation(주기도 평가)은 이러한 기능과 비슷한 역할을 한다.
```

3. 2번에서 구한 Power Spectrum에 Mel Filter bank를 적용하고, 각 필터에 에너지를 합한다.<br>

```
처음 필터는 매우 얇으며, 특히 0Hz(저주파) 주변에서 얼마만큼의 에너지가 있는지를 알려준다.
주파수 올라가면 필터의 폭은 넓어짐, 고주파가 되면 거의 고려 X
Mel Scale은 Filter Bank를 나눌 때 어떤 간격으로 나누어야 하는지 알려준다.
```

4. 3번에서 구한 모든 필터 뱅크 에너지의 Log를 취한다.<br>

```
Filter Bank에 로그를 취함으로 써, 인간이 실제로 듣는것과 유사하게 소리의 특징을 만들 수 있다.
(인간의 귀는 소리의 크기를 Linear Scale로 감지하는 것이 아니기 때문에
 일반적을 소리가 2배 크게 들리기 위해서는 8배의 에너지를 인가해야 한다고 한다.)
 -> 에너지 변화가 좀 크더라도 실제 큰 차이가 없을 수 있기 때문에
```

5. 4번 값에 DCT를 취한다.<br>

```
이유
1. Filter Bank는 모두 Overlapping 되어 있기 때문에 Filter Bank 에너지들 사이에 상관관계가 존재하기 때문
(이해안됨)
2. DCT는 에너지들 사이에 이러한 상관관계를 분리 해주는 역활을 하며, 따라서 Diagonal Covariance Matrice 를 사용할 수 있게 된다.
```

6. DTC를 취한 값에 Ceofficient 2~14 만 남기고 나머지는 버린다 <br>
 
```
26개 DCT Coefficient 들 중 12만 남겨야 하는데, 그 이유는 DCT Coefficient 가 많으면, 
Filter Bank 에너지의 빠른 변화를 나타내게 되고, 이것은 음성인식의 성능을 낮추게 되기 때문
```

### 필요 지식

> Spectrum

```
Spectrum에는 배읍 구조의 특징을 추출한다.
-> 이것을 가능하게 하는 것이 Ceptral
```

> Cepstral Analysis


<img src="/img/speech/mfcc/MFCC_분리.PNG" width="300px" height="250px"></img> <br>

```
포먼트는 소리의 특징을 유추할 수 있는 중요한 단서.
포먼트들을 연결된 곡선과 Spectrum을 분리해 냄.
그 곡선을 Spectral Envelope라 하고, MFCC는 둘을 분리하는 과정
-> 이떄 log 와 IFFT(Inverse FFT: 역 고속 푸리에 변환)을 사용
```

> Mel Spectrum

```
MFCC 는 Spectrum이 아닌 Mel Spectrum에서 Cepstral 분석으로 추출
사람의 청각기관은 고주파수 보다 저주파수 대역에서 더 민감하다.

멜 스케일 (Mel Scale) : 이러한 특성을 반영해서 물리적인 주파수와 실제 사람이 인식하는 주파수 관계를 표현
    -> https://en.wikipedia.org/wiki/Mel_scale

Mel Scale에 기반한 Filter Bank를 Spectrum에 적용하여 도출해낸 것이 Mel Spectrum

-> 사람 청각기관의 특성을 반영해 최종적으로 얻어낸 Mel Spectrum에서 Cepstral 분석을 수행해 MFCC를 추출한다.
```

> FFT(Fast Fourier Transform : 고속 푸리에 변환)

```
신호를 주파수 성분으로 변환하는 알고리즘으로, 기존의 이산 푸리에 변환(DFT)을 더욱 빠르게 수행할 수 있도록 최적화한 알고리즘.
```

> 포먼트(Formants)

```
소리가 공명되는 특정 주파수 대역.

사람의 음성은 성대(vocal folds)에서 형성되어 성도(vocal track)를 거치며 변형되는데,
소리는 성도를 지나면서 포먼트를 만나 증폭되거나 감쇠됩니다.

즉, 포먼트는 배음(harmonics)과 만나 소리를 풍성하게 혹은 선명하게 만드는 필터 역할을 합니다.
```

> 배음(harmonics) 구조

```
소리는 한 가지의 주파수만으로 구성되지 않습니다.
기본 주파수(fundamental frequency)와 함께 기본 주파수의 정수배인 배음(harmonics)들로 구성됩니다.

예를 들어 우리가 피아노 건반에서 4옥타브 '라'(440Hz) 음을 연주했다면 
그 소리는 기본 주파수인 440Hz뿐만 아니라 그 정수배인 880Hz, 그리고 그다음 배음들까지 포함하고 있습니다.
```

# 참고 사이트
- http://keunwoochoi.blogspot.com/2016/03/2.html <br>
- https://m.blog.naver.com/mylogic/220988857132 <br>
- https://brightwon.tistory.com/11 <br>
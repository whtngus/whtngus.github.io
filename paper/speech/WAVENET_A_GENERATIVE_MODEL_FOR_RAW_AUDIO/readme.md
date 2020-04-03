# WAVENET_A_GENERATIVE_MODEL_FOR_RAW_AUDIO

#### 메타 정보

- 19 Sep 2016
- google 에서 발표

### - ABSTRACT

```
WaveNet은 원본 음성파형을 생성한는 딥러닝 모델이다.
2016년도 당시 WaveNet을 통하여 TTS sota를 찍음 
```

### 1. INTRODUCTION

<img src="./pic/1_A_second_of_generated_speech.PNG" width="400px" height="200px"></img> <br>
 
```
images (van den Oord et al.,2016a;b) and text (Jozefowicz et al., 2016)에서 아이디어를 얻어 WAVENET을 구상

WAVENET은 음성 생성모델 이고,  PixelCNN (van den Oord et al., 2016a;b)을 기반으로 작성됨  
```

> 해당 논문에서 소개할 내용 <br>

- WaveNet의 음성 신호 생성 모델에 대한 소개 <br>
- 긴 음성 데이터에 대한 처리 방법과 시간 제약 설명 <br>
- 화자분리 음성 데이터 생성 방법 소개 <br>
- 다른 모델과의 결과 비교 (+ 작은 데이터셋에서도 높은 성능을 보여줌)

### 2. WAVENET

- joint probability 수식 <br>

> Xt : 이전 시퀀스(음성)에 대한 timesteps -> 시계열 데이터 <br>

<img src="./pic/수식_1.PNG" width="200px" height="50px"></img> <br>

- model output : categorical distribution 결과를 softmax 씌운  Xt <br>
- optimize : maximize the log-likelihood

#### 2.1 DILATED CAUSAL CONVOLUTIONS

<img src="./pic/그림_2.PNG" width="600px" height="400px"></img> <br>

- 위 그림은 convolution 네트워크를 기반으로 되어 있음. <br>
- 1-D 데이터를 사용하여 연산량이 비교적 적음 ?!? <br>
- convolution network의 경우 시퀀셜한 데이터를 처리하기힘들기 때문에  introduction에서 PixelCNN 을 언급한듯 
- dilated convolutional layers를 사용하여 시퀀셜한 데이터 문제를 해결 

<img src="./pic/그림_3.PNG" width="600px" height="400px"></img> <br>

- 위 그림은 stacked dilated convolutions <br>
- 데이터의 길이에 따라 dilation이 n으로 늘어남 <br>

#### 2.2 SOFTMAX DISTRIBUTIONS

- "van den Oord et al. (2016)"이 MCGSM보다 softmax distribution이 더 효과가 좋다고 함 <br>
MCGSM : mixture of conditional Gaussian scale mixtures <br> 
(픽셀 오디오등 한정된 데이터에서 적용되는걸로 보임) <br>
- categorical distribution 에서 더욱 좋은 교과를 보임

<img src="./pic/수식_2.PNG" width="200px" height="50px"></img> <br>

#### 2.3 GATED ACTIVATION UNITS

<img src="./pic/수식_3.PNG" width="200px" height="50px"></img> <br>

```
동그라미 2개 모양 : 행렬 곱
σ : sigmoid
k : layer index
f : filter
g : gate
W : 학습 convolution filter
```

#### 2.4 RESIDUAL AND SKIP CONNECTIONS

<img src="./pic/그림_4.PNG" width="400px" height="200px"></img> <br>

```
network 에서  residual 과 skip connection을 사용하여 학습 
사진처럼 위의 레이어를 K개를 사용하여 학습 (병럴 수행 가능해보임)
```

#### 2.5 CONDITIONAL WAVENETS

<img src="./pic/수식_4.PNG" width="200px" height="50px"></img> <br>
<img src="./pic/수식_5.PNG" width="200px" height="50px"></img> <br>

```
h : 캐릭터 하나에 대한 잠재 벡터, Speaker의 특성
* : convolution 연산자
K : layer 번호
f : filter
g : gate
V(*,k) : 학습가능한 직성 투영법 -> ??? 
V(f,k)*y : 1*1 convolution
```

### EXPERIMENTS

- MULTI-SPEAKER SPEECH GENERATION <br>
- TEXT-TO-SPEECH <br>
- MUSIC <br>
- SPEECH RECOGNITION <br>



```
오디오 신호의 긴 부분을 처리하고 지역적으로 더 큰 WaveNet을 처리.
더긴 오디오 시간에 상관 관계를 모형화
```

## 관련 지식 

### Skip connection

```
뉴럴넷은  H(x)−y 를 최소화 하는 방향으로 학습을 진행한다.
이때 Skip network 는 
입력과 출력의 잔차를  F(x)=H(x)−x 라고 정의를 하고 네트워크는 이  F(x) 를 찾는 것이다.
최적의 경우  F(x)=0 이 되어야하므로 학습의 목표가 이미 정해져 있기 때문에 학습 속도가 빨라짐.
네트워크가 잔차를 학습하고 나면, 입력값의 작은 변화에도 민감하게 반응한다는 가설
```

### masked convolution

- PixelCNN 논문에서 masked convolution 방법 제안

<img src="./pic/pixcelCNN_1.PNG" width="600px" height="400px"></img> <br>

- 필터를 마스크하기 위해서는 필터의 중심에서 우측과 아래의 가중치를 0 으로 셋팅

```
두가지 masked filter 를 사용
A. 필터의 중심도 가중치를 0 으로 셋팅
B. 필터의 중심의 값을 이용 
-> 이경우 위의 그림처럼 필터의 아래쪽 가중치를 0으로 셋팅해서 사용

A 타입은 첫 컨볼루션 레이어에서만 사용하고 나머지 레이어에서는 B를 이용한다.

- 내가 생각한
B타입처럼 필터의 아래부분 가중치를 0으로 두는 이유
-> CNN은 시계열 데이터를 처리할 수 없다.  -> 이를  처리하기 위해 필터의 아래부분 가중치를 0으로 치환 
ex) 연속된 사진을 붙여놓은 데이터 혹은 음성,NLP 데이터 라고 보면
위의 사진처럼 데이터의
```

- AR model(Autoregressive Model) <br>

<img src="./pic/AR_model.PNG" width="600px" height="300px"></img> <br>

```
현재 시점의 정상 시계열 (ex: 페어 트레이딩의 스프레드)은 이전 시점의 정상 시계열에 상수 (a)를 곱해준 것과 유사하고, 잔차 정도의 차이만 있음을 모형화 한 것이다. 
이 모형을 AR (Autoregressive) 모형이라 하고 (자기회귀모형), 바로 이전 시점 (t-1 시점) 까지만 고려하면 AR(1), 
그 이전 까지 모두 고려해 주면 일반적으로 AR(p) 모형이라 한다.

[출처] 19. AR(1) 모형 (Autoregressive Model)|작성자 아마퀀트
```

### 장단점 정리

```
powerfull 한 generate model

단점 
1. 매우느림 
이유 : auto regresive 모델인데 audio의경우 매우 긴 입력데이터를 기반으로 하기때문에 
2. end-to-end 모델이 아님

```




## 참조
- WAVENET 논문 <br>
https://arxiv.org/pdf/1609.03499.pdf <br>
- pixelcnn 논문 <br>
https://papers.nips.cc/paper/6527-conditional-image-generation-with-pixelcnn-decoders.pdf <br>
- pixelcnn 설명 블로그 <br>
https://tensorflow.blog/2016/11/29/pixelcnn-1601-06759-summary/ <br>
- pixelcnn 설명 블로그  <br>
https://ratsgo.github.io/generative%20model/2018/01/31/AR/ <br>
- AR 모형 설명 블로그 <br>
https://blog.naver.com/PostView.nhn?blogId=chunjein&logNo=100173614389 <br>
- Skip connection 설명 <br>
https://datascienceschool.net/view-notebook/958022040c544257aa7ba88643d6c032/ <br>
- 유튜브 논문 리뷰 <br>
https://www.youtube.com/watch?v=GyQnex_DK2k&feature=youtu.be <br>





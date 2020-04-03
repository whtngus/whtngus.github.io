# Tacotron 

### history 기존 STT 모델들 
- WaveNet(2016) <br>
정리함 <br>
- DeepVoice(2017) <br>
- Char2Wav(2017) <br>

### Tacotron 이란?
Tacotron v2 도 있음 <br>
2017년에 구글에서 공개한 TTS 모델<br>
Encoder-Decoder 구조 <br>


<img src="./pic/그림_1.PNG" width="500px" height="400px"></img> <br>

```
위 그림에서의 CBHG는 아래그림 
     - CBHG
커널 사이즈 1~16까지 16가지 사용 
postNet에서는 1~8까지 8개 사용
    - 위사진 decoder
CBHG에서 mel spectrogram 생성

Atention RNN 은 GRU Cell을 사용
3개의 output중 가장 오른쪽 하나의 spectrogram이 다음 시퀀스의 인풋으로 들어감
```

<img src="./pic/그림_2.PNG" width="500px" height="400px"></img> <br>


### 학습 방법 

- loss

<img src="./pic/로스_1.PNG" width="500px" height="400px"></img> <br>

```
Adam Optimizer 사용  
-> 논문에서는 Learning rate를 순차적으로 줄여 나감
(decay 와 크래핑? 을 사용)

Linear-scale spectrogram 을 만드는걸 최종 목표로 함.
-> mel spectogram을 거친 후에 Linear spectogram을 생성하면 낮은 주파수(400이하)에서 더 좋은 결과가 나옴
```







## 정리 참고 
- 설명 유튜브 <br>
https://www.youtube.com/watch?v=02odSrfgasI
- tacoron paper <br>
https://arxiv.org/pdf/1703.10135.pdf <br>

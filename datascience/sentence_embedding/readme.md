
# 용어 정리

> 특이값 분해(SVD) <br>

<img src="./pic/svd1.PNG" width="350px" height="250px"></img>
```
고유값 분해(eigendecomposition)처럼 행렬을 대각화하는 한 방법
U : AAT를 고유값분해(eigendecomposition)해서 얻어진 직교행렬(orthogonal matrix)로 
    U의 열벡터들을 A의 left singular vector라 부른다. 
V : ATA를 고유값분해해서 얻어진 직교행렬로서 
    V의 열벡터들을 A의 right singular vector라 부른다.
Σ : AAT, ATA를 고유값분해해서 나오는 고유값(eigenvalue)들의 square root를 대각원소로 하는 
    m x n 직사각 대각행렬로 그 대각원소들을 A의 특이값(singular value)이라 부른다.
-> 대칭행렬(symmetric matrix)은 항상 고유값 분해(eigendecomposition)가 가능하며 더구나 직교행렬(orthogonal matrix)로 대각화할 수 있다. 
    그런데, AAT와 ATA는 모두 대칭행렬(symmetric matrix)이므로 위와 같은 고유값 분해가 항상 가능하다. 

==> 이해가 안간다 ㅠㅠ  
그래서 특이값의 기하학적 의미를 보자  <br>

```
<br>
<img src="./pic/svd1.PNG" width="300px" height="250px"></img>
<img src="./pic/svd1.PNG" width="300px" height="250px"></img><br>
```
 A = UΣVT에서 U, V는 직교행렬, Σ는 대각행렬이므로 Ax는 x를 먼저 VT에 의해 회전시킨 후 Σ로 스케일을 변화시키고 다시 U로 회전시키는 것임을 알 수 있다.
 즉, 행렬의 특이값(singular value)이란 이 행렬로 표현되는 선형변환의 스케일 변환을 나타내는 값으로 해석할 수 있다.
 
```

---
> LSA (Latent Semantic Analysis)
```
 입력 데이터에 특이값 분해를 수행해 데이터의 차원수를 줄여, 계산 효율성을 키우는 한편 행간에 숨어 있는 (latent)의미를 이끌어내기 위한 방법론
 행렬(입력 단어, 문장)을 특이값 분해를 수행
 - 효과
 데이터가 클수록 효과가 더 좋음
 새로운 단어가 추가되면 처음부터 작업을 해야 한다.
 -> 새로운 정보에 대해 업데이트가 어렵다.
```
    
---
> Doc2Vec

![PV-DM](./pic/doc-vec.PNG)
```
Doc2Vec : 구글 연구 팀이 개발한 문서 임베딩 기법.
          이전 단어 n개가 주어진 경우 다음 단어를 맞추는 언어 모델

Paragraph Vector : 문서 수 X 임베딩 차원 수 크기를 가지는 문서 행렬
학습이 종료되면 문서 수 X 임베딩 차원 수 크기를 가지는 문서 행렬 D를 각 문서의 임베딩으로 사용
아래는 입력 데이터 예시
```
<img src="./pic/PV_DM1.PNG" width="350px" height="300px"></img>
<img src="./pic/PV_DM2.PNG" width="350px" height="300px"></img><br/>

---


---
## 참조 링크
https://www.slideshare.net/keunbongkwak/pr12-distributed-representations-of-sentences-and-documents <br>
https://darkpgmr.tistory.com/106 -> 특이값 분해 <br>




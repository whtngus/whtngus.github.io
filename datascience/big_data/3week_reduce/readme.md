# 3주차

## MapReduce
> 대용량을 저장하기 위한 시스템  <br>
> 괜찮은 시간안에 모든 데이터를 보고 분석할 수 있음. <br>
> 실시간 (대화형)분석에는 적합하지 않음 <br>
> 한번 쓰고 여러번 읽어들이는 구조에 특화되어 있음 <br>
> 데이터를 처리하는 프로그래밍 모델
- 데이터 처리 방식 
- word count 같은 집계하는 작업에 강함
<img src="./pictures/MapReduce01.PNG" width="350px" height="300px"></img> <br>
```
- 맵(Map) 단계
    분산된 데이터를 키(key)와 값(value)의 리스트로 만드는 단계
    map()는 데이터를 읽어들여 키 값 쌍으로 출력
- 셔플과 정렬(Shuffle and Sort) 단계
    맵 단계에서 나온 중간 결과를 해당 리듀스 함수에 전달하는 단계
    하둡이 수행 위 작업 후 리듀스로 전달
- 리듀스(Reduce) 단계
    전달받은 리스트에서 원하는 데이터를 찾아서 집계하는 단계
    
    
개발자가 직접 정의
1. 맵(Map) 함수
2. 리듀스(Reduce) 함수
-> 분산처리는 하둡을 통해 자동으로

*위 3단계중 부분적으로 사용도 가능*
```

## hadoop
RDMS아 Hadoop시스템의 경계가 모호함.

Computing 변형 과정
1. Grid Computing
2. Clustering Computing
3. Cloud Computing

- split 단위는 블럭단위
- 기본 블럭사이즈는 128MB
- 작은 여러개의 파일을 읽는경우 오히려 더느릴 수 있음

<br>
Lucene 개발자가 개발을 시작 원래 Apache Nutch에서 시작 
(Web Search를 위해서)

<br>
hadoop : 약어가 아니라 직접 만든것 -> 
 아이가 노란 코끼리인형 이름을 hadoop이라고 불러서 그걸 그대로 적용 <br>

- Nutch 프로젝트 진행시 문제점 -> 웹 페이지를 크롤링하고 유지하는데 너무 많은 비용이 듦 

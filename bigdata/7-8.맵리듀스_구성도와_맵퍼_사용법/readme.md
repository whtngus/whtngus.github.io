# 7.맵리듀스_구성도와_맵퍼_사용법

<img src="./pic/맵리듀스구성도01.PNG" width="350px" height="300px"></img> <br>

```
    - 맵리듀스 작동 순서
job 들어옴 -> map -(중간 결과 shuffle 후 전달)> reduce -> hdfs(저장) -> map ...(작업 끝날때 까지 반복).. 

위 그림에서는 map이 2개의 컴퓨터에서 실행되고 reduce는 3개의 컴퓨터에서 실해되고 있음
(map 과 reduce는 서로 다른컴퓨터 다른 컴퓨터의 개수에서 수행될 수 있다)
-> 어떤 pc에서 map, reduce 작업을 할지는 hadoop에서 결정을 함
    (어떤 pc에서 작업할지는 사용자는 알 필요가 없음 hadoop에서 관리하기 때문에)

map function 의 (reduce 도 마찬가지)
input : key, value 쌍 
output : key, value 의 리스트 
-> Hadoop 뿐만 아니라 spark에서도  key ,value 형식으로 사용함 
```

> 맵퍼(Mapper)

```
    - mapper
map 은 block 단위로 처리
ex) 워드 두 카운트시 
map  
i am
a ,
boy.
<1, "I am">
<2, "a">
<3, "boy">
key - line number, value - 내용 
여기에서는 key에 의미가 없음 대부분 key에는 의미가 없음 
[<I, 1>, <am,1> , <a,1> , <boy, 1>] reduce로 전달
->
reduce 에서는 key 값으로 소팅 후에 값을 합치는 작업을 함
=> 사용하기 에 따라 key를 의미있게 사용가능 (개발자가 쓰기 나름)
```

> 리듀서(The Reducer)

```
맵 단계가 끝나면 shuffle 후 리듀서로 전송
    - shuffle
맵퍼의 작업이 끝낸걸 reduce로 전송하는 과정
맵퍼(하나의 컴퓨터 안에서일어남으로 메모리 안에서 전부 일어남) - 시간소모가 적음
리듀스 또한 하나의 컴퓨터 안에서 일어남으로 시간 소모가 크지않다 
but shuffle 과정은 메모리에서 빠져나와 다른 reduce로 전달하는 과정이기 때문에 많은 시간을 소모한다.
때문에 shuffle은 개발자가 과연하지 않고 hadoop에서 처리를 함. (분산 처리 자동화)
-> 같은 key 값들은 같은 reducer로 전달을 하기 위해 sort를 함 
(key 값을 hash 함수를 이용하여 같은 key값을 같은 reducer로 전송)
```

> 리듀서 예제

```
각 중간 키 값과 관련있는 모든 것들의 합 
같은 키가 있는 값을 묶어 value들을 하나의 리스트로 묶는다.
합의 경우 리듀스에서 같은 키값을 하나로 만들어 합을 해버림 
```














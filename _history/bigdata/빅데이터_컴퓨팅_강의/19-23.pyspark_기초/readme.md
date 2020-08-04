# 19. Pyspark의 RDD 사용법

> RDD(Resilient Distributed Dataset)

```
    - RDD 란
Resilient : 메모리 내에서 데이터가 손실되는 경우, 다시 생성할 수 있다.
Distributed : 클러스터를 통해 메모리에 분산되어 저장된다.
Dataset : 초기데이터는 파일을 통해 가져올수 있다.
RDD는 스파크에서 기본적인 데이터의 단위

대부분의 스파크프로그래밍은 RDD를 통한 동작으로 구성된다.
```

> RDD를 생성하는 방법

```
    - 텍스트 파일을 이용한 생성
ex)
>newRDD = sc.textFile("text.txt"
>newRDD.count()
4  # <- 텍스트의 라인 단위로 RDD레코드를 생성
    - array로 부터 생성
메모리에 있는 데이터를 통해 생성
> num = [1,2,3,4]
> rdd = sc.parallerize(num)
    - RDD를 통해 생성
# rdd의 map fucntion을 통해 생성  
# map function 사용시 RDD하나씩 넘어가면서 처리를 하게 됨
> newRDD_uc = newRDD.map(lambda line : line.upper())
```

> RDD Operations

```
크게 두가지가 있음
    - Actions
값을 리턴
    - Transformations (중요)
현재의 것에 기초하여 새로운 RDD를 정의한다.
(기존 RDD -> 새로운 RDD)
```

> RDD 함수 : Transformations

```
* RDD는 불변(immutable)
RDD는 내용을 바꿀 수 없어 필요에 따라 데이터를 새로 만들면서 수정해야 함

    - map
map(function) : 주어진 RDD의 각 레코드(라인)별로 기능을 수행하여 새로운 RDD를 생성
가장 기본적인 transformation operator
rdd.map(function...)
ex)
newRDD.map(lambda line:line.upper())

    - filter
filter(function) : 주어진 RDD를 라인(레코드)별로 조건에 맞는 라인으로 새로운 RDD를 생성
조건에 맞는 레코드만 수집하여 새로운 RDD생성
ex)
# T로 시작하는 레코드만 추출한다.
# function 의 결과가 True인경우에만 데이터를 가져오는 방식
newRDD.filter(lambda line : line.startswith('T')) 

    - 그 외에도 다양한 함수가 있음 
```

> Actions 함수

```
Transformations 이 끝난후 결과치를 얻어내기 위한 함수
Transformations함수는 새로운 RDD를 만들어 나가지만 Actions 함수는 값을 반환

    - count
count() : RDD의 요소의 갯수를 반환
ex)
>newRDD = sc.textFile("text.txt")
>newRDD.count()
4

    - take
take(n) : RDD의 첫번째 요소부터 n개의 요소를 리스트로 반환
>newRDD.take(2)
[
    u'Time ~~~~~ ',
    u'The ~~~~~'
]

    - collect
collect(n) : RDD의 모든 요소를 반환 , 모든 레코드를 가져오기 때문에 계산 비용이 비쌈
> newRDD.collect()
[
    ...
] 
 
    - saveAsTextFile
saveAsTextFile(path) : RDD를 파일로 저장
> newRDD.saveAsTextFile("output")
```

> Lazy Execution

```
가장 마지막에 실행됨
RDD의 데이터는 action 함수로 인한 작업을 수행 될 때까지, 처리되지 않음
실제로는 Transformations 작업중에는 RDD가 만들어지지 않음 (비어있는 RDD 공간만 생성)
Action 함수가 호출되는 순간 RDD들이 생성되고 계산시작

마지막에 action을 수행ㅅ 너무 작업이 많이 몰릴 수 있어 
Transformations을 생성하다가 중간중간 action을 취해 작업을 분산시키는 방법도 있음 
```
> Chaining Transformations

```
여러 함수를 한라인에 전부 처리 
>sc.textFile("text.txt").map(~~~).filter(~~).collect()
```

> Passing Named Function

```
python 함수를 통한 호출 가능함
ex)
def toUpper(s):
    return s.upper()

> newRDD = sc.textFile("test.txt")
> newRDD = newRDD(toUpper).take(2)
```

> flatMap

```
flatMap(function) : base RDD의 각 라인별 엘리먼트를 각 엘리먼트 단위로 매핑
> RDD.map(lambda line.line.split()) -> list of list가 만들어지기 때문에 하나의리스트로 풀어줘야할 경우
[ ["The", ~~],
    ~~
]
> RDD.flatMap(lambda line : line.split())
[ "The", ~~ ]
```

> distinct

```
distinct(중복제거)
flatMap 사용시 중복된 내용을 제거 
```

# 20. Spark의 RDD와 Operation(1)

> Spark Context

```
Spark 에서는 driver 와 executers가 있음
worker에서 스파크를 생성함 
(강의에서 지난시간 이라고하는데 .. 녹화에 없는 실습수업에서 한것같음. ㅠㅠㅠ)

    - Partition 개수 변경
repartition(n) : n에 변경하고 싶은 partition 개수를 전달
    - getNumPartitions()
RDD 변수가 몇개의 partitions으로 나누어져 있는지를 알고싶을 때
```

> RDD lineage 와 type 확인

```
    - lineage 확인
> xrangeRDD.toDebugString()

> rangdRDD.toDebugString()
    
    - RDD의 type 확인
> type(xrangeRDD)
> xrangeRDD.id() 
```

> map 함수

<img src="./pic/map_function01.PNG width="350px" height="300px"></img> <br>

```
map function을 적용하여 생긴 RDD의 partition 수는 기존 partition수와 같음
```

# 21. 	Spark 프로그램(Wordcount)

> filter 함수

```
map 함수와의 차이는 모든 데이터에 대해 true인 값들만 유지 
output 은 true or false 만 반환하는 함수여야 함
```

> WordCount

```
WordCount시 필요한 action 함수
- first()
첫 번째 partition의 첫 번쨰 Element 만가져옴
- take(n)
첫 번째 partition부터 n개만큼 반환
- top(n), tail(n)
```

> reduce 함수

```
hadoop의 reduce와 유사하며, reduce 함수의 파라매터로 funtion을 전달
reduce 에 전달한 function은 항상 associative 하고 commutative 해야 함
- associative
ex) a + (b+c) = (a+b) + c
- commutative
ex) a + b = b + A 

=> 
+, * 등은 순서에 상관 없음으로 reduce 사용 가능 *reduce 시에는*
-, / 같은 경우 앞뒤 순서가 바뀌면 값이 바뀜으로 사용 불가능  3 - 4 not equal 4 - 3
-> 파티션을 하면 값의 순서가 바뀌기 때문에 위 속성이 유지되는 연산만 사용 가능하다

    - reduce
argument를 가져와서 연산을 하는 작업
```

> takeSample 함수

```
withReplacement : 중복 허용 여부
num : sample 개수
seed : 값을 줄 경우, 항상 같은 samples 추출 
ex)
>rdd.takeSample(withReplacement=True,num=6)
```

# 22. ReducebyKey vs GroupbyKey

> reduceByKey, GroupByKey

<img src="./pic/reduceByKey.PNG width="350px" height="300px"></img> <br>

```
반드시 Key, Value 가 있어야 사용가능
    - reduceByKey (추천)
같은 node의 같은 key 값 기준으로 values를 미리 병합
shuffling할때, 네트워크의 부하룰 줄여준다.
    - groupByKey(비추천)
특별한 작업 없이 모든 pair데이터들이 key 값을 기준으로 shuffling일어남
네트워크 부하가 많이 생김
out of memory 발생 가능
```

> mapValues

```
> word = sc.parallelize([~~~~], ~~~)
> group = word.groupByKey()
> wc = group.mapValues(list)
특정 변수로 변환
```

# 23. RDD and Operations in Spark(2)

<img src="./pic/reducyByKey_응용.PNG width="350px" height="300px"></img> <br>

```
key 값이 같은걸 묶은 후에 value를 묶는 작업 
단, + * 연산만 가능하면 -,/ 연산은 항상 같은값이 나오지 않음 유의!!!
```

> countByValue <br>

<img src="./pic/countByValue.PNG width="350px" height="300px"></img> <br>

```
key 의 개수를 value로 가져옴
```

> flatMap <br>

<img src="./pic/flatMap.PNG width="350px" height="300px"></img> <br>

```
flatMap 사용 예시
-> 추가로 count를 적용하면 wordCount 완성
```







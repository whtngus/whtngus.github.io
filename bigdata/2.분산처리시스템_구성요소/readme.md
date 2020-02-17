# 2. 분산처리시스템 구성요소

> 분산 처리 시스템의 문제점

```
 - 복잡한 프로그래밍
 데이터와 프로세스의 sync 유지 -> mpi
 - partial failures : 수많은 컴퓨터를 사용하는 경우에 일부의 컴퓨터가 고장나는 경우
 컴퓨턴트의 failure(전체 시스템의 failure가 아닌)는 어플리케이션 성능 저하를 유발함
 (하나의 데이터당 3개의 copy를 복사)
```

> 데이터 Recoverability

```
빅데이터의 storage 와 cpu 가 있음
storage가 고장난 경우 다른 storage에서 복구 가능 

    - 데이터가 없어진 경우 복구가 가능하다.
    - 전체 시스탬의 재 시작 없이 수행
    - Consistency
job이 수행되는 동안 컴포넌트의 failure는 결과에 영향을 주지 않아야 한다.
    - Scalability
데이터의 양이 증가하면, 각 작업의 성능이 감소함
시스템의 resource를 증가시키면, 비례적으로 로드 capacity가 증가함
데이터가 많아지면 pc를 더붙여서 성능을 유지할 수 있는 시스템이어야 한다.
-> 데이터 양이 증가함에 따른 시스템 변경할 필요가 없어짐


하둡은 위를 정의하기 위해 
연산, 저장으로 이루어짐
```

> Haddop 의 목적

```
개발자가 아닌 데이터사이언티스트등 다른 직군도 사용할 수 있도록 하는것

    - 애플리케이션을 High-level 코드로 작성
인프라 구조에 대한 고려가 요구되지 않음
    - 각 노드들은 가급적 최소한의 데이터를 주고 받음
데이터를 주고 받는 시간을 절약하기 위하여
개발자는 노드들 사이의 통신에 대한 코드 작성이 필요 없음
`Shared nothing` architecture
    - 데이터는 여러 노드에 미리 분산되어 저장
데이터가 저장된 위치에서 연산을 수행
```

> Haddop : Very High-Lvel Overview

```
    - 시스템이 데이터를 로드할 때 'block'으로 나누어짐
기본적으로 64MB 또는 128MB 크기를 사용
    - 계산은 Map tasks(MapReduce 시스템의 첫 번재 파트)는 single block 단위의 작업을 처리
MapReduce 중  Map tasks
    - 마스터 프로그램은 분산되어 저장된 데이터의 block에 대한 Map task 작업을 각 노드에 할당
```

> Fault Tolerance

```
    - Node 가 fail한 경우, master node는 failure를 감지하고 작업을 다른 node에 할당
    - Task를 재 시작 하는 것은 다른 부분에 대한 작업을 수행중인 다른 노드와의 통신을 필요 하지 않음
    - Fail된 node를 재 시작 하는 경우, 자동적으로 시스템이 연결되어 새로운 task를 할당함
    - 특정 Node의 성능이 매우 낮은 것으로 감지되면, master node는 같은 task를 다른 node에 할당
```
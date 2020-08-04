# 05 추천 시스템

### Contents based Filtering

- Contents based Filtering 개념 <br>
> 아이템이나 유저의 컨텐츠 자체를 분석하여 비슷한 아이템을 추천 <br>
> 많은 양의 유저의 액션을 요구하지 않음 <br>
> 컨텐츠의 타입과 양에 따라 적용 가능 여부가 결정됨, 가능하다면 비슷한 아이템끼리만 추천 <br>

- Contents baed Filtering 예시 <br>
> 웹 페이지(TF-IDF), 음악, 사용자 , 상황 <br>

### Collaborative filtering 

- Collaborative filtering 개념 <br>
> 아이템이나 유저의 유사도를 모델링하고 측정하여 추천 <br>
> 복잡하고 많은 아이템을 어렵게 분석하지 않아도 되는 장점 <br>
> 성능이 매우 좋음 <br>

- Collaborative filtering 한계 <br>
> Cold Start : 처음에 수집 정보(아이템, 유저)가 없어서 모델 학습 불가 <br>
> Scalability : 데이터가 커져서 메모리를 많이 사용 <br>
> Sparseness : 사용자 정보가 붖고할 때 평가가 어려움 <br>
> Popularity bias : 대다수의 사람을 따라가게됨 <br>

- 두 가지 방식이 존재 

1. User-based

```
유저간의 행위를 분석하여 이를 기반으로 유저간 유사도를 추천
```

2. Item-based 

```
아이템간의 유사도를 측정
유저가 어떤 아이템을 선호하면 유사한 다른 아이템을 추천
```













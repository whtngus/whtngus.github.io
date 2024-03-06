---
layout: post
title: "MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL"
date: 2024-03-06 02:05:23 +0900
category: paper
---

MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL
2024년 2월 15일 

buaa 대학교, 텐센트



url : https://arxiv.org/abs/2312.11242

git url : https://github.com/wbbeyourself/mac-sql



# Abstract

최근 LLM 모델 기반의 Text-to-SQL 방법이 좋은 성능을 보이지만 엄청난 연산량을 필요로 하는 문제가 있음

그리고 LLM에 대한 내용은 도외시 하는 경우가 있음 

해당 연구에서는 multi-agent collaborative 프레임워크인 MAC-SQL 모델을 제안함



MAC-SQL은 few-shot chain-of-thought reasoning 방법을 사용함 



GPT-4를 백본으로 둬서 강력한 성능을 보여주지만 해당 연구에서는 SQL-Llama, Code Llama 7B 모델을 이용해서 사용하는 방법도 제안함 -> 7B면 해볼만 할거같은데 

SQL-Llama는 accuracy가 43.94  baseline으로 사용하는 chatgpt-4 가 46.94임 

해당 연구에서는 sota 스코어를 달성했다고 함 

# 1 Introduction

Text-to-SQL은 자연어 질문을 입력 받아 SQL을 자동으로 생성하는것을 목적으로 함 

지난 10년간 3가지 단계를 거쳐 연구됨 ㅠ

1. 입력 텍스트를 임베딩
2. sql decode로 추상 sql 트리 구문 생성 
3. sql 쿼리 생성



최근에는 seq-2-seq 방식을 사용함 -> 최근 LLM을 이용해서 성능이 매우 상승함을 보임 

최근 LLM based 방법론들은 상황에 맞는 프롬프트 전략과 타겟 도메인 데이터를 이용한 fine-tuning 에 집중함 

![f_1](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\f_1.png)

Figure 1 은 multi step reasoning 예시 

MAC-SQL는 LLM-based multi-agent collaborative framework에서 Decomposer(generator)를 통해 효과적인 text-to-sql 파싱을 지원함 

2개의 보조 agent인 Selector와 Refiner를 사용함 

selector는 sub database 를 최소화 시키고 refiner는 decomposer에게 피드백을 줌 

추가로 해당 연구에서 7b 모델을 fine tuning 한 SQL-Llama 를 제안 

# 2 Task Formulation and Annotations

![f1](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\f1.png)

Q : 입력 질문 

S : 데이터베이스 스키마  {T, C ,R}로 정의됨 

Y : 생성된 sql 쿼리 

K : 추가 정보 (선택)

T: Tables

C: Columns

R : foreign key  관계 정보 

f (· | θ)은 모델의 파라미터 



![a_1](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\a_1.png)

```
입력은 : 질문, db, kg

간단한 질문이면 바로 db 추출 해서 사용
아닌경우 dbrepresentation을 통해 추출
```



# 3 Methodology

## 3.1 Overview

![f_2](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\f_2.png)

위의 figure 2와 같은 흐름을 탐 

selector 와 refiner의 반복을 통해 개선작업을 함 

## 3.2 Selector

![f_3](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\f_3.png)

거대한 db에서 작은 sub database로 대상 대상을 줄이는 작업을 함 

관련있는 테이블과 컬럼을 추출 

-> 무관한 정보를 지우는것에 중점을 둠 (LLM 질문 쿼리시 대화 텍스트를 초과하는것을 막기 위함 )



=> 여기에서도 chatgpt를 사용 

figure3 는 selector agent 프롬프트를 보여줌 

1. 사용자 질문과 지식을 바탕으로 관련 없는 테이블 스키마를 버림 
2. 관련 테이블 내의 컬럼을 관령성 높은 순으로 상위6개만 정렬하여 유지
3. 최종 출력에 최소 3개의 테이블이 유지되도록 함 
4. 출력은 json형식으로 제공

사용 비사용은 keep_all, drop_all을 통해 사용



BIRD 데이터셋을 통해 코드를 제공한다고 함 

## 3.3 Decomposer

![f_4](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\f_4.png)

db를 단순화 시켰으면 복잡한 사용자 질문을 단순한 자연어 서브쿼리 쿼리 질문으로 변경하여 사용

-> 복잡한 질문을 처리하기 위해 SQL 을 생성하는 어려움을 해결하기 위함

질문을 분해해 점진적으로 처리하여 확인



질문 난이도를 동적으로 판단하여 질문이 단순한 경우 바로 sql 생성

아닌 경우에는 chain-of-thought (CoT) prompting 방법으로  서브-문제로 시작해 점차적으로 분해해서 사용함 



## 3.4 Refiner

![f_5](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\f_5.png)

SQL 쿼리의 오류를 감지하고 자동으로 수정 

-> query 수정도 가능해보임 

1. SQL 쿼리가 실행되어 오류가 발생하면, Refiner는 오류 피드백 정보 또는 수정 가이드 신호를 기반으로 원본 SQL과 추론하여 수정된 결과를 생성
2. 수정된 결과는 다시 평가되며, 문제가 지속될 경우 이 과정은 결과가 정확하거나 최대 수정 횟수에 도달할 때까지 반복

# 4 Instruction-tuned SQL-Llama

gpt-4와 같은 황경을 사용하지 못하는 폐쇄 환경의 경우를 위해 

데이터베이스 단순화, 질문 분해, SQL 생성, SQL 수정 능력을 강화하기 위해 SQL-Llama를 개발함 (Code Llama 7B 기반)

# 5 Experiments

해당 논문에서는 Spider dataset과 BIRD데이터셋을 사용 

- Spider

7000, 1034개의 학습 평가를 위한  질문 sql 셋 



200개의 databse 와 138개의 도메인을 포함함 

- BIRD

Alibaba DAMO Academy 에서 large scare database를 만들어서 공개함

95개의 db와 높은 수준의 text-sql 셋을 제공 (33.4gb 수준)

37개의 전문적은 도매인을 포함함 

### BIRD Results

exact match accuracy (EM) :  EM은 모델이 생성한 SQL 쿼리가 정답 SQL 쿼리와 정확히 일치하는 비율

valid efficiency score(VES) : 예측된 SQL 쿼리가 정답과 동일한 결과를 반환하는 경우의 비율 + 효용성까지 같이 봄 (계산 방식은 쿼리길이와 복잡성, 실행 시간, 리소스 사용량등을 보며 자세한 내용은 모르겠음)

Execution Accuracy(EX) : SQL 쿼리를 실행했을 때, 그 결과가 정답 쿼리의 실행 결과와 일치하는 비율



![t_1](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\t_1.png)

### Spider Results

![t_3](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\t_3.png)



난이도가 높아도 40 은 나오는걸 볼 수 잇음 

![f_6](\img\2024\MAC-SQL_A_Multi-Agent_Collaborative_Framework_for_Text-to-SQL\f_6.png)





# ChatGPT를 이용한 데이터 예시 

#### Spider

```
질문: "각 학교에서 제공하는 모든 과정의 수를 계산하세요."
데이터베이스 스키마 예시:

  - simple
질문: "모든 고객의 이름을 나열하세요."
데이터베이스 스키마 예시:
- 정답
SELECT Name FROM Customers;

   - moderate
질문: "2010년 이후에 개봉한 모든 영화의 제목과 개봉 연도를 나열하세요."
데이터베이스 스키마 예시:

Movies: MovieID, Title, ReleaseYear
- 정답
SELECT Title, ReleaseYear FROM Movies WHERE ReleaseYear > 2010;

    - complex
   
질문: "각 카테고리별로 평균 가격이 가장 높은 제품의 이름과 가격을 나열하세요."
데이터베이스 스키마 예시:

Products: ProductID, Name, Price, CategoryID
Categories: CategoryID, CategoryName

- 정답
SELECT P.Name, P.Price, C.CategoryName
FROM Products P
JOIN Categories C ON P.CategoryID = C.CategoryID
WHERE P.Price IN (
    SELECT MAX(Price) 
    FROM Products 
    WHERE CategoryID = P.CategoryID
    GROUP BY CategoryID
);

```

### BIRD 

복잡한 질문을 많이 한다고 함 

난이도 구분은 없지만 집계 함수와 조인조건을 사용하는 질문도 많이 있다고함 

```
질문: "2019년에 출시된 모든 영화의 이름과 감독을 나열하세요."
데이터베이스 스키마 예시:

Movie: Movie_ID, Title, Release_Year
Director: Director_ID, Name
Movie_Director: Movie_ID, Director_ID

- 정답
SELECT Movie.Title, Director.Name 
FROM Movie JOIN Movie_Director ON Movie.Movie_ID = Movie_Director.Movie_ID 
JOIN Director ON Movie_Director.Director_ID = Director.Director_ID 
WHERE Movie.Release_Year = 2019;

```





# 참고 

- BIRD-SQL(A Big Bench for Large-Scale Database Grounded Text-to-SQLs)

BiRD NL-to-SQL 데이터셋은 홍콩 대학교와 알리바바가 제안한 대규모의 크로스 도메인 데이터셋으로, 자연어 질문을 SQL 쿼리로 변환할 수 있는 모델의 개발을 지원하기 위해 설계되었습니다. 이 데이터셋은 12,751개 이상의 고유한 질문-SQL 쌍을 포함하며, 95개의 대형 데이터베이스를 포괄하는데, 이 데이터베이스들의 총 크기는 33.4GB에 달합니다. 블록체인, 하키, 헬스케어, 교육 등 37개 이상의 전문 도메인을 아우르는 것으로, 의미 분석 및 데이터베이스에 대한 자연어 인터페이스 분야의 연구 및 개발을 위한 가장 포괄적인 자원 중 하나입니다.

링크 : https://github.com/eosphoros-ai/Awesome-Text2SQL




















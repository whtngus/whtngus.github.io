## 1.	엘라스틱서치 기본 개념 정리
<img src="./pic/1-1.PNG" width="300px" height="300px"></img> 
<img src="./pic/1-2.PNG" width="300px" height="300px"></img> <br>
```
엘라스틱 서치는 text – document 형식으로 데이터를 저장 
(Relation DB 의 경우 구조를 직접 하나씩 접근해야 함) 
 엘라스틱 서치가 더 빠름 (데이터 검색 시 Relation db는 하나씩 접속해서 확을 해야함)
구조
Index > Type > Document Field > Mapping
또한 ElasticSearch는 lastAPI를 사용
```

## 2. 데이터 PUT, POST, PUT, DELETE
<img src="./pic/2-1.PNG" width="300px" height="300px"></img> <br>

> 데이터 읽는 경우 
> Ex)  /indexname
> curl –XGET http://localhost:9200/classes?pretty
```
{
  "error" : {
    "root_cause" : [
      {
        "type" : "index_not_found_exception",
        "reason" : "no such index [classes]",
        "resource.type" : "index_or_alias",
        "resource.id" : "classes",
        "index_uuid" : "_na_",
        "index" : "classes"
      }
    ],
    "type" : "index_not_found_exception",
    "reason" : "no such index [classes]",
    "resource.type" : "index_or_alias",
    "resource.id" : "classes",
    "index_uuid" : "_na_",
    "index" : "classes"
  },
  "status" : 404
}
```
> curl -XPUT http://localhost:9200/classes?pretty  
> index 생성 
```
{
  "acknowledged" : true,
  "shards_acknowledged" : true,
  "index" : "classes"
}
```
> curl -XDELETE http://localhost:9200/classes?pretty <br>
> 인덱스 삭제
```
{
  "acknowledged" : true
}
```
> document 생성 <br>
> index가 없는경우에도 가능 
```
curl -XPOST http://localhost:9200/classes/class/1/ -d '
{ "title" : "Algorithm","professor":"John"}' 

-> 에러 발생
"error":"Content-Type header [application/x-www-form-urlencoded] is not supported","status":406}
=> 명령어 끝에 아래 라인 삽입 
-H 'Content-Type: application/json'
ex) 
curl -XPOST http://localhost:9200/classes/class/1/ -d '
{ "title" : "Algorithm","professor":"John"}' -H 'Content-Type: application/json'

{"_index":"classes","_type":"class","_id":"1","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
```
> 파일을 이용하여 document 생성
```
curl -XPOST http://localhost:9200/classes/class/1/ -d '
@~~~.json' -H 'Content-Type: application/json'
위 ~~~.json 에 삽입할 json 파일명으로 사입 가능
```

## 3. update
> 업데이트 할 도큐먼트 생성
```
curl -XPOST http://localhost:9200/classes/class/1/ -d '
{"title":"Algorithm","pofessor":"John"}'  -H 'Content-Type: application/json'
```
> GET으로 확인 
```
curl –XGET http://localhost:9200/classes/class/1/?pretty
```
> update 하기
```
curl -XPOST http://localhost:9200/classes/class/1/_update -d '
{"doc":{"unit":2}}'   -H 'Content-Type: application/json'
-> 수정 왔다갔다하면서 테스트해보기 

curl -XPOST http://localhost:9200/classes/class/1/_update -d '
```
{"script":"ctx._source.unit += 5"}'   -H 'Content-Type: application/json'

## 4. 벌크 (Bulk)
> BULK POST 
> 여러개의 도큐먼트를 한번에 엘라스틱서치로 삽입
```
데이터 링크 : https://github.com/minsuk-heo/BigData/tree/master/
curl -XPOST http://localhost:9200/_bulk?pretty --data-binary @classes.json  -H 'Content-Type: application/json'
```

## 5. 매핑(Mapping)
> 데이터를 매핑 없이 넣는것은 상당히 위험 
> 타입을 잘 지정해야 키바나 사용시 시각화가 가능
```
매핑 예시 

{
	"class" : {
		"properties" : {
			"title" : {
				"type" : "string"
			},
			"professor" : {
				"type" : "string"
			},
			"major" : {
				"type" : "string"
			},
			"semester" : {
				"type" : "string"
			},
			"student_count" : {
				"type" : "integer"
			},
			"unit" : {
				"type" : "integer"
			},
			"rating" : {
				"type" : "integer"
			},
			"submit_date" : {
				"type" : "date",
				"format" : "yyyy-MM-dd"
			},
			"school_location" : {
				"type" : "geo_point"
			}
		}
	}
}

geo_point, date 등 여러가지 자료형 제공 
먼저 인덱스 생성
curl -XPUT http://localhost:9200/classes?pretty  
매핑 추가하기 
curl -XPUT http://localhost:9200/classes/class/_mapping?pretty -d @mapping.json  -H 'Content-Type: application/json'
```
## 6. SEARCH
```
데이터 다운받아 삽입하기
https://github.com/minsuk-heo/BigData/ch03
에서 데이터 다운받기 
- 도큐먼트 삽입 bulk 를 사용
 curl -XPOST 'localhost:9200/_bulk?pretty' --data-binary @simple_basketball.json -H 'Content-Type: application/json'
 - 검색 
 curl -XGET localhost:9200/basketball/record/_search?pretty
  points = 30인 쿼리 
 curl -XGET 'localhost:9200/basketball/record/_search?q=points:30&pretty'
  request body 를 이용한 query
 curl -XGET localhost:9200/basketball/record/_search?pretty -d '
 {
    "query" : {
        "term" : { "points" : 30}
   }
 }'  -H 'Content-Type: application/json'
```
## 7. Metric Aggregation
```
최소 평균 값등을 구할경우 사용 
데이터 다운받아 삽입하기
https://github.com/minsuk-heo/BigData/ch03
- 데이터 삽입
curl -XPOST 'localhost:9200/_bulk?pretty' --data-binary @simple_basketball.json  -H 'Content-Type: application/json'
- 평균을 구하는 어그리게이션 json 생성 
{
        "size" : 0,
        "aggs" : {  # aggs : Aggregation 
                "avg_score" : {
                        "avg" : { # 평균값 명시 
                                "field" : "points" # 필드 명시
                        }
                }
        }
}
- 생성한 json을 사용 
curl -XGET localhost:9200/_search?pretty --data-binary @avg_points_aggs.json  -H 'Content-Type: application/json'
- 최대 최소도 가능 
{
        "size" : 0,
        "aggs" : {
                "max_score" : {
                        "max" : {
                                "field" : "points"
                        }
                }
        }
}
curl -XGET localhost:9200/_search?pretty --data-binary @avg_points_aggs.json  -H 'Content-Type: application/json'

-> 이런 결과들을 한번에 받기 
{
        "size" : 0,
        "aggs" : {
                "stats_score" : {
                        "stats" : {
                                "field" : "points"
                        }
                }
        }
}
curl -XGET localhost:9200/_search?pretty --data-binary @stats_points_aggs.json  -H 'Content-Type: application/json'
-> 쿼리 결과 
{
  "took" : 3,
  "timed_out" : false,
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 26,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "aggregations" : {
    "stats_score" : {
      "count" : 2,
      "min" : 20.0,
      "max" : 30.0,
      "avg" : 25.0,
      "sum" : 50.0
    }
  }
}
```
## 8. Bucket Aggregation
```
Aggregation : elasticsearch 에서 가지고 있는값의 산술 값을 구하기 위해 사용
Bucket Aggregation : group by 의 역할을 함 
- 예제를 실행하기 위한 도큐먼트 삽입
curl -XPOST 'localhost:9200/_bulk?pretty' --data-binary @simple_basketball.json  -H 'Content-Type: application/json'
- 매핑 넣어주기 
{
        "record" : {
                "properties" : {
                        "team" : {
                                "type" : "string",
                                "fielddata" : true
                        },
                        "name" : {
                                "type" : "string",
                                "fielddata" : true
                        },
                        "points" : {
                                "type" : "long"
                        },
                        "rebounds" : {
                                "type" : "long"
                        },
                        "assists" : {
                                "type" : "long"
                        },
                        "blocks" : {
                                "type" : "long"
                        },
                        "submit_date" : {
                                "type" : "date",
                                "format" : "yyyy-MM-dd"
                        }
                }
        }
}
curl -XPUT 'localhost:9200/basketball/record/_mapping?pretty' -d @basketball_mapping.json -H 'Content-Type: application/json'
->에러 발생 json 버전차이 다음과 같이 String 을 텍스트로 변경후 명령어 실행
{
        "record" : {
                "properties" : {
                        "team" : {
                                "type" : "text",
                                "fielddata" : true
                        },
                        "name" : {
                                "type" : "text",
                                "fielddata" : true
                        },
                        "points" : {
                                "type" : "long"
                        },
                        "rebounds" : {
                                "type" : "long"
                        },
                        "assists" : {
                                "type" : "long"
                        },
                        "blocks" : {
                                "type" : "long"
                        },
                        "submit_date" : {
                                "type" : "date",
                                "format" : "yyyy-MM-dd"
                        }
                }
        }
}
-> 실행스크립트에 include_type_name=true 추가 필요 
curl -XPUT 'localhost:9200/basketball/record/_mapping?include_type_name=true&pretty' -d @basketball_mapping.json -H 'Content-Type: application/json'
curl -XPUT 'localhost:9200/basketball/record/_mapping?pretty' -d @basketball_mapping.json -H 'Content-Type: application/json'
=> 에러나서 json 파일에서 submit_date 삭제하고 위 명령어 실행

- 팀 데이터 삽입 
curl -XPOST 'localhost:9200/_bulk?pretty' --data-binary @twoteam_basketball.json  -H 'Content-Type: application/json'
- term aggregation
{
        "size" : 0, # 어그리게이션 정보만을 보기 위해서 
        "aggs" : { # aggs : 어그리게이션 약어 
                "players" : { # 어그리게이션 네임 설정
                        "terms" : { # terms aggregation
                                "field" : "team" # 필드 설정
                        }
                }
        }
}

curl -XPOST 'localhost:9200/_search?pretty' --data-binary @terms_aggs.json  -H 'Content-Type: application/json'
-> 결과 내용
{
  "took" : 850,
  "timed_out" : false,
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 28,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "aggregations" : {
    "players" : {
      "doc_count_error_upper_bound" : 0,
      "sum_other_doc_count" : 0,
      "buckets" : [
        {
          "key" : "chicago",
          "doc_count" : 2
        },
        {
          "key" : "la",
          "doc_count" : 2
        }
      ]
    }
  }
}

==> 팀별 카운트 밖에 나오지 않아 좀더 자세한 분석해 보기 
팀 분류후 팀별 성적 보기 
{
        "size" : 0,
        "aggs" : { # bucget aggregation은 sub aggregation을 포함할 수 있음 
                "team_stats" : {
                        "terms" : { # team aggregation 팀별로 데이터를 묶음
                                "field" : "team"
                        },
                        "aggs" : { # sub aggregation
                                "stats_score" : { # 점수별 stats를 표시 
                                        "stats" : {
                                                "field" : "points"
                                        }
                                }
                        }
                }
        }
}
 curl -XPOST 'localhost:9200/_search?pretty' --data-binary @stats_by_team.json  -H 'Content-Type: application/json'
 --> 결과 팀별 결과가 보임
 {
  "took" : 8,
  "timed_out" : false,
  "_shards" : {
    "total" : 2,
    "successful" : 2,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 28,
      "relation" : "eq"
    },
    "max_score" : null,
    "hits" : [ ]
  },
  "aggregations" : {
    "team_stats" : {
      "doc_count_error_upper_bound" : 0,
      "sum_other_doc_count" : 0,
      "buckets" : [
        {
          "key" : "chicago",
          "doc_count" : 2,
          "stats_score" : {
            "count" : 2,
            "min" : 20.0,
            "max" : 30.0,
            "avg" : 25.0,
            "sum" : 50.0
          }
        },
        {
          "key" : "la",
          "doc_count" : 2,
          "stats_score" : {
            "count" : 2,
            "min" : 30.0,
            "max" : 40.0,
            "avg" : 35.0,
            "sum" : 70.0
          }
        }
      ]
    }
  }
}
```

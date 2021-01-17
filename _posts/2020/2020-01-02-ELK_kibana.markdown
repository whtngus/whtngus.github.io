---
layout: post
title:  "3. kibana"
date:   2020-08-04 19:31:29 +0900
categories: ELK
---

# 3. 키바나 (Kibana)

## 1. Kibana setup & install
```
참조 사이트 
- https://www.elastic.co/guide/en/kibana/current/targz.html
- 명령어 
curl -O https://artifacts.elastic.co/downloads/kibana/kibana-7.5.2-linux-x86_64.tar.gz
curl https://artifacts.elastic.co/downloads/kibana/kibana-7.5.2-linux-x86_64.tar.gz.sha512 | shasum -a 512 -c - 
tar -xzf kibana-7.5.2-linux-x86_64.tar.gz
cd kibana-7.5.2-linux-x86_64/
(단, 관리자권한으로 실행시 실행 안됨)
- 설정 파일변경
vim "다운받은 설치 드렉토리"/config/kibana.yml
# 주석 해제 
server.port: 5601
elasticsearch.hosts: ["http://localhost:9200"]
server.host: "localhost"
server.name: "kibana"
-> elastic search 서버와 같은 서버인걸 명시해주는 역할
- 실행
해당 위치에서 
bin/kibana --allow-root &

- 접속확인 
localhost:5601
=====
엘라스틱서치도 셋팅 필요
/etc/
network.host: ["127.0.0.1"]

* root 권한으로 실행하려면  --allow-root 커멘드 붙이기 
```

### 키바나 실행시 에러 

> error log 
```
error  [08:00:17.191] [error][reporting] Error: Failed to launch chrome!
[0216/080017.099506:WARNING:resource_bundle.cc(358)] locale_file_path.empty() for locale
[0216/080017.099878:ERROR:zygote_host_impl_linux.cc(89)] Running as root without --no-sandbox is not supported. See https://crbug.com/638180.
TROUBLESHOOTING: https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md
```

> 해결 

```
예상 원인
1. elasticserch 와 kibana의 버전 상이
버전 동일하게 맞췄으나 동일이슈 발생
2. 부족한 라이브러리 설치
apt-get install -y libxtst6 libnss3 libnspr4 libxss1 libasound2 libatk-bridge2.0-0 libgtk-3-0 libgdk-pixbuf2.0-0
동일이슈 발생
3. --allow-root를 해도 루트권한에서는 실행이 안된다고 가정
계정생성하여 권한을 주고 실행하였으나 같은 에러 발생
4. 
```


## 2. Kibana management
```
elasticsaerch에 document insert
해당 github의 데이터 insert
https://github.com/minsuk-heo/BigData/archive/master.zip
- 기존에 있을수도 있으니 삭제후 다시 삽입
curl -XDELETE localhost:9200/basketball?pretty
curl -XPUT localhost:9200/basketball
# 데이터 타입 지정 -> kibana 에서 사용할 수 있도록 
curl -XPUT localhost':9200/basketball/record/_mapping?include_type_name=true&pretty' -d @basketball_mapping.json -H 'Content-Type: application/json'
# 값 삽입
아래 에러 발생 
```
<img src="/img/elk/bulk_error_01.PNG" width="500px" height="300px"></img> <br>
```
값 삽입시 아래 명령어로 해결 


-- java version 변경
update-alternatives --config java
```

```
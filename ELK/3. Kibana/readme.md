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
elasticsearch.hosts: ["http://localhost:9200"]
server.host: "localhost"
-> elastic search 서버와 같은 서버인걸 명시해주는 역할
- 실행
해당 위치에서 
./bin/kibana


=====
엘라스틱서치도 셋팅 필요
/etc/
network.host: ["127.0.0.1"]

* root 권한으로 실행하려면  --allow-root 커멘드 붙이기 



```
# HDFS 사용법

> 가상환경 설치

```
강의에서는 VirtualBox를 사용하나 펴난 사용을 위해 도커를 사용
os : Ubuntu 18.04.3 LTS
```

> cloudera

```
Haddop을 distribution을 위한 프로그램
설치 필요 
설치방법 따로 찾음 

    - Hadoop 을 바로 설치하자 ! (검색해봤더니 복잡해서)
https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
- java 설치 (따로 안적음  /skku/big_data/ 에 이미 정리함
export JAVA_HOME=/usr/java/latest
- sshd를 설치
apt install -y openssh-server
apt install -y pdsh
- 하둡 다운로드
https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.1.3/hadoop-3.1.3.tar.gz
- 다운 받은후 /usr/local/hadoop 으로 이동
-  /etc/profile 에 환경 변수를 설정
export HADOOP_HOME=/usr/local/hadoop
export JAVA_HOME=/usr/local/java
export PATH=$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$PATH
export CLASSPATH=$JAVA_HOME/lib:$CLASSPATH
- 다운받은 hadoop/etc/hadoop 디렉토리로 이동 
```
<img src="./pictures/hadoop_etc.PNG" width="350px" height="300px"></img> <br>
```
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
- 하둡 환경설정
export HADOOP_HOME=/usr/local/hadoop
export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export YARN_CONF_DIR=$HADOOP_HOME/etc/hadoop
```



> hdfs 사용하기

```
HDFS ~~  -> 하둡 파일시스템을 사용
    - 디렉토리 보기
hadoop fs -ls /   -> HDFS안에 root디렉토리의 내용을 볼 수 있다.
    - 파일 HDFS로 주고받기
put, get 명령어를 사용 
ex)
hadoop fs -put abc  /usr/trainig/abc
```


> 설정 참조

```
https://m.blog.naver.com/PostView.nhn?blogId=twilight_teatime&logNo=221204194684&proxyReferer=https%3A%2F%2Fwww.google.com%2F
```

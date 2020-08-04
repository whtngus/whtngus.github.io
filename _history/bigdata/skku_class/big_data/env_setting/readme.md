# HADOOP 설치 
### jdk 설치
sudo apt-get update 
sudo apt-get install openjdk-8-jdk
### hadoop 설치
 wget http://apache.mirror.cdnetworks.com/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz
 tar -xzvf hadoop-3.2.1.tar.gz
 sudo mv hadoop-3.2.1 /usr/local/hadoop
### hadoop 환경 설정
```
     vim /etc/environment       (편집)
PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/local/hadoop/bin:/usr/local/hadoop/sbin"
JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64/jre/"

     ./bashrc  (가장 하단에 추가)
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
export HADOOP_HOME=/usr/local/hadoop
export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin
     
```

# Spark 설치
```
wget http://apache.mirror.cdnetworks.com/spark/spark-3.0.0-preview2/spark-3.0.0-preview2-bin-hadoop3.2.tgz
tar -xvzf spark-3.0.0-preview2-bin-hadoop3.2.tgz
cd spark-3.0.0-preview2-bin-hadoop3.2/bin/
    - spark 실행
./spark-shell
```

> PySpark 설치하기

```
    - python3 우선 설치
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ sudo pip3 install --upgrade pip
    - pyspark 설치
$ pip3 install pyspark --user
$ sudo apt-get -y install ipython3 
    - ipython 실행 후 pyspark 실행해 보기
$ ipython3
In [1]: import pyspark
In [2]: pyspark.__version__
Out[2]: '2.4.4'
```


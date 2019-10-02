# GCP 사용 방법 정리 

## FTP 접속 설정하기
- setting의 ftp_ssh 참조 

## 사용 목표  TPU를 사용한 학습 

1. vm생성 (인스턴스)
2. 기본 설정 (도커 및 파이썬 등)
>> centos_TPU/centos_gcp_setup.sh 실행 <br>
>> 실행 인자중 docker pull은 자신의 설정에 맞게 바꾸기
3. TPU 설정하기 
>> 1. GCP의 좌측 매뉴바의 Compute Engine 클릭 <br>
>> 2. VM인스턴스의 영역 확인하기 (TPU 생성식 영역이 같아야 한다)
>> 3. 좌측 Compute Engine 메뉴바의 TPU 클릭
>> 4. TPU 노드 만들기 클릭 <br>
>> 5. TPU 설정 옵션
>>>> 이름 : tpu 이름 설정<br>
>>>> 영역 : tpu z컴퓨팅 리소스와 데이터를 사용할 위치 -> 인스턴스와 같은 위치로<br> 
>>>> TPU 유형 : TPU 하드웨어 선택 <br>
>>>> TPU 소프트웨어 버전 : 참조 https://cloud.google.com/tpu/docs/supported-versions?hl=ko&_ga=2.150387830.-1932111987.1569384840<br>
>>>> 네트워크 : 인스턴스의 네트워크 중 선택 <br>
>>>> IP주소 :  사용할 인스턴스의 ip주소의 네트워크 ip를 입력<br>
>>>> 선점 : 선점박스 체크시  가격이 저렴하나 24시간 연속사용 제한 및 비선점 사용자가 많을경우 빼앗길 수 있음<br>
```
 위 방법 안되서 콘솔 방법으로 변경
 gcp 콘솔 열기
 gcloud config set compute/zone us-central1-c
 gcloud beta compute tpus create demo-tpu --range=10.240.1.0/29 --version=1.13 --network=default
 // Cloud Shell에서 SSH 만들기
 gcloud compute ssh tpu-demo-vm
 //  tpu 이름 설정 쉘에서 설정해줘야 python실행이 됨 
 export TPU_NAME="demo-tpu"
 //gcp tpu 인증하기 
 gcloud auth list
 gcloud auth application-default login
```

## 오류 정리
#### TPU 생성중 오류
PU 노드를 만들지 못했습니다. 오류: Quota limit <br>
--> 영역 선택 다시보자

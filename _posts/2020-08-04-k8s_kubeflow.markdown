---
layout: post
title: "개념 정리"
date: 2020-08-04 19:20:23 +0900
category: k8s and k9s
---

# Kubeflow

kubeflow : kubernetes + ml flow를 합성한 의미

### 특징

1. JupyterLab을 지원한다 <br>
GPU 지원 여부나 텐서플로우 버전등을 쉽게 선택 가능 <br>
2. GPU 드라이버 <br>
GPU 드라이버를 미리 패키징 해둬서 GPU셋팅이 편리함 <br>
3. 머신러닝 프레임 웍 지원 <br>
tensorflow, pytorch, MxNet 등 지원  <br>
-> 위 2가지만 지원되도 사용에는 지장이 없어보임  <br>
4. 학습 환경  <br>
우버에서 개발된 텐서플로우용 분산 학습 플랫폼인 Hornovod 지원  <br>
-> *자세한 내용 조사 필요*  <br>
5. 모델 서빙  <br>


## 설치하기

### 1. kubeflow를 설치하기 위해 kubernetes 설치 필요 <br>

1. minikube를 설치하기 <br>

```
# centos 의경우 nvida driver 설치 방법 https://likefree.tistory.com/14
https://kubernetes.io/ko/docs/tasks/tools/install-minikube/
리눅스의 경우 아래 명령어 입력 후 가상화 지원 여부 확인
grep -E --color 'vmx|svm' /proc/cpuinfo

    1. brew install
sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
vi ./.bashrc
# brew가 설치된 경로의 bin 패스 추가
PATH=/home/linuxbrew/.linuxbrew/bin:$PATH
export MANPATH=$(brew --prefix)/share/man:$MANPATH
export INFOPATH=$(brew --prefix)/share/info:$INFOPATH

# 환경변수 적용 
source ~/.bashrc
# brew 정보 업데이트
brew update
sudo apt-get install build-essential

    2. minikube 설치
brew install gcc
brew install kubectl
brew install minikube
or  (아래는 공식 홈페이지 설치 방법)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

    3. docker및 기타 설치설치
- 도커 설치
# minikube 실행 위해서는 도커가 설치되어 있어야 한다.
curl -fsSL https://get.docker.com/ | sudo sh
# sudo 없이 도커 사용하기
sudo usermod -aG docker $USER # 현재 접속중인 사용자에게 권한주기
sudo usermod -aG docker your-user # your-user 사용자에게 권한주기
- KVM (Kernel-based Virtual Machine)등 기타 설치파일 
sudo apt install virtualbox-dkms linux-headers-generic
# centos의 경우 
yum install kernel-devel
yum install kernel-headers
sudo yum install yum-plugin-copr
sudo yum copr enable ngompa/snapcore-el7
sudo yum -y install snapd
sudo ln -s /var/lib/snapd/snap /snap
- 도커 상태확인 
service docker status
systemctl status docker
- 도커 데몬 실행
service docker start 
systemctl enable docker.service
- firewalld 비활성화
# systemctl stop firewalld
# systemctl disable firewalld

    4. minikube 실행
# 여유있는 사이즈를 할당해서 실행하기 
minikube start --cpus 4 --memory 8895 --disk-size=60g

-> 에러 발생
 [VBOX_DEVICE_MISSING] Failed to start virtualbox VM. "minikube start" may fix it. creating host: create: precreate: We support Virtualbox starting with version 5. Your VirtualBox install is "WARNING: The character device /dev/vboxdrv does not exist.\n\t Please install the virtualbox-dkms package and the appropriate\n\t headers, most likely linux-headers-Microsoft.\n\n\t You will not be able to start VMs until this problem is fixed.\n5.2.34_Ubuntur133883". Please upgrade at https://www.virtualbox.org
💡  Suggestion: Reinstall VirtualBox and reboot. Alternatively, try the kvm2 driver: https://minikube.sigs.k8s.io/docs/reference/drivers/kvm2/

=> 해결 sudo service docker start
-> 일단은 mminikube start 명령어로 사용 

클러스터 정상실행여부 확인
$kubectl get cs

    5. cilum 실행
cilium 의존성을 위해 etcd를 별도로 배포한다.
$ kubectl create -n kube-system -f https://raw.githubusercontent.com/cilium/cilium/master/examples/kubernetes/addons/etcd/standalone-etcd.yaml
-> port 충돌로 실행 안되서 일정시간 기다린 후 아래 명령어로 실행
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/v1.6/install/kubernetes/quick-install.yaml

### 2. kfctl 가져오기 <br>

# kubectl 설치
curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
# kubeflow install을 위해서 kfctl을 가져온다.
# https://github.com/kubeflow/kfctl/releases 에서 원하는 버전 설치
wget https://github.com/kubeflow/kfctl/releases/download/v1.0.2/kfctl_v1.0.2-0-ga476281_linux.tar.gz
# 압축 해제 
tar -xvf kfctl_v1.0.2-0-ga476281_linux.tar.gz
# kubeflow 설치 위치 지정 - 환경 변수
export PATH=$PATH:$(pwd)
export KF_NAME='kubeflow'
export BASE_DIR=/home/sh/kubeflow
export KF_DIR=${BASE_DIR}/${KF_NAME}
export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.2.yaml
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.2.yaml"
# 지정된 환경변수 실행 - yaml 가져오기
# apply
kfctl build -V -f ${CONFIG_URI}
../kfctl apply -V -f ${CONFIG_FILE} 
```

2. kubernetes 설치 <br>

```
    - 쿠버네티스 실행을 위한 swap 비활성화
sudo swapoff -a
    - iptables 설치하기
sudo apt-get install -y iptables arptables ebtables
    - 쿠버네티스 설치에 필요한 kubelet, kubeadm, kubectl을 설치
$ sudo apt-get update && sudo apt-get install -y apt-transport-https curl
$ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
$ cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
$ sudo apt-get update
# 버전은 https://www.kubeflow.org/docs/started/k8s/overview/#minimum-system-requirements 참고
$ sudo apt-get install -y kubelet=1.15.10-00 kubeadm=1.15.10-00 kubectl=1.15.10-00
$ sudo apt-mark hold kubelet kubeadm kubectl

# centos
- SELinux 설정을 permissive 모드로 변경
sudo setenforce 0
sudo sed -i 's/^SELINUX=enforcing$/SELINUapt-get update && apt-get install apt-transport-https ca-certificates curl software-properties-commonX=permissive/' /etc/selinux/config
- 쿠버네티스 YUM 리포지토리 설정
# cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
exclude=kube*
EOF
- kubeadm 설치
yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
systemctl enable kubelet && systemctl start kubelet


kubeadm config images pull
    - 쿠버네티스 설치
# 아이피 대역 겹치지 않도록 조심하기
sudo kubeadm init --pod-network-cidr=172.16.0.0/16 --apiserver-advertise-address=192.168.37.131
sudo kubeadm init --pod-network-cidr=10.217.0.0/16

```
<img src="/img/k8s_kubeflow/set_0.JPG" width="200px" height="150px"></img>  <br>
실행시 화면  -> 써있는대로 작업하기 <br>

```
    - 쿠버네티스 설정
# kubectl을 사용하기 위해서 관리자 설정 파일을 유저 디렉토리로 복사 
$ mkdir -p HOME/.kube
# $HOME 대신 ~ 으로 사용
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config
# 쿠버네티스 접속 테스트
$ kubectl cluster-info
#  Cilium을 쿠버네티스에 설치
$ kubectl create -f https://raw.githubusercontent.com/cilium/cilium/v1.6/install/kubernetes/quick-install.yaml
# 정상 실행여부 확인 하기
kubectl get pods -n kube-system --selector=k8s-app=cilium
 -> cilim 포드의 READY가 1/1이 되면, 쿠버네티스 클러스터를 사용할 수 있다. 
 (1번의 minikube를 실행한 후 작업해야 실행회는걸로 보임)
```

- nvidia plugin 설치하기  <br>

```
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/master/nvidia-device-plugin.yml

device-plugin 포드가 정상적으로 작동했는지 확인
kubectl -n kube-system get pod -l name=nvidia-device-plugin-ds
kubectl -n kube-system logs  -l name=nvidia-device-plugin-ds
```

- jupyter 테스트

```
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: tf-gpu-jupyter
  name: tf-gpu-jupyter
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tf-gpu-jupyter
  template:
    metadata:
      labels:
        app: tf-gpu-jupyter
    spec:
      containers:
      - image: tensorflow/tensorflow:2.1.0-gpu-py3-jupyter
        imagePullPolicy: IfNotPresent
        name: tf-gpu-jupyter
        ports:
        - containerPort: 8888
          protocol: TCP
        resources:
          limits:
            nvidia.com/gpu: "1"
EOF

- 쥬피터 포드 생성 확인
kubectl get pod -l app=tf-gpu-jupyter
- 로그인정보 조회
kubectl logs -l app=tf-gpu-jupyter

- jupyter 디플로이먼트 삭제
kubectl delete deploy tf-gpu-jupyter
```

- Service Account Token Volume 활성화

```
인증/권한 기능을 위해서 istio 를 사용합니다. 그래서 istio-system 이라는 네임스페이스에 istio 관련 컴포넌트가 설치된다.
    - 기능활성화를 위한  kube-apiserver 매니페스트 파일 편집 
sudo vim /etc/kubernetes/manifests/kube-apiserver.yaml
추가
- --service-account-signing-key-file=/etc/kubernetes/pki/sa.key
- --service-account-issuer=api
- --service-account-api-audiences=api,vault
```

- dynamic volume provisioner 설치 

```
kubeflow를 쉽게 설치하기 위해서는 동적 볼륨 프로비져너(dynamic volume provisioner)가 필요합니다. 
참조한 블로그에서는 로컬 디렉토리를 이용하는 Local Path Provisioner 를 사용

- Local Path Provisioner 설치 
kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml
- 스토리지클래스 조회
kubectl get storageclass 
- kubeflow는 기본 스토리지 클래스를 사용하기 때문에, local-path 스토리지 클래스를 기본 클래스로 설정해야함.
kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

```

### 2. kubeflow 설치하기

```
mkdir ~/kubeflow
cd ~/kubeflow
- 릴리즈 버전 확인하고 최신버전 설치
curl -L -O https://github.com/kubeflow/kfctl/releases/download/v1.0.2/kfctl_v1.0.2-0-ga476281_linux.tar.gz
tar -xvf kfctl_v1.0.2-0-ga476281_linux.tar.gz

- kubeflow 배포를 위한 환경변수 설정
export PATH=$PATH:"/home/sh/kubeflow"
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/master/kfdef/kfctl_istio_dex.v1.0.2.yaml"
export KF_NAME=kf-test
export BASE_DIR=/home/sh/kubeflow
export KF_DIR=${BASE_DIR}/${KF_NAME}

- 블로그에서 kfctl_existing_arrikto.yaml 설정 파일을 이용해 kubeflow를 배포한다고함
-> 나중에 내용 자세히 확인하기
wget -O kfctl_istio_dex.yaml $CONFIG_URI
export CONFIG_FILE=${KF_DIR}/kfctl_istio_dex.yaml
kfctl apply -V -f ${CONFIG_FILE}
-> 요명령어 사용시 kebeflow 설치 시작 

- kubeflow 네임스페이스, istio-system 네임스페이스의 포드를 조회
kubectl -n kubeflow get pod

- 정지 할때 명령어 
minikube stop

- 네트워크 설정
export NAMESPACE=istio-system
kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80


- stio-ingressgateway 서비스를 조회
kubectl -n istio-system get service istio-ingressgateway

```

### - 실행 확인 <br>
- kubeflow 정상 설치 확인 <br> 
kubectl -n kubeflow get all <br>
- kubeflow 네임스페이스와, istio-system 네임스페이스 포드 조회 <br>
kubectl -n kubeflow get pod kubectl -n istio-system get service<br>
istio-ingressgateway <br>




### - 명령어들 <br>

```
# 버전 체크
kubectl version check
# k8s 버전 실행
kubeadm init --kubernetes-version=1.15.0 --apiserver-advertise-address=192.168.3.70 --image-repository registry.aliyuncs.com/google_containers --service-cidr=10.1.0.0/16 --pod-network-cidr=10.244.0.0/16


- 잡다
 1004  kubectl -n kubeflow get deployment
 1005  kubectl get po -n kubeflow
 1006  kubectl describe po -n kubeflow ml-pipeline-persistenceagent-645cb66874-qmj9l
 1007  kubectl get po -n istio-system
 1008  kubectl describe po -n istio-system istio-ingressgateway-565b894b5f-fcgtl
 1009  kubectl get po -n kubeflow
 1010  kubectl describe po -n kubeflow ml-pipeline-persistenceagent-645cb66874-qmj9l
 1011  sudo kubeadm init --feature-gates CoreDNS=true
 1012  kubectl get nodes
 1013  kubectl get po -n kubeflow
 1014  kubectl describe po -n kubeflow ml-pipeline-persistenceagent-645cb66874-qmj9l
 1015  kubelet --version
 1016  kubectl get po -n cert-manager
 1017  kubectl describe po -n cert-manager cert-manager-webhook-755d75845c-xjxxf



```










## 참조 <br>

- kubeflow 설명 <br>
https://bcho.tistory.com/1301 <br>
- document <br>
https://www.kubeflow.org/docs/started/getting-started/ <br>
- 셋팅 및 설치 정리 <br>
https://lsjsj92.tistory.com/580 <br>
https://www.kangwoo.kr/2020/02/17/pc%ec%97%90-kubeflow-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0-2%eb%b6%80-kubernetes-nvidia-device-plugin-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0/ <br>
-> 매우 잘되있음 "https://www.kangwoo.kr/"
https://monkey3199.github.io/develop/ai/kubeflow/2018/10/01/Getting_Started_with_Kubeflow.html <br>
https://ddii.dev/kubernetes/cilium-1/# <br>
https://javacan.tistory.com/entry/k8s-install-in-centos7 <br>
- 파이프라인 죽은 경우 <br>
https://github.com/kubeflow/pipelines/issues/741 <br>
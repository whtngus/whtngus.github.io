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

    4. minikube 실행
# 여유있는 사이즈를 할당해서 실행하기 
minikube start --cpus 4 --memory 8895 --disk-size=60g

-> 에러 발생
 [VBOX_DEVICE_MISSING] Failed to start virtualbox VM. "minikube start" may fix it. creating host: create: precreate: We support Virtualbox starting with version 5. Your VirtualBox install is "WARNING: The character device /dev/vboxdrv does not exist.\n\t Please install the virtualbox-dkms package and the appropriate\n\t headers, most likely linux-headers-Microsoft.\n\n\t You will not be able to start VMs until this problem is fixed.\n5.2.34_Ubuntur133883". Please upgrade at https://www.virtualbox.org
💡  Suggestion: Reinstall VirtualBox and reboot. Alternatively, try the kvm2 driver: https://minikube.sigs.k8s.io/docs/reference/drivers/kvm2/

sudo service docker start
sudo minikube start --cpus 4 --memory 8895 --disk-size=60g  --vm-driver=docker



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
kfctl build -V -f ${CONFIG_URI}
../kfctl apply -V -f ${CONFIG_FILE}
# apply
kfctl apply -V -f ${CONFIG_FILE}
 
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

    - 쿠버네티스 설치
# 아이피 대역 겹치지 않도록 조심하기
sudo kubeadm init --pod-network-cidr=172.16.0.0/16 --apiserver-advertise-address=192.168.37.131
sudo kubeadm init --pod-network-cidr=10.217.0.0/16

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


```



### 2. 실행 확인 <br>

```
# kubeflow 정상 설치 확인
kubectl -n kubeflow get all   
# kubeflow 네임스페이스와, istio-system 네임스페이스 포드 조회
kubectl -n kubeflow get pod
kubectl -n istio-system get service istio-ingressgateway
```










## 참조 <br>

- kubeflow 설명 <br>
https://bcho.tistory.com/1301 <br>
- document <br>
https://www.kubeflow.org/docs/started/getting-started/ <br>
- 셋팅 및 설치 정리 <br>
https://lsjsj92.tistory.com/580 <br>
https://www.kangwoo.kr/2020/02/17/pc%ec%97%90-kubeflow-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0-2%eb%b6%80-kubernetes-nvidia-device-plugin-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0/ <br>
https://monkey3199.github.io/develop/ai/kubeflow/2018/10/01/Getting_Started_with_Kubeflow.html <br>

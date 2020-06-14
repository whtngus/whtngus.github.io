# kubeflow install

### 기본 kubeflow 설치 <br>

- 환경변수 설정 <br>

```
export KF_NAME=handson-kubeflow
export BASE_DIR=/home/${USER}
export KF_DIR=${BASE_DIR}/${KF_NAME}
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.0.yaml"
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/master/kfdef/kfctl_k8s_istio.v1.0.1.yaml"  
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/master/kfdef/kfctl_k8s_istio.v1.0.2.yaml"

export CONFIG="https://raw.githubusercontent.com/kubeflow/kubeflow/v0.6-branch/bootstrap/config/kfctl_k8s_istio.0.6.2.yaml"
```

- kubectl 설치 <br>

```
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
```

- kustomize 패키지 빌드하기

```
mkdir -p ${KF_DIR}
cd ${KF_DIR}
kfctl build -V -f ${CONFIG_URI}

export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.0.yaml
kfctl apply -V -f ${CONFIG_FILE}


# /etc/kubernetes/manifests/kube-apiserver.yaml 에 아래 두줄 추가
- --service-account-issuer=kubernetes.default.svc
- --service-account-signing-key-file=/etc/kubernetes/pki/sa.key

export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_istio_dex.v1.0.2.yaml"
export KF_NAME=kf-sh
export BASE_DIR=/home/sh
export KF_DIR=${BASE_DIR}/${KF_NAME}
mkdir -p ${KF_DIR}
cd ${KF_DIR}
wget -O kfctl_istio_dex.yaml $CONFIG_URI
export CONFIG_FILE=${KF_DIR}/kfctl_istio_dex.yaml
kfctl apply -V -f ${CONFIG_FILE}
# Kubeflow will be available at localhost:8080
kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80








export PATH=$PATH:"/home/kangwoo/kubeflow"
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_istio_dex.v1.0.1.yaml"
export KF_NAME=kf-test
export BASE_DIR=/home/kangwoo/kubeflow
export KF_DIR=${BASE_DIR}/${KF_NAME}
mkdir -p ${KF_DIR}
cd ${KF_DIR}
# Download the config file and change the default login credentials.
wget -O kfctl_istio_dex.yaml $CONFIG_URI
export CONFIG_FILE=${KF_DIR}/kfctl_istio_dex.yaml
kfctl apply -V -f ${CONFIG_FILE}


    -> 에러발생 
WARN[0122] Encountered error applying application cert-manager:  (kubeflow.error): Code 500 with messageError error when creating "/tmp/kout023299073": Internal error occurred: failed calling webhook "webhook.io": the server is currently unable to handle the request  filename="kustomize/kustomize.go:202"
WARN[0122] Will retry in 21 seconds.  
- 해결1 예상원인 istio-system
# 검색
kubectl -n istio-system get pods   -> 많이 죽어있음 
kubectl describe namespace istio-system -> 상태 확인하기 

(1)
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.0.yaml"
kfctl apply -V -f ${CONFIG_URI}
(2) 연달아 실행
wget https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.0.yaml
kfctl apply -V -f ./kfctl_k8s_istio.v1.0.0.yaml

Istio 란?
control plain 에 있던 Pilot, Mixer, Galley, Citadel, Gateway등의 컴포넌트가 pod 형태로 설치
Data Plane의 메인 프록시로 Envoy proxy를 사용하며 이를 컨트롤 해주는 Control Plane의 오픈소스 솔루션이 Istio
kubectl -n istio-system get svc istio-sidecar-injector
- 해결 2 istio-system 지우고 다시 시도
# 삭제
kubectl delete namespaces istio-system
kubectl delete apiservice v1beta1.webhook.cert-manager.io
kubectl delete namespace cert-manager
kubectl label default your-namespace istio-injection=disabled
-> 삭제가안됨 아래 내용에 삭제방법 기제
# 네임스페이스 생성
kubectl create namespace kubeflow-anonymous
# 다시적용해보기 

- 해결 3 
https://docs.projectcalico.org/getting-started/kubernetes/flannel/flannel
위 사이트대로 적용후 다시 설치 시도 


```

     - **istio-system 삭제**
```
# 아래명령어를 치면 응답이 안옴
kubectl delete ns istio-system
# 종료상태에 걸린 네임스페이스 제거하기

-> 최종 
NAMESPACE=istio-system
kubectl get ns $NAMESPACE -o json > ${NAMESPACE}.json
# 아래 텍스트 파일을 생성해서 finalizers안의 내용을 전부 비우기 
vi ${NAMESPACE}.json 
# 지우기
 kubectl replace --raw "/api/v1/namespaces/istio-system/finalize" -f ./istio-system.json
 
```

- 위방식대로 시도후 실패 지운 후 Istio document 참조해서 다시 설치 시작 

```
    - V 1.0 아래 1.0.2 위 두개 동시 적어둠 하나 선택 
wget https://github.com/kubeflow/kfctl/releases/download/v1.0.2/kfctl_v1.0.2-0-ga476281_linux.tar.gz
wget https://github.com/kubeflow/kfctl/releases/download/v1.0/kfctl_v1.0-0-g94c35cf_linux.tar.gz
tar -xvf kfctl_v1.0.2-0-ga476281_linux.tar.gz
tar -xvf kfctl_v1.0-0-g94c35cf_linux.tar.gz
# tar 압축 푼 디렉토리 위치 
export PATH=$PATH:"<path-to-kfctl>"
# kubeflow 설치할 이름
export KF_NAME=<your choice of name for the Kubeflow deployment>
# kubeflow설치할 이름 base 디렉토리
export BASE_DIR=<path to a base directory>
export KF_DIR=${BASE_DIR}/${KF_NAME}

# 설치 컨피그 셋팅
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.0.yaml"
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_k8s_istio.v1.0.2.yaml"
# 설치할 디렉토리로 이동해서 설치시작 - 오래걸림 
mkdir -p ${KF_DIR}
cd ${KF_DIR}
kfctl apply -V -f ${CONFIG_URI}


-> istio.io 미리 설치 필요  
helm repo add istio.io https://storage.googleapis.com/istio-release/releases/charts


->문제가 있어 검색해본 결과 해당 이슈 해결안되어 있고 gcp로 설치해야 한다고 나와 설치해보기 - 여전히 에러 
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/master/kfdef/kfctl_gcp_iap.yaml"
export BASE_DIR=/home/sh
export KF_NAME=kf_sh
kfctl build -V -f ${CONFIG_URI}
export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.2.yaml
kfctl apply -V -f ${CONFIG_URI}

다시
https://github.com/kubeflow/kfctl/releases/download/v1.0.2/kfctl_v1.0.2-0-ga476281_linux.tar.gz
tar -xvf kfctl_v1.0.2-0-ga476281_linux.tar.gz
export BASE_DIR=/home/sh
export KF_NAME=kf-sh
export KF_DIR=${BASE_DIR}/${KF_NAME}
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_istio_dex.v1.0.2.yaml"
cd ${KF_DIR}
wget -O kfctl_istio_dex.yaml $CONFIG_URI
export CONFIG_FILE=${KF_DIR}/kfctl_istio_dex.yaml

```

- 포트 포워딩 하기

```
export NAMESPACE=istio-system
kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80

```
 
- 설치 확인 <br>

```
# 설치확인 
kubectl -n kubeflow get all
kubectl get pods -n istio-system
kubectl get service -n istio-system

- 기타 확인
 kubectl get po -n cert-manager
 kubectl describe po ~~~ -n cert-manager
 
 kubectl get po -n istio-system
 sudo vi /etc/environment -> no procxy
 
```


# 참고
- Istio 설명 <br>
https://gruuuuu.github.io/cloud/service-mesh-istio/# <br>
- Istio 관리, 이슈처리 <br>
https://github.com/istio/istio/issues/21058 <br>
https://github.com/kubeflow/kubeflow/issues/4762 <br>
https://success.docker.com/article/kubernetes-namespace-stuck-in-terminating <br>
https://github.com/kubeflow/kubeflow/issues/4856  - gcp로 설치 <br>
- Istio document <br>
https://www.kubeflow.org/docs/started/k8s/kfctl-k8s-istio/ <br>
https://www.kubeflow.org/docs/started/k8s/kfctl-istio-dex/#notes-on-the-configuration-file <br>

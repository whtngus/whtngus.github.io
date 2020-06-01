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
```

- kustomize 패키지 빌드하기

```
mkdir -p ${KF_DIR}
cd ${KF_DIR}
kfctl build -V -f ${CONFIG_URI}

export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.2.yaml
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
kubectl label default your-namespace istio-injection=disabled
-> 삭제가안됨 아래 내용에 삭제방법 기제
# 네임스페이스 생성
kubectl create namespace kubeflow-anonymous
# 다시적용해보기 

     - istio-system 삭제 
# 아래명령어를 치면 응답이 안옴
kubectl delete ns istio-system
# 종료상태에 걸린 네임스페이스 제거하기

NAMESPACE=istio-system
kubectl get ns $NAMESPACE -o json > ${NAMESPACE}.json
# 아래 텍스트 파일을 생성해서 finalizers안의 내용을 전부 비우기 
vi ${NAMESPACE}.json 
# 지우기
 kubectl replace --raw "/api/v1/namespaces/istio-system/finalize" -f ./istio-system.json
```




# 참고
- Istio 설명 <br>
https://gruuuuu.github.io/cloud/service-mesh-istio/# <br>
- Istio 관리, 이슈처리 <br>
https://github.com/istio/istio/issues/21058 <br>
https://github.com/kubeflow/kubeflow/issues/4762 <br>
https://success.docker.com/article/kubernetes-namespace-stuck-in-terminating <br>
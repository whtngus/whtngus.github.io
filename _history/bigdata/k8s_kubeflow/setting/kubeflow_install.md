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
export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/master/kfdef/kfctl_istio_dex.v1.0.2.yaml"


export KF_NAME=kf-sh
export BASE_DIR=/home/sh
export KF_DIR=${BASE_DIR}/${KF_NAME}
mkdir -p ${KF_DIR}
cd ${KF_DIR}
kfctl build -V -f ${CONFIG_URI}
export CONFIG_FILE=${KF_DIR}/kfctl_k8s_istio.v1.0.0.yaml
kfctl apply -V -f ${CONFIG_FILE}
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





# /etc/kubernetes/manifests/kube-apiserver.yaml 에 아래 두줄 추가
- --service-account-issuer=kubernetes.default.svc
- --service-account-signing-key-file=/etc/kubernetes/pki/sa.key


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

- snap을 이용해서 설치 후 사용해보기 <br>

```
snap 사용 x 버전문제 확인 완료 
sudo yum install snapd
sudo systemctl start snapd.service
sudo ln -s /var/lib/snapd/snap /snap

sudo snap install microk8s --classic
snap refresh microk8s --beta
microk8s.enable dns storage dashboard
# gpu가 있는경우에 
microk8s.enable gpu

# kubeflow 활성화
microk8s.enable kubeflow

```

- 포트 포워딩 하기

```
export NAMESPACE=istio-system
kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80

kubectl port-forward -n istio-system service/istio-ingressgateway 8080:80 --address=0.0.0.0
 -> 에러 발생 an error occurred forwarding 8081 -> 443: error forwarding port 443 to pod 959e20b90486ab491d4dec86c25c4756bf0ead30f81f2bcd9a6d0b02aa0181b5, uid : exit status 1: 2020/06/25 16:31:35 socat[17328] E connect(5, AF=2 127.0.0.1:443, 16): Connection refused
해결 
kubectl create deployment nginx --image=nginx
kubectl create service nodeport nginx --tcp=80:80

    이슈
-> 파이프라인이 충돌로 죽어있음
kubeadm init --feature-gates CoreDNS=true
확인
kubectl -n kubeflow get pods --selector=app=ml-pipeline
kubectl -n kubeflow get pods --selector=app=ml-pipeline-persistenceagent
kubectl logs -n kubeflow ml-pipeline-persistenceagent-645cb66874-qmj9l --previous
 
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
 
 프록시 열기
 kubectl proxy --address 0.0.0.0 --accept-hosts '.*'
 
```

- kubeflow 설치 에러 하나씩 해결하기 

```
    - 대시보드 접속시 UNAVAILABLE:upstream connect error or disconnect/reset before headers. reset reason: connection failure
    

    - 확인 
 kubectl get pod -n kubeflow
NAME                                                           READY   STATUS             RESTARTS   AGE
admission-webhook-bootstrap-stateful-set-0                     1/1     Running            0          11m
admission-webhook-deployment-569558c8b6-gnl4k                  1/1     Running            0          11m
application-controller-stateful-set-0                          1/1     Running            0          12m
argo-ui-7ffb9b6577-gtv5x                                       1/1     Running            0          11m
centraldashboard-659bd78c-hn7zr                                1/1     Running            0          11m
jupyter-web-app-deployment-679d5f5dc4-j7l89                    1/1     Running            0          11m
katib-controller-7f58569f7d-jqxb2                              1/1     Running            1          11m
katib-db-manager-54b66f9f9d-mnkld                              0/1     CrashLoopBackOff   6          11m
katib-mysql-dcf7dcbd5-dqldn                                    0/1     Pending            0          11m
katib-ui-6f97756598-8fk75                                      1/1     Running            0          11m
kfserving-controller-manager-0                                 2/2     Running            1          11m
metacontroller-0                                               1/1     Running            0          11m
metadata-db-65fb5b695d-fxpd4                                   0/1     Pending            0          11m
metadata-deployment-65ccddfd4c-zjxr6                           0/1     Running            0          11m
metadata-envoy-deployment-7754f56bff-5bf7q                     1/1     Running            0          11m
metadata-grpc-deployment-75f9888cbf-ksq77                      1/1     Running            4          11m
metadata-ui-7c85545947-gwn9g                                   1/1     Running            0          11m
minio-69b4676bb7-h9vgf                                         0/1     Pending            0          11m
ml-pipeline-5cddb75848-rf2xk                                   1/1     Running            1          11m
ml-pipeline-ml-pipeline-visualizationserver-7f6fcb68c8-x96sw   1/1     Running            0          11m
ml-pipeline-persistenceagent-6ff9fb86dc-cqqr5                  0/1     CrashLoopBackOff   3          11m
ml-pipeline-scheduledworkflow-7f84b54646-7vhjm                 1/1     Running            0          11m
ml-pipeline-ui-6758f58868-tsz6h                                1/1     Running            0          11m
ml-pipeline-viewer-controller-deployment-745dbb444d-js4xw      1/1     Running            0          11m
mysql-6bcbfbb6b8-kxddt                                         0/1     Pending            0          11m
notebook-controller-deployment-5c55f5845b-4w2tl                1/1     Running            0          11m
profiles-deployment-78f694bffb-brkgw                           2/2     Running            0          11m
pytorch-operator-cf8c5c497-9mdcd                               1/1     Running            0          11m
seldon-controller-manager-6b4b969447-hrv97                     1/1     Running            0          11m
spark-operatorcrd-cleanup-nch68                                0/2     Completed          0          11m
spark-operatorsparkoperator-76dd5f5688-bht8b                   1/1     Running            0          11m
spartakus-volunteer-5dc96f4447-l882f                           1/1     Running            0          11m
tensorboard-5f685f9d79-6mnbc                                   1/1     Running            0          11m
tf-job-operator-5fb85c5fb7-sz7k2                               1/1     Running            0          11m
workflow-controller-689d6c8846-p56g7                           1/1     Running            0          11m

    1. spark 에러부터 확인하기
kubectl describe pod -n kubeflow spark-operatorcrd-cleanup-nch68
Events:
  Type     Reason                  Age   From                     Message
  ----     ------                  ----  ----                     -------
  Normal   Scheduled               12m   default-scheduler        Successfully assigned kubeflow/spark-operatorcrd-cleanup-nch68 to master-node-40
  Normal   Pulled                  12m   kubelet, master-node-40  Container image "gcr.io/spark-operator/spark-operator:v1beta2-1.0.0-2.4.4" already present on machine
  Normal   Created                 12m   kubelet, master-node-40  Created container delete-sparkapp-crd
  Normal   Started                 12m   kubelet, master-node-40  Started container delete-sparkapp-crd
  Normal   Pulled                  12m   kubelet, master-node-40  Container image "gcr.io/spark-operator/spark-operator:v1beta2-1.0.0-2.4.4" already present on machine
  Normal   Created                 12m   kubelet, master-node-40  Created container delete-scheduledsparkapp-crd
  Normal   Started                 12m   kubelet, master-node-40  Started container delete-scheduledsparkapp-crd
  Normal   SandboxChanged          12m   kubelet, master-node-40  Pod sandbox changed, it will be killed and re-created.
  Warning  FailedCreatePodSandBox  12m   kubelet, master-node-40  Failed create pod sandbox: rpc error: code = Unknown desc = failed to start sandbox container for pod "spark-operatorcrd-cleanup-nch68": Error response from daemon: OCI runtime create failed: container_linux.go:349: starting container process caused "process_linux.go:315: copying bootstrap data to pipe caused \"write init-p: broken pipe\"": unknown

-> 커널 업데이트 필요
https://myksb1223.github.io/develop_diary/2018/08/01/Centos-kernel-update.html


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
- snap 을 이용한 설치 추천 <br>
https://github.com/kubeflow/kubeflow/issues/4198 <br>
https://ubuntu.com/kubeflow/install <br>


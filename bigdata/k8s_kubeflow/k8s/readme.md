# Kubernets

## 조사

### 0. 자주 명령어 모음

```
- 모든 pod상태 확인 및 확인
kubectl get pods --all-namespaces
kubectl get nodes
kubectl get pods -o wide | grep <nodename>
- pod제거 
kubectl delete node <nodename>
kubectl delete pod <podname>
- pod 조회
kubectl get pods -n kube-system --selector=k8s-app=cilium
kubectl get pods -o wide --all-namespaces 
kubectl get pod --all-namespaces | grep -v Running
- pod 상세정보 확인
kubectl describe pod "pod 이름" -n kube-system
kubectl logs "pod 이름"  -n kube-system
- 모든 event 정보 확인
kubectl get events -n kube-system
- k8s에 join되어있는 node을의 상태정보 확인
kubectl describe node master

    - minikube
- 기본
minikube stop
minikube start --cpus 4 --memory 8096 --disk-size=40g 
minikube delete
- minikube 접속하기
minikube ssh
minikube dashboard
```

### 1. Kubernets network <br>

```
1. 서로 결합된 컨테이너와 컨테이너 간 통신
    - 도커로 생성된 컨테이너 구조의 경우
기본적으로 같은 노드(host) 내의 컨테이너 끼리 통신은 "docker0" 가상 네트워크 인터페이스 (172.17.0.0/24)를 통해 가능
각 컨테이너는 "veth"라느 가상 네트워크 인터페이스를 고유하게 가지며 각각의 "veth" ip 주소 값으로 통신할 수 있다.
    - Kubernetes Pod 내의 컨테이너 끼리의 통신
여러개의 컨테이너가 하나의 "veth" 가상 네트워크 인터페이스에 할당된다.
**veth0 안에서 각 컨테이너는 고유한 port 번호로 서로를 구분한다.**

2. Pod와 Pod 간의 통신
k8s는 kubenet이라는 간단한 네트워크 플러그인을 제공해주지만, 크로스 노드 네트워킹이나 네트워크 정책 설정 기능은 구현되어있지 안핟.
-> pod 네트워킹 인터페이스로 "CNI 스펙"을 준수하는 다양한 네트워크 플러그인을 사용하는것을 권장.(kubeadm은 기본적으로 CNI 기반 네트워크 플러그인만 사용 가능)
kubeadm : k8s에서 제공해주는 클러스터 빌드 전용 커맨드라인 인터페이스

Pod는 고유한 IP주소를 가진다.(가상 네트워크 인터페이스 "veth"를 가짐)
 -> 각 Pod는 kubenet 혹은 CNI로 구성된 네트워크 인터페이스를 통하여 고유한 ip주소로 통신 가능

3. Pod와 Service간의 통신
Pod는 기본적으로 쉽게 대체될 수 있는 존재이기 때문에 Pod to Pod Network만으로는 Kubernetes 시스템을 내구성있게 구축할 수 없다.

Pod는 계속해서 생성 소멸하기때문에 IP주소가 엔드포인트와 동일하다고 보장할 수 없다 -> 서비스 앞단에 everse-proxy(혹은 Load Balancer)를 위치시키는 방법이 있다.
    - proxy 요구사항
proxy 서버 스스로 내구성이 있어야 하며 장애에 대응할 수 있어야 한다.
트래픽을 전달할 서버 리스트를 가지고 있어야 한다.
서버 리스트 내 서버들이 정상적인지 확인할 수 있는 방법을 알아야 한다.

=> k8s는 "service" 리소스 타입을 만들어서 이를 해결함
    - service 특징
Pod로 액세스 할 수 있는 정책을 정의하는 추상화된 개념이다.+
kubernetes 리소스 타입 중 하나로 각 Pod로 트래픽을 포워딩 해주는 프록시 역할을 한다.
service 네트워크 또한 가상 IP주소
"selector" 라는 것을 이용하여 트래픽을 전달받을 Pod들을 결정
Pod 네트워크는 가상 이더넷 네트워크 인터페이스(veth)가 세팅되서 ifconfig로 조회 가능하지만, service 네트워크는 조회할 수 없다.


3. 외부와 Service 간의 통신
Service 에서 외부 통신을 가능하게 해주는 Service의 타입 -> NodePort, Load Balancer
    - NodePort
ClusterIP 타입(default)과 동일하지만 몇가지 기능들을 더 가지고 있다.
노드 네트워크의 IP를 통하여 접근 할 수 있을 뿐만 아니라 ClusterIP로도 접근이 가능하다.
 -> k8s가 NodePort 타입의 서비스를 생성하면 kube-proxy가 각 노드의 eth0 네트워크 interface에 30000–32767 포트 사이의 임의의 포트를 할당한다. 
    - Load Balancer
외부 클라우드 서비스를 사용하여 로드밸런서를 프로비저닝 할 수 있는 경우에 사용할 수 있는 Service 타입이다.
로드밸런서의 실제 생성은 비동기적으로 수행되며 프로비저닝 될 로드 밸런서에 대한 정보는 Service의 .status.loadBalancer필드에 작성된다.
    - Ingress
Ingress란 리버스 프록시를 통해 클러스터 내부 Service로 어떻게 패킷을 포워딩 시킬 것인지 명시한 쿠버네티스 리소스이다.
Ingress는 Ingress Controller와 짝지어진다.
Ingress Controller는 다양하게 있으며, 대중적으로 많이 사용하는 Ingress Controller는 nginx-ingress 이다.
eks ingress는 ingress 리소스를 읽어서 그에 맞는 리버스 프록시를 구성하기 위해 Application Load Balancer 및 필수 지원 AWS 리소스가 만들어지도록 트리거하는 컨트롤러
```

### 2. 에드온(Addons)

```
애드온은 클러스터 내부에서 필요한 기능들을 위해 실행되는 포드들
애드온에 사용되는 포드들은 디플로이먼트, 리플리케이션컨트롤러등에 의해 관리됩니다. 
애드온이 사용하는 네임스페이스는 kube-system입니다. 애드온에는 몇가지 종류들이 있습니다.

    - 네트워킹 애드온
k8s는 클러스터 내부에 가상네트워크를 구성해서 사용하는데, 이때 kuby-proxy이외에 네트워킹 관련한 애드온을 사용한다.
ACI, Calico, Canal, Cilium, CNI-Genie, Contiv, Falannel, Multus, NSX-T, Nuage, Romana, Weave Net등이 있고, OCI의 CNI(Container Network, Interface) 를 구현하고 있다면 다른 애드온들도 사용할 수 있다.

Cilium - Docker 및 Kubernetes와 같은 Linux 컨테이너 관리 플랫폼을 사용하여 배포된 응용 프로그램 서비스 간의 네트워크 연결을 보호하는 오픈 소스 소프트웨어

    - DNS 애드온
DNS 애드온의 경우 실제로 클러스터 내에서 작동하는 DNS 서버
dns 서비스로는 kube-dns와 core-dns가 있습니다.
    - 대시보드 애드온
kubectl이라는 CLI(Command Line Interface)를 많이 사용합니다. 
 -> 웹 UI가 필요한 경우가 있을수도 있는데, 이런경우에 사용할수 있는 대시보드가 있습니다.
```

### 3. k8s 삭제 방법 <br>

```
Kubernetes 삭제하는 방법
kubeadm reset
systemctl stop kubelet
systemctl stop docker
rm -rf /var/lib/cni/
rm -rf /var/lib/kubelet/*
rm -rf /run/flannel
rm -rf /etc/cni/
rm -rf /etc/kubernetes
rm -rf /var/lib/etcd/

ip link delete cni0
ip link delete flannel.1
yum remove -y kubelet
yum remove -y kubectl
yum remove -y kubeadm
systemctl start docker
```

### 4. 이슈사항 정리 <br>

##### 1. CrashLoopBackOff

```
    1. 네트워크 DNS 문제로 ContainerCreating에 멈춘 경우 <br>     
실행 명령어 : kubectl get pods -n kube-system --selector=k8s-app=cilium

CrashLoopBackOff 에러 발생
- 의미 
crashing 충돌로 인해 start를 반복중 
CrashLoopBackOff는 컨테이너가 다시 시작 후 반복적으로 비정상 종료됨을 나타냅니다. 
컨테이너는 다양한 원인으로 인해 비정상 종료될 수 있습니다. 
Pod의 로그를 확인하면 근본 원인을 해결할 수 있습니다.
기본적으로 비정상 종료된 컨테이너는 5분으로 제한된 지수 지연으로 다시 시작됩니다.

원인찾기 이벤트 로그 명렁어
kubectl describe pod  "pod name"
-> 안나오는 경우 아래 세가지 명령어로 명령어로 검색
kubectl get pods -n kube-system --selector=k8s-app=cilium
kubectl get pods -o wide --all-namespaces 
# kubectl describe pod  -A >> log.txt  #  검색 안나와서 -A로 전체 출력해서봄  
05-cilium.conf 설정파일 위치
/etc/cni/net.d/05-cilium.conf

에러 문구 
Events:
  Type     Reason                  Age                   From                 Message
  ----     ------                  ----                  ----                 -------
  Warning  FailedScheduling        60m (x89 over 3h10m)  default-scheduler    0/1 nodes are available: 1 node(s) had taints that the pod didn't tolerate.
  Normal   Scheduled               54m                   default-scheduler    Successfully assigned kube-system/coredns-5d4dd4b4db-gdz8x to ~~~
  Warning  FailedCreatePodSandBox  53m                   kubelet, ~~  Failed create pod sandbox: rpc error: code = Unknown desc = failed to set up sandbox container "fb94e3727233dd3d5f1c968da061971e2ee07239dfbea54f9d4a8b82bcc8ba69" network for pod "coredns-5d4dd4b4db-gdz8x": NetworkPlugin cni failed to set up pod "coredns-5d4dd4b4db-gdz8x_kube-system" network: unable to connect to Cilium daemon: failed to create cilium agent client after 30.000000 seconds timeout: Get http:///var/run/cilium/cilium.sock/v1/config: dial unix /var/run/cilium/cilium.sock: connect: no such file or directory
Is the agent running?

예상 원인 cni 가 꼬임 ..
https://stackoverflow.com/questions/60007464/nginx-kubernetes-pod-stays-in-containercreating

1. 해결방법 Cluster 다시 구성하기 
# kubeadm reset
# systemctl stop kubelet
# systemctl stop docker
# rm -rf /var/lib/cni/
# rm -rf /var/lib/kubelet/*
# rm -rf /etc/cni/
# ifconfig cni0 down
# ifconfig flannel.1 down
# ifconfig docker0 down
# ip link delete cni0
# ip link delete flannel.1

도커 및 데몬 재실행
sudo systemctl daemon-reload
sudo systemctl restart docker
클러스터 재실행
kubectl drain <node_name> --delete-local-data --force --ignore-daemonsets
kubectl delete node <node_name>
kubeadm reset
확인
kubectl get pods --all-namespaces

2. 원인 파악하기


```

##### 2. error: no configuration has been provided, try setting KUBERNETES_MASTER environment variable

```
실행 명령어
kubectl get pod --all-namespaces
에러 내용
error: no configuration has been provided, try setting KUBERNETES_MASTER environment variable

해결 방법
/etc/profile의 끝에 아래내용 추가 -> config 위치는 본인 설정에 맞게
export KUBECONFIG=/etc/kubernetes/admin.conf
스크립트 실행 -> 환경 변수 업데이트
source /etc/profile
```




## 참조 
- Kubernets network <br>
https://medium.com/finda-tech/kubernetes-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%A0%95%EB%A6%AC-fccd4fd0ae6 <br>
- 에드온(Addons) <br>
https://arisu1000.tistory.com/27828 [아리수] <br>
https://ddii.dev/kubernetes/cilium-1/ <br>
- k8s 삭제 방법 <br>
https://crystalcube.co.kr/202 [유리상자 속 이야기] <br>
- 이슈처리 <br>
CrashLoopBackOff <br>
https://cloud.google.com/kubernetes-engine/docs/troubleshooting?hl=ko <br>
https://waspro.tistory.com/563 <br>
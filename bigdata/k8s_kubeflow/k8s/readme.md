# Kubernets

## 조사

1. Kubernets network <br>

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







## 참조 
- Kubernets network <br>
1. https://medium.com/finda-tech/kubernetes-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%A0%95%EB%A6%AC-fccd4fd0ae6 <br>
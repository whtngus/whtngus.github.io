# k8s install

## 1. os : centos  <br>

### Installing K8s 

```
    0. nvidia 설치
# yum -y install gcc gcc-c++ make binutils libtool autoconf automake patch pkgconfig redhat-rpm-config gettext
# yum -y install kernel-devel-$(uname -r) kernel-headers-$(uname -r) dkms
# yum -y install epel-release

# cat <<HERE > /etc/modprobe.d/nvidia-installer-disable-nouveau.conf 
blacklist nouveau
options nouveau modeset=0
HERE
# cd /boot
# mv initramfs-$(uname -r).img{,_backup}
# dracut
# ls initramfs-$(uname -r).img -> 파일 목록이 생성되지 않으면 부팅 시 Error가 발생합니다.
# systemctl isolate multi-user.target
# chmod +x NVIDIA-Linux-x86_64-xxx.xx.run -> xxx.xx는 설치한 nvidia 그래픽 드라이버 version 입니다.
# ./NVIDIA-Linux-x86_64-xxx.xx.run

    1. docker 설치 
$ sudo su
$ cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
$ mkdir -p /etc/systemd/system/docker.service.d
$ systemctl daemon-reload
$ systemctl restart docker
$ exit

    2. nvidia-docker 설치
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.repo | sudo tee /etc/yum.repos.d/nvidia-docker.repo

sudo yum install -y nvidia-container-toolkit
sudo systemctl restart docker
or
yum install nvidia-docker2
    3. k8s 설치
# cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF

sudo yum install -y kubelet kubeadm kubectl
systemctl enable kubelet
systemctl start kubelet

- set hostname on nodes
sudo hostnamectl set-hostname master-node
or
sudo hostnamectl set-hostname worker-node1

- host entry or DNS record to resolve the hostname for all nodes
192.168.1.10 master.phoenixnap.com master-node
192.168.1.20 node1. phoenixnap.com node1 worker-node

-  Configure Firewall
sudo firewall-cmd --permanent --add-port=6443/tcp
sudo firewall-cmd --permanent --add-port=2379-2380/tcp
sudo firewall-cmd --permanent --add-port=10250/tcp
sudo firewall-cmd --permanent --add-port=10251/tcp
sudo firewall-cmd --permanent --add-port=10252/tcp
sudo firewall-cmd --permanent --add-port=10255/tcp
sudo firewall-cmd –-reload
-> FirewallD is not running 으로 일단 pass , 나중에 firewall 실행시키면 명령어 적용하기

- Disable SELinux
컨테이너가 filesystem의 접근권한을 허용해주기 위해
sudo setenforce 0
sudo sed -i ‘s/^SELINUX=enforcing$/SELINUX=permissive/’ /etc/selinux/config

- Disable SWAP
sudo sed -i '/swap/d' /etc/fstab
sudo swapoff -a

```

### Setup K8s

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
yum install kernel-devel
yum install kernel-headers
sudo yum install yum-plugin-copr
sudo yum copr enable ngompa/snapcore-el7
sudo yum -y install snapd
sudo ln -s /var/lib/snapd/snap /snap

    - 쿠버네티스 초기화

# 아이피 기존 네트워크와 안겹치게 조심하기 
sudo kubeadm init --pod-network-cidr=172.16.0.0/16
    -> error 
[ERROR FileContent--proc-sys-net-bridge-bridge-nf-call-iptables]: /proc/sys/net/bridge/bridge-nf-call-iptables contents are not set to 1
해결
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
vi /etc/sysctl.conf
net.bridge.bridge-nf-call-iptables = 1
sysctl -p
    -> error
[ERROR DirAvailable--etc-kubernetes-manifests]: /etc/kubernetes/manifests is not empty
[ERROR FileAvailable--etc-kubernetes-kubelet.conf]: /etc/kubernetes/kubelet.conf already exists
[ERROR Port-10250]: Port 10250 is in use
[ERROR FileAvailable--etc-kubernetes-pki-ca.crt]: /etc/kubernetes/pki/ca.crt already exists

해결
sudo systemctl stop kubelet
나머지 3개 에러는 해당 데이터 삭제 
    -> 갑자기 sudo 느려짐
service rsyslog restart
재부팅 ㅠ 


$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id –g) $HOME/.kube/config
# enable master node scheduling
$ kubectl taint nodes --all node-role.kubernetes.io/master-
$ kubectl apply -f https://docs.projectcalico.org/v3.11/manifests/calico.yaml

-> 위 명령어실행 시 kubeadm ~~ 어쩌구 나옴 salve sever에서 해당 명령어 실행해서 join
sudo kubeadm join 211.39.140.225:6443 --token 1kjhqe.02wl7j80euplruj6 --discovery-token-ca-cert-hash sha256:8e95e3278fc0af5283760d65ae66adcff733fe25dfee1e651dc64ae2ed9217bf

    -> error
error execution phase preflight: couldn't validate the identity of the API Server: could not find a JWS signature in the cluster-info ConfigMap for token ID 
해결 1
vi /etc/sysctl.conf
net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
sysctl -p
해결 2
# centos REdhat 인경우 보안끄기
systemctl stop firewalld
systemctl disable firwalld

    -> error
[kubelet-check] The HTTP call equal to 'curl -sSL http://localhost:10248/~~' failed with error: Get http://localhost:10248/~~: dial tcp 127.0.0.1:10248: connect: connection refused.
error execution phase kubelet-start: error uploading crisocket: timed out waiting for the condition

# /etc/systemd/system/kubelet.service.d/10-kubeadm.conf 아래내용 추가
Environment="KUBELET_EXTRA_ARGS=--fail-swap-on=false"

systemctl daemon-reload
systemctl restart kubelet
kubeadm init --skip-preflight-checks

    -> error
# sudo kubectl get nodes
error: no configuration has been provided, try setting KUBERNETES_MASTER environment variable
해결
export KUBECONFIG=/etc/kubernetes/admin.conf
source /etc/profile
```

### StorageClass

```
    - Local Path Provisioner 설치
    
https://github.com/rancher/local-path-provisioner
kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml
# install 확인
kubectl -n local-path-storage get pod
# log 확인
kubectl -n local-path-storage logs -f "name 위 install 확인 명력어로 확인 가능"

    - NFS Client 설치
    
https://github.com/helm/charts/tree/master/stable/nfs-client-provisioner
# helm 설치
brew install helm
# helm 을 이용해서 nfs-client-pro-visioner 패키지 설치

# NFS 설치     
sudo yum install -y nfs-utils
sudo systemctl enable rpcbind
sudo systemctl enable nfs-server
sudo systemctl start rpcbind
sudo systemctl start nfs-server
# NFS change the permission 
# 원하는 위치에 
mkdir /var/nfsshare
chmod -R 755 /var/nfsshare
chown nfsnobody:nfsnobody /var/nfsshare
# 마운트할 디렉토리 설정 - 서버
vi /etc/exports
/nfs/ *.*.*.*(rw,all_squash,sync)
- 위에 처음은 공유할 대상 디렉토리 그다음아이피 (권한)
# 옵션 
ro                      -> 읽기 권한 부여 한다.
rw                     -> 읽기 쓰기 권한 부여 한다.
root_squash         -> 클라이언트에서 root를 서버상의 nobody 계정으로 매핑한다.
no_root_squash    -> 클라이언트 및 서버 모두 root 계정 사용한다.
sync                  -> 동기화한다.
all_squash          -> root 계정이 아닌 다른 계정도 사용 할  수 있게한다.
# 적용하기
sudo systemctl restart nfs
chmod o+w "대상 디렉토리"
# 서비스 등록하기
#systemctl   restart   rpcbind
#systemctl   start   nfs-server
#systemctl   start   nfs-lock
#systemctl   start   nfs-idmap
 
#systemctl   enable   rpcbind
#systemctl   enable   nfs-server
#systemctl   enable   nfs-lock
#systemctl   enable   nfs-idmap

 nfsstat -s ->로 마운트 확인

# 클라이언트 설정
sudo mount -t nfs "server ip":/nfs /nfs
touch /nfs/client.txt
yum install showmount  or sudo apt-get install nfs-common
mount -t nfs <공유서버명>:<공유디렉토리명>  <연결디렉토리>

showmount -e "공유서버 ip"
# nfs를 재실행
# systemctl stop nfs-server
# systemctl start nfs-server

kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get > get_helm.sh
./get_helm.sh
kubectl -n kube-system create sa tiller
kubectl create clusterrolebinding tiller --clusterrole cluster-admin --serviceaccount=kube-system:tiller
helm init --service-account tiller
 -> error 
helm init flag 없음
해결
# helm 3.x 이상부터 helm init가 사라짐  2버전으로 다운그래이드 하기
brew uninstall helm
brew install helm@2  
brew link --force helm@2

helm repo update

#  여기서부터 nfs-client-provisioner install
helm install --name my-release --set nfs.server="서버 ip" --set nfs.path="nfs directory" stable/nfs-client-provisioner
kubectl patch storageclass nfs-client -p '{"metadata": { "annotations" : { "storageclass.kubernetes.io/is-default-class":"true"}}}'
# 설치 확인
kubectl get storageclass

     - nvidia-gpu-plugin 설치
kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/1.0.0-beta6/nvidia-device-plugin.yml
# 설치 확인
kubectl get pod -n kube-system


    - 도커 레지스트리 만들기
도커 이미지를 저장할 프라이빗 도커 레지스트리를 설치해야함 
docker pull registry:latest

wget https://raw.githubusercontent.com/mojokb/handson-kubeflow/master/registry/kubeflow-registry-deploy.yaml
wget https://raw.githubusercontent.com/mojokb/handson-kubeflow/master/registry/kubeflow-registry-svc.yaml

sudo kubectl apply -f kubeflow-registry-deploy.yaml
kubectl apply -f kubeflow-registry-svc.yaml

 
내용 : kubeflow-registry-deploy.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  annotations:
    deployment.kubernetes.io/revision: "1"
  generation: 1
  labels:
    run: kubeflow-registry
  name: kubeflow-registry
  namespace: default
spec:
  progressDeadlineSeconds: 600
  replicas: 1
  revisionHistoryLimit: 10
  selector:
    matchLabels:
      run: kubeflow-registry
  strategy:
    rollingUpdate:
      maxSurge: 25%
      maxUnavailable: 25%
    type: RollingUpdate
  template:
    metadata:
      creationTimestamp: null
      labels:
        run: kubeflow-registry
    spec:
      containers:
      - image: registry:2
        imagePullPolicy: IfNotPresent
        name: kubeflow-registry
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      terminationGracePeriodSeconds: 30
      
내용 : kubeflow-registry-svc.yaml
apiVersion: v1
kind: Service
metadata:
  labels:
    run: kubeflow-registry
  name: kubeflow-registry
  namespace: default
spec:
  ports:
  - name: registry
    port: 30000
    protocol: TCP
    targetPort: 5000
    nodePort: 30000
  selector:
    run: kubeflow-registry
  sessionAffinity: None
  type: NodePort
status:
  loadBalancer: {}

** deploy 다운받아서 하는경우 변경해줘야 정상실행됨 -> apiVersion: apps/v1 

# /etc/hosts 에 아래 내용 추가  ip는 본인 아이피
10.X.X.X     kubeflow-registry.defalut.svc.cluster.local
# 명령어로 실행 여부 확인 
curl kubeflow-registry.defalut.svc.cluster.local:30000/v2/_catalog
{"repositories":[]} -> 등록된 이미지가 없어서 이렇게 반환됨 

# 프라이빗 레지스트리에서 보안 허용체크 하기 
#vi /etc/docker/daemon.json  아래내용 추가 
"insecure-registries" : [
    "kubeflow-registry.defalut.svc.cluster.local:30000"
 ]

sudo systemctl restart docker

# 이미지 올리기 
sudo docker login
sudo docker pull busybox
sudo docker tag busybox:latest kubeflow-registry.defalut.svc.cluster.local:30000/busybox:latest
sudo docker push kubeflow-registry.defalut.svc.cluster.local:30000/busybox:latest

# 다시 확인 
curl kubeflow-registry.defalut.svc.cluster.local:30000/v2/_catalog
{"repositories":["busybox"]}

```

### k9s <br>

```
k9s : 쿠버네티스 관리 툴 

wget https://github.com/derailed/k9s/releases/download/v0.19.6/k9s_Linux_x86_64.tar.gz
tar xvzf k9s_Linux_x86_64.tar.gz
sudo mv k9s /usr/bin
k9s 
->  그래픽 기반 관리툴을 볼 수 있음
```

### 다음은 kubeflow_install 로 <br>


# 참고 <br>
- 책 <br>
쿠버네티스에서 머신러닝이 처음이라면! 쿠브플로우 <br>
- nvidia 설치 <br>
https://coding-chobo.tistory.com/20 <br>
- nvidia-docker 설치 <br>
https://github.com/NVIDIA/nvidia-docker <br>
- k8s 설치 <br>
https://phoenixnap.com/kb/how-to-install-kubernetes-on-centos <br>
- nfs 설정 <br>
https://epdl-studio.tistory.com/43 <br>
- 도커 레지스트리 만들기 <br>
https://www.44bits.io/ko/post/running-docker-registry-and-using-s3-storage <br>



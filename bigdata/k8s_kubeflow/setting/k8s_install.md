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


    - NFS Client 설치
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


 Share the NFS directory over the network, creating the /etc/exports file:
vi /etc/exports
/var/nfsshare * (rw,sync,no_root_squash,no_all_squash)
Restart the nfs service to apply the content:
systemctl restart nfs-server
Add NFS and rpcbind services to firewall:
firewall-cmd --permanent --zone=public --add-service=nfs
firewall-cmd --permanent --zone=public --add-service=rpcbind
firewall-cmd --reload
```




# 참고 <br>
- nvidia 설치 <br>
https://coding-chobo.tistory.com/20 <br>
- nvidia-docker 설치 <br>
https://github.com/NVIDIA/nvidia-docker <br>
- k8s 설치 <br>
https://phoenixnap.com/kb/how-to-install-kubernetes-on-centos <br>


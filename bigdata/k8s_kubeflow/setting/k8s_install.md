# k8s install

## 1. os : centos  <br>

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
설명 생략
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

- Iptables settings


```




# 참고 <br>
- nvidia 설치 <br>
https://coding-chobo.tistory.com/20 <br>
- nvidia-docker 설치 <br>
https://github.com/NVIDIA/nvidia-docker <br>
- k8s 설치 <br>
https://phoenixnap.com/kb/how-to-install-kubernetes-on-centos <br>


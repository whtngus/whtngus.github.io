# yum update
sodo yum update -y
# ftp install
sudo yum -y install vsftpd

sudo apt-get install python3-pip -y
# docker install
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
sudo yum makecache fast -y
sudo yum -y install docker-ce
sudo systemctl start docker
# makdir
sudo mkdir /data
sudo chown whtngus32:whtngus32 /data
# docker pull and run
sudo docker pull whtngus3232/bert
sudo docker run -v /data:/data -i -t whtngus3232/bert /bin/bash

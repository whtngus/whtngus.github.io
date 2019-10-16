# yum update
sodo apt-get update -y
# ftp install
sudo apt-get -y install vsftpd

sudo apt-get install python3-pip -y
sudo apt-get install python-pip -y
# docker install
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
sudo apt-cache policy docker-ce
sudo apt install docker-ce -y
# 도커 정상실행 확인
sudo systemctl status docker
# makdir
sudo mkdir /data
sudo chown whtngus32:whtngus32 /data
# docker pull and run
sudo docker pull gcr.io/tpu-pytorch/xla:nightly
sudo docker run -it -v /data:/data --shm-size 16G gcr.io/tpu-pytorch/xla:nightly


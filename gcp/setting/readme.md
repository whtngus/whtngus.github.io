## 기타 설정 

#### 추가 디스크 마운트를 직저 해줘야함
 웹에서 디스크 셋팅후 마운트만 vm에서 진행
 ```
 마운트할 로컬 SSD식별
$lsblk 
 ssd 포맷하기 (Name적어주면 됨)
$sudo mkfs.ext4 -F /dev/[SSD_ID]
마운트할 디렉토리 생성 -> 위치는 편한곳에
$sudo mkdir -p /mnt/disks/[mnt_dir]
마운트 하기
$sudo mount /dev/[ssd_id] /mnt/disk/[mnt_dir]
 ```
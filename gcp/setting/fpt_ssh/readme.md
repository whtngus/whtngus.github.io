## FTP 설정
1. Puttygen을 이용해 public/private key생성 
>> 1. Generate 클릭
>> 2. key comment를 google vm 인스턴스에서 사용하는 서버ID로 지정
>> 3. key값을 복사하고 save private key 버튼을 눌러 key를 파일로 저장한다.
>> 4. 
2. GCP의 Compute Engine탭에서 좌측 바의 메타데이터를 클릭
3. 메타데이터 생성 및 SSH창으로 이동
4. 키 입력 (privatekey를 putty등록시 접속 가능 해짐)

### 셋팅
```
ftp 설정 필요
sudo vi /etc/vsftpd/vsftpd.conf
12번라인 
annoymous_enable No --> 변경
94번라인
python 3version install
100번 라인 대에  접속 허용리스트 설정
chroot_list_enable=YES  chroot_list_file=/etc/vsftpd/chroot_list
sudo vi /etc/vsftpd/chroot_lis 계정 설정
ipv6 No로 변경 listen_ipv6=NO
포트 변경
listen=YES -> 변경   listen_port="포트번호" listen_ipv6=NO  -> 추가

```
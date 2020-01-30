# jupyter notebook 외부접속 허용하기
```

jupyter notebook --generate-config
# 비밀번호 입력
cypered=`python3 -c "from notebook.auth import passwd;print(passwd())"`
sed -i "s/^#c.NotebookApp.ip = 'localhost'/c.NotebookApp.ip='*'/" ~/.jupyter/jupyter_notebook_config.py
sed -i "s/^#c.NotebookApp.password = ''/c.NotebookApp.password = '$cypered'/" ~/.jupyter/jupyter_notebook_config.py
sed -i "s/^#c.NotebookApp.open_browser = True/c.NotebookApp.open_browser = False/" ~/.jupyter/jupyter_notebook_config.py
# 이제 실행  gpu 권한 받기위해 뒤에 옵션 추가
jupyter notebook --allow-root

- centos의 경우 방화벽 해제 
firewall-cmd --get-active-zones
firewall-cmd --zone=public --add-port=8888/tcp
```
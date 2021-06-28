# 프로젝트 개요
회원가입, 로그인, 로그아웃 기능 포함하는 Flask 어플리케이션 구현 
<br>pytest 활용해 유닛테스트 코드 구현
<br><br>

# 실행방법
```bash
$ /bin/bash settings.sh
$ python3 app.py
```
'http://localhost:5000' 접속 >> 홈 화면으로 이동
<br><br>

# 파이썬 모듈
  - flask
  - pymongo 
  - redis 
  - Flask-WTF 
  - Flask-Session
<br><br>

# UI 테스트

### 1) 회원가입

  - `'http://localhost:5000/signup/'`
  - `새 계정 생성 및 MongoDB와 연동 확인`
  - `ID/PW 유효성 검사`

    - 부트스트랩 활용
    
      ![그림1](https://user-images.githubusercontent.com/42771578/123518526-3f205000-d6e1-11eb-8a58-8b7e86f21c96.png)

    - wtforms 적용, flash 메세지
    
      ![그림2](https://user-images.githubusercontent.com/42771578/123518529-40517d00-d6e1-11eb-8107-aedf19ff0590.png)

### 2) 로그인/아웃

  - `'http://localhost:5000/login/', 'http://localhost:5000/logout/'`
  - `세션 타임아웃 확인 완료`
  - `ID/PW 유효성 검사`
    - 로그인 화면
        
      ![그림4](https://user-images.githubusercontent.com/42771578/123538797-658dcc00-d771-11eb-9e68-3b14ded13221.png)
      
    - flash 메세지

      ![그림5](https://user-images.githubusercontent.com/42771578/123538799-66bef900-d771-11eb-974b-c5b21d716980.png)
      
    - 홈 화면 (로그아웃)
      
      ![그림6](https://user-images.githubusercontent.com/42771578/123539713-f23a8900-d775-11eb-8491-ad97ca583333.png)

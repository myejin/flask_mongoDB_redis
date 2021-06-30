def test_signup_page(test_client):
    # 회원가입 페이지 접속
    resp = test_client.get('/signup/')
    assert resp.status_code == 200

def test_valid_signup(test_client, test_db):
    # 회원가입 성공 
    resp = test_client.post('/signup/', data = dict(
        userid = 'test002',
        password = 'test002!',
        re_pw = 'test002!'
    ),
    follow_redirects = True)
    assert resp.status_code == 200
    #assert b'Signed up successfully.' in resp.data 
    assert b"The CSRF token is missing." not in resp.data
    assert b'Please match the ID length.' not in resp.data
    assert b'The ID already exists.' not in resp.data
    assert b'Please match the Password length.' not in resp.data
    assert b'Must contain alphabetic, numeric, and special characters.' not in resp.data
    assert b'The password does not match.' not in resp.data

def test_invalid_signup(test_client, test_db):
    # 1. ID 길이 
    resp = test_client.post('/signup/', data = dict(
        userid = 'test1',
        password = 'test002!',
        re_pw = 'test002!'
    ),
    follow_redirects = True)
    assert b'Please match the ID length.' in resp.data
    
    # 2. 이미 존재하는 ID 
    resp = test_client.post('/signup/', data = dict(
        userid = 'test001',
        password = 'test001!',
        re_pw = 'test001!'
    ),
    follow_redirects = True)
    assert b'The ID already exists.' in resp.data

    # 3. PW 길이
    resp = test_client.post('/signup/', data = dict(
        userid = 'test002',
        password = 'test2!',
        re_pw = 'test2!'
    ),
    follow_redirects = True)
    assert b'Please match the Password length.' in resp.data

    # 4. 비밀번호 영문자, 숫자, 특수문자 미포함
    resp = test_client.post('/signup/', data = dict(
        userid = 'test002',
        password = 'test002',
        re_pw = 'test002'
    ),
    follow_redirects = True)
    assert b'Must contain alphabetic, numeric, and special characters.' in resp.data

    # 5. 비밀번호 확인 불일치 
    resp = test_client.post('/signup/', data = dict(
        userid = 'test002',
        password = 'test002!',
        re_pw = 'test002'
    ),
    follow_redirects = True)
    assert b'The password does not match.' in resp.data

    assert b"The CSRF token is missing." not in resp.data


def test_login_page(test_client):
    # 로그인 페이지 접속
    resp = test_client.get('/login/')
    assert resp.status_code == 200

def test_valid_login(test_client, test_db):
    # 로그인 성공 
    resp = test_client.post('/login/', data = dict(
        userid = 'test001',
        password = 'test001!',
        re_pw = 'test001!'
    ),
    follow_redirects = True)
    assert resp.status_code == 200
    assert b'The ID does not exist.' not in resp.data
    assert b'The password does not match.' not in resp.data

def test_invalid_login(test_client, test_db):
    # 1. 존재하지 않는 ID 
    resp = test_client.post('/login/', data = dict(
        userid = 'test002',
        password = 'test002!'
    ),
    follow_redirects = True)
    assert b'The ID does not exist.' in resp.data
    
    # 2. 비밀번호 불일치
    resp = test_client.post('/login/', data = dict(
        userid = 'test001',
        password = 'test001'
    ),
    follow_redirects = True)
    assert b'The password does not match.' in resp.data

    assert b"The CSRF token is missing." not in resp.data
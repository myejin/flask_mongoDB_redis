import re

def test_invalid_signup(test_client, test_db):
    resp = test_client.post('/signup/', data = dict(
        userid = 'test1',
        password = 'test002!',
        re_pw = 'test002!'
    ),
    follow_redirects = True)
    assert b'Please match the ID length.' in resp.data
    
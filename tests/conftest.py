import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pytest
from mongomock import MongoClient
from project import create_app


@pytest.fixture(scope='module')
def test_client():
    app = create_app('flask_test.cfg')
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client  


@pytest.fixture(scope='module')
def test_db(test_client):
    conn = MongoClient('localhost')
    doc = {
        'userid' : 'test001',
        'password' : 'test001!'
    }
    conn.db.user.insert_one(doc)
    yield
    conn.close()
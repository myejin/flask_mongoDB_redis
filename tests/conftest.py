import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pytest
from project import create_app, mongo 

@pytest.fixture(scope='module')
def test_client():
    app = create_app('flask_test.cfg')
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client  


@pytest.fixture(scope='module')
def test_db():
    doc = {
        'id' : 'test001',
        'pw' : 'test001!'
    }
    mongo.db.user.insert_one(doc)
    yield 
    mongo.db.user.drop()
    
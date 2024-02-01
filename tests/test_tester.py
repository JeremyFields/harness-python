sys.path.append('../dronedemo')
from dronedemo.main import app

def test_pytest():
  assert True

def test_api():
  response = app.test_client().get("/")
  assert response.status_code == 200

from fastapi.testclient import TestClient
import sys
sys.path.insert(0, '../final')
from main import app

client = TestClient(app)
_id = None

def test_hello_msg():
    url = "/hello"
    expected_result = {"msg": "Hello World"}
    actual_result = client.get(url)
    assert actual_result.status_code == 200
    assert actual_result.json() == expected_result

def test_post_insert():
    url = "/"
    actual_result = client.post(
        url,
        json = {
            "motorcycle_code": "Mot1246",
            "motorcycle_name": "win",
            "motorcycle_price" : "20000",
            "down_payment" : "5000",
        }
    )
    expected_result = "Mot1246"
    global _id 
    _id = actual_result.json()[0]['id']
    assert actual_result.status_code == 200
    assert actual_result.json()[0]['motorcycle_code'] == expected_result


def test_get_by_id():
    url = "/"+_id
    actual_result = client.get(url)
    expected_result = "Mot1246"
    assert actual_result.status_code == 200
    assert actual_result.json()['motorcycle_code'] == expected_result
    

def test_put_x_update():
    url = "/"+_id
    actual_result = client.put(
        url,
        json = {
            "motorcycle_code": "Mot1357",
            "motorcycle_name": "win",
            "motorcycle_price" : "20000",
            "down_payment" : "5000",
        }
    )
    expected_result = "Mot1357"
    assert actual_result.status_code == 200
    assert actual_result.json()[0]['motorcycle_code'] == expected_result

def test_delete_by_id():
    url = "/"+_id
    actual_result = client.delete(url)
    assert actual_result.status_code == 200
    assert actual_result.json()['status'] == "ok"
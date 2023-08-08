from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_sensors_data():
    response = client.get("/v1/data")
    assert response.status_code == 200
    assert "data" in response.json()

def test_receive_data():
    input_data = {
        "data": [
            {
                "timestamp": "2018-04-18 04:41:00",
                "machine_status": "RECOVERING",
                "sensors": [
                    {"name": "sensor_07", "value": 11.37153},
                    {"name": "sensor_47", "value": 29.513890000000004},
                ],
            },
        ]
    }
    response = client.post("/v1/receiveData", json=input_data)
    assert response.status_code == 200
    assert response.json() == {'message': 'Data received and processed successfully'}

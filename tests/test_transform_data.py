from src.infra.v1.datasources.transform_data import transform_data

def test_transform_data():
    data_tuples = [
        ("2018-04-18 04:41:00", 11.37153, 29.51389, "RECOVERING"),
    ]
    result = transform_data(data_tuples)
    expected = {
        "data": [
            {
                "timestamp": "2018-04-18 04:41:00",
                "machine_status": "RECOVERING",
                "sensors": [
                    {"name": "sensor_07", "value": 11.37153},
                    {"name": "sensor_47", "value": 29.51389},
                ],
            },
        ]
    }
    assert result == expected
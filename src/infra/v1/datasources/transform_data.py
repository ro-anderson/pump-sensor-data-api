from typing import Dict, List

def transform_data(data_tuples: List[tuple]) -> Dict:
    """
    Transforms raw sensor data into a structured dictionary format.

    This function takes a list of tuples containing sensor data and applies specific filtering criteria to the values
    of sensor_07 and sensor_47. The resulting data is organized into a JSON-friendly dictionary format.

    Criteria:
        - sensor_07: Values must be greater than or equal to 10 and less than or equal to 30.
        - sensor_47: Values must be greater than or equal to 20 and less than or equal to 30.

    The purpose of this transformation is to ensure that only relevant sensor data is included in the response,
    adhering to the constraints defined for the project.

    Args:
        data_tuples (List[tuple]): A list of tuples containing sensor data. Each tuple consists of
                                  timestamp, sensor_07 value, sensor_47 value, and machine_status.

    Returns:
        Dict: A dictionary containing the transformed data, organized into a structure that includes
              timestamp, machine_status, and filtered sensor values based on the criteria.

    Example:
        Input: [(timestamp, 12.5, 25.0, 'RECOVERING'), ...]
        Output: {"data": [{"timestamp": timestamp, "machine_status": "RECOVERING", "sensors": [{"name": "sensor_07", "value": 12.5}, {"name": "sensor_47", "value": 25.0}]} ...]}
    """
    if not data_tuples:
        return {"data": []}

    data = []
    for item in data_tuples:
        timestamp, sensor_07, sensor_47, machine_status = item
        sensors = []

        if sensor_07 is not None and 10 <= sensor_07 <= 30:
            sensors.append({"name": "sensor_07", "value": sensor_07})
        
        if sensor_47 is not None and 20 <= sensor_47 <= 30:
            sensors.append({"name": "sensor_47", "value": sensor_47})

        data_entry = {
            "timestamp": timestamp,
            "machine_status": machine_status,
            "sensors": sensors
        }
        data.append(data_entry)
    return {"data": data}

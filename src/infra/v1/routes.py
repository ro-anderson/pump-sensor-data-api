from fastapi import APIRouter

from fastapi import FastAPI
from typing import List, Dict, Optional
from src.infra.config import DBConnectionHandler
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import text

from pydantic import BaseModel

import pandas as pd

router = APIRouter()

def transform_data(data_tuples: List[tuple]) -> Dict:
    if not data_tuples:
        return {"data": []}

    data = []
    for item in data_tuples:
        timestamp, sensor_07, sensor_47, machine_status = item
        data_entry = {
            "timestamp": timestamp,
            "machine_status": machine_status,
            "sensors": [
                {"name": "sensor_07", "value": sensor_07},
                {"name": "sensor_47", "value": sensor_47}
            ]
        }
        data.append(data_entry)
    return {"data": data}

@router.get("/data")
async def get_data():
    """Filters the sensor data from April 2018 for sensors 07 and 47 with the values according to the constraints mentioned in the project disclaimers"""

    with DBConnectionHandler() as db_connection:
        try:

            engine = db_connection.get_engine()
            conn = engine.connect() 

            query = """
			SELECT
			sd."timestamp" ,
			sd.sensor_07 ,
			sd.sensor_47 ,
			sd.machine_status 
			FROM sensor_data sd
			WHERE strftime('%Y-%m', timestamp) = '2018-04'
			AND (sensor_47  BETWEEN  20 AND 30)
			AND (sensor_07 BETWEEN 10 AND 30)            
			LIMIT 4
            """
            result_proxy = conn.execute(text(query))
            data = result_proxy.fetchall()
            
            data_tuples = transform_data(data)

        except NoResultFound:
            print("not found")
        except:
            db_connection.session.rollback()
            raise
        finally:
            db_connection.session.close()


    # Transforming the data into the required JSON structure

    return data_tuples


class SensorData(BaseModel):
    name: str
    value: float

class DataEntry(BaseModel):
    timestamp: str
    machine_status: str
    sensors: List[SensorData]

class DataInput(BaseModel):
    data: List[DataEntry]

@router.post("/receiveData")
async def receive_data(input_data: DataInput):
    """Receives the filtered data and organizes it into a Pandas DataFrame that is printed at the service running terminal."""

    # Initialize an empty list to store the output rows
    output_rows = []

    # Iterate over the data, extracting and transforming the relevant information
    for entry in input_data.data:
        timestamp = pd.to_datetime(entry.timestamp)
        date = timestamp.date()
        time = timestamp.time()
        machine_status = entry.machine_status

        for sensor in entry.sensors:
            if 10 <= sensor.value <= 30:
                output_rows.append({
                    'Date': date,
                    'Time': time,
                    'Sensor': sensor.name,
                    'Measurement': sensor.value,
                    'Status': machine_status
                })

    # Convert the output rows to a DataFrame
    output_df = pd.DataFrame(output_rows)

    # Display the DataFrame to the console
    print(output_df)

    return {'message': 'Data received and processed successfully'}
# Sensor Data API

This project provides a set of APIs to manage and process sensor data. It includes two main services: a data retrieval service and a data reception service. The project is built using FastAPI and makes use of SQLite for data storage.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Examples](#api-examples)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Data Retrieval Service (GET API):** Fetches filtered sensor data based on specified criteria (e.g., date range, sensor values, etc.).
- **Data Reception Service (POST API):** Accepts sensor data in JSON format and organizes it into a structured Pandas DataFrame.

## Installation

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/sensor-data-api.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd sensor-data-api
    ```

3. **Download the Sensor Data:**
   The `sensor.csv` file is not included in the repository. You must download it from [Kaggle](https://www.kaggle.com/datasets/nphantawee/pump-sensor-data) and place it in the root directory of the project.

4. **Create the SQLite Database:**
    ```bash
    make create_db
    ```

5. **Install Poetry (If Not Already Installed):**
    ```bash
    curl -sSL https://install.python-poetry.org | python -
    ```

6. **Install Project Dependencies with Poetry:**
    ```bash
    poetry install
    ```

7. **Start the FastAPI Server Using the Make Command:**
    ```bash
    make run
    ```

## Usage

1. **Access the APIs at:**
    - GET request: `http://0.0.0.0:5001/data`
    - POST request: `http://0.0.0.0:5001/receiveData`

## API Examples

You can use the following curl commands to interact with the APIs:

**GET Request:**
```bash
curl -X 'GET' 'http://0.0.0.0:5001/data' -H 'accept: application/json'
```

**POST Request:**
```bash
curl -X 'POST' \
  'http://0.0.0.0:5001/receiveData' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data": [
    {
      "timestamp": "2018-04-18 04:41:00",
      "machine_status": "RECOVERING",
      "sensors": [
        {
          "name": "sensor_07",
          "value": 11.37153
        },
        {
          "name": "sensor_47",
          "value": 29.513890000000004
        }
      ]
    },
    {
      "timestamp": "2018-04-18 04:42:00",
      "machine_status": "RECOVERING",
      "sensors": [
        {
          "name": "sensor_07",
          "value": 11.32089
        },
        {
          "name": "sensor_47",
          "value": 29.513890000000004
        }
      ]
    },
    {
      "timestamp": "2018-04-18 04:43:00",
      "machine_status": "RECOVERING",
      "sensors": [
        {
          "name": "sensor_07",
          "value": 11.32089
        },
        {
          "name": "sensor_47",
          "value": 29.22454
        }
      ]
    },
    {
      "timestamp": "2018-04-18 04:44:00",
      "machine_status": "RECOVERING",
      "sensors": [
        {
          "name": "sensor_07",
          "value": 11.32813
        },
        {
          "name": "sensor_47",
          "value": 29.224536895752
        }
      ]
    }
  ]
}'
```

## Project Structure

````bash
.
├── Makefile
├── README.md
├── create_db.py
├── main.py
├── poetry.lock
├── pyproject.toml
├── sensor.csv              # MUST be there before running: make create_db
├── sensor_data.db          # MUST be here before running the application (make run)
└── src
    ├── __init__.py
    └── infra
        ├── __init__.py
        ├── config
        │   ├── __init__.py
        │   ├── db_base.py
        │   └── db_config.py
        └── test
            └── __init__.py

````

- `main.py`: Main file containing the FastAPI app and API endpoints.
- `db_config.py`: Configuration for the SQLite database.
- `db_base.py`: Base configuration for database interactions.


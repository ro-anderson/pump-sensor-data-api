import sqlite3
import pandas as pd

# Define the database name
database_name = "sensor_data.db"

# Connect to the SQLite database
conn = sqlite3.connect(database_name)

# Read the CSV file into a DataFrame
data = pd.read_csv("sensor.csv")

# Write the data to a SQLite table
data.to_sql("sensor_data", conn, if_exists="replace", index=False)

# Check if the data has been loaded correctly
query_result = pd.read_sql_query("SELECT * FROM sensor_data LIMIT 5", conn)

print(query_result)

.PHONY: run clean create_db test

SHELL=/bin/bash                                                                                                                                                                                             
## Up the server on 0.0.0.0:5001 using poetry
run:
	poetry run python main.py

## Delete all .png, .csv, .txt and cache files
clean:
	find . -name "__pycache__" -type d -exec rm -r {} \+

## Create sqlite db based on sensor.csv data (download at: https://www.kaggle.com/datasets/nphantawee/pump-sensor-data)
create_db:
	poetry run python create_db.py

## Run tests with pytest using poetry
test:
	poetry run pytest tests -v
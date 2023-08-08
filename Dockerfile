# Base image
FROM python:3.10 AS base

# Set the working directory inside the container
WORKDIR /app

# Copy the local directory contents into the container
COPY . /app

# Install unzip utility
RUN apt-get update && apt-get install -y unzip

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python -

# Update the PATH to include the Poetry binary
ENV PATH="/root/.local/bin:${PATH}"

# Unzip the sensor_data.db.zip file
RUN unzip -o sensor_data.db.zip

# Check if the sensor_data.db file exists at the root of the project
RUN [ -f /app/sensor_data.db ] || echo "The file sensor_data.db must be at the root of the project to run. Try to unzip manually before building the image."

# Install the required dependencies using Poetry
RUN poetry install

# Expose the port the app runs on
EXPOSE 5001

# Production stage
FROM base AS prod

# Command to run the application
CMD ["make", "run"]

# Test stage
FROM base AS test

# Command to run the tests
CMD ["make", "test"]

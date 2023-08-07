# Use the standard Python 3.10 image (not Alpine)
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the local directory contents into the container
COPY . /app

# Install poetry
RUN curl -sSL https://install.python-poetry.org | python -

#RUN poetry install

# Update the PATH to include the Poetry binary
ENV PATH="/root/.local/bin:${PATH}"

# Check if sensor_data.db exists, if not, create it
RUN [ ! -f /app/sensor_data.db ] && make create_db || echo "sensor_data.db exists"

# Install the required dependencies using Poetry
RUN poetry install

# Expose the port the app runs on
EXPOSE 5001

# Command to run the application
CMD ["make", "run"]


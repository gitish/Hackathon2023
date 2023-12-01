# Use an official Python runtime as a base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and requirements file into the container
COPY requirements.txt .
COPY generate_synthetic_data.py .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Command to execute the Python script for generating synthetic data
CMD ["python", "generate_synthetic_data.py"]

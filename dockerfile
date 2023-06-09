# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Set the entrypoint command for the container
CMD ["python", "app.py"]
# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["uvicorn", "mms_app_backend.main:app", "--host", "0.0.0.0", "--port", "8080"]

# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt ./

# Install the necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code to the container
COPY . .

# Set environment variables for Flask and Gunicorn
ENV FLASK_APP=core.server:app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=7755

# Expose the port the app runs on
EXPOSE 7755

# Command to run the application with Gunicorn
CMD ["gunicorn", "--config", "gunicorn_config.py", "core.server:app"]

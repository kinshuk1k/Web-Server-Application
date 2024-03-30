# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install --upgrade Flask 
RUN pip install gunicorn

# Expose the port the app runs on
EXPOSE 2000
# Define environment variable to run the app in production mode
ENV FLASK_ENV=production

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:2000", "web_server:app"]
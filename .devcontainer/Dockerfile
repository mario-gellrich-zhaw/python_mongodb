# Use the official Python image from the Docker Hub
FROM mcr.microsoft.com/devcontainers/python:3.11-bullseye

# Install MongoDB
RUN apt-get update && apt-get install -y gnupg wget \
    && wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | apt-key add - \
    && echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/debian buster/mongodb-org/6.0 main" | tee /etc/apt/sources.list.d/mongodb-org-6.0.list \
    && apt-get update && apt-get install -y mongodb-org \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create MongoDB data directory
RUN mkdir -p /data/db

# Expose MongoDB port
EXPOSE 27018

# Start MongoDB when the container starts
CMD ["mongod", "--bind_ip_all"]

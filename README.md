# CMPE--272-Assignment-2--Microservices-And-Kubernetes

## Flask Blog Microservices
This repository contains the microservices architecture of a Flask blog application, which has been refactored from a monolithic design. The application is containerized using Docker and is deployable on Kubernetes.

## Overview
The Flask blog application has been broken down into the following microservices:

* User Service: Handles user registration, authentication, and user-related operations.
* Blog Service: Manages blog posts, including creating, updating, deleting, and retrieving posts.
* Frontend Service: Serves the frontend of the application, rendering templates and interacting with other services.
* Database Service: A containerized PostgreSQL (or any other database) to manage database operations.

## Containerization
Each service is containerized using Docker. You can find the Dockerfiles for each service in their respective directories.

## Building Docker Images
Navigate to the directory containing the Dockerfile for a service and run:

``` docker build -t <username>/<service-name>:latest ``` .
Replace <username> with your DockerHub username and <service-name> with the name of the service (e.g., user-service).

## Pushing Docker Images
After building, push the Docker image to DockerHub or your preferred registry:

``` docker push <username>/<service-name>:latest ```
Kubernetes Deployment
Kubernetes manifests for deploying the services are available in the k8s directory. These include configurations for deployments, services, and other necessary resources.

Getting Started
Clone this repository:

``` git clone https://github.com/<username>/flask-blog-microservices.git ```
``` cd flask-blog-microservices ```

Build and push Docker images for each service as described above.

Deploy the application on Kubernetes:


``` kubectl apply -f k8s/ ```
Access the frontend service to interact with the application.

## Screenshots
Screenshots of the running application and Kubernetes resources can be found in the screenshots directory.

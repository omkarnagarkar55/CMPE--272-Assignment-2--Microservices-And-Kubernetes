# CMPE 272 Assignment 2: Microservices And Kubernetes
### Application Report :- (Link To Report)[https://github.com/omkarnagarkar55/CMPE--272-Assignment-2--Microservices-And-Kubernetes/blob/main/ESP%20Assignment%202%20-%20Team%20Yoda.pdf]
## Flask Blog Microservices
This repository contains the microservices architecture of a Flask blog application, which has been refactored from a monolithic design. The application is containerized using Docker and is deployable on Kubernetes.

## Overview
The Flask blog application has been broken down into the following microservices:
- **Post Service**: Manages blog posts, including creating, updating, deleting, and retrieving posts.
- **Frontend Service**: Serves the frontend of the application, rendering templates and interacting with other services.
- **Database Service**: A containerized PostgreSQL (or any other database) to manage database operations.

## Pre-requisites
- Minikube (contains kubectl as a dependency)
- Docker

## Containerization
Each service is containerized using Docker. You can find the Dockerfiles for each service in their respective directories.

## Building Docker Images
1. Build the Docker image for the frontend and posts service:
   ```sh
   docker build -t <YOUR_DOCKERHUB_USERNAME>/flaskblog-frontend:latest -f Dockerfile-frontend
   docker build -t <YOUR_DOCKERHUB_USERNAME>/flaskblog-posts-service:latest -f Dockerfile-posts-service
   
2. Push the Docker image to Docker Hub:
   ```docker push <YOUR_DOCKERHUB_USERNAME>/flaskblog-frontend:latest ```
   ```docker push <YOUR_DOCKERHUB_USERNAME>/flaskblog-posts-service:latest```

## Kubernetes Deployment

### Deployment Steps
1. Create a cluster using minikube: ```minikube start --vm-driver=docker```
2. Apply the Kubernetes manifests: ```kubectl apply -f k8s/```
3. Access the frontend service to interact with the application.
Kubernetes manifests for deploying the services are available in the k8s directory. These include configurations for deployments, services, and other necessary resources.

## Screenshots

![image](https://github.com/omkarnagarkar55/CMPE--272-Assignment-2--Microservices-And-Kubernetes/assets/60735358/621c807c-2732-4460-89e3-57f76c4f7508)


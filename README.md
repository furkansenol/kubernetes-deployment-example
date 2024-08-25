# Flask Hello World Application

This project demonstrates how to deploy a simple Flask "Hello World" application on Kubernetes. It includes the necessary Kubernetes manifests for deployment, service, Ingress class, and Ingress resource.

## Prerequisites

- Kubernetes cluster (e.g., Minikube, kind, or a managed Kubernetes service)
- kubectl CLI tool
- Docker (to build and push the image)

## Project Structure

- `Dockerfile`: Dockerfile for building the Flask application image
- `deployment.yaml`: Kubernetes Deployment resource
- `service.yaml`: Kubernetes Service resource
- `ingress-class.yaml`: IngressClass resource (for NGINX Ingress controller)
- `ingress.yaml`: Ingress resource to route traffic

## Build and Push Docker Image

1. **Build the Docker Image:**
   ```bash
   docker build -t your-dockerhub-username/hello-world-app:latest .
   docker push your-dockerhub-username/hello-world-app:latest
   ```

    Replace "hello-world-app" with your repository name on Docker Hub.

    This step is not needed to run the example project as it already uses an image from public Docker Hub repository.

## Using the application

1. **Applying Kubernetes Manifests**

    Use `make start` command to apply Kubernetes manifests. This command will apply related Kubernetes files using command `kubectl apply -f <resource-file-name>`. You can see Makefile for commands.

    Warning: If you get an error during creation of Kubernetes resources please run `make start` command again. This should be fixed soon.

2. **Accessing the application**

    Use your browser or any API tool to send a GET request to your application. Application uses `http://localhost/hello-world-app` as default. You should see `Hello World!` as response.

3. **Stopping the application**

    Use `make stop` to delete all running Kubernetes resources related to application.

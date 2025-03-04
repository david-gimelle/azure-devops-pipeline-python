# Python Demo Application

Simple example of a Python/FastAPI/Poetry demo Api Application

# Requirements for this app
- Python 3
- Poetry 1.1.11
- FastAPI 

# Setup the application localy

- Install Poetry
> pip install poetry==1.1.11

- build the application project and its dependencies
> poetry install

# Install and build an image of the project
use the script below. This script will ensure poetry 1.1.11 is used to install the project and build an the image
> python install-build.py

you can skip the tests with --skip-tests
> python install-build.py --skip-tests

you can skip the installation of the project and dependency with --skip-install-poetry
> python install-build.py --skip-install-poetry

you can skip build the image with --skip-poetry
> python install-build.py --skip-build-images

# Run the application

python3 and poetry are required.

Run the Application localy with this command and check the url returned
> poetry run python main.py

Ping the app on http://127.0.0.1:5001/ping

Demo on http://127.0.0.1:5001/demo

# Run the unit tests

Run the unit tests with 
> poetry run pytest

# How to change port and url of the react application for cors authorisation

This is configurable from the file config.py

# Images

you can build one localy with this command
> docker build -t python-demo-api .
> docker build --no-cache --progress=plain -t python-demo-api .

You build an image with this script
> python install-build.py
> python install-build.py --skip-install-poetry --skip-tests

Run the image with this command
> docker run -p 5001:5001 python-demo-api

# Deployment to Azure Kubernetes Service (AKS)

This application is deployed to Azure Kubernetes Service (AKS) using Azure DevOps Pipelines.

## CI/CD Pipeline Overview

The deployment process consists of the following stages:

1. **Build Stage**
   - Sets up Python and Poetry
   - Installs dependencies
   - Builds and tests the application
   - Creates and pushes a Docker image to GitHub Container Registry

2. **Infrastructure Stage**
   - Deploys or updates the AKS cluster using Terraform
   - Configures network and security settings

3. **Deploy Stage**
   - Retrieves AKS credentials
   - Updates the Kubernetes manifest with the current image tag
   - Creates necessary Kubernetes secrets for image pulling
   - Deploys the application to AKS
   - Verifies the deployment

## Prerequisites for Deployment

- Azure DevOps project with a service connection to Azure
- GitHub Container Registry credentials stored as pipeline variables
- Terraform state storage in Azure Blob Storage

## Kubernetes Resources

The application is deployed with the following Kubernetes resources:
- Deployment with the container image
- Service to expose the application
- ConfigMap for application configuration
- Secret for container registry authentication
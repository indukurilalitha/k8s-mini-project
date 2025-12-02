# 🚀 Kubernetes Mini Project – Flask App on Docker & Minikube

This project demonstrates how to build, containerize, and deploy a simple Python Flask application using **Docker**, **Kubernetes**, and **Minikube**.  
It also includes **unit testing with pytest** and is fully version-controlled using Git & GitHub.

This is a perfect beginner-to-intermediate project to learn cloud-native development and Kubernetes fundamentals.

---

## 📁 Project Structure

k8s-mini-project/
├── app.py # Flask application
├── Dockerfile # Docker container definition
├── requirements.txt # Python dependencies
├── test_app.py # Unit test for Flask API
├── deployment.yaml # Kubernetes Deployment configuration
├── service.yaml # Kubernetes Service (NodePort)


---

## 🚀 Features

- ✔ Flask REST API (`/` endpoint)
- ✔ Docker containerization with Python 3.10-slim
- ✔ Kubernetes Deployment + Service
- ✔ Exposed via NodePort on Minikube
- ✔ Unit tests using pytest
- ✔ GitHub version control
- ✔ Works entirely on local setup using Minikube

---

## 🧪 API Details

**Endpoint:**  
GET /


**Response:**  
```json
{
  "message": "Hello from Kubernetes!"
}

🧪 Unit Testing (pytest)
Run all tests:

bash
Copy code
pytest
This ensures the Flask endpoint returns the expected JSON response.

🐳 Docker Setup
Build the Docker image:
docker build -t my-k8s-app:local .

Run the container locally:
docker run -p 5000:5000 my-k8s-app:local

☸ Kubernetes Deployment
Load the image into Minikube:
minikube image load my-k8s-app:local

Apply Deployment:
kubectl apply -f deployment.yaml

Apply Service:
kubectl apply -f service.yaml

Check resources:
kubectl get pods
kubectl get services

🌐 Access the Application

To open the app in browser:

minikube service my-k8s-service


Or manually open:

http://localhost:30007

🧰 Tools & Technologies Used

Python

Flask

Docker

Kubernetes

Minikube

kubectl

pytest

Git & GitHub

📘 Learning Outcomes

By completing this project, you learn:

Building Python microservices

Containerizing applications with Docker

Working with Minikube clusters

Writing Kubernetes YAMLs

Deploying apps on Kubernetes

Exposing services using NodePort

Running unit tests

Using Git & GitHub for version control

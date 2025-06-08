# GKE Monitoring Pipeline

This project sets up a basic GKE cluster using Terraform and deploys a sample Python app with integrated monitoring using Prometheus and Grafana. CI/CD is handled via GitHub Actions. Designed for junior DevOps engineers to demonstrate real-world support, automation, and monitoring workflows.

## Tech Stack
- Google Kubernetes Engine (GKE)
- Terraform
- GitHub Actions (CI/CD)
- Docker
- Python (Flask)
- Prometheus + Grafana
- Kubernetes manifests

## Features
- GKE provisioning via Terraform
- Dockerized Flask app with Prometheus metrics endpoint
- CI/CD pipeline using GitHub Actions for image build and deploy
- Monitoring stack deployment with Prometheus + Grafana
- Helm-based deployment model for observability stack

## Prerequisites
- Google Cloud CLI configured
- Terraform installed
- GitHub Actions secrets set (GCP credentials)
- kubectl + Helm installed

## Setup

### 1. Provision GKE
```bash
cd terraform
terraform init
terraform apply
```

### 2. Deploy monitoring stack
```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install monitoring prometheus-community/kube-prometheus-stack
```

### 3. Deploy Python app
```bash
kubectl apply -f k8s-manifests/deployment.yaml
```

## Testing

Access the Flask app (NodePort or LoadBalancer) and hit `/metrics` to see Prometheus metrics:
```
curl http://<EXTERNAL-IP>:5000/metrics
```

Access Grafana:
```
kubectl port-forward svc/monitoring-grafana 3000:80
```

Default login: `admin/prom-operator`

## Folder Structure
```
.
├── terraform/                 # GKE infra as code
├── github-actions/           # CI/CD pipeline config
├── docker/                   # Dockerfile for Flask app
├── k8s-manifests/            # K8s manifests for app
├── scripts/                  # Helper scripts
└── README.md
```

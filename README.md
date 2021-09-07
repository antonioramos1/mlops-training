# MLOps Training
![example workflow](https://github.com/antonioramos1/mlops-training/workflows/github_actions/badge.svg)
[![CI Pipeline status](https://github.com/antonioramos1/mlops-training/workflows/github_actions/badge.svg)](https://github.com/antonioramos1/mlops-training/actions)
![alt text](./imgs/banner-repo-mlops.png)

### 1. Create a MLFlow service
- Push image to an Azure Container Registry
- Deploy in an Azure Container Instance
- Use an Azure blob as artifact storage for model binaries

### 2. Integration pipeline - Train, register and validate model
- GitLab pipeline to train and validate the model
- Models and metadata are stored in MLFlow for governance and reproducibility

### 3. Build pipeline - Build and deploy model service
- GitLab pipeline to package the model from the MLFlow registry into a web-service using FastAPI and docker
- Push model image to an Azure Container Registry
- Update the previous model deployed in the Azure Container Instance

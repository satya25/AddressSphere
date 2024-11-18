#!/bin/bash
# Deploy to Kubernetes
kubectl apply -f ci_cd/kubernetes/deployment.yaml
kubectl apply -f ci_cd/kubernetes/service.yaml

#!/usr/bin/env bash
set -euo pipefail
source scripts/00_env.sh

# asegurar namespace/config
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml

# service placeholder (si luego IRSA lo crea, no pasa nada)
kubectl apply -f k8s/serviceaccount.yaml

# deploy app
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# verificar deploy
kubectl -n "$K8S_NAMESPACE" get pods
kubectl -n "$K8S_NAMESPACE" get svc

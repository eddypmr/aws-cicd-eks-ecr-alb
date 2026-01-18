#!/usr/bin/env bash
set -euo pipefail
source scripts/00_env.sh

# asegurar namespace/config
kubectl apply -f k8s/namespace.yaml
kubectl -n "$K8S_NAMESPACE" apply -f k8s/configmap.yaml
kubectl -n "$K8S_NAMESPACE" apply -f k8s/serviceaccount.yaml
kubectl -n "$K8S_NAMESPACE" apply -f k8s/deployment.yaml
kubectl -n "$K8S_NAMESPACE" apply -f k8s/service.yaml

# 3) verificar
kubectl -n "$K8S_NAMESPACE" get pods
kubectl -n "$K8S_NAMESPACE" get svc

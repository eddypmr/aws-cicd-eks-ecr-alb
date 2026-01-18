#!/usr/bin/env bash
set -euo pipefail
source scripts/00_env.sh

kubectl apply -f k8s/ingress.yaml
kubectl -n "$K8S_NAMESPACE" get ingress
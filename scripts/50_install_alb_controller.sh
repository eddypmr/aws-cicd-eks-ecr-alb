#!/usr/bin/env bash
set -euo pipefail
source scripts/00_env.sh

eksctl create addon \
  --name aws-load-balancer-controller \
  --cluster "$CLUSTER_NAME" \
  --region "$AWS_REGION" 
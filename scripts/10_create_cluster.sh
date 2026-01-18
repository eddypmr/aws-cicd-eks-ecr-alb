#!/usr/bin/env bash
set -euo pipefail
source scripts/00_env.sh

eksctl create cluster \
  --name "$CLUSTER_NAME" \
  --region "$AWS_REGION" \
  --nodes 2 \
  --nodes-type t3.micro \
  --managed
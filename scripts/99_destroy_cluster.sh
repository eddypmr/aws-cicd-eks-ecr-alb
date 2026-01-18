#!/usr/bin/env bash
set -euo pipefail
source scripts/00_env.sh

eksctl delete cluster --name "$CLUSTER_NAME" --region "$AWS_REGION"
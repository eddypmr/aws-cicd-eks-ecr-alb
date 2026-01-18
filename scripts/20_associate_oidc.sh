#!/usr/bin/env bash
set -euo pipefail
source scripts/00_env.sh

eksctl utils associate-iam-oidc-provider \
  --region "$AWS_REGION" \
  --cluster "$CLUSTER_NAME" \
  --approve 
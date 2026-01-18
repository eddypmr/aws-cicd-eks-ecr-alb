#!/usr/bin/env bash
set -euo pipefail
source scripts/00_env.sh

POLICY_ARN="arn:aws:iam::$AWS_ACCOUNT_ID:policy/project4-ddb-access"

eksctl create iamserviceaccount \
  --name "$APP_SA_NAME" \
  --namespace "$K8S_NAMESPACE" \
  --cluster "$CLUSTER_NAME" \
  --attach-policy-arn "$POLICY_ARN" \
  --approve \
  --region "$AWS_REGION"
  --override-existing-serviceaccounts
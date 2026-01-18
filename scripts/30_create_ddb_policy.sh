#!/usr/bin/env bash
set -euo pipefail
source scripts/00_env.sh

cat > ddb-policy.json <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DynamoDBAccess",
            "Effect": "Allow",
            "Action": [
                "dynamodb:PutItem",
                "dynamodb:GetItem",
                "dynamodb:DescribeTable",
                "dynamodb:Scan",
                "dynamodb:Query"
            ],
            "Resource": ["arn:aws:dynamodb:$AWS_REGION:$AWS_ACCOUNT_ID:table/service_registry",
                         "arn:aws:dynamodb:$AWS_REGION:$AWS_ACCOUNT_ID:table/service_status"]

        }
    ]
}
EOF

aws iam create-policy \
  --policy-name project4-ddb-access \
  --policy-document file://ddb-policy.json \
  --region "$AWS_REGION"

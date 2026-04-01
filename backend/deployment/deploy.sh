#!/bin/bash

# Deployment script for backend services

# Build and deploy backend services

aws cloudformation deploy --template-file backend/deployment/backend.yaml --stack-name backend-stack --capabilities CAPABILITY_IAM

# Deploy frontend service

aws s3 sync frontend/build s3://frontend-bucket --delete

# Update frontend service

aws cloudformation deploy --template-file frontend/deployment/frontend.yaml --stack-name frontend-stack --capabilities CAPABILITY_IAM
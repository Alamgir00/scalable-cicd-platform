# Scalable CI/CD Platform (AWS) — Example

This repository demonstrates an end-to-end CI/CD platform on AWS:
- Simple Flask app (Dockerized)
- Terraform to create ECR, ECS (Fargate), ALB, IAM roles, and networking
- GitHub Actions workflow to build, push, and deploy the app

> **Warning**: This example creates AWS resources that may incur cost. Destroy when finished: `terraform destroy`.

## Quick steps
1. Create a new GitHub repo and push this structure.
2. Create AWS credentials with permissions to manage ECR, ECS, ALB, IAM, EC2 (for networking).
3. Add GitHub repo secrets:
   - `AWS_REGION` (e.g. us-east-1)
   - `AWS_ACCOUNT_ID`
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
4. Initialize terraform and apply:
   ```bash
   cd infrastructure
   terraform init
   terraform apply -var="aws_region=us-east-1" -var="project=demo-cicd"

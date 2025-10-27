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

5. **Push code to GitHub** — GitHub Actions will build, push to ECR and update ECS service.

Push code to GitHub — GitHub Actions will build, push to ECR and update ECS service.

**Contents**

**/infrastructure** : Terraform for ECR, ECS Fargate service, load balancer, minimal VPC

**/.github/workflows/ci-cd.yml** : build/push/deploy pipeline

**/app** : sample Flask app + Dockerfile

/infrastructure : Terraform for ECR, ECS Fargate service, load balancer, minimal VPC

/.github/workflows/ci-cd.yml : build/push/deploy pipeline


**Notes:**

This workflow assumes the task family is **demo-cicd-task** and service/cluster names in Terraform are **demo-cicd-cluster** and **demo-cicd-service** — if you change names in Terraform, update the workflow accordingly.

The workflow builds the image tag from the Git commit short SHA.

**How to create the repo and push files (quick)**

# locally
mkdir scalable-cicd-platform && cd scalable-cicd-platform
# copy files as per structure above into proper files
git init
git add .
git commit -m "Initial commit — CI/CD sample app + Terraform infra"
# create repo on GitHub (or use gh CLI)
gh repo create skalamgir/scalable-cicd-platform --public --source=. --remote=origin
git push -u origin main

6. **Required GitHub secrets (Repository → Settings → Secrets & variables → Actions)**

AWS_REGION — e.g., us-east-1

AWS_ACCOUNT_ID — your AWS account id

AWS_ACCESS_KEY_ID — an IAM user key with permissions to manage ECR, ECS, ALB, IAM, EC2

AWS_SECRET_ACCESS_KEY

7. **Terraform deploy hints & next steps**
**terraform init → terraform plan → terraform apply -var="aws_region=us-east-1" -var="project=demo-cicd"**

After apply, Terraform outputs will show ecr_repo_url and alb_dns. You can access the service via the ALB DNS.

After initial apply, push code to GitHub main and GitHub Actions will build and push the image.

If you want the workflow to create the ECR repository if missing, add a step to create it with aws ecr create-repository (or rely on Terraform to create it).

8. **Security & production notes (important)**

Use private subnets for ECS tasks (public subnets used here for simplicity).

Use HTTPS for ALB with a certificate (ACM) for production.

Store minimal required IAM permissions for the CI runner — consider OIDC / GitHub Workflows OIDC provider for short-term credentials (more secure than long-lived keys).

Use separate AWS accounts/environments for dev/stage/prod.

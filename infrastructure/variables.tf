# infrastructure/variables.tf
variable "aws_region" {
  type    = string
  default = "us-east-1"
}
variable "project" {
  type    = string
  default = "demo-cicd"
}
variable "desired_count" {
  type    = number
  default = 1
}

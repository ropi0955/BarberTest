variable "webappName" {
  type    = string
  default = "app-weu-barbertest"
}

variable "dockerimageName" {
  type    = string
  default = "docker.io/ropi0955/barber-test:latest"
}

variable "extraAllowedHosts" {
  type = list(string)
  default = []
}

variable "azureSubscriptionId" {
  description = "Azure Subscription ID"
  type        = string
  default     = null
}

variable "tfStateName" {
  description = "Terraform Statefile Name"
  type        = string
  default     = "barber-webapp"
}
"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import ecr

# Creating an ECR repository
repository = ecr.Repository("dev-docker-images")

# Export the name of the repo
pulumi.export("repository", repository.repository_url)

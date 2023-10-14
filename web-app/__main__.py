"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service, Namespace
from pulumi_kubernetes.networking.v1 import Ingress
import pulumi_docker as docker

# Build the Docker image
#docker_image = docker.Image(
#    "web-app-image",
#    image_name=pulumi.StackReference("cryan1988/aws-resources/dev").get_output("repository"),
#    build=docker.DockerBuild(context='app/'),
#)

# Define the Kubernetes namespace
namespace = Namespace('web-app')

# Create Deployment within the specified namespace
deployment = Deployment('web-app-deployment',
    metadata={
        'namespace': namespace.metadata['name'],
        'labels': {'app': 'web-app'},
    },
    spec={
        'selector': {
            'match_labels': {'app': 'web-app'},
        },
        'replicas': 1,
        'template': {
            'metadata': {'labels': {'app': 'web-app'}},
            'spec': {
                'containers': [{
                    'name': 'web-app',
                    'image': '397008956043.dkr.ecr.us-east-1.amazonaws.com/dev-docker-images-78f25e8:latest',
                    'ports': [{'container_port': 8080}],
                }],
            },
        },
    })

# Create Service
service = Service('web-app-service',
    metadata={
        'labels': {'app': 'web-app'},
        'namespace': namespace.metadata['name'],
    },
    spec={
        'selector': {'app': 'web-app'},
        'ports': [{'port': 8080, 'target_port': 8080}],
        'type': "LoadBalancer",
    })

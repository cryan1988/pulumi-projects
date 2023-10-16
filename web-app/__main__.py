"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service, Namespace
from pulumi_kubernetes.networking.v1 import Ingress
#import pulumi_docker as docker
from pulumi_docker import Image

# Build the Docker image
#image = Image(
#    "web-app-image",
#    image_name=pulumi.StackReference("cryan1988/aws-resources/dev").get_output("repository"),
#    build="./app")

# Retrieve the customMessage configuration variable
config = pulumi.Config()
custom_message = config.require('customMessage')

# Create a namespace
namespace = Namespace('web-app',
    metadata={
        'name': 'web-app',
    })

# Create Deployment within the specified namespace
deployment = Deployment('web-app-deployment',
    metadata={
        'namespace': namespace.metadata['name'],
        'labels': {'app': 'web-app'},
        'name': 'web-app-deployment',
    },
    spec={
        'selector': {
            'match_labels': {'app': 'web-app'},
        },        
        'replicas': 1,
        'template': {
            'metadata': {
                'labels': {'app': 'web-app'},
            },
            'spec': {
                'containers': [{
                    'name': 'web-app',
                    'image': '397008956043.dkr.ecr.us-east-1.amazonaws.com/dev-docker-images-78f25e8:latest',
                    'ports': [{'container_port': 8080}],
                    'env': [{'name': 'MY_CUSTOM_MESSAGE', 'value': custom_message}],
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

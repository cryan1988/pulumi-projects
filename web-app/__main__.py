"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service, Namespace
from pulumi_kubernetes.networking.v1 import Ingress

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
        'replicas': 2,
        'template': {
            'metadata': {'labels': {'app': 'web-app'}},
            'spec': {
                'containers': [{
                    'name': 'web-app',
                    'image': 'docker.apps.papt.to/test/web-app-image',
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
        'ports': [{'port': 80, 'target_port': 8080}],
    })

# Create Ingress
#ingress = Ingress('web-app-ingress',
#    metadata={
#        'labels': {'app': 'web-app'},
#        'namespace': namespace.metadata['name'],
#    },
#    spec={
#        "rules": [
#            {
#                "http": {
#                    "paths": [
#                        {
#                            "backend": {
#                                "service": {
#                                    "name": "test",
#                                    "port": {"number": 80},
#                                }
#                            },
#                            "path": "/testpath",
#                            "pathType": "Prefix",
#                        }
#                    ]
#                }
#            }
#        ]
#    })

import pulumi
from pulumi_kubernetes import core

class NamespaceComponent(pulumi.ComponentResource):
    def __init__(self, name, opts=None):
        super().__init__('custom:namespace:NamespaceComponent', name, {}, opts)

        self.namespace = core.v1.Namespace(
            name,
            metadata={"name": name},
            opts=pulumi.ResourceOptions(parent=self),
        )

import pulumi
from eks_component import EKSComponent

# Create cluster with EKSComponent
dev_eks_stack = EKSComponent("dev-eks-cluster")
stg_eks_stack = EKSComponent("stg-eks-cluster")

# Export values for later use
pulumi.export("kubeconfig", dev_eks_stack.kubeconfig)
pulumi.export("vpc_id", dev_eks_stack.vpc_id)

pulumi.export("kubeconfig", stg_eks_stack.kubeconfig)
pulumi.export("vpc_id", stg_eks_stack.vpc_id)


# Kubectl config files for test service
helloipdeploy.yaml creates a 2 container deployment.

helloipservice.yaml creates a load balancer to frontend the deployment.

uses the docker cthulu13/helloip but built by Google Container Builder.

https://github.com/DonMills/helloipGCPcbuild
```
kubectl apply -f ./helloipdeploy.yaml
kubectl apply -f ./helloipservice.yaml
```



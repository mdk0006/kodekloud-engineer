# _*Lab1*_

## First Lab Create A Pod With Specific Label and Container Name

`kubectl run nginx --image=nginx --labels='app=nginx_app' --dry-run=clien=client -o yaml > pod.yaml`

Then you can open the pod.yaml file and change the name of the container

# _*Lab2*_

## Create a deployment with specific image

`kubectl create deployment nginx --image=nginx`

# _*Lab3*_

## Create a namespace and create a pod under it with specific name

Creating NameSpace

`kubectl create ns dev`

Create a Pod under the newly created namespace

`kubectl run dev-nginx-pod --image=nginx:latest --namespace dev`

# _*Lab4*_

## Setting the resource limit on the objects

For this we will create a yaml like this copied from Kubernetes Documentation

```
---
apiVersion: v1
kind: Pod
metadata:
  name: httpd-pod
spec:
  containers:
  - name: httpd-container
    image: httpd:latest
    resources:
      requests:
        memory: "15Mi"
        cpu: "100m"
      limits:
        memory: "20Mi"
        cpu: "100m"
```

then run

```
kubectl apply -f <file_name.yaml>
```

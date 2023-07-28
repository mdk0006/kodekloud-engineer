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

# **_Lab5_**

## Rolling Updates in Kubernetes

In this you have to be sure about the container name for the deployment for which you want to update the image

```
kubectl set image deployment nginx-deployment nginx-container=nginx:1.9.1
```

Here

```
kubectl set image deployment <name_of_the_deployment> <name_of_the_container>=<image_you_want_to_update>
```

# **_Lab 6_**

## Rollback Deployment in Kubernetes

To the previous version

```
kubectl rollout undo deployment nginx-deployment
```

# **_Lab 7_**

## Create a ReplicaSet in Kubernetes

```
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: frontend
  labels:
    app: guestbook
    tier: frontend
spec:
  # modify replicas according to your case
  replicas: 3
  selector:
    matchLabels:
      tier: frontend
  template:
    metadata:
      labels:
        tier: frontend
    spec:
      containers:
      - name: php-redis
        image: gcr.io/google_samples/gb-frontend:v3
```

**Solution To All**
[Github](https://github.com/MederD/Kodekloud-Engineer-Tasks/blob/main/Tasks/Fix_Issue_with_VolumeMounts_in_Kubernetes.md)

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

# **_Lab8_**

## Creating CronJob in Kubernetes

```
apiVersion: batch/v1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "* * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox:1.28
            imagePullPolicy: IfNotPresent
            command:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure

```

[Cronjob](https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/)

# **_Lab 9_**

## Creating a CountDown Timer in Kubernetes

```
apiVersion: batch/v1
kind: Job
metadata:
  name: countdown-datacenter
spec:
  template:
    metadata:
      name: countdown-datacenter
    spec:
      containers:
      - name: container-countdown-datacenter
        image: debian:latest
        command: ["sleep","5"]
      restartPolicy: Never
```

Point: Need to name template as countdown-datacenter

[Creating Job In Kuberentes](https://kubernetes.io/docs/concepts/workloads/controllers/job/)

# **_Lab 10 _**

## Creating a time check pod in Kuberentes

`configmap.yaml`

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: time-config
  namespace: xfusion
data:
  "TIME_FREQ": "7"
```

Pod with empty directory using the config map

```
apiVersion: v1
kind: Pod
metadata:
  name: time-check
  namespace: xfusion
spec:
  containers:
  - image: busybox:latest
    name: time-check
    command: [ "sh", "-c", "while true; do date; sleep $TIME_FREQ;done >> /opt/itadmin/time/time-check.log" ]
    volumeMounts:
    - mountPath: /opt/itadmin/time
      name: log-volume
    env:
     - name: TIME_FREQ
       valueFrom:
           configMapKeyRef:
            name: time-config         # The ConfigMap this value comes from.
            key: TIME_FREQ # The key to fetch.

  volumes:
  - name: log-volume
    emptyDir: {}
  restartPolicy: Never
```

We created a namespace and then created a configmap then we created a pod with volume which uses the config map and run command

[ConfigMap](https://kubernetes.io/docs/concepts/configuration/configmap/)
[Pod with Empty Dir](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir)

# **_Lab 11_**

# Troubleshooting Issues With Pods

The image name was not correct

We used the command

```
kubectl edit pod <name_of_pod>
```

If it is the element which needs pod to be destroyed you can apply forcefully which will delete
and make new one

```
kubectl apply --force -f <path_to_file>
```

# **_Lab12_**

# Update Existing Deployment in Kubernetes

In this we need to update the Deployment Image Replicas and Service Port

```
kubectl edit deployment <deployment_name>
```

```
kubectl edit service <service_name>
```

[Service In Kubernetes](https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/)
[Service Types](https://kubernetes.io/docs/concepts/services-networking/service/)
[Service Differences](https://medium.com/devops-mojo/kubernetes-service-types-overview-introduction-to-k8s-service-types-what-are-types-of-kubernetes-services-ea6db72c3f8c)
[Pavan Article](https://medium.com/@pavanbelagatti/kubernetes-service-types-explained-2709cde3bc0c#:~:text=There%20are%20four%20types%20of,NodePort%2C%20LoadBalancer%2C%20and%20Ingress.)

# **_Lab13_**

# Creating Replication Controller in K8's

```
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx_app
    type: front-end
  template:
    metadata:
      name: nginx
      labels:
        app: nginx_app
        type: front-end
    spec:
      containers:
      - name: nginx-container
        image: nginx:latest
        ports:
        - containerPort: 80
```

KeyPoint: Labels and Selectors should be same

[ReplicationController](https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/)

# **_Lab14_**

# Troubleshooting Volume Mount in Kubernetes

[Kubectl cp](https://www.middlewareinventory.com/blog/kubectl-cp-example/)

# _Lab1_

## First Lab Create A Pod With Specific Label and Container Name

`kubectl run nginx --image=nginx --labels='app=nginx_app' --dry-run=clien=client -o yaml > pod.yaml`

Then you can open the pod.yaml file and change the name of the container

# _Lab2_

## Create a deployment with specific image

`kubectl create deployment nginx --image=nginx`

_Lab3_

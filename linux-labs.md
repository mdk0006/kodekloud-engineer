# **_Lab1_**

## Creating a user with specific UID and Home Directory

`sudo useradd -u 1990 -d /var/www/javed javed`
You need to ensure that you have the sudo privileges
To check if the user is created or not
`cat /etc/passwd`

We can add user from SSH command as it is if we want to execute command on remote server
`ssh user@<remote-ip> 'sudo useradd -u 1990 -d /var/www/javed javed'`

### Extra Point

_You can check the logged in user info using_
`who` or `w` command in bash

# **_Lab2_**

## Add user and group in the remote servers from your jump host

To complete this lab I have created a small script which will just go to the server and create user and group
-t here is to get the terminal input for the remote server as we want to run the command
So make a script
`vi addgroup.sh`
Add the below lines

```
ssh -t tony@stapp01 'sudo groupadd nautilus_developers && sudo useradd -G nautilus_developers kano
ssh -t steve@stapp02 'sudo groupadd nautilus_developers && sudo useradd -G nautilus_developers kano'
ssh -t banner@stapp03 'sudo groupadd nautilus_developers && sudo useradd -G nautilus_developers kano'
```

Give permissions to the script
`chmod +x addgroup.sg`
Run the script
`./addgroup.sh`
Now the script will ask for the password of user for executing each line on the remote server

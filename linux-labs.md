# **_Lab1_**

## Creating a user with specific UID and Home Directory

```
sudo useradd -u 1990 -d /var/www/javed javed
```

You need to ensure that you have the sudo privileges
To check if the user is created or not

```
cat /etc/passwd
```

We can add user from SSH command as it is if we want to execute command on remote server

```
ssh user@<remote-ip> 'sudo useradd -u 1990 -d /var/www/javed javed'
```

### Extra Point

_You can check the logged in user info using_
`who` or `w` command in bash

# **_Lab2_**

## Add user and group in the remote servers from your jump host

To complete this lab I have created a small script which will just go to the server and create user and group
-t here is to get the terminal input for the remote server as we want to run the command
So make a script

```
vi addgroup.sh
```

Add the below lines

```
ssh -t tony@stapp01 'sudo groupadd nautilus_developers && sudo useradd -G nautilus_developers kano
ssh -t steve@stapp02 'sudo groupadd nautilus_developers && sudo useradd -G nautilus_developers kano'
ssh -t banner@stapp03 'sudo groupadd nautilus_developers && sudo useradd -G nautilus_developers kano'
```

Give permissions to the script

```
chmod +x addgroup.sg
```

Run the script

```
./addgroup.sh
```

Now the script will ask for the password of user for executing each line on the remote server

# **_Lab3 _**

## Create a user on remote server without an interactive shell

As it is on remote I am using the SSH command for my convenience

```
ssh banner@stapp03 -t 'sudo useradd -s /sbin/nologin mark'
```

To check if its added or not

```
ssh user@<remote-ip> -t 'grep 'mark' /etc/passwd'
```

# **_Lab 4_**

## Creating a user without a home

```
ssh -t banner@stapp03 'sudo useradd --no-create-home <user_name>'
```

# **_Lab5_**

## Creating a user with expiry

```
ssh -t tony@stapp01 'sudo useradd john -e 2021-01-28'
```

# **_Lab 6 _**

## Copying file for the specific user to the directory

```
find /home/usersdata/ -type f -user yousuf -exec cp --parents {} /media \;
```

# **_Lab7_**

## Disable Root Login

We need to disable root login

To prevent for the keys

```
sshpass -p  '********' ssh -o StrictHostKeyChecking=no tony@172.16.238.10
sudo su -
```

Go to

```
vi /etc/ssh/sshd_config
```

Search for Permit Root Login

:/PermitRootLogin

Change from yes to no

```
systemctl enable sshd
systemctcl restart sshd
systemcctl status sshd
```

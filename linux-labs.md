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
# *** Lab 8 *** 
## Linux Archives

```
tar -czvf jim.tar.gz /data/jim 
```

Explanation
tar: tar stands for "tape archive," and it is a command-line tool used in Unix-based systems to create and manipulate archive files.

-c: This flag tells tar to create a new archive.

-z: This flag is used to enable gzip compression, which compresses the archive to reduce its size.

-v: This flag enables the verbose mode, which displays the files being processed during the archiving process. It will show the progress and the list of files being added to the archive.

-f: This flag indicates that the following argument (jim.tar.gz) specifies the output file for the archive. The -f flag is used to specify the filename of the archive.

jim.tar.gz: This is the name of the output archive file. In this case, it is jim.tar.gz. The .tar.gz extension indicates that it is a compressed archive using gzip compression.

/data/jim: This is the path to the directory that you want to include in the archive. In this example, it is /data/jim.

When you run this command, tar will create a new archive named jim.tar.gz that contains all the files and directories inside the /data/jim directory. The files will be compressed using gzip compression, resulting in the final jim.tar.gz file. The command will display the progress and the list of files being added to the archive due to the -v flag.


*** Lab 9 *** 
# File Permissions
```
chmod +x <file>
```


*** facl ***




//get code for p
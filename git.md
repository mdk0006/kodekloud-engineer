# **_ Lab1 _**

# Git Installation and Making A Bare Repo

For Installation

```
yum install git -y
```

```
sudo mkdir -p /opt/games.git && cd $_
```

`$_` --> Last argument of the previous command

```
git init --bare
```

# **_ Lab 2 _**

## Cloning The Repo

You can clone the repo from the same machine as well

Go to the directory you want to clone under

```
git clone /opt/official.git
```

# **_ Lab 3 _**

## Forking Repo

Just need to click on Fork Button

#

# **_ Lab 4 _**

## Updating Repo

Just need to use scp command

```
scp john@example.com:/home/john/documents/notes.txt /home/user/downloads/
```

then go to repo add commit and push to master

# **_ Lab5 _**

## Git Branch Deletions

```
git branch -d xfusioncorp_apps
```

For deletion of branch we use -d flag

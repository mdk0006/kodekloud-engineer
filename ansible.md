# **_ Lab 1 _**

## Creating an empty file on the remote server

playbook.yml

```
---
- name: Create an empty file on a remote server
  hosts: stapp03
  become: false  # This is required if you need root privileges to create the file

  tasks:
    - name: Create an empty file
      file:
        path: /tmp/file.txt
        state: touch
      register: file_creation_result

    - name: Check if the file was created
      debug:
        msg: "File created successfully."
      when: file_creation_result.changed
```

inventory file

```
stapp03 ansible_host=172.16.238.12 ansible_user=banner ansible_password=BigGr33n
```

use

```
ansible-playbook playbook.yml -i <path_to_inventory>
```

# **_ Lab2 _**

## Updating Inventory

```
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_port=22 ansible_ssh_pass=Ir0nM@n
```

```
ansible-playbook -i inventory playbook.yaml
```

# **_ Lab3 _**

## Updatng the ansible config file

Go to ansible.cfg in /etc/ansible/ansible.cfg file and search for the remote user
#remote_user=root --> remote_user=ravi

# **_ Lab4 _**

## Ansible Copy Module

```
- name: copy files to destination
  hosts: all
  become: true
  tasks:
    - name: copy src.txt as dest.txt in the same dir
      ansible.builtin.copy:
        src: /usr/src/devops/index.html
        dest: /opt/devops
```

inventory
[managed_nodes]
stapp01 ansible_host= ansible_user= ansible_ssh_pass=
stapp02 ansible_host= ansible_user= ansible_ssh_pass=
stapp03 ansible_host= ansible_user= ansible_ssh_pass=

# **_ Lab 5 _**

# Ansible File Module

playbook.yml
```
---
- name: Deploy playbook
  hosts: all
  become: true
  tasks:
    - name: Create empty file and add contents
      file:
        path: /usr/src/webapp.txt
        state: touch

    - name: Changing file owner and group permissions
      file:
        path: /usr/src/webapp.txt
        owner: "{{ ansible_user }}"
        group: "{{ ansible_user }}"
        mode: 0655                    
```
inventory

[managed_nodes]
stapp01 ansible_host=172.16.238.10 ansible_user=tony ansible_ssh_pass=Ir0nM@n
stapp02 ansible_host=172.16.238.11 ansible_user=steve ansible_ssh_pass=Am3ric@
stapp03 ansible_host=172.16.238.12 ansible_user=banner ansible_ssh_pass=BigGr33n

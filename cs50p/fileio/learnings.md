# Containerization and Docker

Two types of spaces
User space(Restricted Permissions) and Kernel Space (Unrestricted)
Interact with the syscalls --> An operation in the userspace can call multiple syscalls it
depends on the process type
Containers --> Separate user space for each container
They are meant to run the one process (Main process) which can contain multiple child processes
For multiple process to be controlled by same Main Process you can use Supervisor
[Ref](https://techiescamp.com/topic/managing-multiple-processes-in-a-container/#:~:text=What%20if%20I,the%20process%20manager.)
_Linux Concepts of Cgroups and Namespaces_

1. **Namespaces** - A way to isolate a group of resources from other groups or users
   _Namespaces are a feature of the Linux kernel that partitions kernel resources such that one set of processes sees one set of resources while another set of processes sees a different set of resources._
   '
   The key Linux namespaces include:

PID namespace (PID): This namespace isolates the process ID (PID).
Network namespace (NET): This namespace controls network interfaces.
IPC namespace (IPC): This namespace manages access to interprocess communication (IPC) resources.
Mount namespace (MNT): This namespace controls the filesystem mount points.
UTS namespace (UTS): This namespace isolates kernel and version identifiers.
User namespace (USR): This namespace separates user IDs between the host and the container.
Control Group namespace (cgroup): This namespace isolates control group information from the container process.
'
`lsns` to enlist the namespaces
**Cgroup**
By default the kernel automatically assign the resources to the process but if you want to limit the resources for the process you can use controlgroups
Docker made it simple to define the resource for each container using parameters

[_Containers Better Than VM's_](https://techiescamp.com/topic/why-are-containers-better-than-vms/)

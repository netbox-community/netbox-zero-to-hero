# Module 8 - What About Virtualization?

# Introduction

Hello and welcome to module 8 of the NetBox 'Zero-to-Hero' course. In [Module 7: Automate All the Things!](../7-automate-all-the-things/7-automate-all-the-things.md), Eric used Ansible to extract data from NetBox and then use that data to automate the creation of basic device configurations for the WAN Router (Cisco IOS) and the Access Switch (Juniper JunOS), at the new Brisbane branch office. The IT Manager has now decided that as there are going to be two data scientists working out of the Brisbane office, it makes sense to have a Database server located on premises there.  

In this module, Susan will add the required physical servers for the VMWare Vsphere cluster, create the cluster and add the Virtual Machine that will run the PostgreSQL server. She will do all this via the Web Interface. 

By the end of this module you will be able to:
- Describe how NetBox models Virtualization, including Cluster Types, Clusters, Platforms, VM's and VM Interfaces  
- Use the web interface to manually add Virtualization data, including bulk uploading larger amounts of data where required

## Get Hands On
If you'd like to follow along with the examples used in this course, it's super easy to do, and you have a few options: 
1.  Run NetBox as a container with [NetBox Docker](https://github.com/netbox-community/netbox-docker) - This is the quickest way to get your own dedicated NetBox instance going and it only takes a few minutes to spin up on your laptop!
2.  Follow the [official documentation](https://docs.netbox.dev/en/stable/installation/) and do a full installation all the NetBox components. These instructions have been tested on Ubuntu and CentOS Linux.
3.  Use the public [demo instance](https://demo.netbox.dev/) of NetBox

The software versions used in the video for this module are: 
- `NetBox v3.3.2`

## Virtualization In NetBox

From the [docs](https://docs.netbox.dev/en/stable/features/virtualization/)
>Virtual machines and clusters can be modeled in NetBox alongside physical infrastructure. IP addresses and other resources are assigned to these objects just like physical objects, providing a seamless integration between physical and virtual networks.
>
>### Clusters
>A cluster is one or more physical host devices on which virtual machines can run. Each cluster must have a type and operational status, and may be assigned to a group. (Both types and groups are user-defined.) Each cluster may designate one or more devices as hosts, however this is optional.
>
>### Virtual Machines
>A virtual machine is a virtualized compute instance. These behave in NetBox very similarly to device objects, but without any physical attributes. For example, a VM may have interfaces assigned to it with IP addresses and VLANs, however its interfaces cannot be connected via cables (because they are virtual). Each VM may also define its compute, memory, and storage resources as well.

## The Project - Adding The Virtualization Cluster and Database Server VM
Susan has designed the following solution for the new Database server in Brisbane:

### VM Cluster
| Cluster Name | Cluster Type | Devices | Device Type |
| --- | --- | --- | ---|
| AUBRI01-VSPHERE-1 | VMware vSphere | AUBRI01-VSP-1, AUBRI01-VSP-2 | HPE ProLiant DL380 Gen9 |

### Device Interfaces
| Device | Interface | 802.1Q Mode | LAG Interface | 
| ---| --- | ---|  --- |
| AUBRI01-VSP-1 | iLO | Access (vlan 50) | N/A |  
| AUBRI01-VSP-1 | Gig-E 1 | Tagged (all) | ae0 |
| AUBRI01-VSP-1 | Gig-E 2 | Tagged (all) | ae0 |
| AUBRI01-VSP-2 | iLO | Access (vlan 50) | N/A |  
| AUBRI01-VSP-2 | Gig-E 1 | Tagged (all) | ae1 |
| AUBRI01-VSP-2 | Gig-E 2 | Tagged (all) | ae1 |
 
### Rack Positions
The Physical servers for the cluster will be mounted in the Brisbane rack (AUBRI01-RK-01) as follows:  
| Device | Rack Location (RUs) | 
| ---| --- |
| AUBRI01-VSP-1 | 1-2 |
| AUBRI01-VSP-1 | 3-4 |

### Server to Switch Connections
These cables will connect the physical servers to the local access switch:
| Device A | Interface A | Device B | Interface B | Cable Type | Cable Color | Cable Length 
| --- | --- | --- | --- | :---: | :---: | :---: |
| AUBRI01-VSP-1 | iLO | AUBRI01-SW-1 | ge-0/0/44 | CAT6 | Green | 2M |
| AUBRI01-VSP-1 | Gig-E 1 | AUBRI01-SW-1 | ge-0/0/1 | CAT6 | Green | 2M |
| AUBRI01-VSP-1 | Gig-E 2 | AUBRI01-SW-1 | ge-0/0/2 | CAT6 | Green | 2M |
| AUBRI01-VSP-2 | iLO | AUBRI01-SW-1 | ge-0/0/45 | CAT6 | Green | 2M |
| AUBRI01-VSP-2 | Gig-E 1 | AUBRI01-SW-1 | ge-0/0/3 | CAT6 | Green | 2M |
| AUBRI01-VSP-2 | Gig-E 2 | AUBRI01-SW-1 | ge-0/0/4 | CAT6 | Green | 2M |

### Virtual Machine
The VM for the Database server is specified as follows: 
| Name | Platform | Memory | Disk | CPUs | Services | VM Interface
| --- | --- | --- | ---| --- | --- | --- |
| AUBRI01-SQL-01 | Ubuntu 22.10 | 128 GB | 200 GB | 32 | PostgreSQL - tcp/5432, SSH - tcp/22 | eth0 (access vlan 10) |

 
## Video - NetBox Adding Virtualization Clusters and Virtual Machines
OK, so that's the planning work done - let's get to the fun stuff!! This video will step you through the whole process from .... through to ....

If you are following along you can find the...... 

<iframe width="560" height="315" src="https://www.youtube.com/embed/??????" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Summary
In this module you have learned how to ....

## Join the Discussion
If you have any questions as you go through the course then pop on over to the [NetBox Zero to Hero channel](https://netdev-community.slack.com/archives/C0453L6565C) on the NetDev Community Slack! If you aren't already a member then you can sign up for free [here](https://netdev.chat/).

## Useful Links
- [Zero To Hero Git Repo](https://github.com/netbox-community/netbox-zero-to-hero)
- [Official NetBox Documentation](https://docs.netbox.dev/en/stable/)
- [NetBox Docker](https://github.com/netbox-community/netbox-docker)
- [NetBox Cloud](https://www.getnetbox.io/) is a hosted solution offered by NS1
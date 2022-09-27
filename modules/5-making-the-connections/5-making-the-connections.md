# Introduction

Hello and welcome to module 5 of the NetBox 'Zero-to-Hero' course. In [Module 4: IP Addressing and VLANs](../4-ip-addressing-and-vlans/4-ip-addressing-and-vlans.md),  Susan used the [Ansible Galaxy Collection for NetBox](https://galaxy.ansible.com/netbox/netbox) to populate NetBox with the IP addressing and VLAN data for the new Brisbane branch office. 

In this module, Eric will be adding the cables and connections required to hook the devices in the new Brisbane branch office network together. 

By the end of this module you will be able to:
- Describe how NetBox models connections and cables
- Add individual connections and cables using the Web Interface
- Run a simple [python](https://www.python.org/) script to add multiple connections and cables via the NetBox REST API

## Why Use a Python Script to add data to NetBox? 
Of course, you can add data manually via the Web Interface (and the demo video will show you how to do this), but when you are dealing with a lot of data that can quickly become tedious and is error prone. Using scripts is a great way accurately and consistently upload data into NetBox data programmatically via the REST API.

Also, as any Network Engineer / IT Pro looking to stay ahead of the game knows, adding some Python scripting knowledge to your armory is a BIG win! 

## Get Hands On
If you'd like to follow along with the examples used in this course, it's super easy to do, and you have a few options: 
1.  Run NetBox as a container with [NetBox Docker](https://github.com/netbox-community/netbox-docker) - This is the quickest way to get your own dedicated NetBox instance going and it only takes a few minutes to spin up on your laptop!
2.  Follow the [official documentation](https://docs.netbox.dev/en/stable/installation/) and do a full installation all the NetBox components. These instructions have been tested on Ubuntu and CentOS Linux.
3.  Use the public [demo instance](https://demo.netbox.dev/) of NetBox   

The software versions used in the video for this module are: 
- `NetBox v3.3.2`
- `Python 3.8.9`

## Installing Python
If you need to install Python to run the example upload script, then head over [here](https://www.python.org/downloads/) first and download the version you require for your OS. 

## Modelling Cables and Connections in NetBox

## The Project - New Brisbane site Cables and Connections

| VLAN Name | VLAN ID | VLAN Group | Role | Prefix Length |
| :--- | :---: | :--- | :--- | :---: |

## Video - Adding Cables and Connections into NetBox
OK, so that's the planning and design work done - now onto the demo! This video will step you through how to populate NetBox with ........
As always the best way to understand the power of NetBox is to dive right in, so let's get started!

<!-- link to video here -->

In this module you have learned how NetBox Models ?, how to ?, and ?. 

In the next module you will learn how to....

## Useful Links
- [Official NetBox Documentation](https://docs.netbox.dev/en/stable/)
- [NetBox Docker](https://github.com/netbox-community/netbox-docker)

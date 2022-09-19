# Introduction

Hello and welcome to module 4 of the NetBox 'Zero-to-Hero' course. In [Module 3: Adding the Kit](../3-adding-the-kit/3-adding-the-kit.md),  Eric (Awesome Network Engineer) added the devices that are going to be installed at the planned new Brisbane branch office, making use of the NetBox REST API. 

In this module Susan (the other member of the Network Engineering dream team) will populate NetBox with the IP addressing and VLAN data for the new Brisbane branch office. To do this Susan is using the [Ansible Automation Platform](https://www.ansible.com/) and in particular the collection of [NetBox Ansible modules](https://docs.ansible.com/ansible/latest/collections/netbox/netbox/index.html)

By the end of this module you will be able to:
- Describe how NetBox models IPAM (IP Address Management) Data
- Integrate Ansible with NetBox, and run playbooks to populate the NetBox database
- Get started with a set of [Ansible playbooks](../../ansible/) for NetBox that can be easily adapted and extended to suit your own requirements 

## Why Integrate NetBox with Ansible? 
From the [Ansible](https://www.ansible.com/use-cases/network-automation) website: 
>
>Ansible Automation Platform is a single, flexible automation technology that can be used across diverse network devices and other IT domains, making it easy to automate entire network and IT processes.

Of course, you could add IPAM data manually via the Web Interface, but when you are dealing with a lot of data that can quickly become tedious and is error prone. Integrating Ansible with NetBox is quick and easy, and within a few minutes you can be running Ansible playbooks to Create, Read, Update and Delete (CRUD operations in computer programming terms) NetBox data programmatically via the REST API.

Also, as any Network Engineer / IT Pro looking to expand their skill set knows, Automation is becoming critical for managing modern networks, so by adding some Ansible knowledge to your armory, you will stay ahead of the game!

## Get Hands On
If you'd like to follow along with the examples used in this course, it's super easy to do, and you have a few options: 
1.  Run NetBox as a container with [NetBox Docker](https://github.com/netbox-community/netbox-docker) - This is the quickest way to get your own dedicated NetBox instance going and it only takes a few minutes to spin up on your laptop!
2.  Follow the [official documentation](https://docs.netbox.dev/en/stable/installation/) and do a full installation all the NetBox components. These instructions have been tested on Ubuntu and CentOS Linux.
3.  Use the public [demo instance](https://demo.netbox.dev/) of NetBox   

The software versions used in the video for this module are: 
- `NetBox v3.3.2`
- `Python 3.8.9`
- `ansible-core 2.13.4`
- `ansible package 6.4.0`
- `pynetbox 6.6.2`

## Installing Ansible
Ansible runs on Linux based systems, and is installed as a Python package. Follow these steps (they assume Git is already installed and set up on the system):

1. Clone the NetBox Zero to Hero Git repository and change into the Ansible directory:

```
git clone https://github.com/richbibby-NS1/netbox-zero-to-hero.git
cd netbox-zero-to-hero/ansible
```

2. Create a new Python Virtual Environment and activate it: 
```
python3 -m venv .
source bin/activate
```
3. Upgrade PIP (Python package manager) and install Pynetbox (NetBox API client library), and Ansible: 
```
python3 -m pip install --upgrade pip
pip3 install pynetbox
pip3 install ansible
```
4. Set up environment variables for NetBox (these are referenced by the Ansible playbooks):
```
export NETBOX_TOKEN=< YOUR_API_TOKEN >
export NETBOX_API=< YOUR_NETBOX_URL >
```

## Video - Adding IPAM Data Into NetBox
The video demo will now show you how to .... As always the best way to understand the power of NetBox is to dive right in, so let's get started!

If you are following along, don't forget to use the Ansible Playbooks used for adding device types.

[![Adding Devices Into NetBox](../../images/3-adding-the-kit.png)](https://youtu.be/dA3LZiV7UIg) 

OK, so now you know how to ...... in the next module you will learn how to....

## Useful Links
- [Official NetBox Documentation](https://docs.netbox.dev/en/stable/)
- [NetBox REST API Overview](https://docs.netbox.dev/en/stable/integrations/rest-api/)
- [Zero to Hero Postman collection](../../postman/NetBox-Zero-to-Hero.postman_collection.json) 
- [NetBox Community Device Type Library](https://github.com/netbox-community/devicetype-library)
- [NetBox Docker](https://github.com/netbox-community/netbox-docker)
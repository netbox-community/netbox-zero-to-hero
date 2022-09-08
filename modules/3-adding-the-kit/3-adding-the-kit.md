# Introduction

Hello and welcome to module 3 of the NetBox 'Zero-to-Hero' course. In [Module 2: Setting up the Organization](../2-setting-up-the-organization/2-setting-up-the-organization.md) you learned how to model an organization within NetBox, and how to use the Web Interface to both manually create individual objects, and bulk import objects using CSV-formatted data. 

In this module we will continue to populate NetBox with data for our fictional organization, TLE Consulting. This time Network Engineer Eric, will be adding the network devices that are going to be installed at the planned new Brisbane branch office, making use of the NetBox REST API.

By the end of this module you will be able to:  
- Describe how NetBox models devices
- Use Postman to make REST API calls to NetBox
- Save time by making use of the community library of pre-defined device types

## Get Hands On
If you'd like to follow along with the examples used in this course, it's super easy to do, and you have a few options: 
1.  Run NetBox as a container with [NetBox Docker](https://github.com/netbox-community/netbox-docker) - This is the quickest way to get your own dedicated NetBox instance going and it only takes a few minutes to spin up on your laptop!
2.  Follow the [official documentation](https://docs.netbox.dev/en/stable/installation/) and do a full installation all the NetBox components. These instructions have been tested on Ubuntu and CentOS Linux.
3.  Use the public [demo instance](https://demo.netbox.dev/) of NetBox   

- The NetBox version used in the video for this module is v3.3.2. 
- The Postman collection used in the demo for making API calls is available here (add link) 
- The YAML files used for device types can be found [here](device_type_yaml_data/)

## Add The Devices
manufacturers - postman
platforms - postman
device roles - postman
device types
 - upload from device type library
 - add files to repo
 - demo finding the files in project
devices - postman + show how to find values for example device type
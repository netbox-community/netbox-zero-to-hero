# NetBox Cloud ‘Zero-To-Hero’ Series
Training curriculum that takes users through a real world scenario to see the various features in NetBox and to serve as the basis for future educational content.

## Goals
- Enable new customers to get up and running and immediately start to get value from the product
- Build a foundation from which customers can start to leverage NetBox's extra features ie. custom fields, reports, plugins etc
- Introduce the power of NetBox to drive network automation efforts
- Compliment Jeremy’s public NetBox training course

## Format
- bite-sized modules consisting of text and graphics along with an accompanying short video demo of each concept 
- each module introduces a new concept/area within NetBox, and is a step along the road of the example scenario leading to the deployment of a new branch office site
- demo how to do each step via Web UI and REST API (script or postman) 
- code examples available in public github repo (and Postman collection?) 

## Scenario
- Fictional organization of 1000 employees, with a small IT team 
- Network consists of 2 small DC's, multiple sites/branch office locations
- Standard branch office kit (WAN router, access switch, WiFi)
- 1 or 2 awesome Network Engineers with a burning desire to introduce this amazing NetDevOps stuff they keep hearing about (so they can do less work but still wow the bosses!)
- Project is a new branch office deployment in Brisbane, Australia
- NetBox used every step of the way to help deliver the project on time

## Modules

### 1. Introduction
- NetBox overview, what it is and is not
- Intro to WebUI and REST API
- Intro to scenario

### 2. Setting up the Site
- Region, Site, Contacts, Rack 

### 3. IP Addressing and VLANs
- Prefixes, IP Addresses, VLANs

### 4. Adding the Kit  
- Manufacturers, Device Types, Device Roles, Platforms, Components

### 5. Making the Connections
- Cables, Interface, console and power connections

### 6. Setting up the WiFi
- Wireless LANs

### 7. What About Virtualization? 
- Clusters, VMs 

### 8. Powering Up 
- Power Feeds, Power Panels

### 9. Is the Internet Down? 
- Providers, circuit types, circuits

### 10. Adding Some Customization 
- Custom Fields, Bandwidth Use on port (link to monitoring graph)

### 11. The Boss is Asking for a Report (another easy win!) 
- Reports

### 12. Automate All the Things!
- Automated Device Config Generation (pull device vars and feed into Jinja2 templates) 
OR
- Dynamic Inventory to be consumed by automation (Nornir ?) 

## Ideas for extra modules - Series 2?
- WebHook (add a new VLAN and trigger an API call to external system - Ansible/StackStorm etc) 
- SSO
- Modeling the Cloud (DC extended into AWS/Azure/GCP)
- Getting other teams involved, selling NB internally to colleagues and upwards to management
- Plugins
- 3rd Party integration
- Terraform


steve - cert?
OK to use container OS's? for automation pieces?
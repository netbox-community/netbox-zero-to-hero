# NetBox ‘Zero-To-Hero’ Course

## Introduction
Hello and welcome to this short course designed to take new NetBox users from 'Zero to Hero'. We are excited to have you here! 

The goals of this course are as follows: 

- Enable you to get up and running with minimal fuss and immediately start to get value from NetBox
- Build a solid foundation from which you can start to leverage NetBox's extra features ie. custom fields, reports, plugins etc
- Introduce the power of NetBox to drive your Network Automation efforts as the 'Single Source Of Truth' for your NetDevOps workflows

## Course Format
The course consists of bite sized modules, each one introducing a new concept or feature of NetBox. Each module is a step in the journey that leads to the deployment of a new branch office network at a remote site for a fictional company. 

Each module includes a video teaching you how to interact with NetBox both via the Web UI and programmatically using the REST API. You can follow along with your own instance of NetBox, and all code used to interact with the REST API will be available in a Git repo and Postman collection, so you will have a fully working code base which you can clone to get you started!

## Example Scenario
The fictional scenario that will be used throughout this course to demonstrate NetBox features is: 

- The organization is a small consulting firm, with a small IT team 
- The network consists of two Data Centers, plus multiple branch office locations around the world 
- Susan and Eric are awesome Network Engineers with a burning desire to introduce this amazing 'NetDevOps' stuff they keep hearing about (so they can do less work but still wow the bosses!)
- The network team has been handed a new project to deploy a branch office network in the new location in Brisbane, Australia. The corporate standard branch office design consists of a WAN Router, an Access Switch and a Wireless Access Point
- Susan and Eric are going to use NetBox used every step of the way to help deliver the project on time and also to power some network automation to get the devices configured error free (this has long been a problem for them with new sites taking hours and even days to stand up!)

So, with that said, lets dive in!

## Modules

### [Module 1: Introduction](modules/1-Introduction/1-introduction.md)
- NetBox overview
- What NetBox Is (and what it isn't)
- Introduction to the Web Interface and the REST API

### Module 2: Setting up the Site
- Region, Site, Contacts, Rack 

### Module 3: IP Addressing and VLANs
- Prefixes, IP Addresses, VLANs

### Module 4: Adding the Kit
- Manufacturers, Device Types, Device Roles, Platforms, Components

### Module 5: Making the Connections
- Cables, Interface, console and power connections

### Module 6: Setting up the WiFi
- Wireless LANs

### Module 7: What About Virtualization? 
- Clusters, VMs 

### Module 8: Powering Up 
- Power Feeds, Power Panels

### Module 9: Is the Internet Down? 
- Providers, circuit types, circuits

### Module 10: Adding Some Customization 
- Custom Fields, Bandwidth Use on port (link to monitoring graph)

### Module 11: The Boss is Asking for a Report (another easy win!) 
- Reports

### Module 12: Automate All the Things!
- Automated Device Config Generation (pull device vars and feed into Jinja2 templates) 
OR
- Dynamic Inventory to be consumed by automation (Nornir ?) 
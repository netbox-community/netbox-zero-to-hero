# NetBox ‘Zero-To-Hero’ Course
This is a training course that takes new NetBox users through a real world scenario that demonstrates various features of NetBox.

## Goals
This course aims to: 
- enable new customers to get up and running and immediately start to get value from the product
- build a foundation from which customers can start to leverage NetBox's extra features ie. custom fields, reports, plugins etc
- introduce the power of NetBox to drive network automation efforts
- compliment the official NetBox documentation

## Format
- bite-sized modules consisting of text and graphics along with an accompanying short video demo of each concept 
- each module introduces a new concept/area within NetBox, and is a step along the road of the example scenario leading to the deployment of a new branch office site
- demo how to do each step via Web UI and REST API (script or postman) 
- code examples available in public github repo (and Postman collection?) 

## Fictional Scenario
The course will make use of a fictional organization in modules 1 - 12 to help demonstrate NetBox features:  
- medium sized consulting company, with a small IT team 
- the network consists of 2 small DC's, multiple sites/branch office locations
- standard branch office deployments (WAN router, access switch, WiFi)
- 1 or 2 awesome Network Engineers with a burning desire to introduce this amazing NetDevOps stuff they keep hearing about (so they can do less work but still wow the bosses!)
- project is a new branch office deployment in Brisbane, Australia
- use NetBox every step of the way to help deliver the project on time and enable the network team to leverage NetBox as the single source of truth for the network going forward

## Course Modules

### [Module 1: Introduction](modules/1-Introduction/1-introduction.md)
- NetBox overview, what it is and is not
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
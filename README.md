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
- Susan and Eric are going to use NetBox every step of the way to help deliver the project on time and also to power some network automation to get the devices configured error free (this has long been a problem for them with new sites taking hours and even days to stand up!)

So, with that said, lets dive in!

## Modules

### [Module 1: Introduction](modules/1-Introduction/1-introduction.md)
- NetBox overview
- Introduction to the Web Interface and the REST API

### [Module 2: Setting up the Organization](modules/2-setting-up-the-organization/2-setting-up-the-organization.md)
- Model the organization using tenant groups, tenants, regions, site groups, sites, locations, racks and contacts
- Use the web interface to manually add data for the organization
- Use the web interface to bulk upload data for the organization

### [Module 3: Adding the Kit](modules/3-adding-the-kit/3-adding-the-kit.md)
- Add Manufacturers, Device Types, Platforms, Device Roles and Devices
- Use Postman to make REST API calls into NetBox to add devices
  
### [Module 4: IP Addressing and VLANs](modules/4-ip-addressing-and-vlans/4-ip-addressing-and-vlans.md)
- Add IPAM (IP Address Management) Data - RIRs, Aggregates, Prefixes, IP Addresses and VLANs
- Integrate NetBox with Ansible, and run playbooks to populate the NetBox database with IPAM data

### [Module 5: Making the Connections](modules/5-making-the-connections/5-making-the-connections.md)
- Add the Cables, Interface, console and power connections
- Use the web interface to bulk upload data for Cables and Connections
- Use the web interface to view the Cables, Interface and Console connections

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
- Automated Device Config Generation 

## Useful Links
- [Official NetBox Documentation](https://docs.netbox.dev/en/stable/)
- [NetBox GitHub](https://github.com/netbox-community/netbox)
- [GitHub Discussions](https://github.com/netbox-community/netbox/discussions)
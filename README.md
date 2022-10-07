# NetBox - Zero To Hero Course

## Introduction
Hello and welcome to this short course designed to take new NetBox users from 'Zero to Hero'. We are excited to have you here! 

The goals of this course are as follows: 

- Enable you to get up and running with minimal fuss and immediately start to get value from NetBox
- Build a solid foundation from which you can start to leverage NetBox's extra features ie. custom fields, reports, plugins etc
- Introduce the power of NetBox to drive your Network Automation efforts as the 'Single Source Of Truth' for your NetDevOps workflows

## Course Format
The course consists of bite sized modules, each one introducing a new concept or feature of NetBox. Each module is a step in the journey that leads to the deployment of a new branch office network at a remote site for a fictional company. 

Each module includes a video teaching you how to interact with NetBox either via the Web UI or programmatically using the REST API. You can follow along with your own instance of NetBox, and all the code is available in the accompanying [Git Repository](https://github.com/netbox-community/netbox-zero-to-hero) - including a [Postman Collection](https://github.com/netbox-community/netbox-zero-to-hero/tree/main/postman), [Ansible Playbooks](https://github.com/netbox-community/netbox-zero-to-hero/tree/main/ansible) and [Python Scripts](https://github.com/netbox-community/netbox-zero-to-hero/tree/main/python_scripts) - so you will have a fully working code base which you can clone to get you started on your way to becoming a NetBox Hero!

## Join the Discussion
If you have any questions as you go through the course then pop on over to the [NetBox Zero to Hero channel](https://netdev-community.slack.com/archives/C0453L6565C) on the NetDev Community Slack! If you aren't already a member then you can sign up for free [here](https://netdev.chat/)

## Example Scenario
The fictional scenario that will be used throughout this course to demonstrate NetBox features is: 

- The organization is a small consulting firm, with a small IT team 
- The network consists of two Data Centers, plus multiple branch office locations around the world 
- Susan and Eric are awesome Network Engineers with a burning desire to introduce this amazing 'NetDevOps' stuff they keep hearing about (so they can do less work but still wow the bosses!)
- The network team has been handed a new project to deploy a branch office network in the new location in Brisbane, Australia. The corporate standard branch office design consists of a WAN Router, an Access Switch and Wireless Access Points
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

### [Module 6: Setting up the WiFi](modules/6-Setting-up-the-WiFi/6-Setting-up-the-WiFi.md)
- Add Wireless LANs
- Use simple Python scripts to interact with the NetBox REST API to add Wireless LANs
- Use the web interface to view Wireless LAN information

### Module 7: Automate All the Things! (coming soon)
- Automated Device Config Generation 
  
### Module 8: What About Virtualization? (coming soon)
- Clusters, VMs 

### Module 9: Powering Up (coming soon)
- Power Feeds, Power Panels

### Module 10: Is the Internet Down? (coming soon)
- Providers, circuit types, circuits

### Module 11: Adding Some Customization (coming soon)
- Custom Fields, Bandwidth Use on port (link to monitoring graph)

### Module 12: The Boss is Asking for a Report (another easy win!) (coming soon)
- Reports

## Useful Links
- [Official NetBox Documentation](https://docs.netbox.dev/en/stable/)
- [NetBox GitHub](https://github.com/netbox-community/netbox)
- [GitHub Discussions](https://github.com/netbox-community/netbox/discussions)
- [NetBox Cloud](https://www.getnetbox.io/) is a hosted solution offered by NS1
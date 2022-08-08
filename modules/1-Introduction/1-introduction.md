# Introduction

Hello and welcome to the first module in this short course designed to take you from 'Zero to Hero' with NetBox. We are excited to have you here! The goals of this course are as follows: 

- Enable you to get up and running with minimal fuss and immediately start to get value from NetBox
- Build a solid foundation from which you can start to leverage NetBox's extra features ie. custom fields, reports, plugins etc
- Introduce the power of NetBox to drive your Network Automation efforts as the 'Single Source Of Truth' for your NetDevOps workflows

## Course Format
The course consists of bite sized modules, each one introducing a new concept or feature of NetBox. Each module is a step in the journey that leads to the deployment of a new branch office network at a remote site for a fictional company. Each module includes a video teaching you how to interact with NetBox both via the Web UI and programmatically using the REST API. You can follow along with your own instance of NetBox, and all code used to interact with the REST API will be available in a Git repo and Postman collection, so you will have a fully working code base which you can clone to get you started!

So, with that said, lets dive in!

## What NetBox Is (and what it isn't)

To get the most value from NetBox it is key to understand not just what NetBox does but also what it does not do. The following explanation is taken from the official NetBox documentation (https://docs.netbox.dev/en/stable/): 

### What is NetBox?

NetBox is an infrastructure resource modeling (IRM) application designed to empower network automation. Initially conceived by the network engineering team at DigitalOcean, NetBox was developed specifically to address the needs of network and infrastructure engineers. NetBox is made available as open source under the Apache 2 license. It encompasses the following aspects of network management:

- IP address management (IPAM) - IP networks and addresses, VRFs, and VLANs
- Equipment racks - Organized by group and site
- Devices - Types of devices and where they are installed
- Connections - Network, console, and power connections among devices
- Virtualization - Virtual machines and clusters
- Data circuits - Long-haul communications circuits and providers

### What NetBox Is Not

While NetBox strives to cover many areas of network management, the scope of its feature set is necessarily limited. This ensures that development focuses on core functionality and that scope creep is reasonably contained. To that end, it might help to provide some examples of functionality that NetBox does not provide:

- Network monitoring
- DNS server
- RADIUS server
- Configuration management
- Facilities management

That said, NetBox can be used to great effect in populating external tools with the data they need to perform these functions.

## Design Philosophy
NetBox was designed with the following tenets foremost in mind.

- Replicate the Real World
  - Careful consideration has been given to the data model to ensure that it can accurately reflect a real-world network. For instance, IP addresses are assigned not to devices, but to specific interfaces attached to a device, and an interface may have multiple IP addresses assigned to it.

- Serve as a "Source of Truth"
    - NetBox intends to represent the desired state of a network versus its operational state. As such, automated import of live network state is strongly discouraged. All data created in NetBox should first be vetted by a human to ensure its integrity. NetBox can then be used to populate monitoring and provisioning systems with a high degree of confidence.

- Keep it Simple
    - When given a choice between a relatively simple 80% solution and a much more complex complete solution, the former will typically be favored. This ensures a lean codebase with a low learning curve.

## Video Demo - Introduction to the WebUI and REST API


## Example Scenario
The fictional scenario that will be used throughout this course to demonstrate NetBox features is: 

- ABC Corp (better name?) is a legal firm of 1000 employees, with a small IT team 
- The network consists of two small Data Centers, plus multiple branch office locations around the world 
- Susan and Eric are awesome Network Engineers with a burning desire to introduce this amazing 'NetDevOps' stuff they keep hearing about (so they can do less work but still wow the bosses!)
- The network team has been handed a new project to deploy a branch office network in the new location of Brisbane, Australia. The corporate standard standard branch office design consists of a WAN Router, an Access Switch and a Wireless Access Point)
- Susan and Eric are going to use NetBox used every step of the way to help deliver the project on time and also to power some network automation to get the devices configured error free (this has long been a problem for them with new sites taking hours and even days to stand up!)
# Introduction

blah blah blah 

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

## Video Demo 1 - Introduction to the NetBox WebUI

[![Introduction to the NetBox WebUI](../../images/1-introduction-UI.png)](https://youtu.be/zT82jOUCcW4)

## Video Demo 2 - Introduction to the NetBox REST API
For a deep dive into the REST API, head over to the official NetBox documentation at: https://docs.netbox.dev/en/stable/rest-api/overview/

For now, let's take a quick tour of the REST API in this short video, which will help you to get up and running in no time: 

[![Introduction to the NetBox REST API](../../images/1-introduction-API.png)](https://youtu.be/Gsarb0elmoA)

## External Links
- [NetBox Documentation](https://docs.netbox.dev/en/stable/)
- [NetBox Community Device Type Library](https://github.com/netbox-community/devicetype-library)
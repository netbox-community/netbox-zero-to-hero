# Module 8 - What About Virtualization?

# Introduction

Hello and welcome to module 9 of the NetBox 'Zero-to-Hero' course. In [Module 8: What About Virtualization?](../8-what-about-virtualization/8-what-about-virtualization.md), Network Engineer Susan added the required physical servers for the vSphere cluster, created the cluster and added the Virtual Machines. She also defined the services that are running on the VM servers. 

In this video, Eric will add the facility power panels and feeds for the new Brisbane branch office, and then also add the PDUs and power cable connections, so all the devices in the new communications cabinet can be powered on. 

By the end of this module you will be able to:
- Describe how NetBox models facility power as discrete power panels and feeds.
- Understand how to add Power Distribution Units (PDUs) to supply power to individual devices
- Use the web interface to manually add all data relating to facility power including bulk uploading cable connections from CSV data

## Get Hands On
If you'd like to follow along with the examples used in this course, it's super easy to do, and you have a few options: 
1.  Run NetBox as a container with [NetBox Docker](https://github.com/netbox-community/netbox-docker) - This is the quickest way to get your own dedicated NetBox instance going and it only takes a few minutes to spin up on your laptop!
2.  Follow the [official documentation](https://docs.netbox.dev/en/stable/installation/) and do a full installation all the NetBox components. These instructions have been tested on Ubuntu and CentOS Linux.
3.  Use the public [demo instance](https://demo.netbox.dev/) of NetBox

The software versions used in the video for this module are: 
- `NetBox v3.3.2`

## Power Tracking In NetBox

From the [docs](https://docs.netbox.dev/en/stable/features/power-tracking/)
>### Power Tracking
>As part of its DCIM feature set, NetBox supports modeling facility power as discrete power panels and feeds. These are most commonly used to document power distribution within a data center, but can serve more traditional environments as well.
>
>### Power Panels
>A power panel is the furthest upstream power element modeled in NetBox. It typically represents a power distribution panel (or breaker panel) where facility power is split into multiple discrete circuits, which are modeled as feeds.
>
>Each power panel is associated with a site, and may optionally be associated with a particular location within that site. There is no limit to how many power feeds a single panel can supply, however both of these object types should map to real-world objects.
>
>### Power Feeds
>A power feed represents a discrete power circuit originating from an upstream power panel. Each power feed can be assigned a name, operational status, and various electrical characteristics such as supply (AC or DC), voltage, amperage, and so on.
>
>A device power port can be connected to a power feed via a cable. Only one port can be connected to a feed: Where multiple devices draw power from the same feed, a power distribution unit (PDU) must be modeled as an individual device mapping a power port to multiple power outlets to which the downstream devices can connect
>
>Each power feed in NetBox is assigned a type: primary or redundant. This allows easily modeling redundant power distribution topologies. In scenarios involving only a single, non-redundant power supply, mark all power feeds as primary.

## The Project - Adding The Facility Power Panels, Feeds and PDUs
Eric has designed the following solution for power in the new Brisbane Comms Room:

### Power Panels
There are two power panels provided by the facilities management company:

| Panel Name | Location |
| --- | --- | 
| AUBRI01-PWR-PAN-1 | Comms Room |
| AUBRI01-PWR-PAN-2 | Comms Room |

### Power Feeds
Each power panel supplies a single power feed (discrete circuit) to the comms room rack as follows: 

| Feed Name | Power Panel | Rack | Type | Supply | Voltage | Amperage | Phase | 
| --- | --- | --- | --- | :---: | :---: | :---: | :---: |
| AUBRI01-PWR-FEED-1 | AUBRI01-PWR-PAN-1 | AUBRI01-RK-01 | Primary | AC | 200 | 16 | Single | 
| AUBRI01-PWR-FEED-2 | AUBRI01-PWR-PAN-2 | AUBRI01-RK-01 | Secondary | AC | 200 | 16 | Single | 

### Power Distribution Units (PDUs)
Two APC (model AP7921B - 16A, 208/230V) PDU's will be installed in the rack and will connected to the power feeds via a single power port, and each PDU has eight C13 power outlets that can be connected to device power supplies:

| PDU Name | Rack Location | 
| --- | :---: |
| AUBRI01-PDU-1 | 11 (rear) |
| AUBRI01-PDU-2 | 12 (rear) |

### Device to PDU Power Connections
The following cables will be added for power connections between the devices and the PDUs:

| Device | Power Port | PDU | Power Outlet |
| --- | :---: | --- | --- | 
| AUBRI01-SW-1 | PSU0 | AUBRI01-PDU-1 | Outlet 1 |
| AUBRI01-SW-1 | PSU1 | AUBRI01-PDU-2 | Outlet 1 |
| AUBRI01-CON-1 | ps1 | AUBRI01-PDU-1 | Outlet 2 |
| AUBRI01-RTR-1 | PSU0 | AUBRI01-PDU-2 | Outlet 2|
| AUBRI01-VSP-1 | PSU1 | AUBRI01-PDU-1 | Outlet 3|
| AUBRI01-VSP-1 | PSU2 | AUBRI01-PDU-2 | Outlet 3|
| AUBRI01-VSP-2 | PSU1 | AUBRI01-PDU-1 | Outlet 4|
| AUBRI01-VSP-2 | PSU2 | AUBRI01-PDU-2 | Outlet 4|

### PDU to Power Feed and Panel Connections
The following cables will be added for power connections between the PDUs and the power feeds:

| PDU | Power Port | Power Feed | Power Panel | 
| --- | :---: | --- | --- | 
| AUBRI01-PDU-1 | 1 | AUBRI01-PWR-FEED-1 | AUBRI01-PWR-PAN-1 | 
| AUBRI01-PDU-2 | 1 | AUBRI01-PWR-FEED-2 | AUBRI01-PWR-PAN-2 | 

## Video - Adding The Facility Power Panels, Feeds and PDUs
OK, so that's the planning work done - let's get to the fun stuff!! This video will step you through the whole process from adding the ....., creating the ......, through to adding the ...... 

If you are following along you can find the [CSV data](https://github.com/netbox-community/netbox-zero-to-hero/tree/main/modules/9-powering-up/csv_data) for the Device to PDU cable connections in the course Git Repository. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/????" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Summary
In this module you have learned how NetBox models facility power as discrete power panels and feeds. You also learned how to add Power Distribution Units (PDUs) to supply power to individual devices. 

## Join the Discussion
If you have any questions as you go through the course then pop on over to the [NetBox Zero to Hero channel](https://netdev-community.slack.com/archives/C0453L6565C) on the NetDev Community Slack! If you aren't already a member then you can sign up for free [here](https://netdev.chat/).

## Useful Links
- [Zero To Hero Git Repo](https://github.com/netbox-community/netbox-zero-to-hero)
- [Official NetBox Documentation](https://docs.netbox.dev/en/stable/)
- [NetBox Docker](https://github.com/netbox-community/netbox-docker)
- [NetBox Cloud](https://www.getnetbox.io/) is a hosted solution offered by NS1
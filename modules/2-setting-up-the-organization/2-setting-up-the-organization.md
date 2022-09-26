# Introduction

Hello and welcome to module 2 of the NetBox 'Zero-to-Hero' course. In [Module 1: Introduction](../1-Introduction/1-introduction.md) you learned the features of NetBox, and had a guided tour of both the Web Interface and the REST API. In this module we will expand on this by adding the Organizational data for our fictional consulting firm, into NetBox. 

By the end of this module you will be able to:  
- Describe how NetBox models the organization using tenant groups, tenants, regions, site groups, sites, locations, racks and contacts
- Use the web interface to manually add data for an organization
- Use the web interface to bulk upload larger amounts of data for the organization

## Get Hands On
If you'd like to follow along with the examples used in this course, it's super easy to do, and you have a few options: 
1.  Run NetBox as a container with [NetBox Docker](https://github.com/netbox-community/netbox-docker) - This is the quickest way to get your own dedicated NetBox instance going and it only takes a few minutes to spin up on your laptop!
2.  Follow the [official documentation](https://docs.netbox.dev/en/stable/installation/) and do a full installation all the NetBox components. These instructions have been tested on Ubuntu and CentOS Linux.
3.  Use the public [demo instance](https://demo.netbox.dev/) of NetBox   

The NetBox version used in the video for this module is v3.3.2.

## The Organizational Data
Our fictional organization, TLE Consulting, is structured as follows:

### NetBox System Users
TLE Consulting's two awesome Network Engineers, Eric and Susan will be set up with their own user accounts as they will be the two main administrators of the NetBox System. 

### Tenancy
In NetBox most core objects can be associated with a tenant and this conveys ownership of the object. For example a managed service provider can associate network devices with individual customers. 

TLE Consulting is using the Tenancy feature to define it's internal business units and associate them with objects. They have a tenant group (TLE Departments) and this contains the tenants - Sales, Finance, IT, Marketing and Consulting

### Regions
In NetBox, regions are typically used to model countries, states, and cities. TLE Consulting is present in 4 regions - Africa, Asia Pacific, Europe and North America. These 'parent' regions will also contain the Country, State and City regions nested within them.

### Site Groups and Sites
Whereas regions are intended for geographic organization, site groups may be used for functional groupings. A site typically represents a building within a region and/or site group. TLE Consulting has two Site Groups - Branch (consisting of ten sites) and Corporate (consisting of two sites). 

### Locations 
A location can be any logical subdivision within a building, such as a floor or room. All TLE Consulting Branch sites have a single location (Comms Room) and the Corporate sites have an extra location within them (On-Premises Data Center)

### Racks and Rack Roles
Racks are physical objects into which devices are installed. NetBox models each equipment rack as a discrete object within a site and location. In our example all sites have at least one rack where Network/IT equipment is installed. 

Users can also create custom roles to which racks can be assigned, and TLE has defined their rack roles as Infrastructure, Compute and Storage.

### Contacts
To complete the organizational set up we will need to add some contacts. A contact is an individual responsible for a resource within the context of its assigned role. Contacts can be members of a group, and contact roles define the relationship a contact has with an assigned object. Unique contacts are created once and can be assigned to any number of NetBox objects. 

TLE will use 2 contact groups - IT, which contains Susan and Eric and Facilities, which contains Alexa. The contacts will be assigned to site objects and be given one of the contact roles 'Operations' or 'Emergency'. 

## Video - Setting Up The Organization
As always the best way to understand the power of NetBox is to dive right in! This video will step through creating all the objects for the fictional TLE Consulting organization. Also, as TLE's awesome Network Engineers, Susan and Eric are using NetBox to help build out the new branch network in Brisbane, Australia, they will also add the information for this new site to kick off the project.

If you are following along you can find the [CSV data](csv_data/) in course Git Repository.

With that said, let's get started! 

[![Setting Up The Organization](../../images/2-organization.png)](https://youtu.be/Qv1xkyS81v4) 

OK, so now you know how to set up your organization's data in NetBox using the Web Interface, in the next module you will learn how to add network devices using the REST API. 

## Useful Links
- [Official NetBox Documentation](https://docs.netbox.dev/en/stable/)
- [NetBox Docker](https://github.com/netbox-community/netbox-docker)
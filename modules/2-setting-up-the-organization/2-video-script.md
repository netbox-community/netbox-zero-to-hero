Hello and welcome to this short video for module 2 of the NetBox Zero to Hero training course. If you haven't already checked out the first module yet then you can find the link in the video notes below to get started. For the purposes of this demo I have an instance of NetBox running as a docker container locally on my laptop, and if you would like to follow along, then you can easily do that too. There are a couple of links down below to help you spin up your own instance of NetBox, along with a link to the notes that accompany this video module. 

In this video we will be laying the foundations of the NetBox data for our fictional organization called TLE Consulting. This organizational data is critical and according to NetBox best practice should be added at the start - as everything else is built on top of it. OK, so I am logged into NetBox as the admin user and as you can see I have a completely empty database. 

### Users
The very first thing to do is set up the Network Engineers Eric and Susan as users on the system, as they are going to be the 2 main users for now. 

By setting up separate user accounts for them it is easy to track what changes each user is making to the database. To do this, log into the Django back end of the NetBox system by clicking on Admin and then Admin again. Django is a framework for building web applications such as NetBox and this is the Django administration site. 

So go to Users and click add, then enter the username of susan and click save - then select staff and superuser status which means Susan can access both the Django admin portal and has all permissions to the NetBox database objects. Scroll further down and you can see that explicit permissions can be set and this is the way you can be more granular with user permissions - for example you could restrict a user or a group to only have read-only access to Device data - this could be helpful in a scenario where you have junior IT support staff who might need to check what devices are at a certain location, but you don't want them to make any changes. 

For now though, just click 'save and add another' down at the bottom, and add Eric now with the same permissions as Susan. OK now that's done, exit the Django admin portal by clicking 'view site' to get back to the the main NetBox application home screen. So, log out as the admin account and now log back in as Susan. 

Great, so we can stay logged in as Susan to do the rest of the work for this module.


### Tenancy

First of all Susan needs to set up the tenants. TLE Consulting is using the Tenancy feature to define it's internal business units and associate them with objects. 

The individual tenants will be members of a tenant group - so click organization and then click the plus sign next to 'tenant groups'. Then give it the name of 'TLE Departments', - note how the slug is automatically generated and then simply click 'create' and that is the tenant group set up. 

Ok, so next add the tenants by clicking 'Add Tenant' in the top right corner. so the first one is Sales so we will pasted that in - and note that the group has been pre populated as we are already working within the tenant group. 

then, click 'create and add another' and then do the same for Finance, IT, Marketing and Consulting. Great, then click on Tenants to get a nice table view of them all now. 

So, that's the tenants set up based on the departments and Susan can now associate these tenants with other objects as she adds them going through. 

### Regions

Next, set up the regions and as you know from the course notes TLE Consulting is present in 4 parent regions - Africa, Asia Pacific, Europe and North America, with sub-regions nested within them.

From Regions Susan could click add here (click on add to show the interface) just like we did for tenants, but as she needs to add quite a few regions it makes sense to bulk import them to save time. 

To do this, simply click on regions and then click on the import icon in the top right - and here there is an option to either paste in the data in comma separated values format, or upload the data as a CSV file. Note the CSV options section at the bottom tells indicates which fields are required as a minimum for the data to be accepted. 

In this case it's name and slug, and these are already pre-populated. Now within their Regions, our example company TLE Consulting have nested regions for example the City of Los Angeles, is a sub-region of the State of California, which is in the United States - and the USA's parent region is North America. 

I'm sure you get the picture - so use the 'parent' field here too (add 'parent' header) when adding the sub-regions. 

So to start, add the top level regions, by pasting in the names and slugs:  

Africa,africa, 
Asia Pacific,asia-pacific, 
Europe,europe, 
North America,north-america, 

and as these don't have parents, just add a comma, but leave the value empty for the header column.  Then add the other regions that are nested below them, by pasting in those too, and where they have a parent region, include that also: 

So, paste in the countries:

Australia,australia,Asia Pacific
South Africa,south-africa,africa 
New Zealand,new-zealand,Asia Pacific
Malaysia,malaysia,Asia Pacific
United Kingdom,united-kingdom,Europe 
Canada,canada,North America
United States,united-states,North America

then add the US states

California,california,United States
Colorado,colorado,United States
Illinois,illinois,United States

then finally down to the City level: 

Johannesburg,johannesburg,South Africa
Brisbane,brisbane,Australia
Melbourne,melbourne,Australia
Sydney,sydney,Australia
Auckland,auckland,New Zealand
Kuala Lumpur,kuala-lumpur,Asia Pacific
London,london,United Kingdom
Montreal,montreal,Canada
Denver,denver,Colorado
Los Angeles,los-angeles,California
Chicago,chicago,Illinois

OK note here that Brisbane included as a region - and this will be the geographical location of the the new site that Eric and Susan are going to be deploying. 

Ok great, so click on Submit and boom! there are all of the regions created using the bulk upload method. click 'view all' and you can see how the regions are nested - for example Johannesburg, sits under South Africa, which comes under the Africa parent regions. 

### Site Groups and Sites

Alright, so next up Susan needs to set up the Site Groups and Sites. Site groups are used for functional groupings, and a site typically represents a building within a region and/or site group. 

So, TLE Consulting, has 2 Site Groups based on the function of the sites. the first is Branch so let's add that manually by clicking on organization and then the plus sign next to Site Groups. So the name is entered as 'Branch' and add a description of 'TLE Branch Sites'

click create + add another, and this one is 'corporate' for 'TLE Corporate Sites'

OK, so now the Site Groups re set up (click on org--site groups) go ahead and manually add the site for the new Brisbane branch office. So this will be a member of the Branch group (click branch) and then click 'add site'. 

So the name is 'AUBRI01', and leave the default value for the slug. As this site is not active yet, set the status to 'planned'. From the drop down, select 'asia pacific - australia - brisbane'. 

This is a branch site so there's no need for a provider or facility. similarly there is no ASN for this site, so skip that. Set the time zone to be 'australia/brisbane' and add a description of 'New branch site'

There are not tags set up yet so skip that, but do select the 'TLE departments' tenant group and then the 'consulting' department as the tenant. 

Next, paste in the address and co-ordinates:

30 Mills Street BRISBANE, Queensland(QLD), 4000
-27.611508
152.903083

And then just go ahead and click create, down at the bottom here. And that's it! wew have are new site set up. 

OK so as you know TLE Consulting has a number of other sites around the world so we will make use of the bulk upload feature again to save some time. so this time I go to Sites and click the upload link and here I have the form to submit CSV data again. For these sites we will add the name, slug, status,region,group and tenant. So I just paste them in and that's the import completed, so I can click on 'View All' and can now see the full list of sites including the planned new site in Brisbane.

### Locations 

So now the sites are set up, we will go ahead and add the locations - to re-cap, a location can be any logical subdivision within a building, such as a floor or room. All TLE Consulting Branch sites have a single location for IT equipment (the Comms Room) and the Corporate sites the comms room plus an additional location within them (the Data Center). 

So once again we will manually add the the location in the new Brisbane site, and the bulk upload the other sites from CSV data. So from locations I click 'add' and then select the region as Brisbane, the site group is Branch, the site is AUBRI01, the name is Comms Room, we'll pop in a description of 'Main IT Suite'. then lastly the the tenant group is TLE Departments and and the tenant a this location is the Consulting department. OK so I go ahead and click create on that, and there is the new location all set up. 

OK, so we'll now Locations and then the upload button for the bulk import of the rest of the locations. we'll set the headers to site,name,slug,tenant, and description, and paste in the rest of data and click submit. And we have now imported 11 locations, and If I click on 'View all' I get the nice table view again of all the locations.

### Racks and Rack Roles
Racks are physical objects into which devices are installed. NetBox models each equipment rack as a discrete object within a site and location. In our example all sites have at least 1 rack where Network/IT equipment is installed. 

Users can also create custom roles to which racks can be assigned, and TLE has defined their rack roles as Infrastructure, Compute and Storage.

### Contacts
To complete the organizational set up we will need to add some contacts. A contact is an individual responsible for a resource within the context of its assigned role. Contacts can be members of a groups, and contact roles define the relationship a contact has with an assigned object. Unique contacts are created once and can be assigned to any number of NetBox objects. 
Hello and welcome to this short video for module 2 of the NetBox Zero to Hero training course. If you haven't already checked out the first module yet then you can find the link in the video notes below to get started. For the purposes of this demo I have an instance of NetBox running as a docker container locally on my laptop, and if you would like to follow along, then you can easily do that too. There are a couple of links down below to help you spin up your own instance of NetBox, along with a link to the notes that accompany this video module. 

In this video we will be laying the foundations of the netbox data for our fictional organization called TLE Consulting. This organizational data is critical and according to NetBox best practice should be added at the start - as everything else is built on top of it.

OK, so I am logged into NetBox as the admin user and as you can see I have a completely empty database. First of all I need to set up the tenants. TLE Consulting is using the Tenancy feature to define it's internal business units and associate them with objects. 

I will put the tenants inside a tenant group - so I click organization and then click the plus sign next to 'tenant groups'. Then I'll give it the name of 'TLE Departments', then note how the slug is automatically generated for me and then I can simply click 'create' and that is the tenant group set up. 

Ok, so next I can add the tenants by clicking 'Add Tenant' in the top right corner. so the first one is Sales so I will pasted that in - and note that the group has been pre populated as we are already working within the tenant group. 

then, click 'create and add another' and then do the same for Finance, IT, Marketing and Consulting. Great, so if I click on Tenants I get a nice table view of them all now. 

So, that's the tenants set up based on the departments and I can now associate these tenants with other objects as I add them going through. 

Next I will set up the regions and as you know from the course notes TLE Consulting is present in 4 parent regions - Africa, Asia Pacific, Europe and North America, with sub-regions nested within them.

So if I go to Regions I could click add here (click on add to show the interface) just like I did for tenants, but as I am adding quite a few regions it makes sense to bulk import them to save time. 

To do this I simply (click on regions) and then click on the import icon in the top right - and here I have the option to either paste in the data in comma separated values format, or upload the data as a CSV file. Note the CSV options section at the bottom tells me which fields are required as a minimum for the data to be accepted. 

In this case it's name and slug, and these are already pre-populated for us. Now within their Regions, our example company TLE Consulting have nested regions for example the City of Los Angeles, is a sub-region of the State of California, which is in the United States - and the USA's parent region is North America. 

I'm sure you get the picture - and this means I will use the 'parent' field here too (add 'parent' header) when I add the sub-regions. 

So to start, I will add the top level regions, by pasting in the names and slugs:  

Africa,africa, 
Asia Pacific,asia-pacific, 
Europe,europe, 
North America,north-america, 

and as these don't have parents I just add a comma, but leave the value empty for the header column.  Then I can add the other regions that are nested below them, by pasting in those too, and where they have a parent region I will include that also: 

So I'll paste in the countries:

Australia,australia,Asia Pacific
South Africa,south-africa,africa 
New Zealand,new-zealand,Asia Pacific
Malaysia,malaysia,Asia Pacific
United Kingdom,united-kingdom,Europe 
Canada,canada,North America
United States,united-states,North America

then I will add the US states

California,california,United States
Colorado,colorado,United States
New York,new-york,United States

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
New York,new-york,New York

OK note here that I have included Brisbane as a region - and this will be the geographical location of the the new site that Eric and Susan are going to be deploying. 

Ok great, so I click on Submit and boom! there we have all of the regions created using the bulk upload method. and if I refresh the view you can see how the regions are nested for example Johannesburg, sits under South Africa, which comes under the Africa parent regions. 





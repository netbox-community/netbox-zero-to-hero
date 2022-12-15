Hello and welcome to module 11 of the NetBox Zero to Hero training course. If you haven't already checked out the earlier modules yet then you can find the link to them in the notes below to get started. 

For this demo I am using a docker instance of NetBox running locally on my laptop. If you would like to follow along with the demo, then you can easily do that. There are a couple of links down below to help you spin up your own instance of NetBox, along with a link to the course that accompanies this video. 

Now it's time for the Brisbane office to 'go live', so Eric is going to use a custom script to update the status of the Site, plus all the Locations, Racks, Devices, Clusters and VMs at the site from `Planned` to `Active` This will be much quicker and more convenient than having to go into each section of the NetBox UI to update the status of all the objects. He can simply run the script to update everything in a couple of seconds!

Eric's boss has also just informed him that a new branch office is planned for Stockholm, Sweden and that he should start to plan for this. As the company has standardized on the same network equipment for all branch office locations, Eric is going to use another Custom Script to create the planned site in NetBox, and populate it with all the  network devices that he is planning to deploy there. 

Eric is logged into NetBox and has already copied the two scripts into the scripts folder on the NetBox server. To view the available scripts - they are under the 'other' section and under the heading 'scripts', and here you can see the 2 scripts that are available to run - and the first one that Eric will run is the 'Site Status Bulk Updater' script - and if you click on it you can see the description - this script will Update the status of a Site, and all Locations, racks, devices, clusters and VMs at the site. 

So before we run the script lets take a look at the Code - I have opened the file called SiteStatusBulkUpdater.py and starting at the top there are the import statements - All custom scripts must inherit from the extras.scripts.Script base class. This class provides the functionality necessary to generate forms and log activity.

Next, as this script is working with objects within the DCIM and virtualization data models, we import some classes from here too. taking Virtualization as an example - from virtualization.models we import the VirtualMachine and Cluster class, and from virtualization.choices we import VirtualMachineStatusChoices, ClusterStatusChoices 

If you are not familiar with python or just starting out with it then it will help to view the source code of NetBox in the git repo to see what these import statements are doing - so from the UI scroll down to the bottom and click on the Source Code icon to take your there. 

OK, so if you navigate to netbox/virtualization/models/virtualmachines.py and scroll down to 'class VirtualMachine' you see the base class for a virtual machine that is being imported into the custom script.  Next if you navigate back to virtualization / choices.py you can see for example the class of ClusterStatusChoices - and you see the status choices available for clusters. So as the custom script is importing these python classes we can make use of them to be able to update the status of virtualization objects. 

I hope that makes sense - and the point here is that the complete Python environment is available to a custom script, including all of NetBox's internal mechanisms. so if you are developing your own custom scripts then at some point you will probably need to refer to the NetBox source code. 

Ok, back to the script itself - after the imports you have the script class that inherits the Script Base class. There is also some class meta data - in this case the name and a description of what the script dopes. 

The next section is a set of variables that the script will use - and you can see that these map to the user inputs for the script in the web UI - for example the first input is the Site name  - and this means the user will see a drop down menu containing a list of the sites. the next variable is Site status - and this makes use of the SiteStatusChoices class, which means that the user is presented with a drop down of the available status choices for Sites - with a default value of ACTIVE. 

Then moving down the other variables are very similar in that they display the available status choices for each object type. OK so that's the script variables - now the other component that a custom script needs to have is a run method -  and this is where your script's execution logic lives. The run method accepts two arguments - Data which is a dictionary containing all the variable data passed via the web form, and Commit which is a Boolean (ie either true or false) indicating whether database changes will be committed or not. 

So the first part of code here from line 59 down to line 62 is making the update to the status of the site object which is pulled from the Site Objects using the get method with the name being passed in as the value of the 'site_name' key from the data dictionary. then the status is set to be the value of 'site_status', and the object is then saved, and a log message written on a successful update.   

Then the rest of the code is very similar - but because there are likely multiple objects for locations, racks and devices etc, at the site being updated - the script loops over each object - for example in lines 66 to 69 for each location matched by filtering the location objects by the site name - the script updates the status, saves the object, and writes a log message. 

Ok so that's a quick run through of the code - now flip back to the UI and before running it just check the status of the devices for example - and you can see that all devices at the Brisbane site have a status of planned. so let's launch the script now and select the Brisbane site, and then of all the other input variables are defaulted to Active, but just to show you if you click the drop down next to devices for example you can see the Device Status Choices that are available as they were imported at the top of the script.

One last thing to note is that if you just want to test your script without committing any changes to the database then you can simply uncheck the box. We'll leave it checked and click Run Script. the run takes a few seconds to complete and at the end of it you can see all the log messages that were generated for the objects being updated. 

And just to double check that, have a quick look around - and the site is now active, the rack is active and all the devices are active. You can also confirm the changes in in the Change log - if you click the first record you can see the difference in the status from planned to active. 

Fantastic - that's the first script run. the next one Eric will run is the New Branch script - and this is what it looks like in the web interface, with inputs for all the data required to add a new site and all of it's devices. Before running let's just take a quick look at the code again - all the variables are defined again and these display the user inputs for the site name, and the number and model of devices to add - so that's fairly straightforward. 

and then in the run method the site is created first, then take a look at how the access switches are created for example - from line 57 to 68 - the role of the switch is defined as 'Access Switch' which one of the device roles that already exists, and then for each switch it creates a new device with the device type being the switch model, the name being the slug of the site, in upper case then -SW then - the number of the of the switch. 

the site value  is the site that has just been created, the status uses the DeviceStatusChoices method and sets it to planned, and the role is also set based on the value of the switch_role variable. Then the new object is saved, and a success log message is generated.

this same pattern of code repeats for the routers, wireless access points and servers, and then finally the last step from line 110, generates a CSV table of the new devices which is then displayed in the output. 

Ok, so let's give this script a run from the web UI. The new site is in Stockholm, sweden, so the name will be SW STO 01. it will have 4 switches, that are the Juniper EX4300-48P model. then it's 2 ISR4321 WAN routers, 6 MR56 APs, and 4 Proliant DL380 servers. So click on run script - and you can ow see the success log messages, and in the output you have the CSV formatted list of the devices that hve been created.

So to check the data, go to sites, and there is the new site with a status of planned, click on the site and then the devices, and you can see the list of all the newly created devices. How easy was that!

So, I hope that has been a useful overview of what Custom Scripts are in NetBox and what kind of tasks they can be used to accomplish. You also learned the basics of writing Custom Scripts and where to find documentation to help you develop your own scripts. You also got a head start with the two example scripts included with this module.

If you fancy a challenge why not see if you can develop one of the scripts further - for example you could also create the rack for new site, and then assign all newly created devices to the next available rack unit positions. Or you could also add in patch panels, console servers and PDU's - to make adding a new site even easier!

If you want to share your own custom scripts or have any questions as you go through the course then pop on over to the NetBox Zero to Hero channel on the NetDev Community Slack! If you aren't already a member then you can sign up for free using the link below.

So, once again, thanks very much for watching!
Hello and welcome to this video for module 9 of the NetBox Zero to Hero training course. If you haven't already checked out the earlier modules yet then you can find the link to them in the notes below to get started. 

For this demo I am using a docker instance of NetBox running locally on my laptop. If you would like to follow along with the demo, then you can easily do that. There are a couple of links down below to help you spin up your own instance of NetBox, along with a link to the course that accompanies this video. 

In this video, Eric will add the facility power panels and feeds for the new Brisbane branch office, and then also add the PDUs and power cable connections, so all the devices in the new communications cabinet can be powered on. 

So, the first thing to do is to add the 2 power panels, so under the power section, click the plus icon next to power panels, select the brisbane region, the branch site group, and the site AUBRI01. the location is the comms room, and give this one the name of AUBRI01-PWR-PAN-1, then click create and add another - this one is the 2nd power panel so the name ends in -2, and click create.

Next create the primary and secondary power feeds that will come off the power panels. so click on the plus next to power feeds - select the region and the site, and then the power panel - in this case it is panel 1. 

moving down to the power feed section - select the rack and then add the name of feed-1. Now this feed will be the primary feed, so moving down to the characteristics - the supply is AC, 200 volts, 16 amp, single phase - and leave the maximum utilization at 80% - so that we are not at risk of attempting to draw too much power from it. 

then click create and add another. you'll notice that most of the fields are now pre-populated by design, so there are only a couple of things to change here. firstly this is being supplied by power panel 2, and is named feed-2, and this one is going to be the redundant feed, so select that from the drop down. the electrical characteristics are the same, so just click create. 

Excellent, so that's the panels and the feeds set up (click on power feeds to show list), the next things to add are power distribution units or PDUs, that will be supplied by the feeds. so, create the device role for the PDUs - click the plus next to device roles and then add PDU, and go with red for the colour, uncheck vm role, and click create. 

In NetBox PDUs are modelled as normal devices, to as you did for the other devices so far, start by adding the manufacturer, so it's devices, manufacturers click the + and the PDU is made by APC, so add that and click create. 

Next, the device type that Eric has chosen is the AP7921B model, so you can add this by importing from the device type library - so from the github repo (https://github.com/netbox-community/devicetype-library/blob/master/device-types/APC/AP7921B.yaml) copy the yaml definition and then in the UI, click on the blue import icon next to device types, and then paste in the yaml and click submit. 

So if you take a look at the device type - you can see it has 1 power port that will connect to the power feed, and 8 power outlets that will the devices in the rack will connect to.

Next create 2 devices from this device type, by clicking on the blue import icon next to devices, and then paste in the CSV data to define the 2 PDUs - AUBRI01-PDU-1 and 2. Note that the csv data also includes the rack mounting information - with the first PDU located at rack unit 11, and the second at unit 12 and facing the rear of the rack. so after clicking on submit, check the rack elevation now by clicking on the link to the rack - and there are the 2 new PDUs at the of the rack - and you can now also see the 2 power feeds listed underneath. 

Next add the power connections from the power feeds to the PDUs by clicking on power feeds and selecting the first feed and then click connect on the right hand side - you can see that A side is pre-populated with the power panel and power feed - so on the B side, select the region, site group, site, location and rack - and for the device select the 1st PDU, and it's power port - remember this is not a power outlet for devices as this is connected to the upstream power feed. 

The type is power, the tenant group is TLE Departments and the tenant is consulting, and click create. then do the same for the 2nd feed - and this time the B side is going to be the 2nd PDU, again power port 1. type is power and the same tenancy information. and click create. so now if you click on power feeds, you see both the connections to the PDUs.

Fantastic - now it's time to add the power connections for the network devices and servers - and once again do this using the CSV data from the file in the git repo that file accompanies this module. click on connections, and then the blue import icon, and paste in the csv data for the power cables. 

These are connecting the power ports of the devices to the power outlets of the PDUs - and note that as there is a redundant power supply where a device has dual PSU's these connections are split across both PDUs - then click submit. and that is all of the cables required to connect up the power and if you click on Power Connections they are all listed there.

OK, so the last thing to do is to update the allocated draw values for each of the power ports on the devices in the rack, so that we can track the utilization correctly. So go to devices - power ports and then for the ps1 power port for the console server - select it and click edit, then set the allocated draw to 20 and click apply. then for the router set the allocated draw to 100. then select both of the switch power ports and edit them and set them to 700 watts. and lastly select all 4 PSUs for the servers and set the allocated draw too 900 watts. 

Great, so now that is done, check the power utilization is being tracked correctly - firstly go to the rack, under organization, racks and then select the brisbane rack - and here you can see the utilization of the available power for the rack is standing at 57%, so that's looking pretty good!

So, I hope that has been a useful overview of how NetBox models facility power as discrete power panels and feeds, and also how to add Power Distribution Units or PDUs to supply power to individual devices. 

If you have any questions as you go through the course then pop on over to the NetBox Zero to Hero channel on the NetDev Community Slack! If you aren't already a member then you can sign up for free using the link below.

So, once again, thanks very much for watching!
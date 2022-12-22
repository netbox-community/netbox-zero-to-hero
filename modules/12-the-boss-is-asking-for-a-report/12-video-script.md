Hello and welcome to module 12 of the NetBox Zero to Hero training course. If you haven't already checked out the earlier modules yet then you can find the link to them in the notes below to get started. 

For this demo I am using a docker instance of NetBox running locally on my laptop. If you would like to follow along with the demo, then you can easily do that. There are a couple of links down below to help you spin up your own instance of NetBox, along with a link to the course that accompanies this video. 

Now that the new Brisbane site is active, the IT Manager has asked Susan to produce some reports from NetBox to make sure that everything has been deployed in line with company standards. These standards are that every device has either an IPv4 or IPv6 Primary address assigned and that every device meets the required naming convention standard 

Susan is logged into NetBox and has already copied the two reports into the reports folder on the NetBox server. To view the available reports - they are under the 'other' section and under the heading 'reports', and here you can see the 2 reports that are available to run - and the first one that Susan will run is the 'Ip-primary-missing' report - and you can see the description - this report will check that every device has either an IPv4 or IPv6 primary address assigned. 

So before we run the report lets take a look at the Code - I have opened the file called Ip-primary-missing.py and starting at the top there are the import statements - first of all this report is working with objects within the DCIM data model, we import the DeviceStatusChoices and Device classes. and as you can see from line 3 - each report is defined as a Python class inheriting from extras.reports.Report.

Moving down to line 5 - each report is defined as a Python class that performs a certain function - so here we are defining the 'DeviceIPReport' class with it's description. Then the logic of each report is broken down into discrete test methods, each of which applies a small portion of the logic comprising the overall test. So this report has only one test defined - and it loops over all devices that have a status of active, and then checks that they have IPv4 or IPv6 primary addresses or not - and logs either warnings, failures or successes based on the results. 

Ok so that's a quick run through of the code - now flip back to the UI and let's run the report now, so click on 'run again' next to the report name - and it just takes a few seconds to run. and if you look at the results there are 3 failures - so the access points and the console server do not have either v4 or v6 primary IP addresses, and for information the logs show that 4 devices are missing an IPv6 primary IP address - but that is just informational as they have v4 addresses. 

Fantastic - that's the first report run. the next one Susan will run is the 'CheckDeviceNaming' but before running let's just take a quick look at the code again - This one is importing the 're' python module that is used for the regular expression matching on the device name, and the other imports are the same as the first report. 

the report class definition starts on line 10 and you can see the the description stating that this report will verify that each device conforms to the naming convention. on line 13 the test method is defined and this is a very straightforward method - which simply loops over all active devices and then does a regex match on the device name - to make sure it is in the correct format. If a device name is not in the correct format then it will log a failure message stating this.

Ok, so let's give this report a run from the web UI. click on run again - and after a few seconds that has completed - and you can see all of the device names comply to the naming convention as there are no failure messages in the results. So that is great, and means that Susan does not have to fix any incorrectly named devices. 

So, I hope that has been a useful overview of what NetBox reports are and what kind of things they can be used to verify. You now know the basics of reports and also where to find documentation and examples to help you develop your own reports. 

If you fancy a challenge why not see if you can develop one of your own reports, and if you want to share this or have any questions as you go through the course then pop on over to the NetBox Zero to Hero channel on the NetDev Community Slack! If you aren't already a member then you can sign up for free using the link below.

So, once again, thanks very much for watching!
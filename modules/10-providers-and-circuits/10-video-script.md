Hello and welcome to this video for module 10 of the NetBox Zero to Hero training course. If you haven't already checked out the earlier modules yet then you can find the link to them in the notes below to get started. 

For this demo I am using a docker instance of NetBox running locally on my laptop. If you would like to follow along with the demo, then you can easily do that. There are a couple of links down below to help you spin up your own instance of NetBox, along with a link to the course that accompanies this video. 

Now it's time to connect the new site to the Internet, and in this video Network Engineer Susan will add the new Internet Circuit. So, By the end of this video you will be able to, describe how NetBox models service providers and circuits, and understand how to "connect" circuits directly to device interfaces via cables. You'll aso see another example of how to use use Postman to make API calls to NetBox to add this data programmatically. 

Susan is logged into NetBox and has retrieved her API token, which she will use to authenticate her API calls in postman. If you need a re-cap on how to set this up yourself in postman, and how to explore the API documentation, then just check out modules 1and 3 of this course for a quick overview of that. You will also find a link to the postman collection that accompanies this course in the notes below. 

OK, so in postman, you will notice that there is a folder in the collection called Circuits, and in there we have API calls already written to get you started. So, click on get providers for example then you see the API call that is being made is to the circuits/providers endpoint, and clicking on this returns no results yet, as you would expect.

As a reminder, if you need to explore the API to find the end point you need, then simply click on the rest API link in the footer of the web interface - and then for example click on circuits and providers - you see the same results as in the postman request you just made. You also have the link to the rest API swagger documentation, which you can explore to help you build your API calls.

So, with that said, before you can add a circuit you must first add a provider - so the first API call is a POST request to the /circuits/providers/ end point, and in the body of the request there is a json definition of the Telstra provider object. There is a name, slug, account reference, a portal URL and a couple contact emails - one for the NOC and one for admin. 

click send to make the call, and there is a successful request with a 201 response message back from the NetBox server, and the response contains the full json object of the newly created provider. Great so now, the next API call to make is to add the circuit type - 

again there is a POST request in the collection - this time to the /circuits/circuit-types/ end point and the body of the request has a json definition of the circuit type object. which just contains the name, slug, and a description. 

Click send again, and it's another successful request with a 201 response message, and the response contains the newly created circuit type. Once again - note there is a numeric ID for the each of the objects that have been created - these numeric ID'd are very important for future API calls.

great, so with the provider and circuit type all set up you can go ahead and add the actual circuit - again there is a POST request in the collection - this time to the /circuits/circuits end point and the body of the request has a json definition of the circuit, which contains the circuit ID, which is a string, the provider which is the ID of the provider object you just created - if you need to check this you can run the get providers API call to return a list of of all the providers - then the id of the circuit type, the status, tenant and commit_rate. 

So, Click send, and the response is a 201 - so that's great, and the response contains the newly created circuit. All good so far. Now the last API call to make in postman is to add the circuit termination - remember that the documentation states that Each circuit may have up to two terminations (A and Z) defined. Each termination can be associated with a particular site or provider network - so in this case the json payload contains the circuit ID, and it defines Z end as being the site name, and it also defines the port speed as 200 Mega bits per second.   

so, click send again, and it's another successful request! So, now for the las part - switch back to the web UI to check what has now been added by the API calls - starting with circuits and then providers - then click on telstra, and you can now see the provider information, and also note that there is the new circuit that you added - so click the link for that to view the details, and notice the Z end termination into the brisbane site. 

Now, notice that there is a connect icon so click that and select interface. now you can see that you are adding a new cable with the A side defined as the circuit and the for the B side - select the location, and the rack, then the device is the router, and the interface is gigabitethernet0/0/1. Then select the type as cat 6, the colour can be purple, and the cable is 2 metres long. and click create.

And finally, as with all cables, you can click the trace icon, to bring up a visual of the cable connection - and as you can see it goes from the router interface to the new circuit. 

So, I hope that has been a useful overview of how NetBox models providers and circuits, and how to "connect" circuits directly to device interfaces, and also how do to this by using some new API calls added to your Postman collection for NetBox. 

Don't forget, If you have any questions as you go through the course then pop on over to the NetBox Zero to Hero channel on the NetDev Community Slack! If you aren't already a member then you can sign up for free using the link below.

So, once again, thanks very much for watching!
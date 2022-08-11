## Scenario
- Quick overview to familiarize users with the API
- Log into demo instance https://demo.netbox.dev/

Welcome to this short video, in which you will be introduced to the NetBox REST API. Once again we will be using the public demo instance of NetBox which is freely available to use @ demo.netbox.dev. 

There are a couple of links to start exploring the REST API that you can find in the footer of the Web interface. The first one allows you to explore the API via a web browser and takes you to it's root at /api/  

By clicking the link we made a GET request to the API root, and from the json output in red we can clearly see the API endpoint hierarchy, and at the root level the URL's are divided by application, and these apps should be familiar now after the previous video where we explored the WEB UI. So they go from Circuits all the way down to wireless.  

So if we click on the URL for the circuits application, we can see the separate paths for each model. For example if we want to explore the 'providers' model we click on the URL which performs the GET request to the /api/circuits/providers/ endpoint and the json response returns a list of all the providers. 

Each model has 2 types of views associated with it - a list view and a detail view - and what we are looking at here is the 'list' view of 'providers' model - which lists multiple objects in the json output.  The 'List'view is is also used to create new objects via the REST API.

In this case the json output from the GET request returns a list of 9 providers, and in the results part of the json output we can see each provider,  ID number 1 here is the record for 'AT&T' and if we click the URL it will take us to the 'detail' view for this object. 

The 'detail' view allows you to retrieve, update, or delete a single existing object. As you will note here again - all objects are referenced by their numeric primary key (id) in this case the id is '1'. Note also how you can see the full path of the GET request is now /api/circuits/providers/1/

So by using this tool to manually navigate the API in this way you get a clear understanding of the hierarchical structure of the endpoints within it.



So, I hope that has been a useful introduction to the NetBox REST API, and thanks for watching!
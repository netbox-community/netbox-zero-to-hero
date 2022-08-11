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

OK, so if we navigate back to the WEB UI, the other REST API link in the footer takes you to interactive documentation of all the REST API endpoints at /api/docs/. This interface provides a convenient sandbox for researching and experimenting with specific endpoints and request types. 

So let's use the providers example again - and If we scroll down to the 'circuits/providers' endpoint - we can see the API request types that are available to us. if we click on the GET request type and then just scroll down and execute this request without specifying any options we few different things in the responses. 

First of all we see the 'Curl' command has been generated for us to make the API call - so this is really useful as it shows you how to construct the Curl request yourself, you could copy and paste this into your terminal and run the command yourself. Then we see the request URL - which as we know is /api/circuits/providers/

and then we see the actual response from the server - we see the status code of 200 which means the API call was 'successful' and then we can see the full json output in the response body and further down we can see the response headers and the request duration tells us how many milliseconds the request took to complete.

If we review the json output we see that it is the same output as we saw previously with a count of 9 providers returned in the list view. OK, so let's try and filter the output to the detail view for one specific providers, and we can do that easily if we scroll back up we see that we can test out query strings in the API calls - so let's go ahead do that. remember that each object can be referenced by it's numeric primary key, so if we add the id of 1 to the query and then execute it again note that the request URL is now different as it contains the added query parameter of /?id=1. And then in the response we can see that we detail view for this provider, AT&T. 

So now you must be thinking hmm OK, this is great but how about we try adding a new provider via the API? Let's try it out by scrolling down the list of available request types and here we have the POST type has the function of creating a new provider so lets click 'try it out' - and then if we click on the model the first thing to note is that for the provider model there are 2 required fields - name and slug - so these are needed as a bare minimum for the request to be a success. So lets's edit the body and remove all other fields apart from the name and slug which we weill edit to be 'Awesome Provider' OK no click o[n execute - and let's see what happens!

OK so first of all the response code is 201 - which means 'the request has succeeded and has led to the creation of a resource'. and then if we look at the response body we see that we have an ID of 11 and the name and slug of our new provider. OK so let's check in the Web UI that to confirm what we did - and we click on Circuits and Providers - sure enough we see our 'Aweseome Provider' in the list. fantastic!   

As we didn't add any other information as part of the request to set up the provider, let's update it with a  Customer portal URL. Now as we have seen, the documentation is a great way to test interacting with the API, bit let's take it a step further and use Postman to do the update - if you are not familiar with it, Postman is an API platform for building and using APIs and is a great way to interact with the BetBox API. 


- delete new provider
- view in Web UI

So, I hope that has been a useful introduction to the NetBox REST API, and thanks for watching!
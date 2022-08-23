## Scenario
- Quick overview to familiarize users with the API
- Log into demo instance https://demo.netbox.dev/

Hello and welcome to this short video, which will introduce you to the NetBox REST API. Once again we will be using the public demo instance of NetBox which is freely available to use @ demo.netbox.dev. 

There are a couple of links to start exploring the REST API that you can find in the footer of the Web interface. The first one allows you to explore the API via a web browser and takes you to it's root at /api/  

By clicking on that link we made a GET request to the API root, and from the json output in red we can clearly see the API endpoint hierarchy, and at the root level the URL's are divided by application, and these apps should be familiar now after the previous video where we explored the WEB Interface. So they go from Circuits all the way down to wireless.  

And if we click on the URL for the circuits application, we can see the separate paths for each model. For example if we want to explore the 'providers' model we click on the URL which performs the GET request to the /api/circuits/providers/ endpoint and the json response returns a list of all the providers. 

Each model has 2 types of views associated with it - a list view and a detail view - and what we are looking at here is the 'list' view of the 'providers' model - which lists multiple objects in the json output.  The 'List' view is is also used to create new objects via the REST API.

In this case the json output from the GET request returns a list of 9 providers, and in the results part of the json output we can see each provider,  ID number 1 here is the object for 'AT&T' and if we click the URL it will take us to the 'detail' view for this object. 

The 'detail' view allows you to retrieve, update, or delete a single existing object. As you will note here again - all objects are referenced by their numeric primary key in this case the key is id and the value is '1'. Note also how you can see that the full path of the GET request is now /api/circuits/providers/1/

So by using this tool to manually navigate the API in this way, you get a clear understanding of the hierarchical structure of the API and the endpoints within it.

OK, so if we navigate back to the Web interface, the other REST API hyperlink in the footer takes you to interactive documentation of all the REST API endpoints at /api/docs/. This interface provides a convenient sandbox for researching and experimenting with specific endpoints and request types. 

So let's use the providers example again - and If we scroll down to the 'circuits/providers' endpoint - we can see the API request types that are available to us. if we click on the GET request type and then click on 'try it out', and then scroll down and click 'execute' on this request without specifying any options, we then see a few different things in the response. 

First of all we see the 'Curl' command that has been generated for us to make the API call - so this is really useful as it shows you how to construct the Curl request, so you could copy and paste this into your terminal program and run the Curl command yourself. 

Then we see the request URL - which as we know is /api/circuits/providers/

and then we see the actual response from the server - the status code of 200 which means the API call was 'successful' and then we can see the full json output in the response body. Further down we have the response headers, and the request duration tells us how many milliseconds the request took to complete. If we review the json output we see that it is the same output that we saw previously with a count of 9 providers returned in the list view. 

OK, so let's try and filter the output to the 'detail' view for one of the specific providers, and we can do that easily if we scroll back up we see that we can test out query strings in the API calls - so let's go ahead do that. remember that each object can be referenced by it's numeric primary key, so if we add the id of 1 to the query and then execute it again, note that the request URL is now different as it contains the added query parameter of /?id=1. And then in the response body we can see that we now have the 'detail' view for this provider, AT&T. 

So now you might be thinking hmm OK, this is great but how about we try adding a new provider via the API? Let's work out how to do that by scrolling down the list of available request types...and here we have the POST type which has the function of creating a new provider so lets click 'try it out' - and then if we click on the model the first thing to note is that for the provider model there are 2 required fields - name and slug - so these are needed as a bare minimum for the request to be a success. 

So lets's edit the body and remove all other fields apart from the name and slug which we will edit to add a new 'Awesome Provider' 'awesome-provider. OK now click on execute - and let's see what happens!

First of all the response code is 201 - which means 'the request has succeeded and has led to the creation of a resource'. and then if we look at the response body we see that we have an ID of 11 and the name and slug of our new provider. OK so let's check in the Web UI and confirm what we did - and we click on Circuits and Providers - and sure enough we see our 'Awesome Provider' in the list. fantastic!   

As we didn't add any other information as part of the request to set up the provider, let's make another API Call to update it with a Customer portal URL. First of all let's work out how to construct our new API call from the documentation -  scroll down and check the available request types for the circuit/providers endpoint. We can see that the 'patch' request will do partial updates, and it takes the ID of the provider that we want to update - so that sounds like what we need. 

Now as we have seen, the documentation is a great way to test interacting with the API, but let's take it a step further and use a tool called Postman to do the update - if you are not familiar with it, Postman is an API platform tool for building and using APIs, and is a great way to interact with the NetBox API's. 

This is the postman interface, and here we have an API request, that I've already created and I've given it the name of 'update provider'. The request type is 'patch' - you can see from the drop down you can select other types from here also. Note the URL containing the full path to the endpoint including the ID of the provider we are going to update, which had an ID of 11. 

Then you can see we have added some headers to the API call which specifies the content type as json, and also includes an authorization token which is required to authenticate to NetBox via the API (and we will cover tokens in a later module in more detail).  

Next up we have the body of the request, which contains the actual json payload that we are going to send in the API call. the field we are updating the is the 'portal_url' and we will give it the value of support.awesomeprovider.com. 

Ok, so that's our API call built - so let's click send and take a look at the output. firstly the status code is 200 so all good there and in the json response back from the server we can see that provider ID 11 has been updated, which is great! so if we switch back to the UI and hit refresh - we can see our newly added customer portal URL.

So far so good! So lastly, le's say that this provider has turned out to be not quite as awesome as we had hoped and we are no longer using them for any of our circuits. Let's make another API call to delete this provider. ......from the API docs we can see that the 'delete' request type is available and it takes the ID of the provider in the path again. 

so back in postman let's duplicate our first API call and amend it slightly. we will call this one 'delete provider' and change the request type to 'delete' and then We clear the body of the json as we don't need it for this call, and then save it for future use in the collection of API calls we are building in Postman. 

Now in a production set up where you are programmatically interacting with NetBox it would be more realistic to be sending the ID of the provider you are deleting as a variable in some code that is making the API call - well postman lets you set variables too - so if we double click on the ID value of 11 and then click 'set as variable' give it the name 'provider_id' leave the initial value as 11, and set the scope to be the collection of NetBox API calls we are building, and then 'set' the variable. if we now check the collection, and under variables we can see it is set there and we can make use of it in our API call now. 

so that's all good. and we will just click send to make the API call to netbox. this gives us a status code of 204 which means 'the server has successfully processed the request, but is not returning any content', which makes sense. 

I'll just show you one other very nice feature of postman while we are in it and that is if you click on the code icon on the right hand side it will generate the code in whatever language you would like it, in this case it's python as that's what I selected last time I used it - but you can change this to whatever you need, Curl for example or even Go. and then you can copy and paste this into your own scripts and code as your start to build your own tools to interact programmatically with the NetBox API.  

OK, so the last thing we will do is switch back to the Web interface and check that the list of providers has now been updated and the provider has been deleted - and we click on Providers and sure enough the 'not so awesome provider' is no longer in the list view.  

So, I hope that has been a useful introduction to the NetBox REST API, and hopefully you can see how you can very quickly and easily get up and running with it! Thanks for watching.



---
layout: post
title: Here Client
categories: [web, ui]
tags: [Java, here, Client]
---
# Here Client

## Java here Client

    package de.softwareengel.test.here_api;

    import java.net.URI;

    import javax.ws.rs.client.Client;
    import javax.ws.rs.client.ClientBuilder;
    import javax.ws.rs.client.Entity;
    import javax.ws.rs.client.Invocation;
    import javax.ws.rs.client.WebTarget;
    import javax.ws.rs.core.Form;
    import javax.ws.rs.core.MediaType;
    import javax.ws.rs.core.MultivaluedMap;
    import javax.ws.rs.core.Response;
    import javax.ws.rs.core.UriBuilder;

    import org.glassfish.jersey.client.ClientConfig;
    import org.glassfish.jersey.client.ClientResponse;
    import org.glassfish.jersey.internal.util.collection.MultivaluedStringMap;

    public class T2 {

	    public static void main(String[] args) {
    //		ClientConfig config = new ClientConfig();
    //
    //		Client client = ClientBuilder.newClient(config);
    //
    //		WebTarget target = client.target(getBaseURI());
    //
    //		String response = target.path("rest").path("hello").request().accept(MediaType.TEXT_PLAIN).get(Response.class)
    //				.toString();
    //
    //		String plainAnswer = target.path("rest").path("hello").request().accept(MediaType.TEXT_PLAIN).get(String.class);
    //		String xmlAnswer = target.path("rest").path("hello").request().accept(MediaType.TEXT_XML).get(String.class);
    //		String htmlAnswer = target.path("rest").path("hello").request().accept(MediaType.TEXT_HTML).get(String.class);
    //
    //		System.out.println(response);
    //		System.out.println(plainAnswer);
    //		System.out.println(xmlAnswer);
    //		System.out.println(htmlAnswer);

    ////    GET https://matrix.route.api.here.com/routing/7.2/calculatematrix.json?
    //		app_id=MEnNXC76924fZl0qjP97&app_code=ZjOCaOqBSqnfVthq81-HtA&start0=geo%2151.515645%2C7.426471&destination0=geo%2151.513711%2C7.491120&destination1=geo%2151.502130%2C7.460773&mode=balanced%3Bcar%3Btraffic%3Adisabled HTTP/1.1
    ////	Accept-Encoding: gzip,deflate
    ////	Host: matrix.route.api.here.com
    ////	Connection: Keep-Alive
    ////	User-Agent: Apache-HttpClient/4.1.1 (java 1.5)

		    ClientConfig config = new ClientConfig();

		    Client client = ClientBuilder.newClient(config);

		    WebTarget target = client.target(getBaseURI());
		    Form form = new Form();
		    form.param("x", "foo");
		    form.param("y", "bar");

		    Entity<Form> entity = Entity.entity(form, MediaType.APPLICATION_FORM_URLENCODED);

    //		String response = target.path("routing/7.2/calculatematrix.json").request().accept(MediaType.TEXT_PLAIN)
    //				.get(Response.class).toString();

		    // app_id=MEnNXC76924fZl0qjP97&app_code=ZjOCaOqBSqnfVthq81-HtA&start0=geo%2151.515645%2C7.426471&destination0=geo%2151.513711%2C7.491120
    //				&destination1=geo%2151.502130%2C7.460773&mode=balanced%3Bcar%3Btraffic%3Adisabled HTTP/1.1
		    target = client.target(getBaseURI()).path("routing/7.2/calculatematrix.json");
    //		target.path("routing/7.2/calculatematrix.json");
		    MultivaluedMap<String, String> params = new MultivaluedStringMap();
		    params.add("K1", "V1");
		    params.add("K2", "V1");
    //		WebResource resource = client.resource(url);
    //		ClientResponse response = client.queryParams(params).type("application/x-www-form-urlencoded").get(ClientResponse.class);
    //        String en = response.getEntity(String.class);

		



		    WebTarget targetWithQueryParam = target.queryParam("app_id", "MEnNXC76924fZl0qjP97XXX")
				    .queryParam("app_code", "ZjOCaOqBSqnfVthq81-HtAXXX")
				    .queryParam("start0", "geo!51.515645,7.426471")
				    .queryParam("start1", "geo%2151.502130%2C7.460773")
				    .queryParam("destination0", "geo%2151.513711%2C7.491120")
				    .queryParam("destination1", "geo%2151.502130%2C7.460773")
    //				.queryParam("mode", "balanced;car;traffic:disabled");
				    .queryParam("mode", "fastest;truck;traffic:disabled")
				    .queryParam("summaryAttributes", "traveltime,distance,costfactor");

    //		targetWithQueryParam = target.queryParam("start0", "geo%2151.515645%2C7.426471");
    //		targetWithQueryParam = target.queryParam("destination0", "geo%2151.513711%2C7.491120");
    //		targetWithQueryParam = target.queryParam("destination1", "geo%2151.502130%2C7.460773");
    //		targetWithQueryParam = target.queryParam("mode", "balanced;car;traffic:disabled");

		    Invocation.Builder invocationBuilder = targetWithQueryParam.request(MediaType.TEXT_PLAIN_TYPE);
    //		invocationBuilder.header("some-header", "true");

		    Response response2 = invocationBuilder.get();

		    String plainAnswer = targetWithQueryParam.request().accept(MediaType.TEXT_PLAIN).get(String.class);
    //		
    //		String xmlAnswer = target.path("routing/7.2/calculatematrix.json").request().accept(MediaType.TEXT_XML)
    //				.get(String.class);
    //		
    //		String htmlAnswer = target.path("routing/7.2/calculatematrix.json").request().accept(MediaType.TEXT_HTML)
    //				.get(String.class);

    //		System.out.println(response);
		    System.out.println(response2);
    //		System.out.println(responseResult);

		    System.out.println(plainAnswer);
    //		System.out.println(xmlAnswer);
    //		System.out.println(htmlAnswer);
	    }

	    private static URI getBaseURI() {
		    return UriBuilder.fromUri("https://matrix.route.api.here.com").build();
	    }

    }

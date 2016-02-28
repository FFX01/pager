# Pager
Pager is a small headless CMS with hierarchical pages.

## What is a CMS?
A CMS is a a 'Content Management system'. Some widely used CMS frameworks are Wordpress, Wagtail, Drupal, and Django CMS.

## What is a 'Headless CMS'?
A headless CMS is a CMS that does not use a templating engine. It does not serve HTML or static files. It only serves it's content through serving data types like JSON or XML through a RESTful API. 

## What is the advantage of a Headless CMS?
### There are many advantages. Some of these are:
- Decoupling the data layer from the view layer.
- Allow many different applications to hook into your backend without additional configuration.
- Allow different devices such as smart phones or tablets to use the same backend as a website.
- Reduce overhead and response time by removing the need to serve html or populate templates.
- Allows front end developers to use whatever tools and libraries they deem best without modification the application logic.
- Allows application developers to focus on rich content delivery instead of wrestling with front end frameworks and libraries.

### Some trade-offs include:
- In a way, you are developing more than one application. The backend will serve data, but You will need a front end application to fetch this data and allow users to interact with it. 
- A Headless CMS is more difficult to learn to use for some people.
- You will need to write API documentation so front end developers can use your API.

## How Pager Works
At this time Pager only does one thing. It serves a 'Page' model. This 'Page' model is attached to a stock Django 'User' model. It allows for the creation of new 'Page' models through the standard Django admin interface. It also allows creation of new pages by POSTing JSON data to the correct endpoint. Users must be authenticated through the standard Django session middleware in order to allow POST or PUT requests. Basically, Pager doesn't do anything special at this point.

- Pager uses [Django Rest Framework](https://github.com/tomchristie/django-rest-framework) to create it's API endpoints and allow for serializing model data into JSON.
- Pager uses [django-mptt](https://github.com/django-mptt/django-mptt) to allow for hierarchical models.

### New content types/models can be easily created
- Create a new App
- Create a new model(Use MPTTModel for hierachical models)
- Create a new model serializer(check Django Rest Framework docs for how to do this. It's easy.)
- Use Django Rest Framework's ViewSet generic classes to create a view for serving your data
- Wire up a new urlconf in your app's urls.py with the Django Rest Framework Router class

**_note:_** These instructions will be expanded as development progresses. Pager also aims to create helper classes that allow this to be done more simply.

## Contributing
It is very easy to contribute. You can fork this repo and send a pull request. Make sure to add your name to contributors.txt. Try to submit an issue to discuss your modifications before the pull request so we can see if they are inline with Pager's goals.

You can also open an issue for a feature request or architecture suggestion.

You can also check out the code for any _TODO_ comments.

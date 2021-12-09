
# Cookbook
## [Demo Here](https://milestonproject3.herokuapp.com/)
 In this application I use technologies learnt on my coding journey to demonstrate how a document-based database can be utilise efficiently and effectively. 

## UX
I wanted to create a seamless app for people to be able to easily store recipes.
The app is designed to allow for users to create, store and manage recipes. 

## Wireframes 
[Desktop View](https://github.com/waltercarreno/Mongodb3/tree/master/static/images)

## Technology Used
- [Python 3](https://www.python.org/download/releases/3.0/)
- [Flask 1.0.2](http://flask.pocoo.org/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CCS3/SCSS](https://sass-lang.com/)
- [Materialize](https://materializecss.com/)
- [JavaScript](https://www.javascript.com/)
- [jQuery](https://jquery.com/)
- [MongoDB](https://www.mongodb.com/)
- [Fontawesome](https://fontawesome.com/)



##### Why I built 'CookBook

The main reasoning behind the project was inspired by Code Institute as the brief was to create a cookbook type project. 
---


**Testing Flask Views** - In Flask each app's route uses a view template from my app structure these views were tested throughout every stage within my development process. Where needed I would test each view worked as expected when added new code or functionality to my app.

**Testing the database** - Getting my data collections right was the trickiest part of this project. As through developing my application my database schema was constantly changing to the requirements of my app. Where multiple changes had to be made to the database in order for all my app's functionality to work properly.

**Testing CRUD**



**EDITE**

Testing the edite recipes route was a case of trying the update.All method and applying this to a route that allowed the user to update the record based on some input by the user posting by the update recipe form. It can be access through profile.

**DELETE**
Delete functions requires that the user implement the username previous delete. It can be access through profile.

**CREATE**
I used flaskwtf forms to allow users to created forms and allow them to upload their recipies.


### HTML & CSS
All my HTML and CSS is valid, checked with the following validators

- [HTML Validator](https://validator.w3.org/)
-  [CSS Validator](https://jigsaw.w3.org/css-validator/)

## Deployment 
Getting my application ready for deployment consisted of the following: - 
1. Removing all my hard-coded environment variables to project my keys and secrets. These were placed in the heroku Config Vars for production.
2. Ensuring the applications requirements.txt is up-to-date with all the latest packages installed for my app being noted on this file. 
	**The command to update requirements**
		```
		pip3 freeze > requirements.txt
		```
3. Set up the Procfile - *A Procfile is required by Heroku in order to tell the service worker what command to run for my application to start.*
4. Set Flask's debugging to False.
5. Push all my latest production ready code to GitHub ready for deployment via Heroku's GitHub function where you can deploy from GitHub the production ready app.


**Upon successful deployment Heroku will give you the URL that is hosted your app**

*Upon unsuccessful deployment Heroku will log the cause of the error and this is view able in the 'view log' section on the Heroku website. Here you will find a detailed report of what has cause your application not to be deployed successfully. *


**Via GitHub** -  
1. You can manually download locally to your machine and then upload to your preferred IDE. 
2. Install the projects requirements.txt using `pip3 install -r requirements.txt`
3. You will need to update a few environment variables before we can run the app.
	1. app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
	2. app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
	3. app.secret_key = os.environ.get("SECRET_KEY")

4. Once the above steps are complete you can try run the application using `python3 main.py`


## Reference


- Youtuber **Pretty printed**
- Youtuber **Free Bootcamp**




# Cookbook
## [Demo Here](https://cookbook-recipe.herokuapp.com/)
 In this application I use technologies learnt on my coding journey to demonstrate how a document-based database can be utilise efficiently and effectively. 

---
## UX
I wanted to create a seamless app for people to be able to easily store recipes.
The app is designed to allow for users to create, store and manage recipes. 

---
## Wireframes 
[Desktop View](https://github.com/waltercarreno/Mongodb3/tree/master/static/images)


---

---


---
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

---

---

##### Why I built 'CookBook

The main reasoning behind the project was inspired by Code Institute as the brief was to create a cookbook type project. 
---
## Testing
Most of the applications testing was done throughout development, most of which was manual tests. I will outline most of what I did below for documentation purposes.



---

**Testing Flask Views** - In Flask each app's route uses a view template from my app structure these views were tested throughout every stage within my development process. Where needed I would test each view worked as expected when added new code or functionality to my app.


---

**Testing the database** - Getting my data collections right was the trickiest part of this project. As through developing my application my database schema was constantly changing to the requirements of my app. Where multiple changes had to be made to the database in order for all my app's functionality to work properly.

To achieve this I imported my data into my database via .JSON file and ensure all routes worked as expected.

---

**Testing CRUD**

**READ**
Firstly, before anything I wanted to make sure that I could display to my users the recipes I'd already collected and inserted into my db. To do this I had to create a home route and load the recipe collection within this route then pass the data to the view. As previously mentioned for the views I would constantly throughout the project development ensure there was no errors from Flask/Jinja before progressing with functionality of my app. 


**UPDATE**

Testing the update recipes route was a case of trying the update.all method and applying this to a route that allowed the user to update the record based on some input by the user posting by the update recipe form. Upon a successful edit I would check in the single recipe view and by printing the entire recipe to the terminal that all user edited fields have updated.

**DELETE**
Testing the delete function in my app was a case of creating the route and then testing that route within the browser, I would grab a recipe ID and then enter the URL needed for that route to perform. After deleting a record, I would flash a message for the user to be notified and also print a message to the terminal. To ensure the recipe was delete I would check in my view all recipes page along with checking the Atlas website. 

**CREATE**
To test my create functionality of my app I would continuously fill out a recipe form and test that the route when posting create a new recipe within my recipe collection and that all the fields I needed were created successfully.

Once my CRUD functionality was in place, I tested each form multiple times and tried to break each field or manipulate each form to perform unexpected. I have had my apps functionality tested multiple times by friends, family. Where bugs were identified I made a note and fixed each issue.



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
	1. `app.config["MONGO_DBNAME"] = "cookbook_creation"`
	2. `app.config["MONGO_URI"] = os.getenv("MONGO_URI", "monogodb://localhost")`
	3. `app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")`
4. Once the above steps are complete you can try run the application using `python3 main.py`


## Reference


- Youtuber **Pretty printed**
- Youtuber **Free Bootcamp**



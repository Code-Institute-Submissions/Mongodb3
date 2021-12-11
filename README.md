
# Cookbook
## [Demo Here](https://milestonproject3.herokuapp.com/)
 In this application I use technologies learnt on my coding journey to demonstrate how a document-based database can be utilise efficiently and effectively. 

  ## **1. Purpose of the project**
  I wanted to show what I have learned about flasks and python.

## **2. User stories**

### UX
I wanted to create a seamless app for people to be able to easily store recipes.
The app is designed to allow for users to create, store and manage recipes. 
As a user I will like to upload recipes and be able to see other recipes.
As a programmer I want to me able to manage my website.

## **3. Features**

I Have a navbar and and a footer that are present in all the pages.
The body changes depending of websites.
Login: have a login form that allow user to get into the website. Login has a username and a password.
Register: have a registration form that allow user to be register at the website. Register has a username and a password.
Profile: User can see all the recipes that he has created.
Allrecipes: Users can see all the recipes that are upload to the website. Allrecipes appear in card forms.
Editrecipe: Users can edit the recipes that they have created.
Editrecipe: Users can edit the recipes that they have created.

## ** 4. Future features**
Add a commet funcionality and enable users to give feedback to recipes.

## **5. Typography and color scheme**
### Fonts.
Fonts families:

 [Georgia](https://fonts.google.com/noto/specimen/Noto+Serif+Georgian?query=georgia) font.
 [TimesNewRoman](https://fonts.google.com/) font.
 [Serif](https://fonts.google.com/specimen/PT+Serif?query=serif) font.
 [Courier-new](https://docs.microsoft.com/en-us/typography/font-list/courier-new) font.
 [Indie-Flower](https://fonts.google.com/specimen/Indie+Flower) font.
 
### Colors.

body has a background color [#FFA07A](https://www.color-name.com/light-salmon.color) .
footer has a background color [#808080](https://www.canva.com/colors/color-meanings/gray/) .
button have [#00FF00](https://www.canva.com/colors/color-meanings/green/) and 
[#ff0000](https://www.canva.com/colors/color-meanings/red/).
Cards has a background color [#add8e6](https://www.canva.com/colors/color-meanings/light-blue/) and 
borders [#a52900](https://www.color-hex.com/color/a52900).


## 6. Wireframes 
[Desktop View](https://github.com/waltercarreno/Mongodb3/tree/master/static/images)

## 7. Technology Used
- [Python 3](https://www.python.org/download/releases/3.0/)
- [Flask 1.0.2](http://flask.pocoo.org/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CCS3/SCSS](https://sass-lang.com/)
- [Materialize](https://materializecss.com/)
- [JavaScript](https://www.javascript.com/)
- [jQuery](https://jquery.com/)
- [MongoDB](https://www.mongodb.com/)
- [Fontawesome](https://fontawesome.com/)



## **8. Testing**

I have test Flask and jinja to avoid problems rendering in the website.
I have test database and check that work properly with data introduced by users.

8.1 fixed bugs

**EDITE**
Users were able to edit recipes even if they were not the creators. Users were able to edit recipes that didn't exist. Users could edit
without begin loged. Fixed by adding validation in sessions and added exception.

**DELETE**
Users were able to create recipes even if they were not the creators. Users were able to create recipes that didn't exist. Users could deleted
without begin loged.

**CREATE**
Users could create without begin loged. Fixed by adding validation in sessions and added exception.

8.2 code validator

### HTML & CSS
All my HTML and CSS is valid, checked with the following validators

- [HTML Validator](https://validator.w3.org/)
-  [CSS Validator](https://jigsaw.w3.org/css-validator/)

## 9 Deployment 
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


## 10. Credits.

 I would like to thank each and every one who has helped or contributed to my project in any way. Please see list of names below:

- Mentor   **Rohit Sharma**
- Youtuber **Pretty printed**
- Youtuber **Free Bootcamp**
- Youtuber **Fazz**
- Youtuber **Victor Robles**


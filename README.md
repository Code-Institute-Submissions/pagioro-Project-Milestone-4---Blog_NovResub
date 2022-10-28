# **Lulu's Kitchen**
![Lulu's Kitchen](/static/css/images/project4blog.png)
# **Lulu's Kitchen**
A website made for you, with the best typical recipes from Brazil.
Our objective is to encourage and promote Brazilian gastronomy's
richness, complexity and cultural diversity.

[View the live project here](https://project4blog.herokuapp.com/ "Link to deployed site - Lulu's Kitchen")

admin
123321ep

## Contents
* **Introduction**
    * Planning Stage
    * Project Goals
    * User Stories
    * Design Goals
    * Design Choices
        * Font
        * Color Scheme
        * Logo Vegan-a-eat
        * Images
    * Wireframes

* **Features**
    * Design Features
    * Existing Features
    * Future Features

* **Testing**

* **Bugs**

* **Technology Used**
    * Libraries used
    

* **Deployment** 

* **Credits** 

## **Introduction**

**Planning Stage**

I started the project thinking about what functionality it should have, first creating the wireframe. After that, I worked on the database and on the HTML and CSS codes to be able to visualize my creation and only then start adding the codes.

**Project Goals**

It was the creation of a responsive recipe blog that works on any mobile device and is more focused on Brazilian food, but that doesn't prevent anyone from adding their recipes, regardless of where they are.
The blog is interactive; you can share and comment on recipes already posted.

**Site Owner Goals**

* Provide an interactive and easy-to-use website.
* Connecting people who enjoy good food.

**User Goals**

* Ability to share their own favorite recipes.
* Create user account to interact.

**User Stories**



* Access blog with admin privilege: As a site administrator user I can access the blog's URL so that I can get access to the posts and admin profile.

* Access blog: As a site user I can access the blog's URL so that I can have access to the posts.

* Manage data structure: As a site administrator user I can create, view, update and delete data so that it can be displayed on the blog (title, title summary, content, photo, author, comments, likes and post date).

* Manage Drafts: As a site administrator user I can create, view, update and delete draft posts so that I can approve their content later.

* Approve posts: As a site administrator user I can approve post drafts so that the user can view the post 

* Manage posts: As a site administrator user I can create, view, update and delete approved posts so that I can manage blog content.

* View post list: As a site user I can view the list of posts so that I can select the chosen one.

* Open a post: As a site user I can select a post so that I can read the full content.

* Create user account: As a site user I can create an account so that I can comment and like posts.

* Comment on a post: As a site user I can write comments on a post so that I can join the conversation.

* Approve comments: As a site administrator user I can approve or disapprove comments so that I can filter out objectionable or inappropriate comments to the subject.

* View comments: As a site user I can view comments on a post so that I can read the conversation
Like/Dislike 

* posts: As a site user I can like or not like a post so that I can give an opinion.

* View post likes: As a site administrator user I can view the number of likes on each post so that I can understand which is the most popular or viral.

**Design Goals**

* A site that works on all devices. 
* Easy to understand and use.
* Clean and sophisticated design.

**Design Choices**

* Font

The font used was comforta due to its modern style and easy readability.

![Fonts](/static/css/images/Comfortaa.png)

* Color Scheme

On the site, I chose to use softer colours so that the attention wouldn't diverted from the recipes that are the focus, also used a darker green in the main bars so that the person can quickly view the registration and social networks both at the top of the page and at the footer.

- White: #F9F9F9 - Background
- Dark green: #95b5ac - top bar with sign up / login and social footer bar
- light gray - #ced4da - Subscribe and contact bar


* Logo Lulu's Kitchen

I used Photoshop to create my logo and decided on a text and a food image on the left. 

![Logo](/static/css/images/logo.png)

**Wireframes**

I used Balsamic wireframe to define the site's basic structure and visualize the project and plan.

![Home](/static/css/images/Home.png)

![About](/static/css/images/About.png)

![Add Recipe](/static/css/images/add%20recipe.png)

![Post Detail Login](/static/css/images/Post%20Detail%20Login.png)

![Post Detail Logout](/static/css/images/Post%20Detail%20Logout.png)

![Sign In](/static/css/images/Sign%20In.png)

[Back to content](#contents)

## **Data Base Model**

![Entity Relationship Diagram](/static/css/images/data-base-model.png)

## **Features**

### Design Features

* Header

The header consists of a sign-up and login bar in the upper left and social media in the upper right corner. The logo is also centred and stands out due to its size. The navigation menu is simple, easy to use, centralized, and can be seen on all pages.
In responsive mode, the navigation turns into a hamburger button, and the site's logo goes to the top left corner.

* Home Page

When visiting the site, you are already received with the recipes registered with the user registration button and in the menu below the button that will take you to the page to add new recipes.

* Footer

The footer is simple in muted colour tones, and consists of a subscribe bar, copyright information, and social media links.

### Existing Features

* **Header Logo** appears on every page for consistency and easy navigation, clicking the logo takes you back to the home page.
* **Header Nav-Bar** appears on every page for consistency and easy navigation, and the Nav-Bar toggles on smaller screens for a better user experience. The Nav-Bar presents different links if the user is logged in or not.
* **Home Page Image** is to greet the site user and instantly provide what the site is.
* **Recipe Cards** are displayed on the homepage six per page; if there are more than six recipes on the site, they will be displayed on another page. The arrows at the end will show the user the navigation to the following recipes. Cards contain author information, title, creation, short description, number of likes and an image. A default recipe image will appear if the user does not choose a specific image.
* **Recipe Form** can be used by logged-in users. Here, users with an account can add their recipes and edit their own recipes.
* **Comment form** 
is displayed below each recipe when viewed. Logged-in users can comment on recipes and also delete their comments.
* **Comments section** is where all users, logged in or not can read all comments, who wrote them and when. 
* **Like/Unlike button** appears on the recipe website, and all logged-in users can like/unlike the recipes.
* **About the page** provides the user with information about the site and its creator.
* **Recipe page** is displayed when clicking on a recipe. All users, logged in or not, can view the recipe details here. This page also includes features to like and comment on if you are a logged-in user. If you are the author of the recipe, from here, you may be redirected to edit/delete your recipe.
* **Edit/Delete Recipe** is where the recipe author can edit and/or delete their recipes.
* **Login page** here users who have already created an account can log in.
* **Registration page** is where new users can create a new account to interact with the site.
* **Logout** is a page for the user to confirm their desire to log out of their account.

**Future Features**

* **Welcome page**

A welcome page has not been added, which will be made shortly.

* **Print Recipes**

I would add a print button and by clicking open a pdf file with the recipe information to be printed.

* **Comments counter**

I will add a comment counter in the future.

* **Search Recipes**

I would add an exciting feature to search for recipes on the site.

* **Categorize**

Add a category for each type of recipe.

* **Subscribe**

I added the button but not the function where the user would put his email to receive news, this site but still without functionality.

* **Contact Form**

The contact form has been added, but it still doesn't work. I will make it work soon.

[Back to content](#contents)


## **Testing**

## Manual Testing

### Navigation Bar

* Expected Result: The navigation bar should be visible on all site pages. The navigation bar should toggle if the page is rendered on smaller screens for a better user experience.
* Test: I visited all pages on the site in all resolutions to check if the navigation bar was visible.
* Result: The navigation bar is visible on all site pages in any resolution.
* Verdict: The code works perfectly.

### Logo

* Expected Result: When clicking on the logo and changing the screen resolution, the user should be redirected to the homepage, and the logo should change size.
* Test: I clicked on the logo on every page and reduced and increased the resolution.
* Result: each time I clicked on the logo, I was redirected to the homepage and zoomed in and out in different resolutions.
* Verdict: The code works perfectly.

### Links

* Expected Result: When clicking on the links, the user must be redirected to its respective page.
* Test: I clicked on all links on all pages to verify their operation.
* Result: I was redirected to the correct page every time I clicked on the links.
* Verdict: The code works perfectly.

### Footer

* Expected Result: The footer must be visible on all site pages and always be placed at the bottom of the page.
* Test: I visited every page on the site to check if the footer was visible.
* Result: The footer is visible on all pages of the site.
* Verdict: The code works perfectly.

### Recipe overview

* Expected Result: A list of recipes should be displayed upon entering the site. The list should present a preview of each recipe with some basic information.
* Test: I entered the site to check if the recipes were displayed.
* Result: A list of recipes is displayed upon entering the site. Each recipe card previews an image, author, title, snippet, creation date, and a number of likes.
* Verdict: The code works perfectly.

### Pagination

* Expected result: The site must have a maximum of 6 recipes displayed at once. When there are six recipes on the page, it should be paginated, and the user should be able to click to go to the next page.
* Test: I checked that pagination was enabled if there were more than six recipes on the site by adding a larger number of recipes.
* Result: The seventh recipe that was added to the site was displayed on a second page.
* Verdict: The code works perfectly.

### Recipe detail

* Expected result: When a specific recipe is clicked, the recipe should open on a page another page with more detailed information about the recipe.
* Test: I clicked on a recipe to see if it opened and revealed all the information on the other page.
* Result: When a recipe is clicked, it opens and reveals information.
* Verdict: The code now works perfectly.

### Likes

* Expected Result: When viewing a recipe, the total number of likes should be displayed, and if the user is logged in, the ability to like/unlike should be available.
* Test: I opened a recipe to see if the likes were visible and ensured the icon was clickable.
* Result: The number of likes is displayed, and if the user is logged in, the icon is clickable.
* Verdict: The code works perfectly.

### Views comments

* Expected Result: When viewing a recipe in its entirety, all comments should be displayed, showing the oldest first.
* Test: I opened a recipe to see if comments are available to all users and if the oldest is displayed first.
* Result: Comments are displayed for all users, logged in or not. The oldest comment is displayed first.
* Verdict: The code works perfectly.

### Delete comment

* Expected Result: A logged-in user should be able to delete their comments quickly.
* Test: Log in to see if I can only delete my comments.
* Result: When logged in, all comments are displayed, and the ones I created are presented with a "Delete comment" button below. When clicked, the comment disappears.
* Verdict: The code works perfectly.

### Create comments

* Expected result: When viewing a recipe, a logged-in user should be presented with the option to leave a comment.
* Test: If the user is not logged in, he will not be able to comment on the recipe.
* Result: When viewing a recipe in its entirety as a logged in user, the option to leave a comment is presented. When a comment is entered, the user will wait for the site administrator to approve their comment.
* Verdict: The code works perfectly.

### Manage Recipe

* Expected Result: When a logged-in user is viewing their recipes, an option to Edit or Delete the recipe should be presented. If the site user is not the recipe's author, this option should not exist.
* Test: View a recipe I authored, view another user's recipe, and view a recipe as a non-logged-in user.
* Result: When viewing my recipe, an option to Edit or Delete the recipe is presented clearly. When viewing a recipe that I am not a user of or am not logged in to, there is no option to manage the recipe.
* Verdict: The code works perfectly.

### Edit recipe

* Expected Result: When creating your recipes, you should have the option to Edit. When the Edit button is clicked, an Edit Recipe view opens for editing.
* Test: View my recipe and be able to edit it.
* Result: The Edit Recipe view opens when the button is clicked, and all the features of the recipe can be edited.
* Verdict: The code works perfectly.

### Delete recipe

* Expected Result: When viewing your recipes, you will have the option to delete them
* Test: I can see my recipes, and the delete button
* Result: The Delete Recipe page opens when the button is clicked, and the user is presented with the option to return to the feed or, if they are sure, confirm they want to delete their recipe.
* Verdict: The code works perfectly.

### Add recipe

* Expected Result: A logged-in user should be able to add recipes to the site. All fields except the snippet must be completed.
* Test: As logged in user adds a new recipe, trying to leave the fields blank and filling all.
* Result: By leaving one or more mandatory fields blank, the user is encouraged to complete the form.
* Verdict: The code works perfectly.

### Placeholder image

* Expected Result: If the user does not choose to upload an image for their recipe, it should display a placeholder image.
* Test: Add recipe without image.
* Result: The placeholder image will be displayed when adding a recipe but not uploading an image.
* Verdict: The code works perfectly.

### Register new account

* Expected Result: As a user of the site, you must be able to create an account to interact with the site. The username must be unique, and entering an email address is optional.
* Test: I created a new account with a unique username, a new account with an existing username, and a new account with and without an email address.
* Result: If the new account has a unique username, it will create the account regardless of whether an email address is entered or not. When trying to create a new account with an existing username, the user is encouraged to choose a unique username as it already exists. When the account is registered, the user is logged in and is notified by an alert.
* Verdict: The code works perfectly.

### Log in

* Expected Result: As a registered user of the site, you must be able to log into your account to interact.
* Test: I verified the Login functionality as a registered user.
* Result: Upon entering valid login credentials, the user is logged in and redirected to the home page, and an alert notifies the user that he is logged in.
* Verdict: The code works perfectly.

### Logout

* Expected Result: As a registered and logged-in user, you should be able to log out of the site.
* Test: I checked the Logout functionality as a logged-in user.
* Result: When clicking Logout, the user is redirected to the Logout page and asked to confirm that he wants to log out.
* Verdict: The code works perfectly.

[Back to content](#contents)

## Automated Testing

### Code Validation

* HTML Validation - No errors just warning

* CCS Validation - I found an error in the CSS that I couldn't solve.

![CSS Error](/static/css/images/css%20error.png)

* Python Validation - Pep8 online is not working

### Browser Validation

The site has been tested using the following browsers:

* Chrome
* Firefox
* Edge
* Safari

[Back to content](#contents)

## **Bugs**

* **Bug** - *id_recipe = models.AutoField(primary_key=True)*

    Previously, the field type was an integer, and the user would have to know the last recorded recipe.

    **Solution:** - I was to put the field type AutoField, so the database automatically increments the id recipe, never repeating.

* **Bug** - *path('edit_recipe/<slug:slug>', views.RecipeEditView.as_view(), name='edit_recipe')*

    Edit recipe URL was not showing.

    **Solution:** - The solution was to put as_view in views.RecipeEditView.

* **Bug** - *PostDetail(View) in views.py with wrong syntax.*

    Previously, post and recipe.slug was used in views.py so that the recipe information was displayed "slug": post or "slug": recipe.slug

        return render(
                request,
                'post_detail.html',
                {
                    "post": post,
                    "slug": post.slug,
                    "comments": comments,
                    "commented": False,
                    "liked": liked,
                    "comment_form": CommentForm()
                },
            )

    **Solution:** - I changed it to post.slug is fixing the issue

* **Bug** - *class RecipeEditView(UpdateView)*

    In the RecipeEditView(UpdateView) class: in views.py, the update was not working because the return render was being used.

    **Solution:** - It was necessary to create the function below.

        def get_context_data(self, *args, **kwargs):
            context = super(RecipeEditView, self).get_context_data(*args, **kwargs)
            post = self.get_object()
            context['post'] = post
            return context

* **Bug** - *Summernote not responsive*

    Summernote was not responsive on smaller screens, and after several failed attempts trying to change it with CSS, I came up with a solution.

    **Solution:** - I found the solution on slack by adding the code below in settings.py

        SUMMERNOTE_CONFIG = {
        'width': '100%',
        'height': '480',
        }

[Back to content](#contents)

## **Technology Used**

### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5 "Link to HTML Wiki")
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets "Link to CSS Wiki")

### Additional Languages Used
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript "Link to JavaScript Wiki")
     - Used to implement the Summernote feature that allowed the user to add styling to the recipe in the form.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language) "Link to Python Wiki")
     - Used to implement Django functionality, including building models, forms and views for the app.

### Frameworks, Libraries & Programs Used
- [Django](https://www.djangoproject.com/ "Link to Django Project website")
    - Django was used to build the models, forms and views of the app, and was the backbone of this project.
- [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/ "Link to Bootstrap page")
     - Bootstrap was used to implement the responsiveness of the site.
- [Cloudinary](https://cloudinary.com/ "Link to Cloudinary page")
     - Cloudinary was used as free cloud storage for images uploaded to the site through the recipe forms.
- [Summernote](https://summernote.org "Link to Summernote page")
     - Summernote was used to allow users to add styling when adding a recipe to the site.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/ "Link to the Crispy Forms documentation")
    - Crispy Forms was used to style the add and edit recipe forms.
- [Google Fonts](https://fonts.google.com/ "Link to Google Fonts")
    - Google fonts were used to import the fonts "Playfair Display" and "Lato" into the style.css file. These fonts were used throughout the project.
- [Font Awesome](https://fontawesome.com/ "Link to FontAwesome")
     - Font Awesome was used on all pages throughout the website to import icons (e.g. social media icons) for UX purposes.
- [Git](https://git-scm.com/ "Link to Git homepage")
     - Git was used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitHub](https://github.com/ "Link to GitHub")
     - GitHub was used to store the project.
- [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage")
     - Am I Responsive was used to see responsive design throughout the process and to generate mockup image.
- [Balsamiq Wireframes](https://balsamiq.com/learn/articles/what-are-wireframes/ "Link to Balsamiq Wireframes")
     - Balsamiq was used to create the wireframes for the project.  

[Back to content](#contents)

## **Deployment**

This project was developed using a [GitPod](https://gitpod.io/ "Link to GitPod") workspace. The code was commited to [Git](https://git-scm.com/ "Link to Git") and pushed to [GitHub](https://github.com/ "Link to GitHub") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    - In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    - In your GitPod workspace, create an env.py file in the main directory. 
    - Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    - Add the SECRET_KEY value to the Config Vars in Heroku.
    - Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    - Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    - In settings.py add the following sections:
        - Cloudinary to the INSTALLED_APPS list
        - STATICFILE_STORAGE
        - STATICFILES_DIRS
        - STATIC_ROOT
        - MEDIA_URL
        - DEFAULT_FILE_STORAGE
        - TEMPLATES_DIR
        - Update DIRS in TEMPLATES with TEMPLATES_DIR
        - Update ALLOWED_HOSTS with ['project4blog.herokuapp.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, static and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project4blog.wsgi
    - Log in to Heroku using the terminal heroku login -i.
    - Then run the following command: **heroku git:remote -a Project-Milestone-4---Blog**. This will link the app to the Gitpod terminal.
    - After linking your app to your workspace, you can then deploy new versions of the app by running the command **git push heroku main** and your app will be deployed to Heroku.

## **Credits**

### Media

* Food images were used from the website [tudo gostoso website](https://www.tudogostoso.com.br). About image is from [Pexels Photo by Hannah Nelson](https://www.pexels.com/photo/close-up-photography-of-a-woman-near-wall-1065084/).

### Code

References used:


* [CSS](https://css-tricks.com/)
* [Bootstrap](https://getbootstrap.com/)
* [Django Docs](https://docs.djangoproject.com/en/4.0/)
* [Stack Overflow](https://stackoverflow.com/)
* [W3 Schools](https://www.w3schools.com/)

### Acknowledgements

* I want to thank my wife and friends for inspiring me in my project.

* Thanks to the entire team of tutors who helped me on this journey, the people at slack who helped with some problems I had, and my mentor who gave me direction.

[Back to content](#contents)




















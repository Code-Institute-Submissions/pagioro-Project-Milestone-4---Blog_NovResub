# **Lulu's Kitchen**
![Lulu's Kitchen](/static/css/images/project4blog.png)
# **Lulu's Kitchen**
A website made for you, with the best typical recipes from Brazil.
Our objective is to encourage and promote Brazilian gastronomy's
richness, complexity and cultural diversity.

[View the live project here](https://project4blog.herokuapp.com/ "Link to deployed site - Lulu's Kitchen")

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

![Add Recipe](/static/css/images/)

![Post Detail Login](/static/css/images/Post%20Detail%20Login.png)

![Post Detail Logout](/static/css/images/Post%20Detail%20Logout.png)

![Sign In](/static/css/images/Sign%20In.png)

[Back to content](#contents)

## **Data Base Model**

![Entity Relationship Diagram](/static/css/images/data-base-model.png)

* Site Map

![Site Map](/static/)

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


















from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
# from django.core.validators import MaxValueValidator, MinValueValidator

STATUS_RECIPE = ((0, 'Draft'), (1, 'Published')) 


class Recipe(models.Model):
    """
    Model for recipe
    """

    id_recipe = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=200, unique=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    slug = models.SlugField(max_length=200, unique=True)    
    excerpt = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)   
    updated_date = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    prep_time = models.CharField(max_length=20)
    cook_time = models.CharField(max_length=20)
    serves = models.CharField(max_length=20)
    calories = models.IntegerField()
    ingredients = models.TextField()
    description = models.TextField()
    method = models.TextField()
    status_recipe = models.IntegerField(choices=STATUS_RECIPE, default=0)
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)


    class Meta:
        """
        Order the recipes in descending order
        """
        ordering = ['-created_date']

    def __str__(self):
        """
        Returns a string representation of an object
        """
        return self.title

    def number_of_likes(self):
        """
        Returns the number of likes on a post
        """
        return self.likes.count()


    def save(self, *args, **kwargs): 
     if not self.slug: 
           self.slug = slugify(self.title) 
     return super().save(*args, **kwargs)    


class Comment(models.Model):
    """
    Model for comment
    """
    id_comment = models.AutoField(primary_key=True)
    id_recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField() 
    approved = models.BooleanField(default=False)


class Meta:
    """
    Orders the comments in ascending order
    """
    ordering = ['-created_date']

    def __str__(self):
        return f"Comment {self.content} by {self.name}"



class Contact(models.Model):
    """
    Model for contact
    """
    email = models.EmailField() 
    registration_date = models.DateTimeField(auto_now_add=True)


class Meta:
    """
    Orders the contacts in ascending order
    """
    ordering = ['-registration_date']


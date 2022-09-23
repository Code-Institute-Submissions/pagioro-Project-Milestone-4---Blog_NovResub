from .models import Comment, Recipe
from django_summernote.widgets import SummernoteInplaceWidget
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class RecipeForm(forms.ModelForm):
    """
    Form to add recipe
    """
    class Meta:
        model = Recipe
        fields = [
            'title',
            'excerpt',            
            'prep_time',
            'cook_time',   
            'serves',
            'calories', 
            'ingredients',
            'description', 
            'method',
            'image',
        ]

        widgets = {
            'ingredients': SummernoteInplaceWidget(),
            'description': SummernoteInplaceWidget(),
            'method': SummernoteInplaceWidget()
        }


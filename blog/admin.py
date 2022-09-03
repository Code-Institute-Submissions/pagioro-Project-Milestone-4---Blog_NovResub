from django.contrib import admin
from .models import Recipe, Comment, Contact
from django_summernote.admin  import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status_recipe', 'created_date')
    list_display = ('title', 'slug', 'status_recipe', 'created_date') 
    search_fields = ['title', 'description']
    summernote_fields = ('ingredients','description','method')
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'content', 'id_recipe', 'created_date', 'approved')  
    list_filter = ('approved', 'created_date')    
    search_fields = ['name', 'email', 'content']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


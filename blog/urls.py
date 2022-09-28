from . import views
from django.urls import path
from .views import RecipeEditView, RecipeDeleteView


urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='recipe_likes'),
    path('addrecipe', views.add_recipe, name='add_recipe'),
    path('edit_recipe/<slug:slug>', views.RecipeEditView.as_view(), name='edit_recipe'),
    path('delete_comment/<int:pk>', views.RecipeDeleteComment.as_view(), name='delete_comment'),
    path('delete_recipe/<slug:slug>', views.RecipeDeleteView.as_view(), name='delete_recipe'),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]

from . import views
from django.urls import path

urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
    path('like/<slug:slug>', views.PostLike.as_view(), name='recipe_likes'),
    # path("<slug:slug>/", views.add_recipe, name='add_recipe/'),
    path('addrecipe', views.add_recipe, name='add_recipe'),
]

# Example to follow

# from django.urls import path
# from . import views
# from .views import RecipeDeleteView, RecipeEditView


# urlpatterns = [
#     path('', views.RecipeList.as_view(), name='home'),
#     path('about/', views.about, name='about'),
#     path('login/', views.login_page, name='login'),
#     path('logout/', views.logout_user, name='logout'),
#     path('signup/', views.signup_page, name='signup'),
#     path('addrecipe/', views.add_recipe, name='addrecipe'),
#     path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
#     path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
#     path('recipe_edit/<slug:slug>', views.RecipeEditView.as_view(),
#          name='recipe_edit'),
#     path('recipe_delete/<slug:slug>', views.RecipeDeleteView.as_view(),
#          name='recipe_delete'),
#     path('delete_comment/<int:pk>', views.RecipeDeleteComment.as_view(),
#          name='delete_comment'),
# ]
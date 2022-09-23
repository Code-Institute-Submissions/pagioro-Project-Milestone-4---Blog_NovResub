from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
from .forms import CommentForm

#@login_required
def add_recipe(request):

    recipe_form = RecipeForm()
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        if recipe_form.is_valid():
            recipe_form = recipe_form.save(commit=False)
            recipe_form.title = recipe_form.title.title()
            recipe_form.author = request.id_user
            recipe_form.status_recipe = 1
            recipe_form.save()
            return redirect('home')

    return render(request, 'add_recipe.html', context={'recipe_form':
                  recipe_form})

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status_recipe=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 6
    print(queryset)

class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status_recipe=1)
        # recipe = get_object_or_404(Recipe, slug=slug)  
        post = get_object_or_404(queryset, slug=slug)         
        comments = post.comments.filter(approved=True).order_by('-created_date') #voltar se estiver errado
        liked = False
        if post.likes.filter(id=self.request.user.id).exists(): #erro 
            # User, related_name='recipe_l
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status_recipe=1)
        recipe = get_object_or_404(Recipe, slug=slug)  
        post = get_object_or_404(queryset, slug=slug)               
        comments = post.comments.filter(approved=True).order_by('-created_date') #voltar se estiver errado
        liked = False
        if post.likes.filter(id=self.request.user.id).exists(): #erro 
            # User, related_name='recipe_l
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username  
            comment = comment_form.save(commit=False)
            comment.id_recipe = recipe
            comment.save()      
        else:        
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

class PostLike(View):
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
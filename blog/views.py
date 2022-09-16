from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status_recipe=1).order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 6
    print(queryset)

class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status_recipe=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = Comment.filter(approved=True).order_by('-created_date') #voltar se estiver errado
        liked = False
        if Recipe.likes.filter(id=self.request.user.id).exists(): #verificar
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )







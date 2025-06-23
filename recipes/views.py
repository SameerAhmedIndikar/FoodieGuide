from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Recipe, Comment, Rating
from .forms import RecipeForm, CommentForm, RatingForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

def home(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.all().order_by('-created_at')[:6]  # Latest 6 recipes
    return render(request, 'recipes/home.html', {'categories': categories, 'recipes': recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    comments = recipe.comment_set.all()
    ratings = recipe.rating_set.all()
    avg_rating = ratings.aggregate(Avg('stars'))['stars__avg'] or 0  # Fixed syntax
    comment_form = CommentForm()
    rating_form = RatingForm()

    if request.method == 'POST':
        if 'comment' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid() and request.user.is_authenticated:
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.recipe = recipe
                comment.save()
                return redirect('recipe_detail', pk=pk)
        elif 'rating' in request.POST:
            rating_form = RatingForm(request.POST)
            if rating_form.is_valid() and request.user.is_authenticated:
                rating, created = Rating.objects.get_or_create(
                    user=request.user, recipe=recipe, defaults={'stars': rating_form.cleaned_data['stars']}
                )
                if not created:
                    rating.stars = rating_form.cleaned_data['stars']
                    rating.save()
                return redirect('recipe_detail', pk=pk)

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'comments': comments,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'avg_rating': avg_rating,
    })

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

def search_recipes(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    recipes = Recipe.objects.all()

    if query:
        recipes = recipes.filter(title__icontains=query)
    if category_id:
        recipes = recipes.filter(category_id=category_id)

    categories = Category.objects.all()
    return render(request, 'recipes/search.html', {
        'recipes': recipes,
        'categories': categories,
        'query': query,
    })
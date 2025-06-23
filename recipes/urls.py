from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.add_recipe, name='add_recipe'),
    path('search/', views.search_recipes, name='search_recipes'),
    # Removed: path('accounts/signup/', SignUpView.as_view(), name='signup'),
]
from django import forms
from .models import Recipe, Comment, Rating, RecipeIngredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'category', 'image', 'instructions', 'cooking_time']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars']
from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']  # Изменяемые
        exclude = ['author']  # Игнорировать поле при создании формы, но автоматически устанавливаться в представлениях.


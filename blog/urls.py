from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<category>/', views.category, name='category'),
]
"""
URL patterns for the 'blog' app.

This module defines URL patterns for the views in the 'blog' app.

URL Patterns:
- '': index - The main index page.
- '<int:pk>/': detail - The detail page for a specific post.
- '<category>/': category - The category page for posts within a specific category.
"""

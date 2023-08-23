from django.urls import path, include
from tastypie.api import Api

from api.models import PostResource, CategoryResource, CommentResource

api = Api(api_name='v1')
api.register(PostResource())
api.register(CategoryResource())
api.register(CommentResource())

urlpatterns = [
    path('', include(api.urls), name='index'),
]
"""
URL patterns for the API endpoints.

This module defines URL patterns for the API endpoints using Tastypie resources. It creates
a Tastypie API instance, registers resource classes, and includes the API's URLs in the main
urlpatterns.

URL Patterns:
- '': API endpoints provided by Tastypie resources.
"""

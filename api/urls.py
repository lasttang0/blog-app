
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
from django.contrib import admin
from django.urls import path, include
from tastypie.api import Api

from api.models import PostResource, CategoryResource, CommentResource

api = Api(api_name='v1')

post_resource = PostResource()
category_resource = CategoryResource()
comment_resource = CommentResource()

api.register(post_resource)
api.register(category_resource)
api.register(comment_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/', include(api.urls)),
]

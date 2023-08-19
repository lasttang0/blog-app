from django.contrib import admin
from django.urls import path, include

from api.models import PostResource, CategoryResource

post_resource = PostResource()
category_resource = CategoryResource()

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', include('blog.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

    path('api/', include(post_resource.urls)),
    path('api/', include(category_resource.urls)),

]

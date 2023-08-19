from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from blog.models import Category, Post, Comment
from .authentication import CustomAuthentication


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        allowed_methods = ['get']


class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comments'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        bundle.obj.post_id = bundle.data['post_id']

    def dehydrate(self, bundle):
        bundle.data['post_id'] = bundle.obj.post
        return bundle

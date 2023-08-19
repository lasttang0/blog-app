from tastypie.resources import ModelResource

from blog.models import Category, Post, Comment


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CommentResource(ModelResource):
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comments'
        allowed_methods = ['get']


class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        allowed_methods = ['get', 'post', 'delete']

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization

from blog.models import Category, Post, Comment
from .authentication import CustomAuthentication


class CategoryResource(ModelResource):
    """
    Resource for Category model.

    This class defines a Tastypie resource for the Category model. It specifies the allowed
    methods and the name of the resource.

    Attributes:
    - Meta: A nested class containing metadata for the resource.
    """

    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class PostResource(ModelResource):
    """
    Resource for Post model.

    This class defines a Tastypie resource for the Post model. It specifies the allowed
    methods and the name of the resource.

    Attributes:
    - Meta: A nested class containing metadata for the resource.
    """

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'posts'
        allowed_methods = ['get']


class CommentResource(ModelResource):
    """
    Resource for Comment model.

    This class defines a Tastypie resource for the Comment model. It specifies the allowed
    methods, the name of the resource, and applies custom authentication and authorization.

    Attributes:
    - Meta: A nested class containing metadata for the resource.
    - authentication: Custom authentication class for the resource.
    - authorization: Authorization class for the resource.
    """

    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comments'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):
        """
        Hydrate method for Comment resource.

        This method modifies the Comment object during hydration by setting its post_id
        attribute based on data from the bundle.

        Parameters:
        - bundle: Tastypie bundle containing data.

        Returns:
        - None.
        """
        bundle.obj.post_id = bundle.data['post_id']

    def dehydrate(self, bundle):
        """
        Dehydrate method for Comment resource.

        This method modifies the bundle data during dehydration by adding the 'post_id' field.

        Parameters:
        - bundle: Tastypie bundle containing data.

        Returns:
        - Modified Tastypie bundle.
        """
        bundle.data['post_id'] = bundle.obj.post
        return bundle

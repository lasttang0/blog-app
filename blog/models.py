from django.db import models


class Category(models.Model):
    """
    Model representing a category for posts.

    This model defines a category's name and creation timestamp.

    Fields:
    - name: CharField representing the category's name.
    - created_on: DateTimeField representing the creation timestamp.

    Methods:
    - __str__: Returns the category's name as the string representation.
    """

    name = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns the string representation of the category.
        """
        return self.name


class Post(models.Model):
    """
    Model representing a blog post.

    This model defines a post's title, body, creation timestamp, modification timestamp,
    and its associated categories.

    Fields:
    - title: CharField representing the post's title.
    - body: TextField representing the post's content.
    - created_on: DateTimeField representing the creation timestamp.
    - last_modified: DateTimeField representing the last modification timestamp.
    - categories: ManyToManyField relating the post to categories.

    Methods:
    - __str__: Returns the post's title as the string representation.
    """

    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        """
        Returns the string representation of the post.
        """
        return self.title


class Comment(models.Model):
    """
    Model representing a comment on a post.

    This model defines a comment's author, body, creation timestamp, and its associated post.

    Fields:
    - author: CharField representing the comment author's name.
    - body: TextField representing the comment content.
    - created_on: DateTimeField representing the creation timestamp.
    - post: ForeignKey relating the comment to a post.

    Methods:
    - __str__: Returns the string representation of the comment.
    """

    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns the string representation of the comment.
        """
        return f'{self.author} {self.created_on}'

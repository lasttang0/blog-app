from django.contrib import admin
from .models import Post, Category

# Customize the admin site header, title, and index title
admin.site.site_header = 'Blog Admin'
admin.site.site_title = 'Blog App'
admin.site.index_title = 'Welcome to the Blog admin area'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin class for managing blog posts.

    This class provides customization options for displaying and managing blog posts
    in the Django admin interface.

    Attributes:
    - list_display: Fields to display in the list view of posts.
    - search_fields: Fields that can be searched in the admin interface.
    """
    list_display = ('title', 'created_on', 'last_modified')
    search_fields = ('title', 'body')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin class for managing post categories.

    This class provides customization options for displaying and managing post categories
    in the Django admin interface.

    Attributes:
    - list_display: Fields to display in the list view of categories.
    """
    list_display = ('name', 'created_on')

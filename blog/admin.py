from django.contrib import admin
from .models import Post, Category

admin.site.site_header = 'Blog Admin'
admin.site.site_title = 'Blog App'
admin.site.index_title = 'Welcome to the Blog admin area'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on', 'last_modified')
    search_fields = ('title', 'body')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_on')

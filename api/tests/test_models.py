from django.test import TestCase
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.bundle import Bundle

from api.authentication import CustomAuthentication
from blog.models import Category, Post, Comment
from api.models import CategoryResource, PostResource, CommentResource


class CategoryResourceTest(TestCase):
    def test_meta_settings(self):
        """
        Test whether the 'CategoryResource' meta settings are correctly defined.
        """
        resource = CategoryResource()
        meta = resource._meta
        self.assertEqual(meta.queryset.model, Category)
        self.assertEqual(meta.resource_name, 'categories')
        self.assertEqual(meta.allowed_methods, ['get'])


class PostResourceTest(TestCase):
    def test_meta_settings(self):
        """
        Test whether the 'PostResource' meta settings are correctly defined.
        """
        resource = PostResource()
        meta = resource._meta
        self.assertEqual(meta.queryset.model, Post)
        self.assertEqual(meta.resource_name, 'posts')
        self.assertEqual(meta.allowed_methods, ['get'])


class CommentResourceTest(TestCase):
    def test_meta_settings(self):
        """
        Test whether the 'CommentResource' meta settings are correctly defined.
        """
        resource = CommentResource()
        meta = resource._meta
        self.assertEqual(meta.queryset.model, Comment)
        self.assertEqual(meta.resource_name, 'comments')
        self.assertEqual(meta.allowed_methods, ['get', 'post', 'delete'])
        self.assertIsInstance(meta.authentication, CustomAuthentication)
        self.assertIsInstance(meta.authorization, Authorization)

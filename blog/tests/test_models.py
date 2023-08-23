from django.test import TestCase
from blog.models import Category, Post, Comment

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='TestCategory')

    def test_name_label(self):
        """
        Test whether the 'name' field label is correctly set.
        """
        category = Category.objects.get(id=1)
        field_label = category._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_name_max_length(self):
        """
        Test whether the maximum length of the 'name' field is correctly set.
        """
        category = Category.objects.get(id=1)
        max_length = category._meta.get_field('name').max_length
        self.assertEqual(max_length, 20)

    def test_created_on_auto_add(self):
        """
        Test whether the 'created_on' field is automatically populated.
        """
        category = Category.objects.get(id=1)
        self.assertIsNotNone(category.created_on)

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='TestCategory')
        category = Category.objects.get(id=1)
        post = Post.objects.create(title='TestTitle', body='TestBody')
        post.categories.add(category)  # Используем метод add() для добавления связи

    def test_title_label(self):
        """
        Test whether the 'title' field label is correctly set.
        """
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_title_max_length(self):
        """
        Test whether the maximum length of the 'title' field is correctly set.
        """
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_categories_relation(self):
        """
        Test whether the relation between 'Post' and 'Category' models is correctly established.
        """
        post = Post.objects.get(id=1)
        category = Category.objects.get(id=1)
        self.assertIn(category, post.categories.all())

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='TestCategory')
        category = Category.objects.get(id=1)
        post = Post.objects.create(title='TestTitle', body='TestBody')
        post.categories.add(category)  # Используем метод add() для добавления связи
        Comment.objects.create(author='TestAuthor', body='TestCommentBody', post=post)

    def test_author_label(self):
        """
        Test whether the 'author' field label is correctly set.
        """
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('author').verbose_name
        self.assertEqual(field_label, 'author')

    def test_author_max_length(self):
        """
        Test whether the maximum length of the 'author' field is correctly set.
        """
        comment = Comment.objects.get(id=1)
        max_length = comment._meta.get_field('author').max_length
        self.assertEqual(max_length, 60)

    def test_post_relation(self):
        """
        Test whether the relation between 'Comment' and 'Post' models is correctly established.
        """
        comment = Comment.objects.get(id=1)
        post = Post.objects.get(id=1)
        self.assertEqual(comment.post, post)

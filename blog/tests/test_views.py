from django.test import TestCase, Client
from django.urls import reverse
from blog.models import Post, Category, Comment
from blog.forms import CommentForm


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view(self):
        """
        Test whether the 'index' view renders the correct template and context.
        """
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/index.html')
        self.assertIn('posts', response.context)

    def test_category_view(self):
        """
        Test whether the 'category' view renders the correct template and context.
        """
        category = Category.objects.create(name='TestCategory')
        response = self.client.get(reverse('blog:category', args=[category.name]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/category.html')
        self.assertIn('category', response.context)
        self.assertIn('posts', response.context)

    def test_detail_view(self):
        """
        Test whether the 'detail' view renders the correct template and context.
        """
        post = Post.objects.create(title='TestTitle', body='TestBody')
        response = self.client.get(reverse('blog:detail', args=[post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/detail.html')
        self.assertIn('post', response.context)
        self.assertIn('comments', response.context)
        self.assertIn('form', response.context)

    def test_comment_submission(self):
        """
        Test whether a comment can be submitted through the 'detail' view.
        """
        post = Post.objects.create(title='TestTitle', body='TestBody')
        response = self.client.post(reverse('blog:detail', args=[post.pk]), {
            'author': 'TestAuthor',
            'body': 'TestCommentBody'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Comment.objects.count(), 1)

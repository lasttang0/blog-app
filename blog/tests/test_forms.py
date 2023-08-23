from django.test import TestCase
from blog.forms import CommentForm


class CommentFormTest(TestCase):
    def test_author_field_label(self):
        """
        Test whether the author field's label is 'Author'.
        """
        form = CommentForm()
        self.assertEqual(form.fields['author'].label, 'Author')

    def test_body_field_label(self):
        """
        Test whether the body field's label is 'Body'.
        """
        form = CommentForm()
        self.assertEqual(form.fields['body'].label, 'Body')

    def test_author_max_length(self):
        """
        Test whether the max length of the author field is 60 characters.
        """
        form = CommentForm()
        self.assertEqual(form.fields['author'].max_length, 60)

    def test_author_widget_attrs(self):
        """
        Test whether the author field's widget has the expected attributes.
        """
        form = CommentForm()
        author_widget = form.fields['author'].widget
        self.assertEqual(author_widget.attrs['class'], 'form-control')
        self.assertEqual(author_widget.attrs['placeholder'], 'Your Name')

    def test_body_widget_attrs(self):
        """
        Test whether the body field's widget has the expected attributes.
        """
        form = CommentForm()
        body_widget = form.fields['body'].widget
        self.assertEqual(body_widget.attrs['class'], 'form-control')
        self.assertEqual(body_widget.attrs['placeholder'], 'Leave a comment!')

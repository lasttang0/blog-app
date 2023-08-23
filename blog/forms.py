from django import forms


class CommentForm(forms.Form):
    """
    A form for submitting comments.

    This form defines fields for author name and comment body. It provides placeholders and
    CSS classes for styling.

    Fields:
    - author: CharField for the author's name.
    - body: CharField for the comment body.

    Attributes:
    - author: TextInput with custom CSS classes and a placeholder for the author's name.
    - body: Textarea with custom CSS classes and a placeholder for the comment text.
    """

    author = forms.CharField(
        label="Author",
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )

    body = forms.CharField(
        label='Body',
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )

from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Post, Comment


def index(request):
    """
    View function for the index page.

    This view retrieves all posts, orders them by creation timestamp, and renders the
    'blog/index.html' template.

    Parameters:
    - request: The HTTP request object.

    Returns:
    - Rendered HTML response for the index page.
    """
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)


def category(request, category):
    """
    View function for displaying posts within a specific category.

    This view filters posts based on the provided category name, orders them by creation
    timestamp, and renders the 'blog/category.html' template.

    Parameters:
    - request: The HTTP request object.
    - category: The name of the category.

    Returns:
    - Rendered HTML response for the category page.
    """
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category.html', context)


def detail(request, pk):
    """
    View function for displaying post details and handling comments.

    This view retrieves a specific post using its primary key, handles comment submissions,
    and renders the 'blog/detail.html' template.

    Parameters:
    - request: The HTTP request object.
    - pk: The primary key of the post.

    Returns:
    - Rendered HTML response for the post detail page.
    """
    post = get_object_or_404(Post, pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)

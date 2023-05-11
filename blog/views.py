from datetime import date
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Post

# all_posts = []


def get_date(post):
    return post['date']


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/home.html", {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {
        "posts": all_posts
    })


def post_detail(request, slug):
    post_detail = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {
        "slug": slug,
        "post": post_detail,
        "tags": post_detail.tags.all()
    })

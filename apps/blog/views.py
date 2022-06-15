from django.shortcuts import render, redirect
from .models import *
from apps.products.models import Category


# Create your views here.

def blog(request):
    posts = Post.objects.order_by('-id')[:6]
    last_3_posts = Post.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    s = request.GET.get('s')
    if s:
        posts = Post.objects.filter(title__icontains=s)
    cat = request.GET.get('cat')
    if cat:
        posts = Post.objects.filter(category__category__exact=cat)
    tag = request.GET.get('tag')
    if tag:
        posts = Post.objects.filter(tags__tag__exact=tag)
    ctx = {
        'posts': posts,
        'last_3_posts': last_3_posts,
        'tags': tags
    }
    return render(request, 'blog.html', ctx)


def blog_details(request, pk):
    post = Post.objects.get(id=pk)
    last_3_posts = Post.objects.order_by('-id')[:3]
    tags = Tag.objects.all()
    ctx = {
        'post': post,
        'last_3_posts': last_3_posts,
        'tags': tags
    }
    return render(request, 'blog-details.html', ctx)

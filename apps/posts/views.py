from django.shortcuts import render, get_object_or_404
from .models import Category, Posts



def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', context={'categories_list': categories})


def posts_list(request, pk):
    category = Category.objects.get(pk=pk)
    posts_list = Posts.objects.filter(category_id=category)
    return render(request, 'posts_list.html', context={'posts_list': posts_list})

def post_detail(request, pk):
    category = Category.objects.get(pk=pk)
    posts_list = Posts.objects.filter(category_id=category)
    # post_detail = get_object_or_404(posts_list, pk=pk)
    return render(request, 'post_detail.html', {'post_detail': posts_list})

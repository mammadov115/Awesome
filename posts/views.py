from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from bs4 import BeautifulSoup
import requests
from django.contrib import messages
# Create your views here.

def home_view(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()
    categories = Tag.objects.all()

    return render(request, 'posts/home.html', locals())


def post_create_view(request):
    form = PostCreateForm()
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            website = requests.get(form.data['url'])
            source_code = BeautifulSoup(website.text, 'html.parser')
            
            find_image = source_code.select('meta[content^="https://live.staticflickr.com/"]')
            image = find_image[0]['content']
            post.image = image

            find_title = source_code.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title
          
            post.save()
            form.save_m2m()
            return redirect('home')
    return render(request, 'posts/post_create.html', {"form": form})

def post_delete_view(request, pk):
    post = get_object_or_404(Post, id=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post deleted')
        return redirect("home")

    return render(request, 'posts/post_delete.html', locals())

def post_edit_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostEditForm(instance=post)

    if request.method == 'POST':
        form = PostEditForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            messages.success(request, 'Post updated')
            return redirect('home')
    return render(request, 'posts/post_edit.html', locals())

def post_page_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'posts/post_page.html', locals())
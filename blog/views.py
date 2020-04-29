from django.shortcuts import render
from .models import Post
from django.utils import timezone         
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def COVID19_map_data(request):
    return render(request, 'blog/COVID19/COVID_19_in_South_Korea.html', {})

def jays_github(request):
	return redner(request, 'blog/hanjjay_github/Hanjjay_jay.htm',{})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

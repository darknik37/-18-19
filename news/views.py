from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = 'news/post_list.html'
    ordering = ('created_at')
    paginate_by = 10

# def post_list(request):
#     posts = Post.objects.all()
#
#     if request.GET.get('title') is not None:
#         title = request.GET.get('title')
#         posts_filtered = posts.filter(title__iregex=title).order_by('created_at')
#         return render(request, 'news/post_list.html', {"posts": posts_filtered})
#
#     return render(request, 'news/post_list.html', {"posts": posts})

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'name/post_detail.html'

# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request,'news/post_detail.html', {"posts": post})

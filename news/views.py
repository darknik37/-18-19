from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .forms import PostForm
from .models import Post, Author, Category, PostCategory
from .filters import PostFilter

class PostListView(FilterView):
    model = Post
    context_object_name = "posts"
    template_name = 'news/post_list.html'
    ordering = ('created_at',)
    paginate_by = 10
    filterset_class = PostFilter

    # def get_queryset(self):
    #     queryset = super() .get_queryset()
    #     self.post_filtered = PostFilter(self.request.GET, queryset=queryset)
    #     return self.post_filtered.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter']= self.post_filtered
    #     return context

    #    posts = Post.objects.all()


        # if request.GET.get('title') is not None:
        #     title = request.GET.get('title')
        #     posts_filtered = posts.filter(title__iregex=title).order_by('created_at')
        #     return render(request, 'news/post_list.html', {"posts": posts_filtered})
        #     return render(request, 'news/post_list.html', {"posts": posts})

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_detail.html'

 #def post_detail(request, pk):
  #   post = Post.objects.get(pk=pk)
   #  return render(request,'news/post_detail.html', {"posts": post})

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_create.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['create'] = 'Добавление' if self.request.path == '/news/create/' else 'Редактирование'
    #     return context



class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_update.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['update'] = 'Добавление' if self.request.path == '/news/create/' else 'Редактирование'
    #     return context


class PostDeleteView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('post_list')












def post_add(request):
    if request.method == 'POST':
        kwargs = {
            'author_id': request.POST.get('author'),
            'title': request.POST.get('title'),
            'text': request.POST.get('text'),
        }
        category_ids = request.POST.getlist('categories')
        post = Post.objects.create(**kwargs)
        for category_id in category_ids:
            PostCategory.objects.create(post=post, category_id=category_id)
        return redirect ('post_detail', pk=post.pk)
    authors = Author.objects.all()
    categories = Category.objects.all()
    return render(request, 'news/post_add.html', {'authors': authors, 'categories': categories})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.author_id = request.POST.get('author')
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.save()

        categories = request.POST.getlist('categories')
        post.category.set(categories)

        return redirect( 'post_detail', pk=post.pk)

    authors = Author.objects.all()
    categories = Category.objects.all()
    selected_categories = post.Category.values_list('id', flat=True)

    return render(request, 'news/post_edit.html', {
        'post': post,
        'authors': authors,
        'categories': categories,
        'selected_categories': selected_categories,
    })
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Post
from .forms import PostForm

class PostListView(ListView):
    template_name = 'blog/post_list.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostCreateView(CreateView):
    template_name = 'blog/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('post')

class PostUpdateView(UpdateView):
    template_name = 'blog/post_form.html'
    form_class = PostForm
    model = Post
    success_url = reverse_lazy('post')
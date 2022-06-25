from django.shortcuts import render
from I4G011750KUD.blog.models import Post
from django.urls import reverse_lazy
from django.views.generic.edit import(
    DeleteView,
    CreateView,
    UpdateView,
)
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)

class PostDeleteView(DeletView):
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Posts

# Create your views here.
class HomeView(ListView):
    model=Posts
    template_name='post/home.html'
    context_object_name='posts_list'

class PostDetailView(DetailView):
    model=Posts
    template_name='post/post-detail.html'

class PostCreateView(CreateView):
    model=Posts
    template_name='post/post-create.html'
    fields=['title','author','description']

class PostUpdateView(UpdateView):
    model=Posts
    template_name='post/post-update.html'
    fields=['title','description']

class PostDeleteView(DeleteView):
    model=Posts
    template_name='post/post-delete.html'
    success_url=reverse_lazy('home')
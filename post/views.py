from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
class HomeView(ListView):
    model=Posts
    template_name='post/home.html'
    context_object_name='posts_list'
    paginate_by=4

class PostDetailView(DetailView):
    model=Posts
    template_name='post/post-detail.html'

class PostCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model=Posts
    template_name='post/post-create.html'
    fields=['title','description']
    login_url=reverse_lazy('login')
    success_message='Post created success.'

    # def get_success_message(self):
    #     return self.success_message

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Posts
    template_name='post/post-update.html'
    fields=['title','description']
    login_url=reverse_lazy('login')

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Posts
    template_name='post/post-delete.html'
    success_url=reverse_lazy('home')
    login_url=reverse_lazy('login')

    def test_func(self):
        obj=self.get_object()
        return obj.author==self.request.user
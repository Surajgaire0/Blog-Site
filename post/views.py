from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.postgres.search import SearchQuery, SearchRank,SearchVector
from django.db.models import Q

# Create your views here.
class HomeView(ListView):
    model=Posts
    template_name='post/home.html'
    context_object_name='posts_list'
    paginate_by=4

class PostDetailView(DetailView):
    model=Posts
    template_name='post/post-detail.html'

    def get_context_data(self,**kwargs):
        ctx=super().get_context_data(**kwargs)
        ctx['is_owner']=self.request.user==self.get_object().author
        return ctx

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

class PostSearchView(ListView):
    model=Posts
    template_name='post/post-search.html'
    context_object_name='posts_list'
    paginate_by=4

    def get_queryset(self):
        query=self.request.GET['query']
        search_vector=SearchVector('title',weight='A')+SearchVector('description',weight='B')+SearchVector('author',weight='C')
        search_query=SearchQuery(query)
        return Posts.objects.annotate(search=search_query,rank=SearchRank(search_vector,search_query)).filter(Q(search=search_query)&Q(rank__gt=0.1)).order_by('-rank')

    def get_context_data(self,**kwargs):
        ctx=super(PostSearchView,self).get_context_data(**kwargs) #ctx has posts_lists,...
        query=self.request.GET['query']
        ctx['search_query']=query #ctx now has search_query, posts_lists,...
        #print (ctx)
        return ctx


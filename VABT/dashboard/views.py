from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
        )
from .models import Post
#from django.http import HttpResponse
#Create your views here.

#this is now within models

#posts = [
        
#        {
#            'author':'Ian Navarro',
#            'title': 'dashboard Post 1',
#            'content': 'First post!',
#            'date_posted': 'March 5th, 2019'
#            },
#            {
#            'author':'Kyla Navarro',
#            'title': 'dashboard Post 2',
#            'content': '2nd post!',
#            'date_posted': 'March 6th, 2019'
#            }
#    ]

def home(request):
    context = {
        'posts': Post.objects.all() #posts
        }
    return render(request, 'dashboard/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'dashboard/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering  = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'dashboard/about.html',{'title':'About'})


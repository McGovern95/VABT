from django.shortcuts import render
from django.contrib.auth import get_user
from django.contrib.auth.models import User
from users.models import Profile
from users.models import UserExtended 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
        ListView,
        DetailView,
        CreateView,
        UpdateView,
        DeleteView
        )
from .models import Post
from .models import User
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
        'users': User.objects.all() #users
        }
    if (request.user.is_authenticated and request.user.is_staff == False):
        return render(request, 'dashboard/student_home.html', context)
    else:
        return render(request, 'dashboard/home.html', context)

class PostListView(ListView):
    model = User

    template_name = 'dashboard/certifier_home.html'

    context_object_name = 'users'
   #ordering  = ['-date_posted']

class PostDetailView(DetailView):
    model = User
    
class PostCreateView(LoginRequiredMixin ,CreateView):
    model = User
    fields = ['username', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user.is_staff
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['username', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user.is_staff
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == user.username.is_staff:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == user.username.is_staff:
            return True
        return False

def about(request):
    return render(request, 'dashboard/about.html',{'title':'About'})

@user_passes_test(lambda u: u.is_staff)
def certifier_home(request):                                                   
    return render(request, 'dashboard/certifier_home.html',{'title':'Home' })

def student_home(request):  

    ##s0 some form close depending on their  chapter type? 

    #fields = UserExtended.objects.get(user=request.user) #takes the extended fields
    
    #if request.method == 'POST':
    #    form = DocumentForm(request.POST, render.FILES)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('home')
    #else:
    #    form = DocumentForm()
  
    return render(request, 'dashboard/student_home.html',{'title':'Home'})

def contact(request):
    return render(request, 'dashboard/contact.html',{'title':'Contact'})

#checklist stuff here: https://mvp.nmsu.edu/veterans-and-dependents/student-certification-checklists/
#helpful repo im sure: https://github.com/sibtc/simple-file-upload ~ https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html

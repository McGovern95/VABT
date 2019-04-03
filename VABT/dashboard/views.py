from django.shortcuts import render, get_object_or_404
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
    #paginate_by = 10
    #ordering  = ['user']

class UserPostListView(ListView):
    model = User
    template_name = 'dashboard/user_posts.html'
    context_object_name = 'users'
    #paginate_by = 10
    #ordering  = ['user']
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))

   

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

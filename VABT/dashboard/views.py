from django.shortcuts import render, redirect
from django.contrib.auth import get_user
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile
from users.models import UserExtended 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required 
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
from .forms import  CertForm, MVPForm, StudResponForm, ResidTuitAppForm, ConcStudSchedForm, StarDegAuditForm
#from django.http import HttpResponse
#Create your views here.

#CertForm, MVPForm, StudResponForm, ResidTuitAppForm, ConcStudSchedForm, StarDegAuditForm
def home(request):
        return render(request, 'dashboard/home.html')

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
#CertForm, MVPForm, StudResponForm, ResidTuitAppForm, ConcStudSchedForm, StarDegAuditForm
@login_required
def student_home(request):
    if request.method=='POST':
        cert_form = CertForm(request.POST, request.FILES, instance=request.user.userextended)
        mvp_form = MVPForm(request.POST, request.FILES, instance=request.user.userextended)
        stud_form = StudResponForm(request.POST, request.FILES, instance=request.user.userextended)
        resid_form = ResidTuitAppForm(request.POST, request.FILES, instance=request.user.userextended)
        conc_form = ConcStudSchedForm(request.POST, request.FILES, instance=request.user.userextended)
        star_form = StarDegAuditForm(request.POST, request.FILES, instance=request.user.userextended)
        if cert_form.is_valid():
           cert_form.save()
           messages.success(request, f'Your account has been updated!')
           return redirect('student-home')
    else:
        cert_form = CertForm(instance=request.user.userextended)


    context = {
            'cert_form': cert_form
    }


    return render(request, 'dashboard/student_home.html',context)



def contact(request):
    return render(request, 'dashboard/contact.html',{'title':'Contact'})

#checklist stuff here: https://mvp.nmsu.edu/veterans-and-dependents/student-certification-checklists/
#helpful repo im sure: https://github.com/sibtc/simple-file-upload ~ https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html

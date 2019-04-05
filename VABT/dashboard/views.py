from django.shortcuts import render, redirect, get_object_or_404
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
from django.core.mail import EmailMessage
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
  
class UserPostListView(ListView):
    model = User
    template_name = 'dashboard/user_posts.html'
    context_object_name = 'users'
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
    #this dont work. fix it ian!
    def email(request):
        if(request.GET.get('certbtn')):
            email = EmailMessage(
            'VABT Notification',
            'The user has sent you their documents',
            'VABT Notifications' +'<sender@gmail.com>',
            [request.user.email],
            headers = {'Reply-To': 'contact_email@gmail.com' }
            )
            email.send()
            messages.success(request, f'Your Message Has Been Sent to Student')
       

def about(request):
    return render(request, 'dashboard/about.html',{'title':'About'})

@user_passes_test(lambda u: u.is_staff)
def certifier_home(request):
    return render(request, 'dashboard/certifier_home.html',{'title':'Home' })

@login_required
def student_home(request):
    if request.method=='POST':
        cert_form = CertForm(request.POST, request.FILES, instance=request.user.userextended)
        mvp_form = MVPForm(request.POST, request.FILES, instance=request.user.userextended)
        stud_form = StudResponForm(request.POST, request.FILES, instance=request.user.userextended)
        resid_form = ResidTuitAppForm(request.POST, request.FILES, instance=request.user.userextended)
        conc_form = ConcStudSchedForm(request.POST, request.FILES, instance=request.user.userextended)
        star_form = StarDegAuditForm(request.POST, request.FILES, instance=request.user.userextended)
        if cert_form.is_valid() == True:
           cert_form.save()
           messages.success(request, f'Your Certificate of Eligibility has been uploaded!')
           
        if mvp_form.is_valid() == True:
            mvp_form.save()
            messages.success(request, f'Your MVP Information Sheet has been uploaded!')
            
        if stud_form.is_valid() == True:
            stud_form.save()
            messages.success(request, f'Your Student Responsibilites Form has been uploaded!')
            
        if resid_form.is_valid() == True:
            resid_form.save()
            messages.success(request, f'Your Resident Tuition Application has been uploaded!')
            
        if conc_form.is_valid() == True:
            conc_form.save()
            messages.success(request, f'Your Concise Student Schedule has been uploaded!')
            
        if star_form.is_valid() == True:
            star_form.save()
            messages.success(request, f'Your STAR Degree Audit has been uploaded!')
    else:
        cert_form = CertForm(instance=request.user.userextended)
        mvp_form = MVPForm(instance=request.user.userextended)
        stud_form = StudResponForm(instance=request.user.userextended)
        resid_form = ResidTuitAppForm(instance=request.user.userextended)
        conc_form = ConcStudSchedForm(instance=request.user.userextended)
        star_form = StarDegAuditForm(instance=request.user.userextended)

    context = {
            'cert_form': cert_form,
            'mvp_form' : mvp_form,
            'stud_form' : stud_form,
            'resid_form' : resid_form,
            'conc_form' : conc_form,
            'star_form' : star_form
    }
# sending notifications to certifier using built in django email function    
    if(request.GET.get('mybtn')):
        email = EmailMessage(
        'VABT Notification',
        'The user has sent you their documents',
        'VABT Notifications' +'<sender@gmail.com>',
        [request.user.email],
        headers = {'Reply-To': 'contact_email@gmail.com' }
        )
        email.send()
        messages.success(request, f'Your Message Has Been Sent')

    return render(request, 'dashboard/student_home.html',context)

#CHRISTIAN DONT DELETE THIS
#Alltel: phonenumber@message.alltel.com
#AT&T: phonenumber@txt.att.net
#T-Mobile: phonenumber@tmomail.net
#Virgin Mobile: phonenumber@vmobl.com
#Sprint: phonenumber@messaging.sprintpcs.com
#Verizon: phonenumber@vtext.com
#Nextel: phonenumber@messaging.nextel.com
#US Cellular: phonenumber@mms.uscc.net


def contact(request):
    return render(request, 'dashboard/contact.html',{'title':'Contact'})

#def Sendmail(request):
#   if(request.GET.get('mybtn')):
#    email = EmailMessage(
#    'subject_message',
#    'content_message',
#    'sender smtp gmail' +'<sender@gmail.com>',
#    ['user.email'],
#    headers = {'Reply-To': 'contact_email@gmail.com' }
#    )
#    email.send()
#    messages.success(request, f'Your Message Has Been Sent')


#checklist stuff here: https://mvp.nmsu.edu/veterans-and-dependents/student-certification-checklists/
#helpful repo im sure: https://github.com/sibtc/simple-file-upload ~ https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
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

#for x in User
posts =[
    {
        'author':'Ian Navarro',
        'title': 'Blog Post 1',
        'content': 'First post!',
        'date_posted': 'March 5th, 2019'
        },
        {
        'author':'Kyla Navarro',
        'title': 'Blog Post 2',
        'content': '2nd post!',
        'date_posted': 'March 6th, 2019'
        }
    ]


class PostListView(ListView):
    model = Post
    template_name = 'dashboard/certifier_home.html'
    context_object_name = 'posts'
   #ordering  = ['-date_posted']

#@admin.register(Post)  
class UserPostListView(ListView):
    model = Post
    template_name = 'dashboard/user_posts.html'
    context_object_name = 'posts'
    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(student=user)
    
    def response_change(self, request, obj):
        if "_make-unique" in request.POST:
            print("Hello world")
    #        matching_names_except_this = self.get_queryset(request).filter(name=obj.name).exclude(ProcessLookupError=obj.id)
    #        matching_names_except_this.delete()
    #        obj.Certficate_of_eligibility = True
    #        obj.save()
    #        self.message_user(request, "Certificate of eligibility changed")
    #        return HttpResponseRedirect(".")
        return super().response_change(request, obj)

    #need to get the kwarg stuff for the email
    def get(self, request, *args, **kwargs):
        userdefault = User.objects.get(username = kwargs.get('username'))
        userextended = UserExtended.objects.get(user=userdefault)
        studentcert = Post.objects.get(student=userdefault)

        if(studentcert.Certificate_of_eligibility == False ):
            message1 = "Certificate of eligibility (COE) \n"
        if(studentcert.MVP_information_sheet == False ):
            message2 = "Information Sheet \n"
        if(studentcert.Student_responsibility == False ):
            message3 = "Student Responsibility \n"
        if(studentcert.Resident_tuition_app == False ):
            message4 = "Resident Tuition Application \n"
        if(studentcert.Concise_student_schedule == False ):
            message5 = "Concise Student Schedule \n"
        if(studentcert.Star_degree_audit == False ):
            message6 = "Star Degree Audit \n"

        if(studentcert.Certificate_of_eligibility == True ):
            message1 = ""
        if(studentcert.MVP_information_sheet == True ):
            message2 = ""
        if(studentcert.Student_responsibility == True ):
            message3 = ""
        if(studentcert.Resident_tuition_app == True ):
            message4 = ""
        if(studentcert.Concise_student_schedule == True ):
            message5 = ""
        if(studentcert.Star_degree_audit == True ):
            message6 = ""
        
        #logic for phone/email notifications 
        if(userextended.phone_notifications == True):
             if(request.GET.get('certbtn')):
                if(userextended.carrier == 'Verizon'):
                    text = EmailMessage(
                    'VABT Notification ',
                    'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                    'VABT Notifications' +'<sender@gmail.com>',
                    [userextended.phone_number +'@vtext.com'],
                    headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
                    text.send()
                    messages.success(request, f'Your Phone Message Has Been Sent')
                elif(userextended.carrier == 'AT&T'):
                    text = EmailMessage(
                    'VABT Notification',
                    'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                    'VABT Notifications' +'<sender@gmail.com>',
                    [userextended.phone_number +'@txt.att.net'],
                    headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
                    text.send()
                    messages.success(request, f'Your Phone Message Has Been Sent')
                elif(userextended.carrier == 'Sprint'):
                    text = EmailMessage(
                    'VABT Notification',
                    'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                    'VABT Notifications' +'<sender@gmail.com>',
                    [userextended.phone_number +'@messaging.sprintpcs.com'],
                    headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
                    text.send()
                    messages.success(request, f'Your Phone Message Has Been Sent')
                elif(userextended.carrier == 'T-Mobile'):
                    text = EmailMessage(
                    'VABT Notification',
                    'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                    'VABT Notifications' +'<sender@gmail.com>',
                    [userextended.phone_number +'@tmomail.net'],
                    headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
                    text.send()
                    messages.success(request, f'Your Phone Message Has Been Sent')
                elif(userextended.carrier == 'Virgin'):
                     text = EmailMessage(
                    'VABT Notification',
                    'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                    'VABT Notifications' +'<sender@gmail.com>',
                    [userextended.phone_number +'@vmobl.com'],
                    headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
                     text.send()
                     messages.success(request, f'Your Phone Message Has Been Sent')

                email = EmailMessage(
                'VABT Notification',
                'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                'VABT Notifications' +'<sender@gmail.com>',
                [userdefault.email],
                headers = {'Reply-To': 'contact_email@gmail.com' }
                )
                email.send()   
                messages.success(request, f'Your Email Message Has Been Sent to '+ userdefault.first_name) 
                
        elif(userextended.phone_notifications == False):
            if(request.GET.get('certbtn')):
                email = EmailMessage(
                'VABT Notification',
                'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                'VABT Notifications' +'<sender@gmail.com>',
                [userdefault.email],
                headers = {'Reply-To': 'contact_email@gmail.com' }
                )
                email.send()                                                             
                messages.success(request, f'Your Email Message Has Been Sent to '+ userdefault.first_name) 


        return super(UserPostListView, self).get(request, *args, **kwargs)

    
class PostDetailView(DetailView):
    model = Post

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

    certs = Post.objects.all()#for the certification

    context = {
            'cert_form': cert_form,
            'mvp_form' : mvp_form,
            'stud_form' : stud_form,
            'resid_form' : resid_form,
            'conc_form' : conc_form,
            'star_form' : star_form,
            'certs' : certs
    }
    return render(request, 'dashboard/student_home.html',context)

def contact(request):
    return render(request, 'dashboard/contact.html',{'title':'Contact'})



#
#
#NOTES
#
#

#CHRISTIAN DONT DELETE THIS
#Alltel: phonenumber@message.alltel.com
#AT&T: phonenumber@txt.att.net
#T-Mobile: phonenumber@tmomail.net
#Virgin Mobile: phonenumber@vmobl.com
#Sprint: phonenumber@messaging.sprintpcs.com
#Verizon: phonenumber@vtext.com
#Nextel: phonenumber@messaging.nextel.com
#US Cellular: phonenumber@mms.uscc.net

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
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.models import User
from users.models import Profile
from users.models import UserExtended 
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
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

def home(request):
    """
    renders the home page for an unathenticated user. 

    **Template:**

    :template:`dashbaord/home.html`
    """
    return render(request, 'dashboard/home.html')

class PostListView(ListView):
    """
    a ListView that renders the certifiers_home. 
                         
    **Context**
    model
    template_name
    context_object_name
    ordering

    ``mymodel``
        An instance of :model:`dashboard.Post`.

    **Template:**

    :template:`dashboard/certifier_home.html`

    """
    model = Post
    template_name = 'dashboard/certifier_home.html'
    context_object_name = 'posts'
    ordering  = ['progress']


class UserPostListView(ListView):
    """
    a ListView that renders the userpost page. This is the longest function and houses our notifcation
    and certifying features.
                         
    **Context**
    template_name
    context_object_name
    user
    userdefault
    userextended
    studentcert
    date
    email
    text
    message[1,2,3,4,5,6]

    ``mymodel``
        Uses all the models.

    **Template:**

    :template:`dashboard/user_posts.html`

    """
    model = Post
    template_name = 'dashboard/user_posts.html'
    context_object_name = 'posts'
    def get_query_set(self):

        """
        gets the instance of the student when on their webpage. 

        """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(student=user)
    
   
    def get(self, request, *args, **kwargs):

        """
        a general function (get) for ListView classes, our notifications
        and certifying can work with buttons here.

        """
        #gets the students database fields
        userdefault = User.objects.get(username = kwargs.get('username'))
        userextended = UserExtended.objects.get(user=userdefault)
        studentcert = Post.objects.get(student=userdefault)
        date = timezone.now()

   #buttons for certification and progress bars
        if(request.GET.get('boolcoecert')):
            studentcert.date_cert = date
            if(studentcert.Certificate_of_eligibility == False):
               studentcert.Certificate_of_eligibility = True
               if studentcert.progress != 6:
                   studentcert.progress += 1
                   userextended.progress_student +=1
               studentcert.save()
               userextended.save()
              # messages.success(request, f' set to True')
            elif(studentcert.Certificate_of_eligibility == True):
                studentcert.Certificate_of_eligibility = False
                if studentcert.progress != 0:
                   studentcert.progress -= 1
                   userextended.progress_student -=1
                studentcert.save()
                userextended.save()
               # messages.success(request, f' set to False')

        if(request.GET.get('boolinfocert')):
            studentcert.date_info = date
            if(studentcert.MVP_information_sheet == False):
               studentcert.MVP_information_sheet = True
               if studentcert.progress != 6:
                   studentcert.progress += 1
                   userextended.progress_student +=1
               studentcert.save()
               userextended.save()
              # messages.success(request, f' set to True')
            elif(studentcert.MVP_information_sheet == True):
                studentcert.MVP_information_sheet = False
                if studentcert.progress != 0:
                   studentcert.progress -= 1
                   userextended.progress_student -=1
                studentcert.save()
                userextended.save()
               # messages.success(request, f' set to False')

        if(request.GET.get('boolrespcert')):
            studentcert.date_respo = date
            if(studentcert.Student_responsibility == False):
               studentcert.Student_responsibility = True
               if studentcert.progress != 6:
                   studentcert.progress += 1
                   userextended.progress_student +=1
               studentcert.save()
               userextended.save()

              # messages.success(request, f' set to True')
            elif(studentcert.Student_responsibility == True):
                studentcert.Student_responsibility = False
                if studentcert.progress != 0:
                   studentcert.progress -= 1
                   userextended.progress_student -=1
                studentcert.save()
                userextended.save()
               # messages.success(request, f' set to False')

        if(request.GET.get('booltuition')):
            studentcert.date_tuition = date
            if(studentcert.Resident_tuition_app == False):
               studentcert.Resident_tuition_app = True
               if studentcert.progress != 6:
                   studentcert.progress += 1
                   userextended.progress_student +=1
               studentcert.save()
               userextended.save()
              # messages.success(request, f' set to True')
            elif(studentcert.Resident_tuition_app == True):
                studentcert.Resident_tuition_app = False
                if studentcert.progress != 0:
                   studentcert.progress -= 1
                   userextended.progress_student -=1
                studentcert.save()
                userextended.save()
               # messages.success(request, f' set to False')

        if(request.GET.get('boolconcise')):
            studentcert.date_concise = date
            if(studentcert.Concise_student_schedule == False):
               studentcert.Concise_student_schedule = True
               if studentcert.progress != 6:
                   studentcert.progress += 1
                   userextended.progress_student +=1
               studentcert.save()
               userextended.save()
              # messages.success(request, f' set to True')
            elif(studentcert.Concise_student_schedule == True):
                studentcert.Concise_student_schedule = False
                if studentcert.progress != 0:
                   studentcert.progress -= 1
                   userextended.progress_student -=1
                studentcert.save()
                userextended.save()
               # messages.success(request, f' set to False')

        if(request.GET.get('boolaudit')):
            studentcert.date_audit = date
            if(studentcert.Star_degree_audit == False):
               studentcert.Star_degree_audit = True
               if studentcert.progress != 6:
                   studentcert.progress += 1
                   userextended.progress_student +=1
               studentcert.save()
               userextended.save()
              # messages.success(request, f' set to True')
            elif(studentcert.Star_degree_audit == True):
                studentcert.Star_degree_audit = False
                if studentcert.progress != 0:
                   studentcert.progress -= 1
                   userextended.progress_student -=1
                studentcert.save()
                userextended.save()
                        


        #automated messages for notifcations
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
                    if(message1=="" and message2=="" and message3=="" and message4=="" and message5=="" and message6==""):
                        text = EmailMessage(
                        'VABT Notification ',
                        'You are now Cetified! \n',
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@vtext.com'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    else:
                        text = EmailMessage(
                        'VABT Notification ',
                        'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@vtext.com'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    text.send()
                    messages.success(request, f'A Text (SMS) Notification Has Been Sent to '+ userdefault.first_name)
                elif(userextended.carrier == 'AT&T'):
                    if(message1=="" and message2=="" and message3=="" and message4=="" and message5=="" and message6==""):
                        text = EmailMessage(
                        'VABT Notification ',
                        'You are now Cetified! \n',
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@txt.att.net'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    else:
                        text = EmailMessage(
                        'VABT Notification',
                        'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@txt.att.net'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    text.send()
                    messages.success(request, f'A Text (SMS) Notification Has Been Sent to '+ userdefault.first_name)
                elif(userextended.carrier == 'Sprint'):
                    if(message1=="" and message2=="" and message3=="" and message4=="" and message5=="" and message6==""):
                        text = EmailMessage(
                        'VABT Notification ',
                        'You are now Cetified! \n',
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@messaging.sprintpcs.com'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    else:
                        text = EmailMessage(
                        'VABT Notification',
                        'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@messaging.sprintpcs.com'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    text.send()
                    messages.success(request, f'A Text (SMS) Notification Has Been Sent to '+ userdefault.first_name)
                elif(userextended.carrier == 'T-Mobile'):
                    if(message1=="" and message2=="" and message3=="" and message4=="" and message5=="" and message6==""):
                        text = EmailMessage(
                        'VABT Notification ',
                        'You are now Cetified! \n',
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@tmomail.net'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    else:
                        text = EmailMessage(
                        'VABT Notification',
                        'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@tmomail.net'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    text.send()
                    messages.success(request, f'A Text (SMS) Notification Has Been Sent to '+ userdefault.first_name)
                elif(userextended.carrier == 'Virgin'):
                    if(message1=="" and message2=="" and message3=="" and message4=="" and message5=="" and message6==""):
                        text = EmailMessage(
                        'VABT Notification ',
                        'You are now Cetified! \n',
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@vmobl.com'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    else:
                         text = EmailMessage(
                        'VABT Notification',
                        'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                        'VABT Notifications' +'<sender@gmail.com>',
                        [userextended.phone_number +'@vmobl.com'],
                        headers = {'Reply-To': 'contact_email@gmail.com' }
                        )
                    text.send()
                    messages.success(request, f'A Text (SMS) Notification Has Been Sent to '+ userdefault.first_name)

                if(message1=="" and message2=="" and message3=="" and message4=="" and message5=="" and message6==""):
                    email = EmailMessage(
                    'VABT Notification ',
                    'You are now Cetified! \n',
                    'VABT Notifications' +'<sender@gmail.com>',
                    [userdefault.email],
                    headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
                else:
                    email = EmailMessage(
                    'VABT Notification',
                    'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                    'VABT Notifications' +'<sender@gmail.com>',
                    [userdefault.email],
                    headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
                email.send()   
                messages.success(request, f'An Email Notification Has Been Sent to '+ userdefault.first_name) 
                
        elif(userextended.phone_notifications == False):
            if(request.GET.get('certbtn')):
                if(message1=="" and message2=="" and message3=="" and message4=="" and message5=="" and message6==""):
                    email = EmailMessage(
                    'VABT Notification ',
                    'You are now Cetified! \n',
                    'VABT Notifications' +'<sender@gmail.com>',
                    [userextended.phone_number +'@vtext.com'],
                    headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
                else:
                    email = EmailMessage(
                    'VABT Notification',
                    'Please turn in the following forms: \n'+message1+message2+message3+message4+message5+message6,
                    'VABT Notifications' +'<sender@gmail.com>',
                    [userdefault.email],
                    headers = {'Reply-To': 'contact_email@gmail.com' }
                    )
                email.send()   
                messages.success(request, f'An Email Notification Has Been Sent to '+ userdefault.first_name) 


        return super(UserPostListView, self).get(request, *args, **kwargs)

    
class PostDetailView(DetailView):
    model = Post

def about(request):
    """
    renders the about page. 

    **Template:**

    :template:`dashbaord/about.html`
    """
    return render(request, 'dashboard/about.html',{'title':'About'})

#@user_passes_test(lambda u: u.is_staff)
#def certifier_home(request):
#    return render(request, 'dashboard/certifier_home.html',{'title':'Home' })

@login_required
def student_home(request):
    """
    this renders the student home page, file uploading is handling by this view 
                         
    **Context**
    cert_form
    mvp_form
    stud_form
    resid_form
    conc_form
    cert_form
    star_form
    certs


    ``mymodel``
        An instance of :model:`users.UserExtended` and :model:`auth.User`.

    **Template:**

    :template:`users/student_home.html`
    """
    if request.method=='POST':
        cert_form = CertForm(request.POST, request.FILES, instance=request.user.userextended)
        mvp_form = MVPForm(request.POST, request.FILES, instance=request.user.userextended)
        stud_form = StudResponForm(request.POST, request.FILES, instance=request.user.userextended)
        resid_form = ResidTuitAppForm(request.POST, request.FILES, instance=request.user.userextended)
        conc_form = ConcStudSchedForm(request.POST, request.FILES, instance=request.user.userextended)
        star_form = StarDegAuditForm(request.POST, request.FILES, instance=request.user.userextended)

        if cert_form.is_valid() and mvp_form.is_valid() and stud_form.is_valid() and resid_form.is_valid() and conc_form.is_valid() and star_form.is_valid() == True:     
            cert_form.save()
            mvp_form.save()
            stud_form.save()       
            resid_form.save()
            conc_form.save()
            star_form.save()
            messages.success(request, f'Your File(s) has been uploaded!')
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
    """
    renders the contact page. 

    **Template:**

    :template:`dashbaord/contact.html`
    """
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

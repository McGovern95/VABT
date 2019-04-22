from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required #user must be logged in to view profile
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, authenticate
from dashboard.models import Post
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, UserExtendedRegisterForm, UserExtendedUpdateForm, ChecklistCreate
# Create your views here.

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        formExtended = UserExtendedRegisterForm(request.POST)
        #changed a bit for phone numbers
        if form.is_valid() and formExtended.is_valid():    
            user = form.save()      
            user.userextended.phone_number = formExtended.cleaned_data.get('phone_number')
            user.userextended.carrier = formExtended.cleaned_data.get('carrier')
            user.userextended.phone_notifications = formExtended.cleaned_data.get('phone_notifications')
            user.userextended.save()
            user.refresh_from_db()
            user.save()

            Post.objects.create(title="Checklist for"+user.last_name,comment="Default", student = user)

            request.user.is_staff = False
            request.user.is_student = True
            request.user.is_firsttime = True
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
        formExtended = UserExtendedRegisterForm()
    context = {
            'form':form,
            'formExtended':formExtended
    }
    return render(request,'users/registers.html',context)

@login_required
def profile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        ue_form = UserExtendedUpdateForm(request.POST, instance=request.user.userextended)
        if u_form.is_valid() and p_form.is_valid() and ue_form.is_valid() :
           u_form.save()
           p_form.save()
           ue_form.save()
           messages.success(request, f'Your account has been updated!')
           return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        ue_form = UserExtendedUpdateForm(instance=request.user.userextended)

    context = {
            'u_form': u_form,
            'p_form': p_form,
            'ue_form' : ue_form
    }
    return render(request, 'users/profile.html',context)

@user_passes_test(lambda u: u_form.is_staff)
def alerts(request):
    alerts = Alerts.objects.filter(user_id=request.user)

    if request.method == 'POST':
        removed_alerts = request.POST.getlist('alert_select')
        alerts.filter(id__in=removed_alerts).delete()
        alerts = alerts.filter(~Q(id__in=removed_alerts))

    paged_alerts = get_page_items(request, alerts, 25)
    alert_title = "Alerts"
    if request.user.get_full_name():
        alert_title += " for " + request.user.get_full_name()
        
    add_breadcrumb(title=alert_title, top_level=True, request=request)
    return render(request,
                  'users/about.html',
                  context)
#message.debug
#message.info
#message.success
#message.warning
#message.error
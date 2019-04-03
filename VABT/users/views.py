from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required #user must be logged in to view profile
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():#django handles backend to validate some stuff
            username = form.cleaned_data.get('username') #flash message
            form.save()#omaga! so easy
            request.user.is_staff = False
            request.user.is_student = True
            request.user.is_firsttime = True
            messages.success(request, f'Your account has been created! You are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/registers.html', {'form':form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
           u_form.save()
           p_form.save()
           messages.success(request, f'Your account has been updated!')
           return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
            'u_form': u_form,
            'p_form': p_form
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
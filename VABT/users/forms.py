from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from dashboard.models import Post
from users.models import UserExtended

#forms for user registering and profile updating

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
   
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name' ,'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserExtendedRegisterForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ['phone_number','phone_notifications','carrier']

class UserExtendedUpdateForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ['phone_number','phone_notifications','carrier']

class ChecklistCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'comment', 'student']

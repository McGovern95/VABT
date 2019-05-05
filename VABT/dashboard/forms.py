from django import forms
from users.models import UserExtended

#forms used for file upload

class CertForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ['cert_of_elig']

class MVPForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ['MVP_info_sheet']

class StudResponForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ['stud_respon']

class ResidTuitAppForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ['resid_tuit_app']

class ConcStudSchedForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ['conc_stud_sched']

class StarDegAuditForm(forms.ModelForm):
    class Meta:
        model = UserExtended
        fields = ['star_deg_audit']


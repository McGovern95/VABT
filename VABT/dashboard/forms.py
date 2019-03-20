from django import forms
from upload.core.models import Document

class Ch33Form(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document',)



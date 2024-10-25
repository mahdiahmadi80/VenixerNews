from django import forms
from .models import Contact
    # name = forms.CharField(max_length=100)
    # email = forms.CharField(max_length=150)
    # subject = forms.CharField(max_length=150)
    # messege = forms.CharField(widget=forms.Textarea)
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields='__all__'


from django import forms
from .models import *


class EnquiryForm(forms.ModelForm):
    Name=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Your Name ...'}))
    last_name=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Last Name ...'}))
    phone_no=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Enter Mobile Number ...','pattern':'[0-9]+'}))
    email_id=forms.EmailField()
    message=forms.CharField(required=True,widget=forms.Textarea(attrs={'placeholder':'Enter Your Message ...'}))


    class Meta:
        model= Enquiry
        fields = ["Name","last_name","phone_no", "email_id", "message"]
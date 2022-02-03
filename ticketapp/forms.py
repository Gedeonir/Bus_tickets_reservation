from email.policy import default
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,required=False) 
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)
   
    cc_myself = forms.BooleanField(required=False)
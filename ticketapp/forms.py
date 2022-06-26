from dataclasses import fields
import email
from email.policy import default
from pyexpat import model
from random import choices
from django import forms
from django.contrib.auth import (
    authenticate
)

from django.contrib.auth.models import User

from ticketapp.models import bookings, customers, schedules



class bookTicketForm(forms.Form):
    

    TICKET_CHOICES =(
        (1, 1,),
        (2, 2,),
        (3, 3,),
        (4, 4,),
        (5, 5,),
    )
    customer_email = forms.EmailField(label='Email Address',help_text='You will receive your ticket on this email',widget=forms.EmailInput(attrs={'class': 'inputField','readonly':True}))
    contacts = forms.IntegerField(label='Contacts',widget=forms.TextInput(attrs={'class': 'inputField'}))
    tickets = forms.ChoiceField(label='Number of tickets',choices=TICKET_CHOICES,widget=forms.Select(choices=TICKET_CHOICES,attrs={'class': 'inputField'}))

    class Meta():
        model:bookings

        fields = [
            'customer_email',
            'schedule',
            'From',
            'To',
            'travelDate',
            'travelTime',
            'tickets',
            'total_amount_to_pay',
            'status',
            'bookingTime'
        ]


from django.contrib.auth.forms import UserCreationForm 

class userSignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email Address',help_text='Required',widget=forms.EmailInput(attrs={'class': 'inputField'}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class':'inputField'
        })
        self.fields['password1'].widget.attrs.update({
            'class':'inputField passwordField1'
        })
        self.fields['password2'].widget.attrs.update({
        'class':'inputField passwordField2'
        })
        
    class Meta:
        model=User
        fields = ('username', 'email', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        email_qs = User.objects.filter(email__iexact=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered"
            )
        return email


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username',widget=forms.TextInput(attrs={'class': 'inputField'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class': 'inputField password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            # if not user:
            #     raise forms.ValidationError('Invalid credentials')
            # if not user.is_active:
            #     raise forms.ValidationError('This user is not active')
 

from django.contrib.auth.forms import PasswordResetForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'inputField',
        'placeholder': 'Enter your email',
        }))
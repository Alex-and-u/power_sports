from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Field, Booking
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib import messages
from datetime import datetime, timedelta


class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


        # def save(self, commit=True):
        #     user = super(RegisterForm, self).save(commit=False)
        #     user.email = self.cleaned_data['email']
        #     if commit:
        #         user.save()
        #     return user


    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Username', 'class': 'form-control'}
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password', 'class': 'form-control'}
        ))


class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = '__all__'




class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['no_of_players'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['time'].widget.attrs['class'] = 'form-control'

    date = forms.DateField(widget=forms.SelectDateWidget)

    TIME_CHOICES = (
        ('9:00 - 9:30', '9:00 - 10:30'),
        ('9:31 - 10:00', '10:31 - 12:00'),
        ('10:31 - 11:00', '12:01 - 13:30'),
        ('11:01 - 11:30', '13:31 - 15:00'),
        ('11:31 - 12:30', '15:01 - 16:30'),
        ('12:31 - 13:00', '16:31 - 18:00'),
        ('13:01 - 13:30', '18:01 - 19:30'),
        ('13:31 - 14:00', '19:31 - 21:00'),
        ('14:01 - 14:30', '21:01 - 22:30'),
        ('14:31 - 15:00', '22:31 - 00:00'),
    )
    time = forms.ChoiceField(
        choices=TIME_CHOICES)






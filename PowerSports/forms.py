from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Field
from django.forms import ModelForm, TextInput, EmailInput
from django.contrib import messages
from datetime import datetime, timedelta


class RegisterForm(UserCreationForm):
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form-control'}))
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


# class PlayerForm(forms.ModelForm):
#     class Meta:
#         model = Player
#         fields = ['user']


class ChoiceForm(forms.Form):
    cities = (
    ("1", "Cluj"),
    ("2", "Timisoara"),
    ("3", "Brasov"),
    ("4", "Bucuresti"),
    ("5", "Iasi")
)
    city = forms.ChoiceField(
        choices=cities
    )

    addresses = (
    ("1", "Str. Tăbăcarilor 15c, Cluj-Napoca, Romania"),
    ("2", "Strada Versului 34, Timișoara, Romania"),
    ("3", "Strada Colonia Metrom 12, Brașov 505600, Romania"),
    ("4", "Complex Mirano, Strada Progresului 90-100, București 050798, Romania"),
    ("5", "Strada Cicoarei, Iași 707515, Romania")

)
    address = forms.ChoiceField(
        choices=addresses)

    number_of_players = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("13", "13"),
        ("14", "14"),
        ("15", "15"),
        ("16", "16"),
        ("17", "17"),
        ("18", "18"),
        ("19", "19"),
        ("20", "20")

    )
    players = forms.ChoiceField(
        choices=number_of_players)

    date = forms.DateTimeField(widget=forms.SelectDateWidget)

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




from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Field
from .models import Player
from django.contrib import messages
from datetime import datetime, timedelta

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # fields = ['username', 'password1', 'password2']
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        def save(self, commit=True):
            user = super(RegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user


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


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['user']


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

    date = forms.DateTimeField(widget = forms.SelectDateWidget)




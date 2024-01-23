from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Field


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

# class FieldForm(forms.ModelForm):
#     class Meta:
#         model = Field
#         field = '__all__'




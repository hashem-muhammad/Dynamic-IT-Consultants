from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.conf import settings

# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ("full_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        if commit:
            user.save()
        return user


class loginForm(forms.Form):
    email = forms.EmailField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)

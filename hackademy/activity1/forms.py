from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class OverrideRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError()
        user = super(UserCreationForm, self).save(commit=True)
        
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        user_profile = Profile(
            user = user
        )

        user_profile.save()
        return user, user_profile
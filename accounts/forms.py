from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class RegistrationForm(UserCreationForm):
      email = forms.EmailField(required=True)
      class Meta:
        model = User
        fields=(
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
        )
      def save(self, commit=True):
          user = super(RegistrationForm, self).save(commit=False)
          user.first_name = self.cleaned_data['first_name']
          user.last_name = self.cleaned_data['first_name']
          user.email = self.cleaned_data['email']
          if commit:
              user.save()
          return user

class EditProfileform(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
        )
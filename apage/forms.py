from django.contrib.auth.models import User
from django import forms


#here we make new user_form class and we can tweak it what we want to display on user form we are going to create

class User_Form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', ]


